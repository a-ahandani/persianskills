# persianskills

Agent skills that make AI write Persian correctly, for readers in Iran,
Afghanistan and Tajikistan. Works with Claude Code, Codex, Cursor and any
agent that reads `SKILL.md`. The full directory, including skills by other
authors, is at **[persianskills.com](https://persianskills.com)**.

مهارت‌هایی که به ایجنت هوش مصنوعی کمک می‌کنند فارسی را درست بنویسد، برای خواننده‌ای در ایران، افغانستان یا تاجیکستان. فهرست کامل، همراه با مهارت‌های سازندگان دیگر، در [persianskills.com](https://persianskills.com) است.

## Skills in this repo

Every skill here is about the Persian language: writing and register,
translation, orthography, Dari and Tajik, typography and right-to-left
layout, and calendar and locale. Each copied skill keeps its author's license
file and credit: 21 skills from 13 authors, plus 9 of our own.
Integrations with Iranian services and general tools are listed on the site
as links only. [CREDITS.md](CREDITS.md) gives each skill's source repo,
commit, license and what we changed.

Our own skills:

| Skill | For | Status |
|---|---|---|
| [`persian-localization`](skills/persian-localization) | Product and UI translation into any Persian variety | Draft |
| [`dari-writing`](skills/dari-writing) | Dari for Afghanistan, Hazaragi, Persian speakers in Pakistan | Draft, needs native Dari review |
| [`tajik-writing`](skills/tajik-writing) | Tajik in Cyrillic, for Tajikistan, Uzbekistan and Russia | Draft, needs native Tajik review |
| [`persian-locales`](skills/persian-locales) | CLDR data for fa-IR, fa-AF and tg | Draft |
| [`persian-translation-review`](skills/persian-translation-review) | Translator plus independent reviewer | Draft |
| [`persian-orthography`](skills/persian-orthography) | Copyediting by the Academy's «دستور خطّ فارسی» (1401), with page references | Draft |
| [`persian-book-translation`](skills/persian-book-translation) | Whole-book translation and RTL EPUB | Draft |
| [`persian-skill-standard`](skills/persian-skill-standard) | The rules every skill here follows, for preparing or normalizing a skill | Draft |
| [`persian-skill-evaluation`](skills/persian-skill-evaluation) | Evaluating a Persian skill: gates, accuracy, a with/without test, a verdict | Draft |

**Font:** every skill that bundles or recommends a Persian font uses
[Sahel](https://github.com/rastikerdar/sahel-font) by Saber Rastikerdar
(SIL OFL). Where an upstream skill used another font, we changed it and
say so in CREDITS.md.

## Install

```bash
npx skills add a-ahandani/persianskills                         # every skill
npx skills add a-ahandani/persianskills --skill dari-writing    # one skill
```

Claude Code plugin:

```
/plugin marketplace add a-ahandani/persianskills
/plugin install persian-skills@persianskills
```

For ChatGPT, Gemini and other chat apps, upload a skill's `SKILL.md` as
knowledge.

## Credits

- **Copied skills** keep their authors' licenses (MIT, Apache-2.0) in their
  folders. [CREDITS.md](CREDITS.md) lists each source and every change.
  Star and contribute upstream.
- **`persian-writing`** is the work of
  [ali2000hos/persian-writing](https://github.com/ali2000hos/persian-writing)
  and its contributors (v1.4.0, commit `75fcdf3`), with its font switched to
  Sahel.
- **`persian-localization`** comes from a native Persian speaker's review of
  [Edyt](https://edyt.app)'s Persian translation.
- **Our other skills** were written from Unicode CLDR data and the sources
  listed in each. Five cover topics from skills whose authors gave no
  license, so we couldn't copy them; we wrote our own and credit them as
  the inspiration.
- **Link only:** nutq and persian-writing-mcp are MCP servers with no skill
  file, and the openaccountants tax skills use a license that doesn't
  allow redistribution here, so the site links to them.

## Skill standard

Every skill follows one standard, written as a skill:
[`persian-skill-standard`](skills/persian-skill-standard/SKILL.md). It sets the
name (`persian-`, `dari-` or `tajik-` plus a plain topic), the folder layout,
file names, frontmatter, body and credit. New skills are prepared with it and
evaluated with `persian-skill-evaluation`; see [CONTRIBUTING.md](CONTRIBUTING.md).
Check with:

```bash
node scripts/check-skills.mjs
```

## Add a skill to the directory

The site lists every entry in [`catalog.json`](catalog.json). Add a row with
the skill's name, author, URL, variety (`iran`, `afghanistan`, `tajikistan`
or `all`), category, license and a one-line description, then open a pull
request. Dari, Hazaragi and Tajik skills are the scarcest.

## Site

```bash
node site/dev.mjs       # http://localhost:4823, rebuilds and reloads on every save
node site/build.mjs     # writes site/dist once (what Cloudflare Pages runs)
```

No dependencies, Node 20 or later. Page copy lives in `site/build.mjs`,
styles in `site/style.css`, the skill list in `catalog.json`, and the logos
in `site/favicon.svg` (the Edyt logo on gold), `site/edyt-mark.svg` (header),
`site/agents/` (agent logos) and `site/logo.svg` (the پ mark, not used on the
page). Set `PORT` to use another port.

## License

MIT for this repo's own skills and site. `skills/persian-writing` keeps its
own license; see [LICENSE](LICENSE).
