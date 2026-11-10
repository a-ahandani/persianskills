#!/usr/bin/env python3
"""Convert the provided IPL Signal Processing Glossary PDF to a terminology TOML register."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import pdfplumber
import tomlkit

EXPECTED_ENTRY_COUNT = 1814
EXPECTED_EMPTY_TRANSLATIONS = {"Prepend"}
LEFT_COLUMN = (36.0, 30.0, 285.0)
RIGHT_COLUMN = (315.79, 305.0, 565.0)
SOURCE_AUTHORITY = (
    "Signal Processing Glossary; Shohreh Kasaei; Image Processing Lab (IPL); "
    "Sharif University of Technology"
)

# These corrections repair extraction-only punctuation without changing terms.
SAFE_LAYOUT_CORRECTIONS = {
    "Yaw": "چرخش افقی (چرخش حول محور عمودی)",
}


@dataclass(slots=True)
class ExtractedEntry:
    english: str
    persian: str
    source_page: int
    top: float


def contains_latin(value: str) -> bool:
    return any(character.isascii() and character.isalpha() for character in value)


def contains_persian(value: str) -> bool:
    return any("\u0600" <= character <= "\u06ff" for character in value)


def reverse_pdf_rtl_token(value: str) -> str:
    if contains_persian(value):
        return value[::-1]
    return value


def join_translation(words: list[dict[str, Any]]) -> str:
    lines: list[list[dict[str, Any]]] = []
    for word in sorted(words, key=lambda item: (item["top"], -item["x0"])):
        if not lines or abs(lines[-1][0]["top"] - word["top"]) > 2:
            lines.append([word])
        else:
            lines[-1].append(word)

    tokens: list[str] = []
    for line in lines:
        for word in sorted(line, key=lambda item: -item["x0"]):
            tokens.append(reverse_pdf_rtl_token(word["text"]))

    text = " ".join(tokens)
    text = re.sub(r"\s+([،؛:؟,.!?])", r"\1", text)
    text = re.sub(r"([،؛:؟,.!?])(?=\S)", r"\1 ", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    text = re.sub(r"\s+", " ", text).strip(" ،")
    return unicodedata.normalize("NFC", text)


def extract_column(
    words: list[dict[str, Any]],
    page_number: int,
    column: tuple[float, float, float],
) -> list[ExtractedEntry]:
    base, minimum_x, maximum_x = column
    starts = [
        word
        for word in words
        if abs(word["x0"] - base) < 1
        and contains_latin(word["text"])
        and not (len(word["text"]) == 1 and word["text"].isupper())
    ]
    starts.sort(key=lambda item: item["top"])

    draft: list[ExtractedEntry] = []
    for index, start in enumerate(starts):
        bottom = starts[index + 1]["top"] - 1 if index + 1 < len(starts) else 775
        region = [
            word
            for word in words
            if minimum_x <= word["x0"] < maximum_x
            and start["top"] - 1 <= word["top"] < bottom
        ]
        english_words = [
            word
            for word in region
            if abs(word["top"] - start["top"]) < 2
            and contains_latin(word["text"])
            and not contains_persian(word["text"])
        ]
        english_ids = {id(word) for word in english_words}
        translation_words = [
            word
            for word in region
            if id(word) not in english_ids
            and (contains_persian(word["text"]) or re.fullmatch(r"[()]", word["text"]))
        ]
        english = " ".join(word["text"] for word in sorted(english_words, key=lambda item: item["x0"]))
        draft.append(
            ExtractedEntry(
                english=unicodedata.normalize("NFC", english.strip()),
                persian=join_translation(translation_words),
                source_page=page_number,
                top=start["top"],
            )
        )

    # Word exported several long English headings as a second visual line.
    merged: list[ExtractedEntry] = []
    for entry in draft:
        if not entry.persian and merged and entry.top - merged[-1].top < 17:
            separator = "" if merged[-1].english.endswith("-") else " "
            merged[-1].english += separator + entry.english
            continue
        merged.append(entry)
    return merged


def extract_entries(pdf_path: Path) -> list[ExtractedEntry]:
    entries: list[ExtractedEntry] = []
    with pdfplumber.open(pdf_path) as document:
        if len(document.pages) != 31:
            raise ValueError(f"Expected a 31-page IPL glossary, found {len(document.pages)} pages")
        for page_number, page in enumerate(document.pages[1:], start=2):
            words = page.extract_words(use_text_flow=False, keep_blank_chars=False)
            entries.extend(extract_column(words, page_number, LEFT_COLUMN))
            entries.extend(extract_column(words, page_number, RIGHT_COLUMN))

    entries.sort(key=lambda entry: (entry.english.casefold(), entry.source_page, entry.top))
    for entry in entries:
        entry.persian = SAFE_LAYOUT_CORRECTIONS.get(entry.english, entry.persian)
    validate_extraction(entries)
    return entries


def validate_extraction(entries: list[ExtractedEntry]) -> None:
    if len(entries) != EXPECTED_ENTRY_COUNT:
        raise ValueError(f"Expected {EXPECTED_ENTRY_COUNT} entries, extracted {len(entries)}")
    if any(not entry.english for entry in entries):
        raise ValueError("Extraction produced an empty English headword")
    empty = {entry.english for entry in entries if not entry.persian}
    if empty != EXPECTED_EMPTY_TRANSLATIONS:
        raise ValueError(f"Unexpected empty Persian translations: {sorted(empty)}")
    controls = {
        character
        for entry in entries
        for character in entry.persian
        if unicodedata.category(character) == "Cf"
    }
    if controls:
        values = ", ".join(f"U+{ord(character):04X}" for character in sorted(controls))
        raise ValueError(f"Extraction retained bidi/control characters: {values}")


def slugify(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_value = decomposed.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "_", ascii_value).strip("_")
    return slug or "entry"


def split_candidates(value: str) -> list[str]:
    return list(dict.fromkeys(part.strip() for part in re.split(r"[،,]", value) if part.strip()))


def extract_acronym(value: str) -> str:
    match = re.search(r"\(([A-Za-z0-9-]{2,8})\)$", value)
    if not match:
        return ""
    candidate = match.group(1)
    return candidate if sum(character.isupper() for character in candidate) >= 2 else ""


def build_document(entries: list[ExtractedEntry]) -> str:
    document = tomlkit.document()
    document.add(tomlkit.comment("Generated from the provided IPL glossary PDF; edit source corrections in the importer."))

    metadata = tomlkit.table()
    metadata.add("schema_version", 1)
    metadata.add("title", "Signal Processing Glossary")
    metadata.add("author", "Shohreh Kasaei")
    metadata.add("organization", "Image Processing Lab (IPL), Sharif University of Technology")
    metadata.add("created", "2009-08")
    metadata.add("edition_date", "2025-12-01")
    metadata.add("source_file", "IPL Glossary.pdf")
    metadata.add("source_license", "No license statement was found in the provided PDF.")
    metadata.add("language_from", "en")
    metadata.add("language_to", "fa")
    metadata.add("entry_count", len(entries))
    metadata.add("authority", "reference-candidate-only")
    document.add("glossary", metadata)

    id_counts: Counter[str] = Counter()
    tables = tomlkit.aot()
    for entry in entries:
        base_id = f"ipl_{slugify(entry.english)}"
        id_counts[base_id] += 1
        entry_id = base_id if id_counts[base_id] == 1 else f"{base_id}_{id_counts[base_id]}"

        table = tomlkit.table()
        table.add("id", entry_id)
        table.add("concept_id", entry_id)
        table.add("english", entry.english)
        table.add("persian", entry.persian)
        acronym = extract_acronym(entry.english)
        if acronym:
            table.add("acronym", acronym)
        candidates = split_candidates(entry.persian)
        if candidates:
            table.add("candidates", candidates)
        table.add("source_or_authority", SOURCE_AUTHORITY)
        table.add("category", entry.english[0].upper() if entry.english[0].isalpha() else "other")
        table.add("source_page", entry.source_page)
        table.add("status", "reference")
        if not entry.persian:
            table.add("notes", ["The source PDF provides no Persian equivalent for this headword."])
        tables.append(table)
    document.add("entries", tables)
    return tomlkit.dumps(document)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Path to the IPL glossary PDF.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("assets/terminology-register.toml"),
        help="Generated TOML path (default: assets/terminology-register.toml).",
    )
    parser.add_argument("--check", action="store_true", help="Fail if the existing output differs; do not write.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        entries = extract_entries(args.pdf)
        output = build_document(entries)
        if args.check:
            if not args.output.exists() or args.output.read_text(encoding="utf-8") != output:
                print(f"error: {args.output} is stale", file=sys.stderr)
                return 1
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output, encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"Validated {len(entries)} IPL glossary entries in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
