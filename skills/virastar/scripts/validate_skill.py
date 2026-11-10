#!/usr/bin/env python3
"""Validate the packaged Virastar skill."""

from __future__ import annotations

import re
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML front matter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md front matter is not closed")
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Unsupported front-matter line: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def main() -> int:
    errors: list[str] = []
    text = SKILL.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        errors.append(str(exc))
        frontmatter = {}

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not name:
        errors.append("front matter is missing name")
    elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"invalid skill name: {name!r}")
    if not description:
        errors.append("front matter is missing description")
    elif len(description) < 80:
        errors.append("description is too vague/short for reliable routing")

    # Validate packaged paths mentioned in SKILL.md.
    path_pattern = re.compile(r"`((?:references|assets|scripts|overlays|agents)/[^`]+)`")
    referenced = sorted(set(path_pattern.findall(text)))
    for relative in referenced:
        # Ignore command arguments after a path if any ever appear.
        clean = relative.split()[0]
        if not (ROOT / clean).exists():
            errors.append(f"referenced path does not exist: {clean}")

    required = [
        "CONTRIBUTING.md",
        "README.md",
        "agents/openai.yaml",
        "references/00-authority-and-profile.md",
        "references/10-source-audit.md",
        "scripts/audit_virastar.py",
        "scripts/terminology.py",
        "scripts/run_evals.py",
        "evals/cases.json",
        "assets/project-profile.example.toml",
        "assets/terminology-register.toml",
        "pyproject.toml",
        "uv.lock",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            errors.append(f"required package file missing: {relative}")

    packaged_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part.startswith(".") for part in path.relative_to(ROOT).parts)
        and "__pycache__" not in path.parts
    ]
    csv_files = [path.relative_to(ROOT) for path in packaged_files if path.suffix.lower() == ".csv"]
    if csv_files:
        errors.append(f"CSV terminology assets are not supported: {', '.join(map(str, csv_files))}")
    yaml_files = {
        path.relative_to(ROOT)
        for path in packaged_files
        if path.suffix.lower() in {".yaml", ".yml"}
    }
    unexpected_yaml = yaml_files - {Path("agents/openai.yaml")}
    if unexpected_yaml:
        errors.append(f"unexpected YAML package files: {', '.join(map(str, sorted(unexpected_yaml)))}")

    for relative in (
        "scripts/audit_virastar.py",
        "scripts/import_ipl_glossary.py",
        "scripts/terminology.py",
        "scripts/run_evals.py",
        "scripts/validate_skill.py",
    ):
        path = ROOT / relative
        if path.exists() and not (path.stat().st_mode & stat.S_IXUSR):
            errors.append(f"script is not executable: {relative}")

    openai_yaml = ROOT / "agents" / "openai.yaml"
    if openai_yaml.exists():
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        for token in ("interface:", "display_name:", "short_description:", "default_prompt:"):
            if token not in yaml_text:
                errors.append(f"agents/openai.yaml is missing {token}")
        if "$virastar" not in yaml_text:
            errors.append("agents/openai.yaml default_prompt must mention $virastar")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 2

    print(f"Validated skill `{name}`")
    print(f"  referenced packaged paths: {len(referenced)}")
    print(f"  description length: {len(description)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
