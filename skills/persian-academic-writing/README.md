# Virastar

Virastar is a report-first scholarly editing skill for Codex, Claude Code, and other Agent Skills-compatible tools. It supports Persian theses, dissertations, papers, research reports, academic translation, English-to-Persian scholarly terminology lookup, and LaTeX/XePersian workspaces.

The skill keeps four kinds of authority separate:

1. Persian language and orthography;
2. institution or journal requirements;
3. discipline-specific scientific writing;
4. project terminology and editorial decisions.

That separation prevents house-style preferences from being presented as language rules and keeps mechanical cleanup from changing scientific meaning.

## Requirements

- Codex, Claude Code, or another agent that supports `SKILL.md` skills;
- Node.js 22.20 or newer and npm for installation with the `skills` CLI;
- Python 3.11 or newer and [`uv`](https://docs.astral.sh/uv/) for deterministic tools;
- no third-party runtime packages for audit or terminology lookup. The reproducible PDF importer uses a locked, non-default dependency group.

## Install

Virastar uses the [`skills` CLI](https://github.com/vercel-labs/skills). From the manuscript project where you want to use the skill, run:

```bash
cd /path/to/manuscript
npx skills add mhyrzt/virastar
```

The CLI discovers the root `SKILL.md`, detects supported coding agents, and prompts for installation targets. Project installation is the default. Use `--global` to make Virastar available across projects:

```bash
npx skills add mhyrzt/virastar --global
```

Target agents explicitly when needed:

```bash
# Install for selected agents in the current project
npx skills add mhyrzt/virastar \
  --agent codex \
  --agent claude-code \
  --agent opencode

# Non-interactive global installation for Codex
npx skills add mhyrzt/virastar --global --agent codex --yes
```

Claude Code can invoke the installed skill explicitly with `/virastar`; supported agents can also select it automatically when a request matches its description.

## Upgrade

Check whether Virastar is installed in the current project or globally:

```bash
npx skills@latest list
npx skills@latest list --global
```

Upgrade the existing installation in the same scope in which it was installed:

```bash
# Project-local installation; run from the manuscript project
npx skills@latest update virastar --project

# Global installation
npx skills@latest update virastar --global
```

Running `npx skills@latest update virastar` without a scope flag opens the CLI's scope prompt. If the installed copy is not present in the local skills lock or cannot be discovered, repeat the original installation command to fetch the latest revision:

```bash
# Project-local installation
npx skills@latest add mhyrzt/virastar --yes

# Non-interactive global installation for Codex
npx skills@latest add mhyrzt/virastar --global --agent codex --yes
```

## Optional repository instructions

The skill can trigger from its description without extra repository instructions. Add the following block to `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code when a repository should explicitly enforce its editorial workflow. Merge it with existing instructions; do not replace them blindly.

```markdown
## Persian thesis and paper editing

When a task involves Persian/Farsi academic prose, a thesis/dissertation,
a research paper/report, academic translation into Persian, or a
LaTeX/XePersian manuscript, use the `virastar` skill.

Repository policy:

- Default to audit-only and report findings with stable IDs. Modify files only
  after approval unless the user explicitly requests direct editing or rewriting.
- The current university/faculty/journal guide, supervisor decisions, project
  profile, and terminology register override generic conventions.
- Preserve scientific meaning, claim strength, numbers, equations, citations,
  labels, bibliography keys, glossary keys, notation, and author voice.
- Do not apply blanket ZWNJ, digit-conversion, passive-voice, first-person, or
  “anti-AI prose” rules.
- For LaTeX projects, inspect recursive inputs, macros, bibliography,
  glossary/acronym files, assets, and the compiled PDF when available.
- After approved changes, run the project's normal checks and compile command.

Project-specific files, when present:

- `editorial/project-profile.toml`
- `editorial/terminology-register.toml`
- `editorial/decisions.md`
```

## Set up a manuscript project

The recommended project layout is:

```text
repo/
├── AGENTS.md or CLAUDE.md
├── .agents/, .claude/, or .opencode/
│   └── skills/
│       └── virastar/
├── editorial/
│   ├── project-profile.toml
│   ├── terminology-register.toml
│   ├── decisions.md
│   └── audits/
├── main.tex
└── chapters/
```

Create `editorial/`, then copy and customize the relevant templates from the skill's `assets/` directory:

- `project-profile.example.toml` → `editorial/project-profile.toml`;
- `decision-log.example.md` → `editorial/decisions.md`;
- `issue-report-template.md` → an audit report when needed.

Create a project terminology register as schema-versioned TOML. Project entries may use the richer `[[entries]]` shape documented in [`references/06-terminology-bilingual-text.md`](references/06-terminology-bilingual-text.md); project-approved entries override bundled reference candidates.

For a University of Tehran project, start with `project-profile.ut-tehran.example.toml` and load `overlays/university-of-tehran.md`. Always attach the current university-wide guide and the applicable faculty or department supplement.

## Typical workflow

The default workflow is:

```text
resolve authority → gather context → detect → report → approve → patch → verify
```

Severity, confidence, edit risk, and authority are tracked independently. The first pass normally reports issues without changing files.

Example prompts:

```text
Audit chapters/03-methodology.tex with Virastar.
Do not edit. Report orthography, terminology, scientific-claim, notation,
and LaTeX issues with stable IDs.
```

```text
Compare the English and Persian versions of Chapter 4. Preserve every
number, hedge, limitation, equation, and citation. Report semantic drift
before proposing Persian revisions.
```

```text
Apply ORTH-001..ORTH-014, TERM-003, and CLAIM-002. Leave all STYLE issues
untouched, then compile and summarize the remaining findings.
```

## Deterministic audit helper

Run a basic audit with:

```bash
uv run python scripts/audit_virastar.py --root main.tex
```

Include project policy and terminology with:

```bash
uv run python scripts/audit_virastar.py \
  --root main.tex \
  --profile editorial/project-profile.toml \
  --terms editorial/terminology-register.toml \
  --format both \
  --output editorial/audits/pre-edit
```

Safe normalization is deliberately narrow and opt-in:

```bash
# Preview a diff without changing files
uv run python scripts/audit_virastar.py thesis/ --fix-safe

# Write changes and create .bak files
uv run python scripts/audit_virastar.py thesis/ --fix-safe --write
```

The safe fixer only normalizes Unicode character variants and cleans up tatweel and duplicate ZWNJ in unprotected prose. It does not rewrite words, compounds, punctuation, or sentences.

When the skill is installed outside the manuscript repository, invoke the script using its installed path instead of `scripts/audit_virastar.py`.

## English-to-Persian terminology lookup

Query the bundled IPL glossary:

```bash
uv run python scripts/terminology.py "accuracy"
```

Use a project glossary with custom-first precedence:

```bash
uv run python scripts/terminology.py "signed-KL policy guidance" \
  --glossary editorial/terminology-register.toml
```

Lookup uses normalized exact English matching and labels every result by status and source. A matching custom entry suppresses the bundled entry for that key. When no exact match exists, suggestions are reported separately and are not presented as translations. Use `--json` for structured output or `--no-builtin` to disable fallback.

The committed TOML asset can be reproduced from an authorized local copy of the supplied PDF:

```bash
uv run --group glossary-build python scripts/import_ipl_glossary.py \
  "IPL Glossary.pdf"
```

The source PDF is not distributed with the skill.

## Included material

- the production [`SKILL.md`](SKILL.md) workflow;
- authority resolution and project-profile guidance;
- Persian orthography, grammar, terminology, translation, and scientific-claim references;
- citation, figure, table, equation, and LaTeX/XePersian safety checks;
- a conservative static auditor with tests and routing evals;
- a TOML terminology loader and English-to-Persian lookup tool;
- 1,814 attributed IPL glossary headwords stored as reference candidates;
- a University of Tehran overlay;
- a source audit recording retained, adapted, and rejected guidance.

## Sources and acknowledgements

This skill is a synthesis. No single repository is treated as a complete or normative guide to Persian scholarly writing.

Material influences include:

- [`sinamomken/tehran-thesis`](https://github.com/sinamomken/tehran-thesis) for thesis organization, glossary management, bibliography handling, and useful XePersian patterns. Its September 2013 formatting assumptions are historical guidance, not current institutional authority.
- [`LimHyungTae/awesome-claudecode-paper-proofreading`](https://github.com/LimHyungTae/awesome-claudecode-paper-proofreading) for the report-first proofreading workflow and source/rendered-output verification.
- [`ali2000hos/persian-writing`](https://github.com/ali2000hos/persian-writing) for practical Persian and RTL concerns including ZWNJ, Unicode variants, punctuation, translationese, and register.
- [`0xRadikal/Academic-Paper-Writer-Skill`](https://github.com/0xRadikal/Academic-Paper-Writer-Skill) for citation discipline, terminology consistency, section functions, and non-fabrication principles.

The bundled terminology register includes words transcribed from *Signal Processing Glossary* by Shohreh Kasaei, Image Processing Lab (IPL), Sharif University of Technology. The glossary was created in August 2009; the provided PDF edition is dated December 1, 2025. These records are attributed `reference` candidates, not automatically preferred translations, and they never override an approved project glossary. The provided PDF contains no license statement, and IPL or Sharif University is not represented as endorsing Virastar.

The controlling authoritative sources within their proper scope are the [Academy of Persian Language and Literature](https://apll.ir/), the target institution or journal, and resources from [IranDoc](https://irandoc.ac.ir/). For exact provenance and scope decisions, see [`references/10-source-audit.md`](references/10-source-audit.md).

## Validate the package

```bash
uv lock --check
uv run python -m unittest discover -s tests -v
uv run python scripts/run_evals.py
uv run python scripts/validate_skill.py
uv run python -m compileall -q scripts tests
```

## Version and license

Current Virastar version: `0.2.0` (2026-08-16).

See [`LICENSE`](LICENSE) for license terms.
