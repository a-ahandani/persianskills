---
name: dari-writing
description: >-
  Write, translate and localize Dari (Afghan Persian) for readers in
  Afghanistan, Afghan communities in Pakistan and Iran, Hazara communities
  and the Afghan diaspora. Covers the fa-AF locale (afghani, solar Hijri
  months حمل to حوت, Thursday and Friday weekend), Afghan vocabulary that
  differs from Iranian Persian (شفاخانه، پوهنتون، ولایت، موتر), Afghan
  formal register, Pashto letters inside Dari text, Hazaragi, and Persian
  typed on Urdu keyboards in Pakistan. Use whenever the audience is Afghan,
  the locale is fa-AF or prs, or the text mentions Afghanistan, Kabul,
  Herat, Mazar, Dari, دری, افغانستان or Hazaragi, even if the user only
  says "Persian".
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/a-ahandani/persianskills
  version: 0.1.0
  status: AI drafted and source checked; needs native Dari review
---

# Dari writing

Dari is the Persian of Afghanistan. Iranian readers understand it and Afghan
readers understand Iranian Persian, but each notices the other at once:
Iranian words, tomans and Iranian month names make a text read as foreign or
as written for someone else.

**Load with `persian-writing`** for orthography, ZWNJ, punctuation and RTL
documents. Where the two disagree, this skill wins for Afghan readers. Load
`persian-localization` for product and UI copy.

**Status:** drafted from the sources at the end and checked against Unicode
CLDR data. It has not had a native Dari review yet. Treat vocabulary marked
"check" as a prompt to ask, not a rule.

## Locale facts (CLDR `fa_AF`)

| | Afghanistan | Iran, for contrast |
|---|---|---|
| Locale code | `fa-AF` (CLDR maps `prs` to `fa_AF`) | `fa-IR` |
| Currency | افغانی, sign `؋`, code AFN | تومان in speech, ریال officially |
| Week | starts Saturday; weekend Thursday and Friday | starts Saturday; weekend Friday |
| Solar year months | حمل، ثور، جوزا، سرطان، اسد، سنبله، میزان، عقرب، قوس، جدی، دلو، حوت | فروردین … اسفند |
| Gregorian months | جنوری، فبروری، مارچ، اپریل، می، جون، جولای، اگست، سپتمبر، اکتوبر، نومبر، دسمبر | ژانویه، فوریه، مارس … |
| Spelling of names | دالر امریکا، تاجکستان | دلار آمریکا، تاجیکستان |
| Plurals (ICU) | `one`, `other` | same |

**Calendar choice:** daily life, media and most private use follow the solar
Hijri year with the month names above. Since 2021 the current authorities
date administrative letters in the lunar Hijri calendar. For anything
official, ask which calendar the client uses; for consumer copy use the solar
year or Gregorian dates with Dari month names.

## Vocabulary: Iran vs Afghanistan

Use the Afghan word for Afghan readers. Several of these (for example
«دانشگاه» vs «پوهنتون») have been public disputes in Afghanistan, so the
choice is noticed.

| Meaning | Iran | Afghanistan |
|---|---|---|
| hospital | بیمارستان | شفاخانه |
| university | دانشگاه | پوهنتون |
| faculty | دانشکده | پوهنځی |
| university student | دانشجو | محصل |
| school / class | مدرسه / کلاس | مکتب / صنف |
| school pupil | دانش‌آموز | شاگرد، متعلم |
| province / governor | استان / استاندار | ولایت / والی |
| district | شهرستان | ولسوالی |
| municipality / mayor | شهرداری / شهردار | شاروالی / شاروال |
| army / police | ارتش / پلیس | اردو / پولیس |
| car / bus / ticket | ماشین، خودرو / اتوبوس / بلیت | موتر / بس / تکت |
| doctor / nurse | دکتر، پزشک / پرستار | داکتر / نرس |
| tomato / potato | گوجه‌فرنگی / سیب‌زمینی | بادنجان رومی / کچالو |
| computer / internet | رایانه، کامپیوتر / اینترنت | کمپیوتر / انترنت |
| thank you | ممنون، مرسی، متشکرم | تشکر |
| beautiful | قشنگ، زیبا | مقبول (check for formal text) |

Two habits mark a text as Iranian even when the words are fine:
- the progressive with «داشتن» («دارم می‌نویسم»): write «می‌نویسم» or
  «در حال نوشتن هستم»;
- Tehran slang and colloquial spellings («میخوام»، «چیکار»، «باحال»).

## Register

- **Official and administrative Dari** keeps forms that Iranian style
  guides, and `persian-writing`'s AI-tell list, call stiff: «نمودن» for
  «کردن», «می‌باشد», Arabic loans and honorifics («محترم»، «جناب»،
  «مهربانی نموده…»). In letters, notices and government-facing text they are
  the expected register. Do not strip them.
- **Product, marketing and social copy** stays plain, as in any Persian:
  short sentences, «شما» for the reader, no administrative padding.
- Letters and formal emails usually open with a greeting such as
  «السلام علیکم» or «با عرض سلام و احترام».
- Spoken Kabuli forms («استم» for «هستم», «کده» for «کرده») belong in
  dialogue and informal posts only.

## Script and letters

- Same base rules as Iranian Persian: «ی» U+06CC and «ک» U+06A9, real ZWNJ
  (U+200C). Afghan print is less consistent with ZWNJ («میشود» is common);
  write it with ZWNJ anyway. It is correct Unicode and reads well to both.
- **Pashto letters appear inside Dari** in names, places and official terms:
  ټ ځ څ ډ ړ ږ ښ ګ ڼ ۍ ې (CLDR lists them for `fa_AF`). Keep them exactly.
  Never "correct" «پوهنځی» to «پوهنحی».
- **Do not normalize Pashto.** In Pashto, ي، ې، ۍ and ی are different
  letters. A blanket ي→ی replacement corrupts Pashto words and names. Run
  normalization on Dari prose only.
- Pashto is a separate language, not a dialect of Dari. Bilingual
  Dari/Pashto material needs a Pashto writer for the Pashto half.

## Hazaragi

Hazaragi is the spoken Persian of the Hazara people: central Afghanistan
(Hazarajat, Bamyan, Daikundi), large communities in Quetta, Pakistan, and in
Iran, and a wide diaspora. It is mostly spoken; written Hazaragi appears in
social posts, songs and some literature.

- For written products, use standard Dari unless the brief asks for Hazaragi.
- If it does, work only with a native Hazaragi reviewer. Do not invent
  dialect words or spellings, and never imitate the dialect for humour.
- Avoid ethnic stereotypes and assumptions about religion or politics; in
  mixed audiences, refer to people by the name they use for themselves.

## Persian speakers in Pakistan

Persian readers in Pakistan are mostly Afghan refugees and migrants (Dari)
and the Hazara community of Quetta (Hazaragi, standard Dari in writing).
Urdu and English are their everyday written languages.

- Locale around the text: Pakistani rupee (Rs, PKR), Gregorian dates,
  Pakistani phone and address formats.
- **Urdu keyboards type the wrong letters for Persian.** Urdu «ہ» (U+06C1)
  and «ۂ» look like Persian «ه» (U+0647) but break search and fonts; Urdu
  «ے» (U+06D2) and «ں»، «ٹ»، «ڈ»، «ڑ»، «ھ» do not belong in Persian at all.
  Convert «ہ» to «ه» and remove the rest by rewriting the word.
- Urdu shares many Persian words with different meanings or spellings.
  Do not read Urdu usage into Dari text.

## Politics and naming

Afghanistan's government, flag and national terms are contested. In neutral
copy, name the country «افغانستان» and avoid naming the government. For
anything that must name it, follow the client's wording. The words for the
people («افغان»، «افغانستانی») are also debated; use the client's choice and
keep it consistent.

## Checklist before handing over

1. Currency is afghani (؋) and dates use Afghan month names or the
   calendar the client chose.
2. No Iranian-only words from the table, no «داشتن» progressive, no Tehran
   slang.
3. Register fits the job: administrative forms kept in official text, plain
   language in product copy.
4. Pashto letters and words left untouched; no Urdu letters.
5. Say in the handoff that a native Dari speaker has not reviewed the text,
   unless one has.

## Sources

- Unicode CLDR, `common/main/fa_AF.xml` (months, currency, spellings,
  auxiliary letters) and `supplemental/supplementalData.xml` (week data,
  calendar preference): https://github.com/unicode-org/cldr
- Academy of Sciences of Afghanistan, the national language authority:
  https://asa.gov.af
- Workshop on standardizing Pashto and Dari orthography, Kabul, 2026:
  https://www.ariananews.af/five-day-workshop-launched-in-kabul-to-standardize-pashto-and-dari-orthography/
- Review of Newid and Thurmair's comparative Farsi/Dari vocabulary:
  https://journals.openedition.org/abstractairanica/57034
- IAM Language and Culture Program, "They don't use that word here":
  https://www.iam-afghanistan.org/lcp/2015/07/04/they-dont-use-that-word-here-a-personal-view/
- Dari and Hazaragi overviews: https://en.wikipedia.org/wiki/Dari,
  https://en.wikipedia.org/wiki/Hazaragi
- Reporting on the lunar calendar in administration (8am.media):
  https://8am.media/eng/taliban-changes-solar-year-to-hijri-lunar-calendar/
