# Installing

## The CLI

**You do not have to install anything.** `./install.sh` bundles the engine and
the full lexicon into every skill it installs, reachable as `bin/salsi` inside
the skill folder. Python 3.10+ is the only requirement, and there are no
dependencies.

Installing it on your PATH as well is optional:

```bash
pip install salsi      # or, from a clone: pip install -e .
salsi info
```

On systems where pip refuses to touch the environment (PEP 668), use the
bundled copy or a virtualenv. `python3 -m salsi` works identically to
`salsi` wherever the package is importable.

## The skill

`./install.sh` from the repository root detects what you have and offers to
install into each. Or do it by hand:

| Tool | Where the skill goes |
| --- | --- |
| Claude Code (all users) | `~/.claude/skills/salsi/` |
| Claude Code (one project) | `.claude/skills/salsi/` |
| Claude.ai / Claude Desktop | `./install.sh --bundle ./dist` then upload that folder |
| Codex | append `skills/adapters/AGENTS.md` to your `AGENTS.md` |
| Cursor | `.cursor/rules/salsi.mdc` |
| Windsurf | `.windsurf/rules/salsi.md` |
| Cline / Roo | `.clinerules/salsi.md` |
| Continue | `.continue/rules/salsi.md` |
| Zed | add to `.rules` |
| Anything else | paste `skills/adapters/PROMPT.md` into the system prompt |

Copy the whole `salsi/` directory, not just `SKILL.md` — the bundled
engine and the reference files are what make the skill work on its own. Use
`./install.sh --bundle <dir>` to produce that self-contained folder anywhere.

## Without a shell

Where an assistant cannot run commands at all, the skill falls back to
`reference/core-words.md` — the settled replacements only, ~119 words rather
than 20,129. That is a real reduction in capability, so the skill is told to
say when it is working that way.

## As a check in CI

```yaml
- run: pip install salsi
- run: salsi scan docs/**/*.md --level safe --strict
```

`--level safe` only fails on replacements nobody argues about, which is the
right bar for a gate that blocks a merge.

## As a git hook

```bash
#!/bin/sh
# .git/hooks/pre-commit
git diff --cached --name-only --diff-filter=ACM | grep '\.md$' \
  | xargs -r salsi scan --level safe --strict
```
