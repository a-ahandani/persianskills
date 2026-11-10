# Credits

Every skill in `skills/` that we didn't write is a copy of its author's work,
made under the license its author chose. That license file sits in the
skill's folder. Star and contribute upstream. To update a copy, recopy it
from upstream and change its commit below.

**Font:** we switched every bundled or recommended Persian font to
[Sahel](https://github.com/rastikerdar/sahel-font) v3.4.0 by Saber Rastikerdar
(SIL Open Font License 1.1). Each change is listed below. The modified
Apache-2.0 skills (persian-rtl-design, persian-finglish and the four
persian-typography skills) keep their upstream NOTICE text, and their NOTICE
file lists what we changed, as that license asks.

## Copied skills

Every copied skill was also brought to the repo's standard
([`persian-skill-standard`](skills/persian-skill-standard/SKILL.md)): a name
that says what it does, the standard folder layout and file names, English
instructions with Persian examples, a third-person description, and standard
frontmatter with author, source and upstream commit. Upstream repo files that
agents don't load (READMEs, changelogs, install notes, host plugin manifests,
packaging files, README screenshots and copies of SKILL.md for other hosts)
were removed.

| Skill | Source | Path upstream | Commit | License | What we changed |
|---|---|---|---|---|---|
| [`persian-writing`](skills/persian-writing) | [ali2000hos/persian-writing](https://github.com/ali2000hos/persian-writing) | `.` | `75fcdf3` | MIT (fonts SIL OFL) | Bundled and recommended font changed from Vazirmatn (body) and Lalezar (display) to Sahel, with Sahel Black as the display weight; frontmatter standardized, description and Persian-only phrasing put in English, long references given contents lists, universal edition regenerated. |
| [`tajik-proofreading`](skills/tajik-proofreading) | [firdavsi-tech/tajik-toolkit](https://github.com/firdavsi-tech/tajik-toolkit) | `.` | `975cd6e` | MIT | Renamed from `tajik-toolkit`; frontmatter standardized; the 10 reference files moved into `references/` with links updated. |
| [`persian-seo`](skills/persian-seo) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-seo` | `7d56b50` | MIT | Frontmatter standardized (third-person description, Persian triggers in «», metadata). |
| [`persian-rtl-ui`](skills/persian-rtl-ui) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-rtl-ui` | `7d56b50` | MIT | Suggested Persian UI font changed from Vazirmatn to Sahel; frontmatter standardized; `persian-calendar` named where it applies. |
| [`persian-conversational`](skills/persian-conversational) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-conversational` | `7d56b50` | MIT | Description in the third person with Persian triggers in «», one heading put in English, metadata added. |
| [`persian-ui-copy`](skills/persian-ui-copy) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-ui-copy` | `7d56b50` | MIT | Description in the third person with Persian triggers in «», emoji column headers replaced with words, metadata added. |
| [`persian-formal`](skills/persian-formal) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-formal` | `7d56b50` | MIT | Description in the third person with Persian triggers in «», letter heading put in English, emoji markers replaced with words, metadata added. |
| [`persian-calendar`](skills/persian-calendar) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/jalali-calendar` | `7d56b50` | MIT | Renamed from `jalali-calendar`; frontmatter standardized; the `persiantools` library named for one-off conversions. |
| [`persian-scientific-translation`](skills/persian-scientific-translation) | [isArman/scientific-fa-translation-skill](https://github.com/isArman/scientific-fa-translation-skill) | `.` | `27cad0f` | MIT | Renamed from `scientific-fa-translation-skill`; preferred Persian font changed from Vazirmatn to Sahel (`scripts/fetch-vazirmatn.sh` became `scripts/fetch-sahel.sh`); frontmatter standardized, description and Persian-only phrasing put in English, long references given contents lists. |
| [`persian-voice`](skills/persian-voice) | [RezaEsmailGol/lahne-man](https://github.com/RezaEsmailGol/lahne-man) | `skills/lahne-man` | `168e2a6` | MIT | Renamed from `lahne-man`; instructions, headings and description translated from Persian into English with every Persian example kept; `eval.md` moved to `references/eval.md` and translated. |
| [`persian-telegram`](skills/persian-telegram) | [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) | `skills/telegram-persian-enforcer` | `bac8138` | MIT | Renamed from `telegram-persian-enforcer`; instructions, headings, description, checker messages and list-file comments translated from Persian into English with every Persian example kept; version moved into metadata. |
| [`persian-translation`](skills/persian-translation) | [Mojtaba-Alehosseini/persian-skill](https://github.com/Mojtaba-Alehosseini/persian-skill) | `.` | `4264f6e` | MIT | Renamed from `persian` (name clash); default document font changed from Arial to Sahel with Arial as fallback; English title, fuller description, contents lists, metadata added. |
| [`persian-academic-writing`](skills/persian-academic-writing) | [mhyrzt/virastar](https://github.com/mhyrzt/virastar) | `.` | `04937f4` | MIT | Renamed from `virastar`; description in the third person, the audit command uses the skill's own folder, contents lists added to all 12 references, metadata added. |
| [`persian-finglish`](skills/persian-finglish) | [thesamehosuh/xratu](https://github.com/thesamehosuh/xratu) | `assets/skills/finglish-normalize` | `c88daf5` | Apache-2.0 | Renamed from `finglish-normalize`; description in the third person, pointers to the removed `natural-farsi` now point to `persian-conversational`, upstream app reference removed (see NOTICE). |
| [`persian-rtl-design`](skills/persian-rtl-design) | [Baghlani/rtl-design](https://github.com/Baghlani/rtl-design) | `skills/rtl-design` | `b7c5229` | Apache-2.0 | Renamed from `rtl-design`; default Persian font changed from Vazirmatn to Sahel in the font table and recipes (Vazirmatn and Estedad kept as alternatives); description in the third person, metadata added, contents lists in long references (see NOTICE). |
| [`persian-typography`](skills/persian-typography), [`persian-typography-web`](skills/persian-typography-web), [`persian-typography-documents`](skills/persian-typography-documents), [`persian-typography-review`](skills/persian-typography-review) | [landco-llc/kumihan](https://github.com/landco-llc/kumihan) | `plugins/kumihan-fa` | `1b27c93` | Apache-2.0 | Renamed from `kumihan-fa`; suggested font changed from Vazirmatn to Sahel in `references/web.md` and copies; prebuilt release zips removed; the four skills' descriptions and instructions made English only, how to run `runtime/check_source.py` added, inventory checksums updated (see NOTICE). |
| [`persian-motion-design`](skills/persian-motion-design) | [atmirrr/persian-motion-director](https://github.com/atmirrr/persian-motion-director) | `.` | `5499640` | MIT | Renamed from `persian-motion-director`; bundled font changed from Vazirmatn to Sahel (the pre-shaped letter outlines and preview GIFs were made with Vazirmatn and not regenerated); frontmatter standardized, description in the third person, script usage added. |
| [`persian-native-words`](skills/persian-native-words) | [pooooooriya/salsi](https://github.com/pooooooriya/salsi) | `skills/salsi` | `303ebc8` | MIT | Renamed from `salsi`; install instructions corrected (the engine isn't bundled; `pip install git+https://github.com/pooooooriya/salsi`), `reference/` renamed to `references/`, contents lists added, metadata added. |

## Our own skills

MIT, written for this repo. Five of them cover topics from skills whose authors
gave no license, so we couldn't copy them. We wrote our own from scratch, without
copying any text, and credit those authors for the idea.

| Skill | Notes |
|---|---|
| [`persian-localization`](skills/persian-localization) | From a native speaker's review of Edyt's Persian translation. |
| [`dari-writing`](skills/dari-writing) | Drafted from Unicode CLDR and the sources it lists; needs native review. |
| [`tajik-writing`](skills/tajik-writing) | Drafted from Unicode CLDR and the sources it lists; needs native review. |
| [`persian-locales`](skills/persian-locales) | Inspired by skills-on-ai/skills-on-ai locale cards. |
| [`persian-translation-review`](skills/persian-translation-review) | Inspired by jwiegley/claude-prompts (persian). |
| [`persian-orthography`](skills/persian-orthography) | Built from the Academy of Persian Language and Literature's «دستور خطّ فارسی (ویراست جدید)», 1401 ([PDF](https://apll.ir/wp-content/uploads/2023/07/Dastour-e-Khat-17.04.1402.pdf)): rules summarized in our own words with page references; the book's text and full word lists are not copied. Inspired by Byte-Magazine/skills (byte-virastari). |
| [`persian-book-translation`](skills/persian-book-translation) | Inspired by m4tinbeigi-official/hermes-literary-translation-mastery. |
| [`persian-skill-standard`](skills/persian-skill-standard) | The repo's skill standard, written as a skill. |
| [`persian-skill-evaluation`](skills/persian-skill-evaluation) | Built from this repo's reviews of Persian skills, with the Academy's «دستور خطّ فارسی» and Unicode CLDR as references. |

## Listed but not copied

| Entry | Why |
|---|---|
| [BAHROMTJ/nutq](https://github.com/BAHROMTJ/nutq) | MCP server with no skill file |
| [masoudroot/persian-writing-mcp](https://github.com/masoudroot/persian-writing-mcp) | MCP server with no skill file |
| [openaccountants](https://github.com/openaccountants/openaccountants) af-* and tj-* | The OpenAccountants Guide License doesn't allow redistribution here |
| [i18n-agent/i18nstack](https://github.com/i18n-agent/i18nstack) (`localize-fa`) | Overlaps `persian-localization`, so it was removed in the review of 2026-11-10 |
| [clawic/skills](https://github.com/clawic/skills) (`persian`) | Overlaps `persian-conversational`, so it was removed in the review of 2026-11-10 |
| [Ariiima/persian-writer](https://github.com/Ariiima/persian-writer) (`persian-writer`) | Overlaps `persian-writing`, so it was removed in the review of 2026-11-10 |
| [nimaansari/persian-language](https://github.com/nimaansari/persian-language) (`persian-language`) | Overlaps `persian-writing`, so it was removed in the review of 2026-11-10 |
| [sadrmanesh/commerce-agent-skills](https://github.com/sadrmanesh/commerce-agent-skills) (`rtl-and-persian-localization`) | Overlaps `persian-rtl-ui`, so it was removed in the review of 2026-11-10 |
| [PouyaRN/persian-formatting-skill](https://github.com/PouyaRN/persian-formatting-skill) (`persian-formatting`) | Overlaps `persian-writing`, so it was removed in the review of 2026-11-10 |
| [mmgghh/persian-writing-skills](https://github.com/mmgghh/persian-writing-skills) (`persian-formal-mmgghh`) | Overlaps `persian-formal`, so it was removed in the review of 2026-11-10 |
| [mmgghh/persian-writing-skills](https://github.com/mmgghh/persian-writing-skills) (`persian-informal`) | Overlaps `persian-conversational`, so it was removed in the review of 2026-11-10 |
| [siawash1991/persian-agent-skills](https://github.com/siawash1991/persian-agent-skills) (`persian-unslop`) | Overlaps `persian-voice`, so it was removed in the review of 2026-11-10 |
| [thesamehosuh/xratu](https://github.com/thesamehosuh/xratu) (`natural-farsi`) | Overlaps `persian-conversational`, so it was removed in the review of 2026-11-10 |
| [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) (`iran-validation`) | Validation of Iranian identifiers, not about the Persian language; removed on 2026-11-10 |
| [majiidd/persiantools](https://github.com/majiidd/persiantools) (`convert-persian-dates`) | A wrapper for one Python library; the calendar is covered by `persian-calendar` and `persian-locales`; removed on 2026-11-10 |
| [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) (`persian-documents`) | Its RTL document rules are covered by `persian-writing`, which also checks Word and PDF output; removed on 2026-11-10 |
| [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) (`persian-resume`) | Mostly generic resume advice; Persian document rendering is covered by `persian-writing`; removed on 2026-11-10 |
| [karimi-mohammad/local-time-mcp](https://github.com/karimi-mohammad/local-time-mcp) (`local-time`) | A clock tool, not about the Persian language; removed on 2026-11-10 |
| [Abulfadl-Ahmadi/shadcn-persian](https://github.com/Abulfadl-Ahmadi/shadcn-persian) (`shadcn-persian`) | A UI component kit; its RTL parts are covered by `persian-rtl-ui` and `persian-rtl-design`; removed on 2026-11-10 |
| [sadrmanesh/commerce-agent-skills](https://github.com/sadrmanesh/commerce-agent-skills) (`iranian-payment-gateways`) | A payment integration, not about the Persian language; removed on 2026-11-10 |
| [ParsBench/ParsBench](https://github.com/ParsBench/ParsBench) (`parsbench`) | Usage notes for a benchmarking framework, not about the Persian language; removed on 2026-11-10 |
| [sepehr071/iran-mcp](https://github.com/sepehr071/iran-mcp) (`iran-mcp/*`) | Connectors for Iranian web services, not about the Persian language; removed on 2026-11-10 |
