#!/usr/bin/env python3
"""Conservative static audit helper for Virastar manuscripts.

The checker is intentionally narrower than the accompanying editorial skill. It
finds deterministic candidates and workspace-integrity problems; it does not
make substantive scientific or linguistic judgments.

Python 3.11+; standard library only.
"""

from __future__ import annotations

import argparse
import bisect
import datetime as dt
import difflib
import hashlib
import json
import os
import re
import shutil
import sys
import textwrap
from collections import Counter, defaultdict, deque
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

try:
    import tomllib
except ModuleNotFoundError as exc:  # pragma: no cover - Python < 3.11
    raise SystemExit("Python 3.11+ is required (tomllib is used).") from exc

try:
    from scripts.terminology import GlossaryEntry as TermEntry, load_glossary
except ModuleNotFoundError:  # Direct execution from the scripts directory.
    from terminology import GlossaryEntry as TermEntry, load_glossary

VERSION = "0.2.0"
TEXT_EXTENSIONS = {".tex", ".md", ".markdown", ".txt"}
BIB_EXTENSIONS = {".bib"}
ALL_EXTENSIONS = TEXT_EXTENSIONS | BIB_EXTENSIONS

PERSIAN_RANGE = "\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF"
PERSIAN_LETTER_RE = re.compile(f"[{PERSIAN_RANGE}]")

ARABIC_TO_PERSIAN = str.maketrans({
    "ي": "ی",  # U+064A -> U+06CC
    "ى": "ی",  # U+0649 -> U+06CC, conservative code-point normalization
    "ك": "ک",  # U+0643 -> U+06A9
})

BIDI_CONTROLS = {
    "\u202a": "LEFT-TO-RIGHT EMBEDDING",
    "\u202b": "RIGHT-TO-LEFT EMBEDDING",
    "\u202c": "POP DIRECTIONAL FORMATTING",
    "\u202d": "LEFT-TO-RIGHT OVERRIDE",
    "\u202e": "RIGHT-TO-LEFT OVERRIDE",
    "\u2066": "LEFT-TO-RIGHT ISOLATE",
    "\u2067": "RIGHT-TO-LEFT ISOLATE",
    "\u2068": "FIRST STRONG ISOLATE",
    "\u2069": "POP DIRECTIONAL ISOLATE",
    "\u200e": "LEFT-TO-RIGHT MARK",
    "\u200f": "RIGHT-TO-LEFT MARK",
}

DEFAULT_PROTECTED_COMMANDS = {
    "cite", "citet", "citep", "parencite", "textcite", "autocite", "footcite",
    "nocite", "ref", "pageref", "eqref", "autoref", "cref", "Cref", "vref",
    "label", "gls", "Gls", "glspl", "acrshort", "acrlong", "acrfull",
    "url", "href", "path", "email", "includegraphics", "input", "include",
    "subfile", "bibliography", "addbibresource", "bibliographystyle", "index",
    "lstinline", "verb",
}

DEFAULT_PROTECTED_ENVIRONMENTS = {
    "equation", "equation*", "align", "align*", "alignat", "alignat*", "gather",
    "gather*", "multline", "multline*", "displaymath", "math", "verbatim",
    "verbatim*", "lstlisting", "minted", "tikzpicture", "asy",
}

STYLE_PHRASES: dict[str, str] = {
    "لازم به ذکر است": "Delete it when the following proposition can stand directly; otherwise state the actual relevance.",
    "شایان ذکر است": "Delete it when it only announces importance; state the important fact directly.",
    "شایان توجه است": "State the evidential or argumentative reason for attention instead of announcing it.",
    "در راستای": "Check whether a precise relation such as برای، با هدف، در چارچوب، or بر پایه is intended.",
    "در خصوص": "Consider درباره or a more precise syntactic relation when no venue preference requires this form.",
    "در رابطه با": "Consider درباره، از نظر، در مقایسه با, or the exact relation.",
    "مورد بررسی قرار گرفت": "Consider naming the actor/procedure and using بررسی شد/بررسی کرد when meaning remains unchanged.",
    "مورد استفاده قرار گرفت": "Consider به کار رفت/استفاده شد and make agency explicit where relevant.",
    "می\u200cباشد": "This is grammatical in many contexts but often bureaucratic; consider است only when semantics and register permit.",
}

DRAFT_MARKERS = re.compile(r"(?i)(?<![A-Za-z])(TODO|FIXME|XXX|TBD|DRAFT|PLACEHOLDER)(?![A-Za-z])")


@dataclass(slots=True)
class Finding:
    prefix: str
    rule: str
    title: str
    severity: str
    confidence: str
    layer: str
    edit_risk: str
    authority: list[str]
    path: str
    line: int
    column: int
    original: str
    diagnosis: str
    why_it_matters: str
    proposed_repair: str
    context: str = ""
    dependencies: list[str] = field(default_factory=list)
    fingerprint: str = ""
    id: str = ""

    def finalize(self) -> None:
        seed = "\x1f".join(
            [self.prefix, self.rule, self.path, self.original.strip(), self.context.strip()]
        )
        self.fingerprint = hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12]
        self.id = f"{self.prefix}-{self.fingerprint[:7].upper()}"

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        return data


@dataclass(slots=True)
class SourceText:
    path: Path
    text: str
    masked: str
    protected: list[bool]
    line_starts: list[int]

    @classmethod
    def build(
        cls,
        path: Path,
        text: str,
        protected_commands: set[str],
        protected_environments: set[str],
    ) -> "SourceText":
        suffix = path.suffix.lower()
        if suffix == ".tex":
            protected = build_tex_protection(text, protected_commands, protected_environments)
        elif suffix in {".md", ".markdown"}:
            protected = build_markdown_protection(text)
        elif suffix == ".bib":
            protected = [True] * len(text)
        else:
            protected = build_generic_protection(text)

        # URLs, e-mail addresses, and DOI-like identifiers are protected in all text formats.
        add_regex_protection(
            text,
            protected,
            re.compile(r"(?i)\b(?:https?://|ftp://|www\.)\S+|\b\S+@\S+\.\S+|\b10\.\d{4,9}/\S+"),
        )
        masked = "".join(" " if protected[i] and ch != "\n" else ch for i, ch in enumerate(text))
        starts = [0]
        starts.extend(i + 1 for i, ch in enumerate(text) if ch == "\n")
        return cls(path=path, text=text, masked=masked, protected=protected, line_starts=starts)

    def line_col(self, index: int) -> tuple[int, int]:
        line_idx = bisect.bisect_right(self.line_starts, index) - 1
        return line_idx + 1, index - self.line_starts[line_idx] + 1

    def line_text(self, line: int) -> str:
        start = self.line_starts[max(0, line - 1)]
        if line < len(self.line_starts):
            end = self.line_starts[line] - 1
        else:
            end = len(self.text)
        return self.text[start:end].strip()

    def span_is_plain(self, start: int, end: int) -> bool:
        return not any(self.protected[start:end])


@dataclass(slots=True)
class AuditResult:
    targets: list[str]
    files: list[str]
    profile_path: str | None
    terms_path: str | None
    findings: list[Finding]
    safe_fix_diffs: list[str]
    safe_fix_files: list[str]
    assumptions: list[str]
    metadata: dict[str, Any]


# ---------------------------------------------------------------------------
# Protection/masking
# ---------------------------------------------------------------------------


def mark(protected: list[bool], start: int, end: int) -> None:
    start = max(0, start)
    end = min(len(protected), end)
    for i in range(start, end):
        protected[i] = True


def add_regex_protection(text: str, protected: list[bool], pattern: re.Pattern[str]) -> None:
    for match in pattern.finditer(text):
        mark(protected, match.start(), match.end())


def is_escaped(text: str, index: int) -> bool:
    backslashes = 0
    i = index - 1
    while i >= 0 and text[i] == "\\":
        backslashes += 1
        i -= 1
    return bool(backslashes % 2)


def balanced_brace_end(text: str, open_index: int) -> int | None:
    if open_index >= len(text) or text[open_index] != "{":
        return None
    depth = 0
    i = open_index
    while i < len(text):
        ch = text[i]
        if ch == "{" and not is_escaped(text, i):
            depth += 1
        elif ch == "}" and not is_escaped(text, i):
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None


def build_tex_protection(
    text: str,
    protected_commands: set[str],
    protected_environments: set[str],
) -> list[bool]:
    protected = [False] * len(text)

    # Comments.
    for line_match in re.finditer(r".*(?:\n|$)", text):
        segment = line_match.group(0)
        for offset, ch in enumerate(segment):
            absolute = line_match.start() + offset
            if ch == "%" and not is_escaped(text, absolute):
                mark(protected, absolute, line_match.end())
                break

    # Verbatim-like environments and protected mathematical environments.
    env_names = sorted(protected_environments, key=len, reverse=True)
    if env_names:
        env_alt = "|".join(re.escape(name) for name in env_names)
        env_re = re.compile(
            rf"\\begin\s*\{{(?P<env>{env_alt})\}}.*?\\end\s*\{{(?P=env)\}}",
            re.DOTALL,
        )
        for match in env_re.finditer(text):
            mark(protected, match.start(), match.end())

    # \verb and \lstinline have delimiter-based arguments.
    for cmd_match in re.finditer(r"\\(?:verb\*?|lstinline)(?![A-Za-z@])", text):
        i = cmd_match.end()
        while i < len(text) and text[i].isspace() and text[i] != "\n":
            i += 1
        if i >= len(text):
            continue
        delim = text[i]
        end = text.find(delim, i + 1)
        mark(protected, cmd_match.start(), len(text) if end == -1 else end + 1)

    # Display/inline math delimiters. This is conservative and deliberately
    # ignores already protected spans.
    i = 0
    while i < len(text):
        if protected[i]:
            i += 1
            continue
        if text.startswith("\\[", i):
            end = text.find("\\]", i + 2)
            mark(protected, i, len(text) if end == -1 else end + 2)
            i = len(text) if end == -1 else end + 2
            continue
        if text.startswith("\\(", i):
            end = text.find("\\)", i + 2)
            mark(protected, i, len(text) if end == -1 else end + 2)
            i = len(text) if end == -1 else end + 2
            continue
        if text[i] == "$" and not is_escaped(text, i):
            delim = "$$" if text.startswith("$$", i) else "$"
            end = text.find(delim, i + len(delim))
            while end != -1 and is_escaped(text, end):
                end = text.find(delim, end + len(delim))
            mark(protected, i, len(text) if end == -1 else end + len(delim))
            i = len(text) if end == -1 else end + len(delim)
            continue
        i += 1

    # Protect command names. Protect complete arguments only for commands whose
    # arguments are identifiers, paths, citations, references, or raw content.
    command_re = re.compile(r"\\(?P<name>[A-Za-z@]+)\*?")
    for match in command_re.finditer(text):
        mark(protected, match.start(), match.end())
        name = match.group("name")
        if name not in protected_commands:
            continue
        i = match.end()
        # Optional argument(s).
        while i < len(text) and text[i].isspace():
            i += 1
        while i < len(text) and text[i] == "[":
            end = text.find("]", i + 1)
            if end == -1:
                mark(protected, i, len(text))
                i = len(text)
                break
            mark(protected, i, end + 1)
            i = end + 1
            while i < len(text) and text[i].isspace():
                i += 1
        # One or two braced arguments (href commonly has two, but its visible
        # text is intentionally protected because URL macros have project-specific semantics).
        arg_count = 2 if name == "href" else 1
        for _ in range(arg_count):
            while i < len(text) and text[i].isspace():
                i += 1
            if i < len(text) and text[i] == "{":
                end = balanced_brace_end(text, i)
                if end is None:
                    mark(protected, i, len(text))
                    break
                mark(protected, i, end)
                i = end

    return protected


def build_markdown_protection(text: str) -> list[bool]:
    protected = [False] * len(text)
    # Fenced code blocks.
    fence_re = re.compile(r"(?ms)^\s*(```+|~~~+).*?^\s*\1\s*$")
    for match in fence_re.finditer(text):
        mark(protected, match.start(), match.end())
    # Inline code.
    for match in re.finditer(r"(?s)(?<!`)`+[^`\n]*?`+", text):
        mark(protected, match.start(), match.end())
    # Link destinations and autolinks.
    for match in re.finditer(r"\]\((?:[^()\\]|\\.)*\)|<https?://[^>]+>", text):
        mark(protected, match.start(), match.end())
    return protected


def build_generic_protection(text: str) -> list[bool]:
    return [False] * len(text)


def quote_protection(text: str, base: Sequence[bool]) -> list[bool]:
    """Return a stricter mask for auto-fix: direct quotations are not rewritten."""
    protected = list(base)
    for pattern in (
        re.compile(r"«[^»\n]*»"),
        re.compile(r'"[^"\n]*"'),
        re.compile(r"‘[^’\n]*’|“[^”\n]*”"),
    ):
        for match in pattern.finditer(text):
            mark(protected, match.start(), match.end())
    return protected


# ---------------------------------------------------------------------------
# Loading project data
# ---------------------------------------------------------------------------


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def load_profile(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    with path.open("rb") as handle:
        return tomllib.load(handle)


def load_terms(path: Path | None) -> list[TermEntry]:
    if path is None:
        return []
    return load_glossary(path)


def profile_list(profile: dict[str, Any], section: str, key: str, default: Iterable[str]) -> set[str]:
    value = profile.get(section, {}).get(key)
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return set(value)
    return set(default)


# ---------------------------------------------------------------------------
# File discovery and LaTeX dependency graph
# ---------------------------------------------------------------------------


def normalize_target(path: Path) -> Path:
    return path.expanduser().resolve()


def iter_directory_files(root: Path) -> Iterator[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in {".git", "build", "out", "dist", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() in ALL_EXTENSIONS:
            yield path


def resolve_tex_candidate(base: Path, raw: str, extensions: Sequence[str]) -> Path | None:
    cleaned = raw.strip()
    if not cleaned or any(token in cleaned for token in ("#", "\\", "{")):
        return None
    candidate = (base / cleaned).resolve()
    if candidate.suffix:
        return candidate
    for ext in extensions:
        with_ext = candidate.with_suffix(ext)
        if with_ext.exists():
            return with_ext
    return candidate.with_suffix(extensions[0])


def discover_from_tex_roots(
    roots: list[Path],
) -> tuple[set[Path], list[tuple[Path, str, str, int]], set[Path], set[Path]]:
    """Return text files, missing dependencies, bibliography files, assets."""
    discovered: set[Path] = set()
    bib_files: set[Path] = set()
    asset_files: set[Path] = set()
    missing: list[tuple[Path, str, str, int]] = []
    queue: deque[Path] = deque(path.resolve() for path in roots)

    include_re = re.compile(r"\\(?P<cmd>input|include|subfile)\s*(?:\[[^\]]*\])?\s*\{(?P<arg>[^}]+)\}")
    addbib_re = re.compile(r"\\addbibresource\s*(?:\[[^\]]*\])?\s*\{(?P<arg>[^}]+)\}")
    bib_re = re.compile(r"\\bibliography\s*\{(?P<arg>[^}]+)\}")
    graphic_re = re.compile(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{(?P<arg>[^}]+)\}")

    while queue:
        path = queue.popleft()
        if path in discovered:
            continue
        discovered.add(path)
        if not path.exists() or path.suffix.lower() != ".tex":
            continue
        text = read_text(path)
        base = path.parent

        for match in include_re.finditer(text):
            candidate = resolve_tex_candidate(base, match.group("arg"), [".tex"])
            if candidate is None:
                continue
            line = text.count("\n", 0, match.start()) + 1
            if candidate.exists():
                queue.append(candidate)
            else:
                missing.append((path, match.group("cmd"), match.group("arg"), line))

        for match in addbib_re.finditer(text):
            candidate = resolve_tex_candidate(base, match.group("arg"), [".bib"])
            if candidate is None:
                continue
            line = text.count("\n", 0, match.start()) + 1
            if candidate.exists():
                bib_files.add(candidate)
            else:
                missing.append((path, "addbibresource", match.group("arg"), line))

        for match in bib_re.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            for item in match.group("arg").split(","):
                candidate = resolve_tex_candidate(base, item, [".bib"])
                if candidate is None:
                    continue
                if candidate.exists():
                    bib_files.add(candidate)
                else:
                    missing.append((path, "bibliography", item.strip(), line))

        for match in graphic_re.finditer(text):
            raw = match.group("arg").strip()
            line = text.count("\n", 0, match.start()) + 1
            candidate = (base / raw).resolve()
            candidates = [candidate] if candidate.suffix else [
                candidate.with_suffix(ext) for ext in (".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg")
            ]
            found = next((item for item in candidates if item.exists()), None)
            if found:
                asset_files.add(found)
            elif not any(token in raw for token in ("#", "\\", "{")):
                missing.append((path, "includegraphics", raw, line))

    discovered.update(bib_files)
    return discovered, missing, bib_files, asset_files


def collect_files(targets: list[Path], root: Path | None) -> tuple[set[Path], list[tuple[Path, str, str, int]], set[Path], set[Path]]:
    files: set[Path] = set()
    tex_roots: list[Path] = []
    missing: list[tuple[Path, str, str, int]] = []
    bib_files: set[Path] = set()
    assets: set[Path] = set()

    all_targets = list(targets)
    if root is not None:
        all_targets.append(root)

    for target in all_targets:
        if target.is_dir():
            files.update(iter_directory_files(target))
        elif target.is_file():
            files.add(target)
            if target.suffix.lower() == ".tex":
                tex_roots.append(target)
        else:
            raise FileNotFoundError(f"Target does not exist: {target}")

    if root is not None and root.suffix.lower() == ".tex":
        tex_roots.append(root)

    if tex_roots:
        graph_files, graph_missing, graph_bibs, graph_assets = discover_from_tex_roots(tex_roots)
        files.update(graph_files)
        missing.extend(graph_missing)
        bib_files.update(graph_bibs)
        assets.update(graph_assets)

    files = {path.resolve() for path in files if path.suffix.lower() in ALL_EXTENSIONS and path.exists()}
    return files, missing, bib_files, assets


# ---------------------------------------------------------------------------
# Finding helpers
# ---------------------------------------------------------------------------


def make_finding(
    source: SourceText,
    start: int,
    end: int,
    *,
    prefix: str,
    rule: str,
    title: str,
    severity: str,
    confidence: str,
    layer: str,
    edit_risk: str,
    authority: Sequence[str],
    diagnosis: str,
    why: str,
    proposed: str,
    original: str | None = None,
) -> Finding:
    line, column = source.line_col(start)
    finding = Finding(
        prefix=prefix,
        rule=rule,
        title=title,
        severity=severity,
        confidence=confidence,
        layer=layer,
        edit_risk=edit_risk,
        authority=list(authority),
        path=str(source.path),
        line=line,
        column=column,
        original=source.text[start:end] if original is None else original,
        diagnosis=diagnosis,
        why_it_matters=why,
        proposed_repair=proposed,
        context=source.line_text(line),
    )
    finding.finalize()
    return finding


def literal_findings(
    source: SourceText,
    needle: str,
    **kwargs: Any,
) -> Iterator[Finding]:
    start = 0
    while True:
        index = source.masked.find(needle, start)
        if index == -1:
            return
        end = index + len(needle)
        if source.span_is_plain(index, end):
            yield make_finding(source, index, end, original=source.text[index:end], **kwargs)
        start = max(end, index + 1)


def regex_findings(source: SourceText, pattern: re.Pattern[str], **kwargs: Any) -> Iterator[Finding]:
    for match in pattern.finditer(source.masked):
        start, end = match.span()
        if source.span_is_plain(start, end):
            yield make_finding(source, start, end, original=source.text[start:end], **kwargs)


def count_persian(text: str) -> int:
    return len(PERSIAN_LETTER_RE.findall(text))


def is_persian_context(source: SourceText, index: int) -> bool:
    line, _ = source.line_col(index)
    line_text = source.line_text(line)
    return count_persian(line_text) >= 3


# ---------------------------------------------------------------------------
# Text checks
# ---------------------------------------------------------------------------


def check_unicode(source: SourceText) -> list[Finding]:
    findings: list[Finding] = []
    mapping = {
        "ي": ("Arabic Yeh in Persian prose", "Replace U+064A with Persian Yeh U+06CC (`ی`) after confirming this is not a faithful Arabic quotation or identifier."),
        "ى": ("Arabic Alef Maksura in Persian prose", "Replace U+0649 with Persian Yeh U+06CC (`ی`) when it represents Persian yeh."),
        "ك": ("Arabic Kaf in Persian prose", "Replace U+0643 with Persian Kaf U+06A9 (`ک`) after confirming the span is Persian prose."),
    }
    for char, (title, repair) in mapping.items():
        for finding in literal_findings(
            source,
            char,
            prefix="UNI",
            rule=f"codepoint-{ord(char):04x}",
            title=title,
            severity="MINOR",
            confidence="HIGH",
            layer="MECHANICAL",
            edit_risk="SAFE",
            authority=["UNICODE", "ACADEMY"],
            diagnosis=f"The character is U+{ord(char):04X}, not the normal Persian code point used in Persian prose.",
            why="Mixed Arabic/Persian code points break search, sorting, term matching, and consistent rendering.",
            proposed=repair,
        ):
            findings.append(finding)

    for finding in literal_findings(
        source,
        "ـ",
        prefix="UNI",
        rule="tatweel",
        title="Tatweel/kashida in source text",
        severity="MINOR",
        confidence="HIGH",
        layer="MECHANICAL",
        edit_risk="SAFE",
        authority=["UNICODE", "EDITORIAL"],
        diagnosis="U+0640 tatweel is being used in the stored text.",
        why="Manual elongation is fragile in search, copy/paste, indexing, and TeX shaping; layout should be handled typographically.",
        proposed="Remove the tatweel unless exact quoted/archival typography must be preserved.",
    ):
        findings.append(finding)

    for finding in regex_findings(
        source,
        re.compile("\u200c{2,}"),
        prefix="UNI",
        rule="repeated-zwnj",
        title="Repeated ZWNJ",
        severity="MINOR",
        confidence="HIGH",
        layer="MECHANICAL",
        edit_risk="SAFE",
        authority=["UNICODE", "ACADEMY"],
        diagnosis="Two or more zero-width non-joiners occur consecutively.",
        why="Repeated invisible controls create unstable matching and are not an orthographic distinction.",
        proposed="Collapse the sequence to one ZWNJ after checking the word boundary.",
    ):
        findings.append(finding)

    for char, name in BIDI_CONTROLS.items():
        for finding in literal_findings(
            source,
            char,
            prefix="UNI",
            rule=f"bidi-{ord(char):04x}",
            title=f"Bidirectional control: {name}",
            severity="MAJOR" if char in {"\u202d", "\u202e"} else "MINOR",
            confidence="HIGH",
            layer="MECHANICAL",
            edit_risk="MEANING-SENSITIVE",
            authority=["UNICODE"],
            diagnosis=f"The source contains {name} (U+{ord(char):04X}).",
            why="Invisible direction controls can reorder visible text, hide source differences, or create unsafe identifiers.",
            proposed="Inspect the exact code point and rendered output; replace it with semantic TeX/HTML direction handling when it is not demonstrably required.",
        ):
            findings.append(finding)

    for finding in literal_findings(
        source,
        "\u200d",
        prefix="UNI",
        rule="zwj",
        title="Zero-width joiner in Persian prose",
        severity="MINOR",
        confidence="MEDIUM",
        layer="MECHANICAL",
        edit_risk="MEANING-SENSITIVE",
        authority=["UNICODE"],
        diagnosis="U+200D zero-width joiner occurs in a plain-text span.",
        why="ZWJ is rarely needed in ordinary Persian scholarly prose and may alter glyph joining invisibly.",
        proposed="Inspect context and remove only if no deliberate shaping requirement exists.",
    ):
        findings.append(finding)

    # Mixed digit scripts inside one numeric token.
    number_re = re.compile(r"[0-9۰-۹٠-٩]+(?:[.,٫٬][0-9۰-۹٠-٩]+)*")
    for match in number_re.finditer(source.masked):
        if not source.span_is_plain(*match.span()):
            continue
        token = source.text[match.start():match.end()]
        scripts = set()
        if re.search(r"[0-9]", token):
            scripts.add("Latin")
        if re.search(r"[۰-۹]", token):
            scripts.add("Persian")
        if re.search(r"[٠-٩]", token):
            scripts.add("Arabic-Indic")
        if len(scripts) > 1:
            findings.append(make_finding(
                source,
                match.start(),
                match.end(),
                prefix="UNI",
                rule="mixed-digit-token",
                title="Mixed digit scripts inside one number",
                severity="MAJOR",
                confidence="HIGH",
                layer="MECHANICAL",
                edit_risk="MEANING-SENSITIVE",
                authority=["UNICODE", "PROJECT"],
                diagnosis=f"This numeric token mixes {', '.join(sorted(scripts))} digits.",
                why="Mixed scripts can change search, parsing, copy/paste, and the perceived value in RTL text.",
                proposed="Verify the authoritative value, then render the whole token in the context-approved digit script.",
            ))
        elif "Arabic-Indic" in scripts:
            findings.append(make_finding(
                source,
                match.start(),
                match.end(),
                prefix="UNI",
                rule="arabic-indic-digits",
                title="Arabic-Indic digits in Persian manuscript",
                severity="MINOR",
                confidence="MEDIUM",
                layer="MECHANICAL",
                edit_risk="MEANING-SENSITIVE",
                authority=["UNICODE", "PROJECT"],
                diagnosis="The token uses U+0660–U+0669 Arabic-Indic digits rather than Persian or Latin digits.",
                why="The manuscript may contain visually similar but semantically different digit code points.",
                proposed="Follow the project’s contextual digit policy; verify the value before conversion.",
            ))

    return findings


def check_orthography_and_punctuation(source: SourceText, profile: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    patterns: list[tuple[re.Pattern[str], dict[str, Any]]] = [
        (
            re.compile(rf"(?<![{PERSIAN_RANGE}\u200c])(?:ن?می)[ \t]+(?=[{PERSIAN_RANGE}])"),
            dict(
                prefix="ORTH", rule="separated-mi-prefix", title="Possible separated verbal prefix `می/نمی`",
                severity="MINOR", confidence="MEDIUM", layer="LINGUISTIC", edit_risk="MEANING-SENSITIVE",
                authority=["ACADEMY"], diagnosis="`می` or `نمی` is separated by an ordinary space from a Persian token.",
                why="When this is the verbal prefix, standard orthography uses a ZWNJ; the noun `می` and lexical exceptions must not be changed by regex alone.",
                proposed="Confirm that the token is a verb, then use `می‌...` or `نمی‌...`.",
            ),
        ),
        (
            re.compile(rf"([{PERSIAN_RANGE}]{{2,}})[ \t]+ها(?![{PERSIAN_RANGE}\u200c])"),
            dict(
                prefix="ORTH", rule="separated-plural-ha", title="Plural suffix `ها` separated by a full space",
                severity="MINOR", confidence="HIGH", layer="LINGUISTIC", edit_risk="SAFE",
                authority=["ACADEMY", "PROJECT"], diagnosis="A likely plural suffix is written as an independent token.",
                why="In ordinary plural morphology, `ها` should follow the base with the project-approved joined/ZWNJ realization, not an ordinary word space.",
                proposed="Use the project’s plural policy, normally a ZWNJ form such as `داده‌ها`, after confirming the parse.",
            ),
        ),
        (
            re.compile(rf"([{PERSIAN_RANGE}]{{2,}})[ \t]+(تر|ترین)(?![{PERSIAN_RANGE}\u200c])"),
            dict(
                prefix="ORTH", rule="separated-comparative", title="Possible comparative/superlative suffix separated by a full space",
                severity="MINOR", confidence="MEDIUM", layer="LINGUISTIC", edit_risk="MEANING-SENSITIVE",
                authority=["ACADEMY"], diagnosis="`تر` or `ترین` follows a Persian word with an ordinary space.",
                why="When it is a suffix, the orthographic boundary normally uses ZWNJ or natural non-joining behavior; names and independent tokens are exceptions.",
                proposed="Confirm suffix function and apply the approved spelling.",
            ),
        ),
        (
            re.compile(r"[ \t]+(?=[،؛؟])"),
            dict(
                prefix="PUNCT", rule="space-before-persian-punctuation", title="Space before Persian punctuation",
                severity="MINOR", confidence="HIGH", layer="MECHANICAL", edit_risk="SAFE",
                authority=["EDITORIAL", "PROJECT"], diagnosis="Ordinary whitespace occurs immediately before Persian punctuation.",
                why="Persian punctuation normally attaches to the preceding token.",
                proposed="Remove the space unless a protected technical construction requires it.",
            ),
        ),
        (
            re.compile(r"[،؛؟](?=[\u0600-\u06FF])"),
            dict(
                prefix="PUNCT", rule="missing-space-after-punctuation", title="Missing space after Persian punctuation",
                severity="MINOR", confidence="HIGH", layer="MECHANICAL", edit_risk="SAFE",
                authority=["EDITORIAL", "PROJECT"], diagnosis="A Persian letter immediately follows punctuation without ordinary separation.",
                why="This usually merges sentence constituents and harms readability/search.",
                proposed="Insert one ordinary space unless the following character is deliberately attached in a technical token.",
            ),
        ),
        (
            re.compile(r"«[ \t]+|[ \t]+»"),
            dict(
                prefix="PUNCT", rule="space-inside-guillemets", title="Space immediately inside guillemets",
                severity="MINOR", confidence="HIGH", layer="MECHANICAL", edit_risk="SAFE",
                authority=["EDITORIAL", "PROJECT"], diagnosis="Whitespace occurs directly after `«` or before `»`.",
                why="Ordinary Persian quotation typography does not use spaces immediately inside guillemets.",
                proposed="Remove the internal space unless reproducing an exact source layout.",
            ),
        ),
    ]

    for pattern, kwargs in patterns:
        findings.extend(regex_findings(source, pattern, **kwargs))

    # Persian line with Latin punctuation candidates. Avoid decimal/comma numerals.
    for match in re.finditer(r"[,;?]", source.masked):
        if not source.span_is_plain(*match.span()) or not is_persian_context(source, match.start()):
            continue
        before = source.text[match.start() - 1] if match.start() > 0 else ""
        after = source.text[match.end()] if match.end() < len(source.text) else ""
        if match.group() == "," and before.isdigit() and after.isdigit():
            continue
        replacement = {",": "،", ";": "؛", "?": "؟"}[match.group()]
        findings.append(make_finding(
            source,
            match.start(), match.end(),
            prefix="PUNCT", rule="latin-punctuation-in-persian", title="Latin punctuation in Persian prose",
            severity="MINOR", confidence="MEDIUM", layer="MECHANICAL", edit_risk="MEANING-SENSITIVE",
            authority=["PROJECT", "EDITORIAL"],
            diagnosis=f"Latin `{match.group()}` appears in a Persian-dominant line.",
            why="Mixed punctuation can be a copy/paste artifact, but technical notation and bibliographic conventions are exceptions.",
            proposed=f"Confirm prose context and use `{replacement}` if the project’s Persian punctuation policy applies.",
        ))

    # Straight double quotes around Persian text when guillemets are selected.
    quote_policy = profile.get("orthography", {}).get("quotation_marks", "")
    if quote_policy == "guillemets":
        for match in re.finditer(r'"[^"\n]*[\u0600-\u06FF][^"\n]*"', source.masked):
            findings.append(make_finding(
                source,
                match.start(), match.end(),
                prefix="PUNCT", rule="straight-quotes", title="Straight quotation marks in Persian prose",
                severity="STYLE", confidence="HIGH", layer="VENUE", edit_risk="MEANING-SENSITIVE",
                authority=["PROJECT"], diagnosis="The project profile selects guillemets, but this Persian quotation uses straight quotes.",
                why="Quotation typography should be consistent; direct quotations must retain exact content while delimiters follow policy.",
                proposed="Use `«…»` after confirming this is a quotation rather than code or a literal identifier.",
            ))

    # Digit-policy checks only when profile is explicit; contextual policy is not regex-safe.
    digit_policy = profile.get("orthography", {}).get("digit_policy", "contextual")
    if digit_policy in {"persian-prose", "latin"}:
        target_re = re.compile(r"[0-9]+" if digit_policy == "persian-prose" else r"[۰-۹]+")
        for match in target_re.finditer(source.masked):
            if not is_persian_context(source, match.start()):
                continue
            findings.append(make_finding(
                source,
                match.start(), match.end(),
                prefix="PUNCT", rule=f"digit-policy-{digit_policy}", title="Digit script differs from explicit project policy",
                severity="MINOR", confidence="MEDIUM", layer="VENUE", edit_risk="MEANING-SENSITIVE",
                authority=["PROJECT"], diagnosis=f"The profile requests `{digit_policy}`, but this token uses another digit script.",
                why="Digit conversion is context-sensitive; identifiers, equations, versions, and official names may be protected exceptions.",
                proposed="Verify the token’s role and value, then apply the profile only if this is ordinary prose data.",
            ))

    return findings


def check_style(source: SourceText) -> list[Finding]:
    findings: list[Finding] = []
    for phrase, repair in STYLE_PHRASES.items():
        findings.extend(literal_findings(
            source,
            phrase,
            prefix="STYLE",
            rule=f"candidate-{hashlib.sha1(phrase.encode('utf-8')).hexdigest()[:8]}",
            title=f"Academic-style candidate: `{phrase}`",
            severity="STYLE",
            confidence="MEDIUM",
            layer="LINGUISTIC",
            edit_risk="MEANING-SENSITIVE",
            authority=["EDITORIAL"],
            diagnosis="This expression can be legitimate, but it often adds bureaucratic scaffolding or obscures the proposition.",
            why="Academic register is improved by precision and direct logical relations, not automatic formality.",
            proposed=repair,
        ))
    return findings


def check_draft_markers(source: SourceText) -> list[Finding]:
    findings: list[Finding] = []
    # Search raw source intentionally, including comments.
    for match in DRAFT_MARKERS.finditer(source.text):
        findings.append(make_finding(
            source,
            match.start(), match.end(),
            prefix="QC", rule="draft-marker", title="Draft marker remains in source",
            severity="MAJOR", confidence="HIGH", layer="MECHANICAL", edit_risk="SAFE",
            authority=["PROJECT", "VENUE"], diagnosis=f"The source contains `{match.group(0)}`.",
            why="Draft residue can leak into the final PDF or indicate unresolved scholarly work.",
            proposed="Resolve the underlying task and remove the marker; verify the rendered PDF and conditional branches.",
        ))
    for match in re.finditer(r"\?\?", source.text):
        if source.path.suffix.lower() == ".tex":
            findings.append(make_finding(
                source,
                match.start(), match.end(),
                prefix="QC", rule="visible-question-marks", title="Possible unresolved placeholder `??`",
                severity="MAJOR", confidence="MEDIUM", layer="MECHANICAL", edit_risk="MEANING-SENSITIVE",
                authority=["PROJECT"], diagnosis="Two question marks appear in TeX source.",
                why="They may be deliberate punctuation, but often indicate an unresolved reference or placeholder.",
                proposed="Inspect source and compiled PDF; resolve the reference/placeholder if unintended.",
            ))
    return findings


def check_terms(source: SourceText, terms: list[TermEntry]) -> list[Finding]:
    findings: list[Finding] = []
    for entry in terms:
        if not entry.preferred_fa:
            continue
        for rejected in entry.rejected_variants:
            if not rejected:
                continue
            for finding in literal_findings(
                source,
                rejected,
                prefix="TERM",
                rule=f"rejected-{entry.concept_id or hashlib.sha1(entry.preferred_fa.encode()).hexdigest()[:6]}",
                title=f"Rejected terminology variant for `{entry.concept_id or entry.preferred_fa}`",
                severity="MAJOR" if entry.status == "approved" else "MINOR",
                confidence="HIGH" if entry.status == "approved" else "MEDIUM",
                layer="LINGUISTIC",
                edit_risk="MEANING-SENSITIVE",
                authority=["PROJECT"],
                diagnosis=f"The terminology register marks `{rejected}` as rejected/confusable; preferred form is `{entry.preferred_fa}`.",
                why="Terminology drift can merge distinct concepts or make bilingual sections inconsistent.",
                proposed=f"Replace only after confirming this occurrence denotes the registered concept; preferred form: `{entry.preferred_fa}`.",
            ):
                findings.append(finding)
    return findings


# ---------------------------------------------------------------------------
# TeX/Bib workspace checks
# ---------------------------------------------------------------------------


def parse_tex_objects(source: SourceText) -> dict[str, list[tuple[str, int, int]]]:
    text = source.text
    objects: dict[str, list[tuple[str, int, int]]] = defaultdict(list)

    label_re = re.compile(r"\\label\s*\{([^}]*)\}")
    ref_re = re.compile(r"\\(?:ref|pageref|eqref|autoref|cref|Cref|vref)\s*\{([^}]*)\}")
    # Supports common citation commands while avoiding arbitrary words ending in cite.
    cite_re = re.compile(r"\\(?:cite|citet|citep|parencite|textcite|autocite|footcite|nocite)\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}")

    for kind, pattern in (("label", label_re), ("ref", ref_re), ("cite", cite_re)):
        for match in pattern.finditer(text):
            raw = match.group(1)
            start = match.start(1)
            for item in raw.split(","):
                key = item.strip()
                item_offset = raw.find(item)
                objects[kind].append((key, start + max(0, item_offset), match.end(1)))

    return objects


def parse_bib_keys(path: Path) -> list[tuple[str, int, int, str]]:
    text = read_text(path)
    results: list[tuple[str, int, int, str]] = []
    for match in re.finditer(r"(?im)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", text):
        entry_type = match.group(1).lower()
        if entry_type in {"comment", "preamble", "string"}:
            continue
        key = match.group(2)
        line = text.count("\n", 0, match.start(2)) + 1
        col = match.start(2) - text.rfind("\n", 0, match.start(2))
        results.append((key, line, col, text.splitlines()[line - 1].strip()))
    return results


def check_workspace(
    sources: dict[Path, SourceText],
    missing_dependencies: list[tuple[Path, str, str, int]],
) -> list[Finding]:
    findings: list[Finding] = []

    for parent, command, raw, line in missing_dependencies:
        text = read_text(parent) if parent.exists() else ""
        source = sources.get(parent)
        if source is None:
            source = SourceText.build(parent, text, DEFAULT_PROTECTED_COMMANDS, DEFAULT_PROTECTED_ENVIRONMENTS)
        # Locate the dependency string near the recorded line for a useful column.
        line_start = source.line_starts[min(max(line - 1, 0), len(source.line_starts) - 1)]
        index = source.text.find(raw, line_start)
        if index == -1:
            index = line_start
        findings.append(make_finding(
            source,
            index,
            min(len(source.text), index + max(1, len(raw))),
            prefix="WS", rule=f"missing-{command}", title=f"Missing `{command}` dependency",
            severity="BLOCKER" if command in {"input", "include", "subfile", "bibliography", "addbibresource"} else "MAJOR",
            confidence="HIGH", layer="MECHANICAL", edit_risk="STRUCTURAL",
            authority=["PROJECT", "VENUE"],
            diagnosis=f"`\\{command}` refers to `{raw}`, but no matching file was found relative to `{parent.parent}`.",
            why="The manuscript cannot be reviewed or built completely when a declared dependency is missing.",
            proposed="Correct the path, add the missing file, or document the generated-file/build step; then rerun the audit.",
        ))

    label_defs: dict[str, list[tuple[SourceText, int, int]]] = defaultdict(list)
    refs: list[tuple[str, SourceText, int, int]] = []
    cites: list[tuple[str, SourceText, int, int]] = []

    for path, source in sources.items():
        if path.suffix.lower() != ".tex":
            continue
        objects = parse_tex_objects(source)
        for key, start, end in objects["label"]:
            label_defs[key].append((source, start, end))
            if not key:
                findings.append(make_finding(
                    source, start, max(start + 1, end),
                    prefix="LATEX", rule="empty-label", title="Empty LaTeX label",
                    severity="MAJOR", confidence="HIGH", layer="MECHANICAL", edit_risk="STRUCTURAL",
                    authority=["PROJECT"], diagnosis="`\\label{}` has no key.",
                    why="The object cannot be referenced reliably and may create duplicate/empty destinations.",
                    proposed="Assign a unique project-compliant label and update intended references.", original="\\label{}",
                ))
        for key, start, end in objects["ref"]:
            refs.append((key, source, start, end))
            if not key:
                findings.append(make_finding(
                    source, start, max(start + 1, end),
                    prefix="LATEX", rule="empty-ref", title="Empty LaTeX reference",
                    severity="MAJOR", confidence="HIGH", layer="MECHANICAL", edit_risk="STRUCTURAL",
                    authority=["PROJECT"], diagnosis="A reference command has an empty key.",
                    why="The reference cannot resolve.", proposed="Insert the intended existing label key.", original="empty key",
                ))
        for key, start, end in objects["cite"]:
            cites.append((key, source, start, end))
            if not key:
                findings.append(make_finding(
                    source, start, max(start + 1, end),
                    prefix="CITE", rule="empty-citation", title="Empty citation key",
                    severity="MAJOR", confidence="HIGH", layer="MECHANICAL", edit_risk="MEANING-SENSITIVE",
                    authority=["PROJECT"], diagnosis="A citation command contains an empty key.",
                    why="The claim has an unresolved or malformed citation.", proposed="Insert a verified bibliography key or remove the empty citation after reviewing the claim.", original="empty key",
                ))

        # Layout hacks and visible review commands are candidates.
        for match in re.finditer(r"\\vspace\s*\{\s*-", source.text):
            findings.append(make_finding(
                source, match.start(), min(len(source.text), match.start() + 20),
                prefix="LATEX", rule="negative-vspace", title="Negative vertical-space layout hack",
                severity="STYLE", confidence="HIGH", layer="VENUE", edit_risk="STRUCTURAL",
                authority=["PROJECT", "VENUE"], diagnosis="A negative `\\vspace` adjustment appears in source.",
                why="Manual layout compression can become unstable after edits or violate venue formatting, though it may be deliberate.",
                proposed="Inspect the rendered page and controlling guide; remove or centralize only if the layout remains correct.",
            ))

    for key, locations in label_defs.items():
        if key and len(locations) > 1:
            for source, start, end in locations:
                findings.append(make_finding(
                    source, start, end,
                    prefix="LATEX", rule="duplicate-label", title=f"Duplicate label `{key}`",
                    severity="BLOCKER", confidence="HIGH", layer="MECHANICAL", edit_risk="STRUCTURAL",
                    authority=["PROJECT"], diagnosis=f"The label `{key}` is defined {len(locations)} times.",
                    why="References may resolve to the wrong object and PDF hyperlinks become unreliable.",
                    proposed="Assign unique semantic keys and update all dependent references atomically.", original=key,
                ))

    known_labels = {key for key in label_defs if key}
    for key, source, start, end in refs:
        if key and key not in known_labels:
            findings.append(make_finding(
                source, start, end,
                prefix="LATEX", rule="missing-label", title=f"Reference to undefined label `{key}`",
                severity="BLOCKER", confidence="HIGH", layer="MECHANICAL", edit_risk="STRUCTURAL",
                authority=["PROJECT"], diagnosis=f"No `\\label{{{key}}}` was found in the discovered workspace.",
                why="The compiled manuscript will contain an unresolved or incorrect cross-reference.",
                proposed="Correct the key, restore the missing labeled object, or expand the workspace scope if the definition is generated externally.", original=key,
            ))

    bib_key_locations: dict[str, list[tuple[Path, int, int, str]]] = defaultdict(list)
    for path in sources:
        if path.suffix.lower() != ".bib":
            continue
        for key, line, col, context in parse_bib_keys(path):
            bib_key_locations[key].append((path, line, col, context))

    for key, locations in bib_key_locations.items():
        if len(locations) > 1:
            for path, line, col, context in locations:
                source = sources[path]
                index = source.line_starts[line - 1] + col - 1
                findings.append(make_finding(
                    source, index, index + len(key),
                    prefix="CITE", rule="duplicate-bib-key", title=f"Duplicate bibliography key `{key}`",
                    severity="BLOCKER", confidence="HIGH", layer="MECHANICAL", edit_risk="STRUCTURAL",
                    authority=["PROJECT"], diagnosis=f"The key `{key}` is defined {len(locations)} times across discovered bibliography resources.",
                    why="Citation resolution may be non-deterministic or silently select the wrong record.",
                    proposed="Merge duplicate records or assign verified unique keys, then update citations atomically.", original=key,
                ))

    known_bib = set(bib_key_locations)
    if known_bib:
        for key, source, start, end in cites:
            if key == "*":
                continue
            if key and key not in known_bib:
                findings.append(make_finding(
                    source, start, end,
                    prefix="CITE", rule="missing-bib-key", title=f"Citation key not found: `{key}`",
                    severity="BLOCKER", confidence="HIGH", layer="MECHANICAL", edit_risk="MEANING-SENSITIVE",
                    authority=["PROJECT"], diagnosis=f"No bibliography entry with key `{key}` was found in the discovered `.bib` files.",
                    why="The citation cannot resolve and the underlying claim may be unsupported.",
                    proposed="Locate and verify the intended source, then correct the key or bibliography resource; never invent metadata.", original=key,
                ))
    elif cites:
        # Report the first citation: a root may obtain bibliography resources via
        # generated/custom mechanisms, so this is a workspace-level candidate.
        key, source, start, end = cites[0]
        findings.append(make_finding(
            source, start, end,
            prefix="CITE", rule="no-bibliography-resource", title="Citations found but no bibliography resource was discovered",
            severity="MAJOR", confidence="MEDIUM", layer="MECHANICAL", edit_risk="STRUCTURAL",
            authority=["PROJECT"], diagnosis="The discovered TeX workspace contains citation commands but no readable `.bib` resource.",
            why="Citation integrity cannot be checked and the build may rely on a missing or generated bibliography input.",
            proposed="Identify the bibliography backend/resource or document the generation step, then rerun the audit.", original=key or "citation",
        ))

    return findings


# ---------------------------------------------------------------------------
# Cross-document consistency checks
# ---------------------------------------------------------------------------


def check_ezafe_consistency(sources: dict[Path, SourceText], profile: dict[str, Any]) -> list[Finding]:
    styles = {
        "hamza-above": re.compile(r"هٔ"),
        "heh-yeh": re.compile(r"ۀ"),
        "yeh-form": re.compile(r"ه\u200c?ی(?=[\s،؛؟.!:])"),
    }
    occurrences: dict[str, list[tuple[SourceText, int, int]]] = defaultdict(list)
    for source in sources.values():
        if source.path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        for name, pattern in styles.items():
            for match in pattern.finditer(source.masked):
                if source.span_is_plain(*match.span()):
                    occurrences[name].append((source, match.start(), match.end()))

    present = {name: locs for name, locs in occurrences.items() if locs}
    preferred = profile.get("orthography", {}).get("ezafe_after_heh", "infer")
    findings: list[Finding] = []

    if preferred in styles:
        for name, locs in present.items():
            if name == preferred:
                continue
            for source, start, end in locs:
                findings.append(make_finding(
                    source, start, end,
                    prefix="ORTH", rule="ezafe-profile", title="Ezafe form differs from project profile",
                    severity="MINOR", confidence="HIGH", layer="VENUE", edit_risk="MEANING-SENSITIVE",
                    authority=["PROJECT"], diagnosis=f"The profile selects `{preferred}` after final `ه`, but this span uses `{name}`.",
                    why="Multiple defensible digital forms exist; consistency must follow the controlling project/institution decision.",
                    proposed="Convert only after confirming this is an ezafe construction and preserve quotations/proper names.",
                ))
    elif len(present) > 1:
        # One project-level finding at the first occurrence of each minority style.
        dominant = max(present, key=lambda name: len(present[name]))
        counts = ", ".join(f"{name}={len(locs)}" for name, locs in sorted(present.items()))
        for name, locs in present.items():
            if name == dominant:
                continue
            source, start, end = locs[0]
            findings.append(make_finding(
                source, start, end,
                prefix="ORTH", rule="mixed-ezafe-style", title="Mixed ezafe styles after final `ه`",
                severity="STYLE", confidence="HIGH", layer="VENUE", edit_risk="MEANING-SENSITIVE",
                authority=["PROJECT"], diagnosis=f"The manuscript uses multiple ezafe forms ({counts}); dominant observed form is `{dominant}`.",
                why="The Academy orthography source does not by itself settle every digital/editorial realization; the project should record one defensible convention.",
                proposed="Choose the controlling institutional/project form, record it in the profile, then review occurrences contextually rather than global blind replacement.",
            ))
    return findings


def check_term_consistency(sources: dict[Path, SourceText], terms: list[TermEntry]) -> list[Finding]:
    findings: list[Finding] = []
    for entry in terms:
        forms = [entry.preferred_fa, *entry.accepted_variants]
        counts: dict[str, list[tuple[SourceText, int, int]]] = defaultdict(list)
        for form in forms:
            if not form:
                continue
            for source in sources.values():
                if source.path.suffix.lower() not in TEXT_EXTENSIONS:
                    continue
                start = 0
                while True:
                    index = source.masked.find(form, start)
                    if index == -1:
                        break
                    end = index + len(form)
                    if source.span_is_plain(index, end):
                        counts[form].append((source, index, end))
                    start = max(end, index + 1)
        present = {form: locs for form, locs in counts.items() if locs}
        if len(present) <= 1:
            continue
        # Accepted variants may encode real distinctions; this is a consistency candidate.
        minority_forms = sorted(present, key=lambda form: len(present[form]))[:-1]
        summary = ", ".join(f"`{form}`={len(locs)}" for form, locs in sorted(present.items()))
        for form in minority_forms:
            source, start, end = present[form][0]
            findings.append(make_finding(
                source, start, end,
                prefix="TERM", rule=f"variant-mix-{entry.concept_id}", title=f"Multiple registered variants used for `{entry.concept_id or entry.preferred_fa}`",
                severity="MINOR", confidence="MEDIUM", layer="LINGUISTIC", edit_risk="MEANING-SENSITIVE",
                authority=["PROJECT"], diagnosis=f"Observed registered forms: {summary}. Preferred form is `{entry.preferred_fa}`.",
                why="Variation may be intentional sense distinction or first-use behavior, but uncontrolled synonymy harms terminological traceability.",
                proposed="Inspect meanings and first-use context; normalize only occurrences that denote the same concept.",
            ))
    return findings


# ---------------------------------------------------------------------------
# Safe fixer
# ---------------------------------------------------------------------------


def safe_normalize(source: SourceText) -> str:
    strict_protection = quote_protection(source.text, source.protected)
    chars = list(source.text)
    i = 0
    while i < len(chars):
        if strict_protection[i]:
            i += 1
            continue
        ch = chars[i]
        if ch in {"ي", "ى", "ك"}:
            chars[i] = ch.translate(ARABIC_TO_PERSIAN)
        elif ch == "ـ":
            chars[i] = ""
        elif ch == "\u200c" and i + 1 < len(chars) and chars[i + 1] == "\u200c" and not strict_protection[i + 1]:
            chars[i] = ""
        i += 1
    return "".join(chars)


def available_backup(path: Path) -> Path:
    candidate = path.with_name(path.name + ".bak")
    counter = 1
    while candidate.exists():
        candidate = path.with_name(path.name + f".bak.{counter}")
        counter += 1
    return candidate


def apply_or_preview_safe_fixes(
    paths: Iterable[Path],
    protected_commands: set[str],
    protected_environments: set[str],
    write: bool,
) -> tuple[list[str], list[str]]:
    diffs: list[str] = []
    changed_files: list[str] = []
    for path in sorted(paths):
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        original = read_text(path)
        source = SourceText.build(path, original, protected_commands, protected_environments)
        normalized = safe_normalize(source)
        if normalized == original:
            continue
        diff = "".join(difflib.unified_diff(
            original.splitlines(keepends=True),
            normalized.splitlines(keepends=True),
            fromfile=str(path),
            tofile=str(path) + (" (safe-normalized)" if not write else ""),
        ))
        diffs.append(diff)
        changed_files.append(str(path))
        if write:
            backup = available_backup(path)
            shutil.copy2(path, backup)
            path.write_text(normalized, encoding="utf-8")
    return diffs, changed_files


# ---------------------------------------------------------------------------
# Audit orchestration
# ---------------------------------------------------------------------------


def deduplicate(findings: list[Finding]) -> list[Finding]:
    seen: set[tuple[str, str, int, int, str]] = set()
    result: list[Finding] = []
    for finding in findings:
        key = (finding.rule, finding.path, finding.line, finding.column, finding.original)
        if key in seen:
            continue
        seen.add(key)
        result.append(finding)
    severity_rank = {"BLOCKER": 0, "MAJOR": 1, "MINOR": 2, "STYLE": 3}
    result.sort(key=lambda item: (
        item.path,
        item.line,
        item.column,
        severity_rank.get(item.severity, 9),
        item.prefix,
        item.id,
    ))
    return result


def relative_display(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def determine_project_base(targets: Sequence[Path], root: Path | None) -> Path:
    if root is not None:
        return root.parent if root.is_file() or root.suffix else root
    anchors: list[Path] = []
    for target in targets:
        anchors.append(target if target.is_dir() else target.parent)
    if not anchors:
        return Path.cwd().resolve()
    try:
        return Path(os.path.commonpath([str(item) for item in anchors])).resolve()
    except ValueError:
        return Path.cwd().resolve()


def run_audit(args: argparse.Namespace) -> AuditResult:
    targets = [normalize_target(Path(item)) for item in args.targets]
    root = normalize_target(Path(args.root)) if args.root else None
    profile_path = normalize_target(Path(args.profile)) if args.profile else None
    terms_path = normalize_target(Path(args.terms)) if args.terms else None
    project_base = determine_project_base(targets, root)

    profile = load_profile(profile_path)
    terms = load_terms(terms_path)
    protected_commands = profile_list(profile, "protected_latex", "commands", DEFAULT_PROTECTED_COMMANDS)
    protected_environments = profile_list(profile, "protected_latex", "environments", DEFAULT_PROTECTED_ENVIRONMENTS)

    files, missing, bib_files, assets = collect_files(targets, root)
    if not files:
        raise ValueError("No supported manuscript files were discovered.")

    safe_fix_diffs: list[str] = []
    safe_fix_files: list[str] = []
    if args.fix_safe:
        safe_fix_diffs, safe_fix_files = apply_or_preview_safe_fixes(
            files, protected_commands, protected_environments, args.write
        )

    sources: dict[Path, SourceText] = {}
    for path in sorted(files):
        sources[path] = SourceText.build(path, read_text(path), protected_commands, protected_environments)

    findings: list[Finding] = []
    for source in sources.values():
        if source.path.suffix.lower() in TEXT_EXTENSIONS:
            findings.extend(check_unicode(source))
            findings.extend(check_orthography_and_punctuation(source, profile))
            findings.extend(check_style(source))
            findings.extend(check_draft_markers(source))
            findings.extend(check_terms(source, terms))

    findings.extend(check_workspace(sources, missing))
    findings.extend(check_ezafe_consistency(sources, profile))
    findings.extend(check_term_consistency(sources, terms))

    # Repository-relative locations make issue IDs stable across clones/machines.
    for finding in findings:
        finding.path = relative_display(Path(finding.path), project_base)
        finding.finalize()
    findings = deduplicate(findings)

    assumptions = [
        "This deterministic helper reports candidates; substantive Persian editing and scientific review require the SKILL.md workflow.",
        "Compounds, digit conversion, ezafe, claim strength, citation support, and sentence rewriting are not auto-fixed.",
    ]
    if not profile:
        assumptions.append("No project profile was supplied; venue and house-style findings are intentionally limited.")
    if not terms:
        assumptions.append("No terminology register was supplied; concept-level terminology consistency is not fully assessable.")
    if root and root.suffix.lower() == ".tex":
        assumptions.append("The LaTeX dependency graph was discovered from the supplied root using static source analysis.")

    return AuditResult(
        targets=[relative_display(item, project_base) for item in ([*targets] + ([root] if root else []))],
        files=[relative_display(path, project_base) for path in sorted(files)],
        profile_path=relative_display(profile_path, project_base) if profile_path else None,
        terms_path=relative_display(terms_path, project_base) if terms_path else None,
        findings=findings,
        safe_fix_diffs=safe_fix_diffs,
        safe_fix_files=[relative_display(Path(path), project_base) for path in safe_fix_files],
        assumptions=assumptions,
        metadata={
            "version": VERSION,
            "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project_base": str(project_base),
            "root": relative_display(root, project_base) if root else None,
            "discovered_bibliography_files": [relative_display(path, project_base) for path in sorted(bib_files)],
            "discovered_assets": [relative_display(path, project_base) for path in sorted(assets)],
            "safe_fix_mode": "written" if args.fix_safe and args.write else "preview" if args.fix_safe else "off",
        },
    )


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def markdown_escape_code(text: str) -> str:
    return text.replace("`", "\\`")


def render_markdown(result: AuditResult) -> str:
    counts = Counter(finding.severity for finding in result.findings)
    category_counts = Counter(finding.prefix for finding in result.findings)
    lines: list[str] = [
        "# Deterministic Virastar Audit",
        "",
        f"- Tool version: `{result.metadata['version']}`",
        f"- Generated: `{result.metadata['generated_at']}`",
        f"- Files scanned: **{len(result.files)}**",
        f"- Project profile: `{result.profile_path or 'not supplied'}`",
        f"- Terminology register: `{result.terms_path or 'not supplied'}`",
        f"- Safe-fix mode: `{result.metadata['safe_fix_mode']}`",
        "",
        "> This is a static candidate report. It is not a substitute for the report-first linguistic and scientific review defined in `SKILL.md`.",
        "",
        "## Scope and assumptions",
        "",
    ]
    lines.extend(f"- {item}" for item in result.assumptions)
    lines.extend(["", "### Targets", ""])
    lines.extend(f"- `{item}`" for item in result.targets)
    lines.extend(["", "### Discovered files", ""])
    lines.extend(f"- `{item}`" for item in result.files)

    lines.extend([
        "",
        "## Summary",
        "",
        "| Severity | Count |",
        "|---|---:|",
        f"| BLOCKER | {counts['BLOCKER']} |",
        f"| MAJOR | {counts['MAJOR']} |",
        f"| MINOR | {counts['MINOR']} |",
        f"| STYLE | {counts['STYLE']} |",
        "",
        "| Category | Count |",
        "|---|---:|",
    ])
    for category, count in sorted(category_counts.items()):
        lines.append(f"| {category} | {count} |")

    if result.safe_fix_files:
        lines.extend([
            "",
            "## Safe normalization",
            "",
            f"Files changed/proposed: **{len(result.safe_fix_files)}**",
            "",
        ])
        lines.extend(f"- `{item}`" for item in result.safe_fix_files)
        if result.safe_fix_diffs:
            lines.extend(["", "<details>", "<summary>Unified diff</summary>", "", "```diff"])
            lines.append("\n".join(result.safe_fix_diffs).rstrip())
            lines.extend(["```", "", "</details>"])

    lines.extend(["", "## Findings", ""])
    if not result.findings:
        lines.append("No deterministic findings were detected in the scanned scope.")
    else:
        for finding in result.findings:
            lines.extend([
                f"### {finding.id} — {finding.title}",
                "",
                f"- Severity: **{finding.severity}**",
                f"- Confidence: **{finding.confidence}**",
                f"- Layer: **{finding.layer}**",
                f"- Edit risk: **{finding.edit_risk}**",
                f"- Authority: {', '.join(finding.authority)}",
                f"- Location: `{finding.path}:{finding.line}:{finding.column}`",
                f"- Fingerprint: `{finding.fingerprint}`",
                f"- Original: `{markdown_escape_code(finding.original)}`",
                f"- Context: `{markdown_escape_code(finding.context)}`" if finding.context else "- Context: —",
                f"- Diagnosis: {finding.diagnosis}",
                f"- Why it matters: {finding.why_it_matters}",
                f"- Proposed repair: {finding.proposed_repair}",
            ])
            if finding.dependencies:
                lines.append(f"- Depends on: {', '.join(finding.dependencies)}")
            lines.append("")

    lines.extend([
        "## Limits",
        "",
        "- The checker does not establish whether a citation truly supports a claim.",
        "- It does not judge grammar beyond narrow candidate patterns.",
        "- It does not determine scientific validity, causal identification, statistical correctness, or chapter logic.",
        "- It does not inspect rendered PDF pages; use the skill’s final-QC workflow for RTL, fonts, floats, and visible annotations.",
        "",
    ])
    return "\n".join(lines)


def render_json(result: AuditResult) -> str:
    payload = {
        "metadata": result.metadata,
        "targets": result.targets,
        "files": result.files,
        "profile_path": result.profile_path,
        "terms_path": result.terms_path,
        "assumptions": result.assumptions,
        "summary": {
            "total": len(result.findings),
            "by_severity": dict(Counter(item.severity for item in result.findings)),
            "by_category": dict(Counter(item.prefix for item in result.findings)),
        },
        "safe_fix_files": result.safe_fix_files,
        "safe_fix_diffs": result.safe_fix_diffs,
        "findings": [item.to_dict() for item in result.findings],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def write_outputs(result: AuditResult, fmt: str, output: str | None) -> None:
    markdown = render_markdown(result)
    json_text = render_json(result)

    if output is None:
        if fmt == "markdown":
            print(markdown)
        elif fmt == "json":
            print(json_text)
        else:
            print(markdown)
            print("\n--- JSON ---\n")
            print(json_text)
        return

    out = Path(output).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)

    if fmt == "markdown":
        path = out if out.suffix else out.with_suffix(".md")
        path.write_text(markdown, encoding="utf-8")
        print(path)
    elif fmt == "json":
        path = out if out.suffix else out.with_suffix(".json")
        path.write_text(json_text, encoding="utf-8")
        print(path)
    else:
        if out.suffix in {".md", ".json"}:
            base = out.with_suffix("")
        else:
            base = out
        md_path = base.with_suffix(".md")
        json_path = base.with_suffix(".json")
        md_path.write_text(markdown, encoding="utf-8")
        json_path.write_text(json_text, encoding="utf-8")
        print(md_path)
        print(json_path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Conservative Virastar audit for Persian scholarly text and LaTeX/XePersian workspaces.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """
            Examples:
              audit_virastar.py --root main.tex
              audit_virastar.py thesis/ --profile editorial/project-profile.toml
              audit_virastar.py --root main.tex --terms editorial/terminology-register.toml --format both --output editorial/audits/pre-edit
              audit_virastar.py thesis/ --fix-safe          # diff preview
              audit_virastar.py thesis/ --fix-safe --write  # creates .bak files
            """
        ),
    )
    parser.add_argument("targets", nargs="*", help="File(s) or directory/directories to scan.")
    parser.add_argument("--root", help="Root TeX file; recursive inputs, bibliography resources, and graphics are discovered.")
    parser.add_argument("--profile", help="TOML project profile.")
    parser.add_argument("--terms", help="TOML terminology register.")
    parser.add_argument("--format", choices=("markdown", "json", "both"), default="markdown")
    parser.add_argument("--output", help="Output path or basename. With --format both, writes .md and .json.")
    parser.add_argument("--fix-safe", action="store_true", help="Preview narrow Unicode-level safe normalization.")
    parser.add_argument("--write", action="store_true", help="Write --fix-safe changes and create .bak files.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.targets and not args.root:
        parser.error("Provide at least one target or --root.")
    if args.write and not args.fix_safe:
        parser.error("--write requires --fix-safe.")

    try:
        result = run_audit(args)
        write_outputs(result, args.format, args.output)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
