# persianskills

Agent skills that make AI write Persian correctly, for readers in Iran,
Afghanistan and Tajikistan. Works with Claude Code, Codex, Cursor and any
agent that reads `SKILL.md`. The full directory, including skills by other
authors, is at **[persianskills.com](https://persianskills.com)**.

مهارت‌هایی که به ایجنت هوش مصنوعی کمک می‌کنند فارسی را درست بنویسد، برای خواننده‌ای در ایران، افغانستان یا تاجیکستان. فهرست کامل، همراه با مهارت‌های سازندگان دیگر، در [persianskills.com](https://persianskills.com) است.

## Skills in this repo

| Skill | For | Status |
|---|---|---|
| [`persian-writing`](skills/persian-writing) | Iranian Persian prose, orthography, cleanup scripts, RTL documents | By [ali2000hos](https://github.com/ali2000hos/persian-writing), copied unchanged from v1.4.0 |
| [`persian-localization`](skills/persian-localization) | Product and UI translation into any Persian variety | Draft |
| [`dari-writing`](skills/dari-writing) | Dari for Afghanistan, Hazaragi, Persian speakers in Pakistan | Draft, needs native Dari review |
| [`tajik-writing`](skills/tajik-writing) | Tajik in Cyrillic, for Tajikistan, Uzbekistan and Russia | Draft, needs native Tajik review |

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

- **`persian-writing`** is the work of
  [ali2000hos/persian-writing](https://github.com/ali2000hos/persian-writing)
  and its contributors, copied at commit `75fcdf3` (v1.4.0) under its MIT
  license, with fonts under the SIL OFL. Star and contribute upstream; to
  update this copy, recopy it from there and change the commit above.
- **`persian-localization`** comes from a native Persian speaker's review of
  [Edyt](https://edyt.app)'s Persian translation.
- **`dari-writing`** and **`tajik-writing`** were drafted from Unicode CLDR
  data and the sources listed at the end of each skill. They need native
  review; corrections are the most useful contribution.

## Add a skill to the directory

The site lists every entry in [`catalog.json`](catalog.json). Add a row with
the skill's name, author, URL, variety (`iran`, `afghanistan`, `tajikistan`
or `all`), category, license and a one-line description in English and
Persian, then open a pull request. Dari, Hazaragi and Tajik skills are the
scarcest.

## Site

```bash
node site/build.mjs     # writes site/dist (no dependencies)
```

## License

MIT for this repo's own skills and site. `skills/persian-writing` keeps its
own license; see [LICENSE](LICENSE).
