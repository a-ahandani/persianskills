# Repository Guidelines

## Project Structure & Module Organization

Virastar is a Persian scholarly-editing skill with deterministic Python helpers. `SKILL.md` defines the agent workflow; detailed editorial rules live in `references/`, while institution-specific policies belong in `overlays/`. Reusable profiles, terminology registers, prompts, and report templates are in `assets/`. Executable helpers live in `scripts/`, routing cases in `evals/cases.json`, and automated checks in `tests/`. Keep `agents/openai.yaml` synchronized with skill metadata.

## Build, Test, and Development Commands

No dependency installation or build step is required; Python code uses the standard library and requires Python 3.11+.

```bash
uv run python -m unittest discover -s tests -v  # Python test suite
uv run python scripts/run_evals.py              # routing/behavior evaluations
uv run python scripts/validate_skill.py         # skill structure and metadata checks
uv run python -m compileall -q scripts tests    # syntax/bytecode validation
```

Run the complete set before submitting changes. Remove generated `__pycache__/` directories before committing.

## Coding Style & Naming Conventions

Use four-space indentation and PEP 8 conventions for Python: `snake_case` functions and variables, `PascalCase` classes, type hints where they improve clarity, and `pathlib.Path` for paths. Keep scripts compatible with the standard library. Keep Markdown concise and route extensive guidance from `SKILL.md` into `references/`.

## Testing Guidelines

Python tests use `unittest`; name files `test_*.py` and methods `test_<behavior>`. Add focused regression tests for every detector or fixer change. Protect LaTeX commands, citation keys, labels, URLs, and code spans. There is no numeric coverage threshold; changed behavior must be exercised by tests or eval cases.

## Commit & Pull Request Guidelines

Use concise Conventional Commits, matching repository history and existing policy: `feat(audit): detect duplicate labels`, `fix(audit): protect glossary keys`, or `docs: clarify authority`. Keep pull requests focused. Describe the problem and intended behavior, link relevant issues or authoritative sources, include tests/evals, and show representative before/after output for report or audit UX changes. Note compatibility implications when changing paths, report formats, or stable finding IDs. Never commit credentials, generated files, or manuscript data.
