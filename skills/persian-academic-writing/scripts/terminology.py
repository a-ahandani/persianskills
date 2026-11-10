#!/usr/bin/env python3
"""Load and query TOML terminology registers."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import tomllib
import unicodedata
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Sequence

ROOT = Path(__file__).resolve().parents[1]
BUILTIN_GLOSSARY = ROOT / "assets" / "terminology-register.toml"
ALLOWED_STATUSES = {"reference", "proposed", "approved", "deprecated"}

STRING_FIELDS = (
    "preferred_fa",
    "acronym",
    "definition_or_scope",
    "first_use_form",
    "source_or_authority",
    "grammatical_behavior",
    "capitalization",
    "category",
    "plural_english",
    "definition_ref",
    "first_use",
)
LIST_FIELDS = (
    "candidates",
    "accepted_variants",
    "rejected_variants",
    "notes",
    "aliases",
)
KNOWN_FIELDS = {
    "id",
    "concept_id",
    "english",
    "persian",
    "status",
    "source_page",
    *STRING_FIELDS,
    *LIST_FIELDS,
}


@dataclass(frozen=True, slots=True)
class GlossaryEntry:
    """One English-to-Persian terminology record."""

    id: str
    concept_id: str
    english: str
    persian: str
    status: str
    preferred_fa: str = ""
    acronym: str = ""
    definition_or_scope: str = ""
    first_use_form: str = ""
    source_or_authority: str = ""
    grammatical_behavior: str = ""
    capitalization: str = ""
    category: str = ""
    plural_english: str = ""
    definition_ref: str = ""
    first_use: str = ""
    candidates: tuple[str, ...] = ()
    accepted_variants: tuple[str, ...] = ()
    rejected_variants: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    aliases: tuple[str, ...] = ()
    source_page: int | None = None
    extra: dict[str, Any] = field(default_factory=dict, compare=False)

    @property
    def translations(self) -> tuple[str, ...]:
        """Return ordered lookup values without assigning new authority."""

        values: list[str] = []
        if self.preferred_fa:
            values.append(self.preferred_fa)
        values.extend(self.candidates)
        if not values and self.persian:
            values.append(self.persian)
        if self.status in {"approved", "proposed"}:
            values.extend(self.accepted_variants)
        return tuple(dict.fromkeys(value for value in values if value))

    @property
    def lookup_keys(self) -> tuple[str, ...]:
        values = [self.english, self.plural_english, self.acronym, *self.aliases]
        return tuple(dict.fromkeys(value for value in values if value))

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result.pop("extra", None)
        result.update(self.extra)
        result["translations"] = list(self.translations)
        for name in LIST_FIELDS:
            result[name] = list(result[name])
        return result


@dataclass(frozen=True, slots=True)
class LookupResponse:
    query: str
    matches: tuple[GlossaryEntry, ...] = ()
    suggestions: tuple[str, ...] = ()
    source: str = "none"

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "source": self.source,
            "matches": [entry.to_dict() for entry in self.matches],
            "suggestions": list(self.suggestions),
        }


def _require_string(row: dict[str, Any], key: str, index: int, *, allow_empty: bool = False) -> str:
    value = row.get(key)
    if not isinstance(value, str):
        raise ValueError(f"Entry {index}: `{key}` must be a string")
    value = value.strip()
    if not value and not allow_empty:
        raise ValueError(f"Entry {index}: `{key}` must not be empty")
    return value


def _optional_string(row: dict[str, Any], key: str, index: int) -> str:
    value = row.get(key, "")
    if not isinstance(value, str):
        raise ValueError(f"Entry {index}: `{key}` must be a string")
    return value.strip()


def _string_list(row: dict[str, Any], key: str, index: int) -> tuple[str, ...]:
    value = row.get(key, [])
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"Entry {index}: `{key}` must be an array of strings")
    return tuple(item.strip() for item in value if item.strip())


def load_glossary(path: Path) -> list[GlossaryEntry]:
    """Load a schema-versioned TOML glossary."""

    path = Path(path).expanduser().resolve()
    with path.open("rb") as handle:
        document = tomllib.load(handle)

    metadata = document.get("glossary")
    if not isinstance(metadata, dict):
        raise ValueError(f"{path}: missing `[glossary]` metadata table")
    if metadata.get("schema_version") != 1:
        raise ValueError(f"{path}: unsupported or missing glossary schema version")

    rows = document.get("entries")
    if not isinstance(rows, list):
        raise ValueError(f"{path}: `[[entries]]` must be an array of tables")

    entries: list[GlossaryEntry] = []
    seen_ids: set[str] = set()
    for index, raw_row in enumerate(rows, start=1):
        if not isinstance(raw_row, dict):
            raise ValueError(f"Entry {index}: expected a TOML table")
        row = dict(raw_row)
        entry_id = _require_string(row, "id", index)
        if entry_id in seen_ids:
            raise ValueError(f"Entry {index}: duplicate id `{entry_id}`")
        seen_ids.add(entry_id)

        english = _require_string(row, "english", index)
        status = _require_string(row, "status", index)
        if status not in ALLOWED_STATUSES:
            allowed = ", ".join(sorted(ALLOWED_STATUSES))
            raise ValueError(f"Entry {index}: `status` must be one of {allowed}")
        persian = _require_string(row, "persian", index, allow_empty=status == "reference")
        concept_id = _optional_string(row, "concept_id", index) or entry_id

        source_page = row.get("source_page")
        if source_page is not None and (not isinstance(source_page, int) or source_page < 1):
            raise ValueError(f"Entry {index}: `source_page` must be a positive integer")

        string_values = {name: _optional_string(row, name, index) for name in STRING_FIELDS}
        list_values = {name: _string_list(row, name, index) for name in LIST_FIELDS}
        if status in {"approved", "proposed"} and not string_values["preferred_fa"]:
            string_values["preferred_fa"] = persian

        entries.append(
            GlossaryEntry(
                id=entry_id,
                concept_id=concept_id,
                english=english,
                persian=persian,
                status=status,
                source_page=source_page,
                extra={key: value for key, value in row.items() if key not in KNOWN_FIELDS},
                **string_values,
                **list_values,
            )
        )
    return entries


DASHES_AND_SEPARATORS = str.maketrans({
    "-": " ",
    "‐": " ",
    "‑": " ",
    "‒": " ",
    "–": " ",
    "—": " ",
    "―": " ",
    "_": " ",
    "/": " ",
})


def normalize_english(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).translate(DASHES_AND_SEPARATORS).casefold()
    value = re.sub(r"[()\[\]{},.;:]+", " ", value)
    return " ".join(value.split())


def _matching_entries(entries: Sequence[GlossaryEntry], query_key: str) -> tuple[GlossaryEntry, ...]:
    return tuple(
        entry
        for entry in entries
        if any(normalize_english(key) == query_key for key in entry.lookup_keys)
    )


def _suggestions(
    query_key: str,
    entries: Sequence[GlossaryEntry],
    limit: int,
) -> tuple[str, ...]:
    key_to_display: dict[str, str] = {}
    for entry in entries:
        key_to_display.setdefault(normalize_english(entry.english), entry.english)
    prefix_keys = [
        key for key in key_to_display
        if key.startswith(query_key) or query_key.startswith(key)
    ]
    close_keys = difflib.get_close_matches(query_key, key_to_display, n=limit * 2, cutoff=0.55)
    ordered = sorted(prefix_keys, key=lambda key: (abs(len(key) - len(query_key)), key)) + close_keys
    return tuple(dict.fromkeys(key_to_display[key] for key in ordered if key in key_to_display))[:limit]


def lookup_english_to_persian(
    query: str,
    custom_glossary: Path | None = None,
    *,
    include_builtin: bool = True,
    suggestion_limit: int = 5,
) -> LookupResponse:
    """Look up an English term, with custom entries overriding bundled IPL data."""

    query = query.strip()
    if not query:
        raise ValueError("Lookup query must not be empty")
    if suggestion_limit < 0:
        raise ValueError("Suggestion limit must be non-negative")
    query_key = normalize_english(query)

    custom_entries = load_glossary(custom_glossary) if custom_glossary else []
    custom_matches = _matching_entries(custom_entries, query_key)
    if custom_matches:
        return LookupResponse(query=query, matches=custom_matches, source="custom")

    builtin_entries = load_glossary(BUILTIN_GLOSSARY) if include_builtin else []
    builtin_matches = _matching_entries(builtin_entries, query_key)
    if builtin_matches:
        return LookupResponse(query=query, matches=builtin_matches, source="builtin")

    suggestion_pool = [*custom_entries, *builtin_entries]
    return LookupResponse(
        query=query,
        suggestions=_suggestions(query_key, suggestion_pool, suggestion_limit),
    )


def render_text(response: LookupResponse) -> str:
    if not response.matches:
        if response.suggestions:
            return "No exact match. Suggestions: " + ", ".join(response.suggestions)
        return "No exact match."

    blocks: list[str] = []
    for entry in response.matches:
        translations = "؛ ".join(entry.translations) or "[no Persian equivalent in source]"
        lines = [f"{entry.english} → {translations}", f"  status: {entry.status}"]
        if entry.source_or_authority:
            source = entry.source_or_authority
            if entry.source_page:
                source += f", p. {entry.source_page}"
            lines.append(f"  source: {source}")
        if entry.notes:
            lines.append("  notes: " + " ".join(entry.notes))
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Look up English terms in TOML terminology glossaries.")
    parser.add_argument("query", nargs="+", help="English term or acronym to look up.")
    parser.add_argument("--glossary", type=Path, help="Custom TOML glossary; matching entries override IPL data.")
    parser.add_argument("--no-builtin", action="store_true", help="Do not fall back to the bundled IPL glossary.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--limit", type=int, default=5, help="Maximum no-match suggestions (default: 5).")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        response = lookup_english_to_persian(
            " ".join(args.query),
            args.glossary,
            include_builtin=not args.no_builtin,
            suggestion_limit=args.limit,
        )
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(response.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(render_text(response))
    return 0 if response.matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
