---
name: persian-skill-standard
description: >-
  Writes, copies or normalizes an agent skill for Persian (Iranian Persian,
  Dari or Tajik) to the persianskills standard: the skill name, the folder
  layout, file names, frontmatter, description, body, content, licenses,
  credit and registration in the collection. Use when creating a new Persian
  skill, bringing a copied skill into the persianskills repo, renaming skills
  or their files, cleaning a skill folder, or preparing a skill for a pull
  request. Triggers include "normalize this skill", "make this skill follow
  the standard", "prepare a skill for persianskills", «استاندارد مهارت»,
  «یکدست کردن اسکیل».
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/a-ahandani/persianskills
  version: 0.1.0
---

# Persian skill standard

Every skill in the persianskills collection follows these rules, whether we
wrote it or copied it. Apply them in order. Rules marked **(checked)** are
enforced by `node scripts/check-skills.mjs` at the repo root; follow the rest
by reading. When the skill is ready, evaluate it with
`persian-skill-evaluation`.

## Steps

1. Check the gates: scope and license.
2. Name the skill.
3. Lay out the folder and remove what doesn't belong.
4. Name every file and update every reference.
5. Write the frontmatter and description.
6. Write the body.
7. Clean the content.
8. Credit the author and keep the license.
9. Register the skill in the collection.
10. Run the validator, then `persian-skill-evaluation`.

## 1. Gates

- **Scope:** the skill teaches the agent something about the Persian
  language: writing, register, translation, orthography, Dari, Tajik,
  typography, right-to-left layout, calendar or locale. Integrations with
  Iranian services and general tools are listed in `catalog.json` as links
  and not copied.
- **Duplicates:** if a skill here already covers the topic, improve that one
  instead, or state what the new skill does that the existing one doesn't.
- **License (to copy):** MIT, Apache-2.0, BSD, MIT-0 or CC0. Read the license
  file itself. Anything else (no license, non-commercial, no
  redistribution) becomes a link-only row in `catalog.json`.

## 2. Name (checked)

The name is `<variety>-<topic>`:

- **Variety:** `persian` for Iranian Persian or for every variety, `dari` for
  Afghanistan, `tajik` for Tajikistan.
- **Topic:** plain English for what the skill does: `persian-calendar`,
  `persian-rtl-design`, `persian-native-words`, `tajik-proofreading`.
- Lowercase letters, digits and hyphens, at most 64 characters, unique in
  the repo, and the same as the folder name.
- No project, product or brand names, no language codes, and no `-skill`,
  `-skills` or `-toolkit` suffix. Examples of renamed copies:

  | Upstream | Here |
  |---|---|
  | `virastar` | `persian-academic-writing` |
  | `salsi` | `persian-native-words` |
  | `kumihan-fa` | `persian-typography` |
  | `scientific-fa-translation-skill` | `persian-scientific-translation` |
  | `tajik-toolkit` | `tajik-proofreading` |

- A copied skill gets a name that follows this rule. Its CREDITS.md row
  starts with "Renamed from `<upstream name>`".

## 3. Folder layout (checked)

```
skills/<name>/
├── SKILL.md      required
├── references/   Markdown the agent reads when SKILL.md says so
├── scripts/      code the agent runs
├── assets/       templates, fonts, and data files used in output or read by scripts
├── evals/        test prompts, expected results and fixtures for evaluating the skill
├── tests/        automated tests for the scripts
├── LICENSE       the author's license, for copied skills
└── NOTICE        Apache-2.0 notices and our modification notes
```

- Nothing else sits at the top level of a skill folder.
- Every skill sits directly in `skills/<name>/`. Split a bundle of several
  skills into sibling folders, each with its own `LICENSE` and `NOTICE`.
- Remove upstream repo files that agents don't load: README, CONTRIBUTING,
  CHANGELOG, INSTALL, UPDATES and AGENTS files; host manifests
  (`.claude-plugin/`, `.codex-plugin/`, `gemini-extension.json`,
  `agents/openai.yaml`, `.cursor/`); packaging (`pyproject.toml`, lockfiles,
  `.gitignore`); README screenshots and preview media; release inventories;
  and copies of `SKILL.md` made for other hosts.
- If `SKILL.md` relied on a removed file, rewrite the instruction. For
  example, `uv run --project <dir> python scripts/x.py` becomes
  `python3 scripts/x.py`, with any dependencies named in `compatibility`.
- No caches or build output: `__pycache__`, `.DS_Store`, `node_modules`,
  `dist`.
- Reference files sit one level below `SKILL.md`. A reference doesn't send the
  agent on to another reference.

## 4. File names (checked)

- Lowercase words joined by hyphens, with one extension:
  `rule-catalog.json`, `report-schema.json`, `persian-words.txt`,
  `sketch-player.tsx`, `install-fonts.sh`.
- Python files use underscores instead (`check_source.py`), because Python
  can't import a module whose name has a hyphen. This applies to every `.py`
  file.
- Folder names are lowercase words joined by hyphens.
- Exceptions: `SKILL.md`, `LICENSE` and `NOTICE`; files a tool requires by
  name (`package.json`, `tsconfig.json`, `remotion.config.ts`,
  `__init__.py`); and files in a `fonts/` folder, which keep the font
  family's own names (`Sahel-Bold.ttf`, `Sahel-OFL.txt`).
- No old or brand names in file names: `audit_virastar.py` became
  `audit.py`.
- After a rename, update every reference to the file: `SKILL.md`, references,
  scripts, tests, imports and paths built in code. Then search the folder for
  the old name.

## 5. Frontmatter (checked)

```yaml
---
name: persian-example
description: >-
  Does X for Persian text. Use when the user asks for Y, mentions Z, or
  writes «…».
license: MIT
compatibility: Optional. What the skill needs to run (tools, network).
allowed-tools: Optional, only when the skill runs specific tools.
metadata:
  author: who wrote it
  source: https://github.com/owner/repo
  version: "1.0.0"
---
```

- Allowed fields: `name`, `description`, `license`, `compatibility`,
  `allowed-tools`, `metadata`. Move anything else under `metadata` or drop
  it.
- `metadata.author` and `metadata.source` are required. Copied skills also
  record the upstream commit and a one-line `changes` summary.
- `description`: English, third person, at most 1,024 characters. It says
  what the skill does and when to use it, and includes the words a user
  would type, with Persian ones in «» where they help matching. It doesn't
  start with "I", "we" or "you".

## 6. Body (checked in part)

- Instructions are in English. Persian appears only as examples, quoted
  terms, sample output and word lists.
- One `#` title in English that names the topic, then sections that start
  with what the agent has to do. No emoji in headings.
- Under 500 lines. Move long tables, catalogs and examples into
  `references/` and say in `SKILL.md` when to read each file. A reference
  longer than 100 lines starts with a short contents list.
- Concise: assume the agent is capable and keep only what it wouldn't know.
  Generic advice that isn't about Persian doesn't belong.
- One term per concept: "ZWNJ (نیم‌فاصله)" for the half-space, "register" for
  formality level, and "Iranian Persian", "Dari" and "Tajik" for the three
  standards.
- No time-sensitive statements ("as of this year"), no marketing.
- Every file the body points to exists (checked for `references/`,
  `scripts/`, `assets/`, `evals/` and `tests/` paths). Scripts come with the
  command that runs them.
- The bundled and recommended Persian font is Sahel
  (https://github.com/rastikerdar/sahel-font, SIL OFL).

## 7. Content

- Name other skills by their names, in backticks (`persian-writing`), when
  the agent should load them too.
- The skill refers to itself by its name or its topic, never by the upstream
  project's brand. That covers titles, "Act as …" lines, report headings,
  script help text, docstrings and test names. Brand names appear only as
  credit: `metadata`, CREDITS.md, `NOTICE` and `LICENSE`.
- External names stay as they are: another project's command-line tool or
  package (`salsi`, `pdfplumber`), upstream repo URLs, environment
  variables, font family names, and provenance fields in data files.
- Paths are relative to the skill folder, such as scripts/audit.py, never to
  an upstream repo layout such as skills/old-name/scripts/audit.py.
- Install instructions point at this repo: `npx skills add
  a-ahandani/persianskills --skill <name>`.

## 8. Credit and licenses

- Keep the author's `LICENSE` file unchanged.
- **Apache-2.0:** keep the upstream `NOTICE` text unchanged and add a
  `## Modifications` section that lists every change with its date. If
  upstream has no `NOTICE`, create one that names the original skill, its
  repo and its license.
- Add a row to CREDITS.md: the skill, its source repo, the path upstream, the
  commit, the license, and what we changed.
- For a skill we wrote from someone else's idea, credit the idea in
  CREDITS.md and copy no text.

## 9. Register

- `catalog.json`: a row with `name`, `author`, `url`, `path`, `here`,
  `variety` (`iran`, `afghanistan`, `tajikistan` or `all`), `category`,
  `license`, `commit` for copies, and a one-line `description`.
- `.claude-plugin/marketplace.json`: add `./skills/<name>` to the plugin's
  `skills` list.
- README.md: our own skills go in its table.

## 10. Check

1. Run `node scripts/check-skills.mjs`. It must report 0 problems.
2. Search the skill folder for its old names and the upstream brand.
3. Run the skill's own tests, if it has any.
4. Evaluate the skill with `persian-skill-evaluation` and put the report in
   the pull request. A skill joins the collection with the verdict **Keep**,
   or **Fix** once the listed fixes are made.
