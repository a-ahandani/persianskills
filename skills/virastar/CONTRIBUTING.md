# Contributing to Virastar

Thank you for helping improve Virastar. Contributions may refine the editorial workflow, add authoritative references, improve the deterministic auditor, extend test coverage, or make installation and documentation clearer.

## Contribution principles

Virastar edits scholarly material, so correctness is more important than aggressive normalization.

- Preserve scientific meaning, evidence strength, citations, numbers, equations, notation, and author voice.
- Keep language rules, institution or journal requirements, discipline conventions, and project preferences distinct.
- Do not promote an opinionated style preference to a universal Persian rule.
- Prefer report-first detection and explicitly approved changes.
- Keep deterministic fixes narrow, reviewable, and safe around LaTeX and Markdown syntax.
- Never introduce fabricated sources, citations, terminology, or institutional requirements.

## Development setup

Requirements:

- Python 3.11 or newer;
- `uv` for locked Python environments and commands;
- Git.

Clone the repository and enter it:

```bash
git clone https://github.com/mhyrzt/virastar.git
cd virastar
```

Audit and lookup use only the Python standard library. `uv` installs the locked `glossary-build` dependency group only when reproducing the PDF-derived TOML asset.

## Repository structure

- `SKILL.md` — core agent workflow and routing instructions;
- `references/` — detailed editorial and technical guidance;
- `overlays/` — institution-specific rules with explicit scope;
- `assets/` — project profiles, terminology registers, and report templates;
- `scripts/` — deterministic audit, validation, and eval helpers;
- `evals/` — routing and behavior cases;
- `tests/` — Python tests for deterministic behavior;
- `agents/openai.yaml` — Codex-facing skill metadata;

## Making changes

### Editorial rules and references

For every new normative rule, record:

- the source and direct link or bibliographic identity;
- publication or access date and version when available;
- authority level and exact scope;
- whether the rule is obligatory, recommended, or a project preference;
- exceptions and conflicts with higher-priority authorities.

Update `references/10-source-audit.md` when a source materially changes Virastar's behavior. Prefer current primary, institutional, or authoritative sources over derivative repositories and informal summaries.

### Auditor changes

- Add or update a focused test for every detection or fixer change.
- Protect code spans, LaTeX commands, citation keys, labels, URLs, and other structured content.
- Keep `--fix-safe` conservative; uncertain lexical or stylistic edits belong in reports, not automatic rewriting.
- Preserve stable finding IDs and UTF-8 output.

### Terminology and glossary changes

- Use the schema-versioned TOML `[[entries]]` format; do not add CSV terminology assets.
- Preserve source wording and provenance. Keep reference candidates distinct from project-approved preferred terms.
- Regenerate the IPL asset through `scripts/import_ipl_glossary.py`; record extraction-only corrections in that importer instead of hand-editing generated output.
- Never invent an equivalent for a source row that omits one.

### Skill workflow changes

- Keep `SKILL.md` concise and route detailed guidance through `references/`.
- Update routing eval cases when trigger behavior changes.
- Keep `agents/openai.yaml` consistent with the skill name and description.

## Validation

Run the complete validation suite before submitting:

```bash
uv lock --check
uv run python -m unittest discover -s tests -v
uv run python scripts/run_evals.py
uv run python scripts/validate_skill.py
uv run python -m compileall -q scripts tests
```

Remove generated `__pycache__/` directories before committing them.

## Pull requests

Keep pull requests focused. Include:

- the problem and intended behavior;
- the authority or rationale behind editorial changes;
- tests or eval cases covering changed behavior;
- compatibility or migration notes when paths, reports, or finding IDs change;
- representative before-and-after output when changing reports or audit UX.

Before requesting review, confirm that:

- [ ] the complete validation suite passes;
- [ ] new rules have traceable provenance and scope;
- [ ] automatic changes cannot alter scientific meaning;
- [ ] documentation matches the implemented behavior;
- [ ] no generated files, credentials, or manuscript data are included.

## Commit messages

Use concise Conventional Commits where practical, for example:

```text
feat(audit): detect duplicate LaTeX labels
docs: clarify University of Tehran authority
fix(audit): protect glossary keys during normalization
```

By contributing, you agree that your work is distributed under the repository's license.
