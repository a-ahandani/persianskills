#!/usr/bin/env python3
"""Validate the skill routing/evaluation case file.

This does not score an LLM. It checks that every case has the fields needed for
manual or agent-based evaluation and prints a compact coverage report.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ALLOWED_MODES = {
    "audit", "apply-approved", "direct-copyedit", "substantive-review",
    "translate-fa", "translation-audit", "terminology-lookup", "workspace-audit",
    "final-qc", "do-not-trigger",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=str(Path(__file__).resolve().parents[1] / "evals" / "cases.json"))
    args = parser.parse_args()
    path = Path(args.path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        print("cases.json must be a non-empty JSON array", file=sys.stderr)
        return 2

    errors: list[str] = []
    seen: set[str] = set()
    coverage = Counter()
    for index, case in enumerate(data):
        if not isinstance(case, dict):
            errors.append(f"case {index}: not an object")
            continue
        for key in ("id", "prompt", "should_trigger", "expected_mode", "must", "must_not"):
            if key not in case:
                errors.append(f"case {index}: missing {key}")
        case_id = case.get("id")
        if case_id in seen:
            errors.append(f"duplicate id: {case_id}")
        seen.add(case_id)
        mode = case.get("expected_mode")
        if mode not in ALLOWED_MODES:
            errors.append(f"{case_id}: invalid mode {mode!r}")
        if bool(case.get("should_trigger")) != (mode != "do-not-trigger"):
            errors.append(f"{case_id}: trigger/mode mismatch")
        if not isinstance(case.get("must", []), list) or not isinstance(case.get("must_not", []), list):
            errors.append(f"{case_id}: must/must_not must be arrays")
        coverage[mode] += 1

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 2

    print(f"Validated {len(data)} eval cases from {path}")
    for mode, count in sorted(coverage.items()):
        print(f"  {mode}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
