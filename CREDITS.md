# Credits

Every skill in `skills/` that we didn't write is a copy of its author's work,
made under the license its author chose. That license file sits in the
skill's folder. Star and contribute upstream. To update a copy, recopy it
from upstream and change its commit below.

**Font:** we switched every bundled or recommended Persian font to
[Sahel](https://github.com/rastikerdar/sahel-font) v3.4.0 by Saber Rastikerdar
(SIL Open Font License 1.1). Each change is listed below. Skills that ship NOTICE files keep them, and the
two modified Apache-2.0 skills (rtl-design, kumihan-fa) also carry a
`MODIFIED.md` stating what changed, as that license asks.

## Copied skills

Every copied skill was also brought to the repo's skill standard (see
CONTRIBUTING.md): English instructions with Persian examples, a third-person
description, standard frontmatter with author, source and upstream commit.

| Skill | Source | Path upstream | Commit | License | What we changed |
|---|---|---|---|---|---|
| [`persian-writing`](skills/persian-writing) | [ali2000hos/persian-writing](https://github.com/ali2000hos/persian-writing) | `.` | `75fcdf3` | MIT (fonts SIL OFL) | Bundled and recommended font changed from Vazirmatn (body) and Lalezar (display) to Sahel, with Sahel Black as the display weight; frontmatter standardized, description and Persian-only phrasing put in English, long references given contents lists, universal edition regenerated. |
| [`tajik-toolkit`](skills/tajik-toolkit) | [firdavsi-tech/tajik-toolkit](https://github.com/firdavsi-tech/tajik-toolkit) | `.` | `975cd6e` | MIT | Frontmatter standardized; the 10 reference files moved into `references/` with links updated. |
| [`persian-seo`](skills/persian-seo) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-seo` | `7d56b50` | MIT | Frontmatter standardized (third-person description, Persian triggers in «», metadata). |
| [`persian-rtl-ui`](skills/persian-rtl-ui) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-rtl-ui` | `7d56b50` | MIT | Suggested Persian UI font changed from Vazirmatn to Sahel; frontmatter standardized; `jalali-calendar` and `iran-validation` named where they apply. |
| [`persian-conversational`](skills/persian-conversational) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-conversational` | `7d56b50` | MIT | Description in the third person with Persian triggers in «», one heading put in English, metadata added. |
| [`persian-ui-copy`](skills/persian-ui-copy) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-ui-copy` | `7d56b50` | MIT | Description in the third person with Persian triggers in «», emoji column headers replaced with words, metadata added. |
| [`persian-formal`](skills/persian-formal) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-formal` | `7d56b50` | MIT | Description in the third person with Persian triggers in «», letter heading put in English, emoji markers replaced with words, metadata added. |
| [`jalali-calendar`](skills/jalali-calendar) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/jalali-calendar` | `7d56b50` | MIT | Frontmatter standardized; `convert-persian-dates` and `local-time` named for one-off conversions. |
| [`iran-validation`](skills/iran-validation) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/iran-validation` | `7d56b50` | MIT | Frontmatter standardized (third-person description, Persian triggers in «», metadata). |
| [`convert-persian-dates`](skills/convert-persian-dates) | [majiidd/persiantools](https://github.com/majiidd/persiantools) | `.agents/skills/convert-persian-dates` | `f210eef` | MIT | Frontmatter standardized (third-person description, Persian triggers, compatibility, metadata). |
| [`scientific-fa-translation-skill`](skills/scientific-fa-translation-skill) | [isArman/scientific-fa-translation-skill](https://github.com/isArman/scientific-fa-translation-skill) | `.` | `27cad0f` | MIT | Preferred Persian font changed from Vazirmatn to Sahel (`scripts/fetch-vazirmatn.sh` became `scripts/fetch-sahel.sh`); frontmatter standardized, description and Persian-only phrasing put in English, long references given contents lists. |
| [`lahne-man`](skills/lahne-man) | [RezaEsmailGol/lahne-man](https://github.com/RezaEsmailGol/lahne-man) | `skills/lahne-man` | `168e2a6` | MIT | Instructions, headings and description translated from Persian into English with every Persian example kept; `eval.md` moved to `references/eval.md` and translated. |
| [`persian-documents`](skills/persian-documents) | [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) | `skills/persian-documents` | `bac8138` | MIT | Default font changed from B Nazanin to Sahel in the DOCX and PDF generators; frontmatter standardized, description in the third person, script usage and config format added, long references given contents lists. |
| [`persian-resume`](skills/persian-resume) | [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) | `skills/persian-resume` | `bac8138` | MIT | Default font changed from Vazir to Sahel (HTML, PDF) and from B Nazanin to Sahel (DOCX); frontmatter standardized, description in the third person, script usage added, schema reference given a contents list. |
| [`telegram-persian-enforcer`](skills/telegram-persian-enforcer) | [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) | `skills/telegram-persian-enforcer` | `bac8138` | MIT | Instructions, headings, description, checker messages and list-file comments translated from Persian into English with every Persian example kept; version moved into metadata. |
| [`persian-skill`](skills/persian-skill) | [Mojtaba-Alehosseini/persian-skill](https://github.com/Mojtaba-Alehosseini/persian-skill) | `.` | `4264f6e` | MIT | Renamed from `persian` (name clash); default document font changed from Arial to Sahel with Arial as fallback; English title, fuller description, contents lists, metadata added. |
| [`virastar`](skills/virastar) | [mhyrzt/virastar](https://github.com/mhyrzt/virastar) | `.` | `04937f4` | MIT | Description in the third person, the audit command uses the skill's own folder, contents lists added to all 12 references, metadata added. |
| [`local-time`](skills/local-time) | [karimi-mohammad/local-time-mcp](https://github.com/karimi-mohammad/local-time-mcp) | `skill` | `821afce` | MIT | Only the `skill/` folder copied (the MCP server stays upstream); instructions translated from Persian to English, emoji removed, `local_time.py` moved into `scripts/`. |
| [`shadcn-persian`](skills/shadcn-persian) | [Abulfadl-Ahmadi/shadcn-persian](https://github.com/Abulfadl-Ahmadi/shadcn-persian) | `.` | `ac1d0c8` | MIT | Default Persian font changed from Vazirmatn to Sahel (jsDelivr, Farsi digits from Sahel FD instead of `ss01`); SKILL.md translated from Persian to English, emoji removed, folder map corrected. |
| [`iranian-payment-gateways`](skills/iranian-payment-gateways) | [sadrmanesh/commerce-agent-skills](https://github.com/sadrmanesh/commerce-agent-skills) | `skills/iranian-payment-gateways` | `308c909` | MIT | Frontmatter standardized (source, commit, Persian triggers); a pointer to an upstream skill not in this repo reworded. |
| [`parsbench`](skills/parsbench) | [ParsBench/ParsBench](https://github.com/ParsBench/ParsBench) | `skills/parsbench` | `bf1ba79` | Apache-2.0 | Frontmatter standardized, description in the third person, contents list added to `references/goldens.md` (see MODIFIED.md). |
| [`finglish-normalize`](skills/finglish-normalize) | [thesamehosuh/xratu](https://github.com/thesamehosuh/xratu) | `assets/skills/finglish-normalize` | `c88daf5` | Apache-2.0 | Description in the third person, pointers to the removed `natural-farsi` now point to `persian-conversational`, upstream app reference removed (see MODIFIED.md). |
| [`rtl-design`](skills/rtl-design) | [Baghlani/rtl-design](https://github.com/Baghlani/rtl-design) | `skills/rtl-design` | `b7c5229` | Apache-2.0 | Default Persian font changed from Vazirmatn to Sahel in the font table and recipes (Vazirmatn and Estedad kept as alternatives); description in the third person, metadata added, contents lists in long references (see MODIFIED.md). |
| [`kumihan-fa`](skills/kumihan-fa) | [landco-llc/kumihan](https://github.com/landco-llc/kumihan) | `plugins/kumihan-fa` | `1b27c93` | Apache-2.0 | Suggested font changed from Vazirmatn to Sahel in `references/web.md` and copies; prebuilt release zips removed; the four skills' descriptions and instructions made English only, how to run `runtime/check_source.py` added, inventory checksums updated (see MODIFIED.md). |
| [`persian-motion-director`](skills/persian-motion-director) | [atmirrr/persian-motion-director](https://github.com/atmirrr/persian-motion-director) | `.` | `5499640` | MIT | Bundled font changed from Vazirmatn to Sahel (the pre-shaped letter outlines and preview GIFs were made with Vazirmatn and not regenerated); frontmatter standardized, description in the third person, script usage added. |
| [`salsi`](skills/salsi) | [pooooooriya/salsi](https://github.com/pooooooriya/salsi) | `skills/salsi` | `303ebc8` | MIT | Install instructions corrected (the engine isn't bundled; `pip install git+https://github.com/pooooooriya/salsi`), `reference/` renamed to `references/`, contents lists added, metadata added. |
| [`iran-mcp/*`](skills/iran-mcp) (77) | [sepehr071/iran-mcp](https://github.com/sepehr071/iran-mcp) | `plugins/*/skills/*` | `51ba858` | MIT | Only the skill folders copied (servers stay upstream); frontmatter standardized with license and source. |

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
| [`farhangestan-orthography`](skills/farhangestan-orthography) | Built from the Academy of Persian Language and Literature's «دستور خطّ فارسی (ویراست جدید)», 1401 ([PDF](https://apll.ir/wp-content/uploads/2023/07/Dastour-e-Khat-17.04.1402.pdf)): rules summarized in our own words with page references; the book's text and full word lists are not copied. Inspired by Byte-Magazine/skills (byte-virastari). |
| [`persian-book-translation`](skills/persian-book-translation) | Inspired by m4tinbeigi-official/hermes-literary-translation-mastery. |

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
| [siawash1991/persian-agent-skills](https://github.com/siawash1991/persian-agent-skills) (`persian-unslop`) | Overlaps `lahne-man`, so it was removed in the review of 2026-11-10 |
| [thesamehosuh/xratu](https://github.com/thesamehosuh/xratu) (`natural-farsi`) | Overlaps `persian-conversational`, so it was removed in the review of 2026-11-10 |
