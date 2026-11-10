---
name: tajik-writing
description: >-
  Write, translate and localize Tajik (тоҷикӣ), the Persian of Tajikistan,
  in Cyrillic, for readers in Tajikistan, Tajik speakers in Uzbekistan
  (Samarkand, Bukhara) and Tajik migrants in Russia. Covers the 35-letter
  alphabet and the six letters that get lost on Russian keyboards
  (ғ ӣ қ ӯ ҳ ҷ), Tajik words instead of Russian loans, Tajik grammar that
  differs from Iranian Persian, tg locale formats (сомонӣ, dates, decimal
  comma), and converting between Cyrillic and Perso-Arabic script. Use
  whenever the audience is in Tajikistan, the locale is tg or tg-Cyrl, or
  the text is Tajik, Тоҷикӣ, Душанбе or Tajik Cyrillic, even if the user only
  says "Persian".
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/edyt-app/persianskills
  version: 0.1.0
  status: AI drafted and source checked; needs native Tajik review
---

# Tajik writing

Tajik is Persian written in Cyrillic, with its own standard, its own
spelling rules and a century of Russian contact. Most Tajik readers do not
read Perso-Arabic script, so a text in Iranian Persian does not reach them
at all.

Not for Afghan Tajiks: Tajiks in Afghanistan write Dari in Perso-Arabic
script. Use `dari-writing` for them.

**Status:** drafted from the sources at the end and checked against Unicode
CLDR data. It has not had a native Tajik review yet.

Related tools:
- `tajik-proofreading` (by firdavsi-tech): Tajik proofreading, OCR and
  document restoration with scripts and tests. Use it for proofreading and
  scanned texts.
- `BAHROMTJ/nutq` (not in this repo): MCP server for Cyrillic↔Perso-Arabic conversion,
  number-to-words and text cleanup.

## Alphabet

35 letters (CLDR `tg` exemplar set):

а б в г ғ д е ё ж з и ӣ й к қ л м н о п р с т у ӯ ф х ҳ ч ҷ ш ъ э ю я

ц щ ы ь are not Tajik letters; they appear only in unadapted Russian names.

The six letters Russian keyboards do not have:

| Letter | Code point | Typed wrongly as | Sound |
|---|---|---|---|
| Ғ ғ | U+0492 U+0493 | г | gh (غ) |
| Ӣ ӣ | U+04E2 U+04E3 | и, й | stressed final ī |
| Қ қ | U+049A U+049B | к | q (ق) |
| Ӯ ӯ | U+04EE U+04EF | у, Uzbek ў (U+045E) | ō |
| Ҳ ҳ | U+04B2 U+04B3 | х | h (ه، ح) |
| Ҷ ҷ | U+04B6 U+04B7 | ч | j (ج) |

- Use exactly these code points. Look-alikes from other alphabets (Uzbek
  ў, Bashkir ҡ, Latin letters) break search and spell checkers.
- **Restoring lost letters needs a dictionary, not a replace-all.** Both
  letters of each pair are real: хона (house) vs ҳам (also), кор (work) vs
  қалам (pen). Fix word by word, or with a tool that checks a lexicon.

## Grammar that differs from Iranian Persian

- **The ezafe is written:** китоби нав, забони тоҷикӣ, Ҷумҳурии Тоҷикистон.
  Follow the orthography rules for words ending in a vowel.
- **Verb prefixes are joined:** мехонам, намехонам. No space, no hyphen.
- **Progressive uses «истодан»:** хонда истодаам (I am reading). The Iranian
  «дорам мехонам» pattern reads as foreign.
- **Plural:** -ҳо (китобҳо), -он for people (одамон). No plural after a
  number: се китоб.
- **Definite object:** -ро (китобро).
- **Address:** Шумо for the reader in product and public text; it is
  commonly capitalized when addressing one person in letters. Ту is
  informal.

## Words: Tajik first, Russian second

The State Language Law and the Committee on Language and Terminology push
Tajik terms over Russian loans. Prefer the Tajik word when it is in use:

| Meaning | Tajik | Russian loan to avoid in formal text |
|---|---|---|
| airport | фурудгоҳ | аэропорт |
| plane | ҳавопаймо | самолёт |
| station, stop | истгоҳ | станция |
| information | иттилоот | информация |
| website | сомона | сайт |
| program, app | барнома | программа |
| university / student | донишгоҳ / донишҷӯ | университет / студент |
| province / district | вилоят / ноҳия | область / район |
| hospital | беморхона | больница |
| school | мактаб | школа |
| thank you | ташаккур, раҳмат | спасибо |

Common international loans stay (телефон, интернет, компютер), spelled the
Tajik way: no ь, ы, ц or щ. So компютер, not компьютер.

**Do not calque Russian.** Tajik is subject-object-verb with the verb last.
Do not copy Russian word order or translate Russian prepositions one by one.

**Do not pour in Iranian vocabulary.** Words that are everyday in Tehran can
be bookish or unknown in Dushanbe. When an Iranian word and a Tajik word
differ, use the Tajik one.

## Locale formats (CLDR `tg`)

| | Tajik |
|---|---|
| Locale code | `tg` (also `tg-Cyrl`, `tg-TJ`) |
| Currency | сомонӣ (TJS), CLDR symbol «сом.»; 1 сомонӣ = 100 дирам |
| Numbers | decimal comma, non-breaking space for thousands: 1 250,50 |
| Dates | short dd/MM/yy; long `dd MMMM y` (10 ноябр 2026); in prose often «10 ноябри соли 2026» |
| Months | январ, феврал, март, апрел, май, июн, июл, август, сентябр, октябр, ноябр, декабр |
| Weekdays | Душанбе, Сешанбе, Чоршанбе, Панҷшанбе, Ҷумъа, Шанбе, Якшанбе |
| Week | starts Monday; weekend Saturday and Sunday |
| Calendar | Gregorian. Persian month names (фарвардин … исфанд) only in cultural contexts such as Наврӯз |
| Quotes | «…» in print |
| Plurals (ICU) | `one`, `other` |

## Converting between Cyrillic and Perso-Arabic

There is no official one-to-one mapping, and the conversion loses
information in both directions.

- **Perso-Arabic to Cyrillic:** vowels must be supplied, and Tajik
  pronunciation decides them (Tajik о is Persian آ/ā, ӯ is classical ō).
- **Cyrillic to Perso-Arabic:** several Arabic letters collapse into one
  Cyrillic letter: ث س ص → с; ذ ز ض ظ → з; ت ط → т; ح ه → ҳ; ع → ъ or
  nothing. Going back needs a dictionary to choose the right letter.
- Use a tested converter (for example `nutq`) and have a person check names,
  quotations and legal text. Never convert poetry or a person's name blindly.

## Names

Many Tajik surnames now use Tajik endings (-зода, -ӣ, -ён) instead of the
Russian -ов, -ев. Write each person's name exactly as their documents show.
Place names use Tajik forms: Душанбе, Хуҷанд, Бохтар, Хоруғ.

## Audiences outside Tajikistan

- **Uzbekistan:** Tajik speakers in Samarkand, Bukhara and Surkhandarya
  read Tajik Cyrillic; Uzbek is the state language and is written in Latin
  script (Cyrillic is still common). Currency is the Uzbek sum (UZS).
- **Russia:** Tajik migrants read Russian too. Bilingual Tajik/Russian copy
  is common; keep each language in its own grammar.
- **Pamir languages** (Shughni, Wakhi and others) in Gorno-Badakhshan are
  separate Iranian languages, not Tajik dialects.

## Checklist before handing over

1. Every ғ ӣ қ ӯ ҳ ҷ is the real Tajik letter; no ь, ы, ц, щ outside
   Russian names.
2. Tajik terms over Russian loans; no Russian word order.
3. No Iranian-only words or Perso-Arabic spellings.
4. Formats: сомонӣ, decimal comma, Tajik month names.
5. Say in the handoff that a native Tajik speaker has not reviewed the text,
   unless one has.

## Sources

- Unicode CLDR, `common/main/tg.xml` (alphabet, months, weekdays, number
  and currency formats) and `supplemental/supplementalData.xml` (calendar
  preference): https://github.com/unicode-org/cldr
- Committee on Language and Terminology under the Government of
  Tajikistan: https://kumitaizabon.tj. The current orthography rules
  (Қоидаҳои имлои забони тоҷикӣ) were approved by government decree on
  4 October 2011, No. 458: https://kumitaizabon.tj/en/printpdf/113
- Tajik alphabet and keyboard: https://en.wikipedia.org/wiki/Tajik_alphabet,
  https://kbdlayout.info/kbdtajik
- ALA-LC romanization for non-Slavic Cyrillic, including Tajik:
  https://www.loc.gov/catdir/cpso/romanization/nonslav.pdf
- Research on Tajik–Persian transliteration: https://aclanthology.org/2024.lrec-main.1459,
  https://aclanthology.org/L12-1601
