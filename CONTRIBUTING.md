# Contributing

Every skill in `skills/` follows the standard below, whether we wrote it or
copied it from its author. `node scripts/check-skills.mjs` checks the parts a
script can check; run it before opening a pull request.

## Adding a skill

1. Open a pull request that adds the skill folder under `skills/<name>/` and a
   row to `catalog.json`.
2. A copied skill keeps its author's license file in its folder, and gets a row
   in `CREDITS.md` with the source repo, path, commit, license and what was
   changed. Apache-2.0 skills that we modify also carry a `MODIFIED.md`.
3. Don't add a skill that duplicates one already here. Improve the existing
   skill instead, or explain in the pull request what the new one covers that
   the existing one doesn't.

## The skill standard

The standard follows the [Agent Skills specification](https://agentskills.io)
and Anthropic's skill-authoring best practices.

### Folder

```
skills/<name>/
├── SKILL.md          required
├── references/       optional, loaded only when SKILL.md points to them
├── scripts/          optional, run rather than read
├── assets/           optional, templates and fonts
└── LICENSE           for copied skills, the author's license
```

- The folder name equals the skill's `name`.
- Reference files sit one level below `SKILL.md`; a reference doesn't send the
  agent on to another reference.
- Paths use forward slashes.

### Frontmatter

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
  `allowed-tools`, `metadata`. Anything else goes under `metadata` or is
  dropped.
- `name`: lowercase letters, digits and hyphens; at most 64 characters; unique
  in the repo.
- `description`: English, at most 1,024 characters, third person. It says
  what the skill does and when to use it, and includes the words a user would
  type, Persian ones in «» where they help matching.
- `metadata.author` and `metadata.source` are required for copied skills.

### Body

- Instructions are in English. Persian appears only as examples, quoted terms,
  sample output and word lists.
- One `#` title in English, then sections that start with what the agent has
  to do.
- Under 500 lines. Move long tables, catalogs and examples into `references/`
  and say in `SKILL.md` when to read each file. A reference longer than 100
  lines starts with a short contents list.
- Concise: assume the agent is capable, and keep only what it wouldn't know.
- One term per concept. Use "ZWNJ (نیم‌فاصله)" for the half-space, "register"
  for formality level, "Iranian Persian", "Dari" and "Tajik" for the three
  standards.
- Name other skills in backticks (`persian-writing`) when the agent should
  load them too.
- No time-sensitive statements ("as of this year"), no marketing, no emoji.
- Scripts the skill mentions exist in its `scripts/` folder, with how to run
  them.
- The bundled and recommended Persian font is Sahel
  (https://github.com/rastikerdar/sahel-font, SIL OFL).
