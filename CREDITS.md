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

| Skill | Source | Path upstream | Commit | License | What we changed |
|---|---|---|---|---|---|
| [`persian-writing`](skills/persian-writing) | [ali2000hos/persian-writing](https://github.com/ali2000hos/persian-writing) | `.` | `75fcdf3` | MIT (fonts SIL OFL) | Bundled and recommended font changed from Vazirmatn (body) and Lalezar (display) to Sahel, with Sahel Black as the display weight. |
| [`tajik-toolkit`](skills/tajik-toolkit) | [firdavsi-tech/tajik-toolkit](https://github.com/firdavsi-tech/tajik-toolkit) | `.` | `975cd6e` | MIT | Unchanged. |
| [`localize-fa`](skills/localize-fa) | [i18n-agent/i18nstack](https://github.com/i18n-agent/i18nstack) | `localize-fa` | `6bf6587` | MIT | Unchanged. |
| [`persian-seo`](skills/persian-seo) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-seo` | `7d56b50` | MIT | Unchanged. |
| [`persian-rtl-ui`](skills/persian-rtl-ui) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-rtl-ui` | `7d56b50` | MIT | Suggested Persian UI font changed from Vazirmatn to Sahel. |
| [`persian-conversational`](skills/persian-conversational) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-conversational` | `7d56b50` | MIT | Unchanged. |
| [`persian-ui-copy`](skills/persian-ui-copy) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-ui-copy` | `7d56b50` | MIT | Unchanged. |
| [`persian-formal`](skills/persian-formal) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/persian-formal` | `7d56b50` | MIT | Unchanged. |
| [`jalali-calendar`](skills/jalali-calendar) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/jalali-calendar` | `7d56b50` | MIT | Unchanged. |
| [`iran-validation`](skills/iran-validation) | [TronIsHere/vibefarsiui](https://github.com/TronIsHere/vibefarsiui) | `registry/skills/iran-validation` | `7d56b50` | MIT | Unchanged. |
| [`convert-persian-dates`](skills/convert-persian-dates) | [majiidd/persiantools](https://github.com/majiidd/persiantools) | `.agents/skills/convert-persian-dates` | `f210eef` | MIT | Unchanged. |
| [`scientific-fa-translation-skill`](skills/scientific-fa-translation-skill) | [isArman/scientific-fa-translation-skill](https://github.com/isArman/scientific-fa-translation-skill) | `.` | `27cad0f` | MIT | Preferred Persian font changed from Vazirmatn to Sahel; `scripts/fetch-vazirmatn.sh` became `scripts/fetch-sahel.sh`. |
| [`lahne-man`](skills/lahne-man) | [RezaEsmailGol/lahne-man](https://github.com/RezaEsmailGol/lahne-man) | `skills/lahne-man` | `168e2a6` | MIT | Unchanged. |
| [`persian`](skills/persian) | [clawic/skills](https://github.com/clawic/skills) | `skills/persian` | `f825206` | MIT | Skill name lowercased (`Persian` to `persian`). |
| [`persian-documents`](skills/persian-documents) | [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) | `skills/persian-documents` | `bac8138` | MIT | Default font changed from B Nazanin to Sahel in the DOCX and PDF generators. |
| [`persian-resume`](skills/persian-resume) | [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) | `skills/persian-resume` | `bac8138` | MIT | Default font changed from Vazir to Sahel (HTML and PDF) and from B Nazanin to Sahel (DOCX). |
| [`telegram-persian-enforcer`](skills/telegram-persian-enforcer) | [ehsanghaffar/skills](https://github.com/ehsanghaffar/skills) | `skills/telegram-persian-enforcer` | `bac8138` | MIT | Unchanged. |
| [`persian-skill`](skills/persian-skill) | [Mojtaba-Alehosseini/persian-skill](https://github.com/Mojtaba-Alehosseini/persian-skill) | `.` | `4264f6e` | MIT | Renamed from `persian` (name clash). Default document font changed from Arial to Sahel, with Arial as the fallback. |
| [`virastar`](skills/virastar) | [mhyrzt/virastar](https://github.com/mhyrzt/virastar) | `.` | `04937f4` | MIT | Unchanged. |
| [`persian-writer`](skills/persian-writer) | [Ariiima/persian-writer](https://github.com/Ariiima/persian-writer) | `.` | `5792f72` | MIT | Unchanged. |
| [`persian-language`](skills/persian-language) | [nimaansari/persian-language](https://github.com/nimaansari/persian-language) | `.` | `8c228b3` | MIT | Unchanged. |
| [`local-time`](skills/local-time) | [karimi-mohammad/local-time-mcp](https://github.com/karimi-mohammad/local-time-mcp) | `skill` | `821afce` | MIT | Only the `skill/` folder copied; the MCP server stays upstream. |
| [`shadcn-persian`](skills/shadcn-persian) | [Abulfadl-Ahmadi/shadcn-persian](https://github.com/Abulfadl-Ahmadi/shadcn-persian) | `.` | `ac1d0c8` | MIT | Default Persian font changed from Vazirmatn to Sahel, loaded from jsDelivr, with Farsi digits from the Sahel FD build instead of `ss01`. |
| [`rtl-and-persian-localization`](skills/rtl-and-persian-localization) | [sadrmanesh/commerce-agent-skills](https://github.com/sadrmanesh/commerce-agent-skills) | `skills/rtl-and-persian-localization` | `308c909` | MIT | Unchanged. |
| [`iranian-payment-gateways`](skills/iranian-payment-gateways) | [sadrmanesh/commerce-agent-skills](https://github.com/sadrmanesh/commerce-agent-skills) | `skills/iranian-payment-gateways` | `308c909` | MIT | Unchanged. |
| [`persian-formatting`](skills/persian-formatting) | [PouyaRN/persian-formatting-skill](https://github.com/PouyaRN/persian-formatting-skill) | `.` | `a271bf3` | MIT | Default Persian font changed from Vazirmatn (Google Fonts) to Sahel (jsDelivr). |
| [`persian-formal-mmgghh`](skills/persian-formal-mmgghh) | [mmgghh/persian-writing-skills](https://github.com/mmgghh/persian-writing-skills) | `plugins/persian-writing/skills/persian-formal` | `028f0b2` | MIT | Renamed from `persian-formal` (name clash with TronIsHere/vibefarsiui). |
| [`persian-informal`](skills/persian-informal) | [mmgghh/persian-writing-skills](https://github.com/mmgghh/persian-writing-skills) | `plugins/persian-writing/skills/persian-informal` | `028f0b2` | MIT | Unchanged. |
| [`persian-unslop`](skills/persian-unslop) | [siawash1991/persian-agent-skills](https://github.com/siawash1991/persian-agent-skills) | `skills/persian-unslop` | `d287521` | MIT | Unchanged. |
| [`parsbench`](skills/parsbench) | [ParsBench/ParsBench](https://github.com/ParsBench/ParsBench) | `skills/parsbench` | `bf1ba79` | Apache-2.0 | Unchanged. |
| [`natural-farsi`](skills/natural-farsi) | [thesamehosuh/xratu](https://github.com/thesamehosuh/xratu) | `assets/skills/natural-farsi` | `c88daf5` | Apache-2.0 | Unchanged. |
| [`finglish-normalize`](skills/finglish-normalize) | [thesamehosuh/xratu](https://github.com/thesamehosuh/xratu) | `assets/skills/finglish-normalize` | `c88daf5` | Apache-2.0 | Unchanged. |
| [`rtl-design`](skills/rtl-design) | [Baghlani/rtl-design](https://github.com/Baghlani/rtl-design) | `skills/rtl-design` | `b7c5229` | Apache-2.0 | Default Persian font changed from Vazirmatn to Sahel in the font table and pairing recipes; Vazirmatn and Estedad kept as alternatives. |
| [`kumihan-fa`](skills/kumihan-fa) | [landco-llc/kumihan](https://github.com/landco-llc/kumihan) | `plugins/kumihan-fa` | `1b27c93` | Apache-2.0 | Suggested font changed from Vazirmatn to Sahel in `references/web.md` and its copies (inventory checksums updated). Prebuilt release zips in `downloads/` removed. |
| [`persian-motion-director`](skills/persian-motion-director) | [atmirrr/persian-motion-director](https://github.com/atmirrr/persian-motion-director) | `.` | `5499640` | MIT | Bundled font changed from Vazirmatn to Sahel. The pre-shaped letter outlines (`glyphs.js`, `glyphs-intro.js`) and preview GIFs were made with Vazirmatn and not regenerated. |
| [`salsi`](skills/salsi) | [pooooooriya/salsi](https://github.com/pooooooriya/salsi) | `skills/salsi` | `303ebc8` | MIT | Unchanged. |
| [`iran-mcp/*`](skills/iran-mcp) (77) | [sepehr071/iran-mcp](https://github.com/sepehr071/iran-mcp) | `plugins/*/skills/*` | `51ba858` | MIT | Only the skill folders copied; plugin manifests and servers stay upstream. |

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
| [`persian-text-editor`](skills/persian-text-editor) | Inspired by SamanQasempour/persian-skills. |
| [`persian-translation-review`](skills/persian-translation-review) | Inspired by jwiegley/claude-prompts (persian). |
| [`farhangestan-orthography`](skills/farhangestan-orthography) | Built from the Academy of Persian Language and Literature's «دستور خطّ فارسی (ویراست جدید)», 1401 ([PDF](https://apll.ir/wp-content/uploads/2023/07/Dastour-e-Khat-17.04.1402.pdf)): rules summarized in our own words with page references; the book's text and full word lists are not copied. Inspired by Byte-Magazine/skills (byte-virastari). |
| [`persian-book-translation`](skills/persian-book-translation) | Inspired by m4tinbeigi-official/hermes-literary-translation-mastery. |

## Listed but not copied

| Entry | Why |
|---|---|
| [BAHROMTJ/nutq](https://github.com/BAHROMTJ/nutq) | MCP server with no skill file |
| [masoudroot/persian-writing-mcp](https://github.com/masoudroot/persian-writing-mcp) | MCP server with no skill file |
| [openaccountants](https://github.com/openaccountants/openaccountants) af-* and tj-* | The OpenAccountants Guide License doesn't allow redistribution here |
