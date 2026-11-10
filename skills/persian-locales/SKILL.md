---
name: persian-locales
description: >-
  Reference data for the three Persian locales: fa-IR (Iran), fa-AF / prs
  (Dari, Afghanistan) and tg (Tajik, Tajikistan). Locale codes, script and
  direction, digits and separators, currency, calendars and month names,
  weekdays, week start and weekend, date patterns and ICU plural rules, all
  from Unicode CLDR. Use when setting up i18n for a Persian locale,
  formatting numbers, dates or money for Persian readers, writing ICU
  messages, or checking that a locale file uses the right conventions.
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/a-ahandani/persianskills
  version: 0.1.0
  based-on: Unicode CLDR (common/main/fa.xml, fa_AF.xml, tg.xml; supplemental data), checked 2026-11-10
  inspired-by: skills-on-ai/skills-on-ai locale cards (locale-fa-ir, locale-prs-af, locale-tg-001); written from CLDR, no text copied
---

# Persian locales

Use the platform's own locale data (`Intl`, ICU, CLDR-based libraries)
whenever it exists. This sheet is for checking what that data should
produce and for the decisions it leaves to you.

For writing in each variety, load `persian-writing` (Iran), `dari-writing`
(Afghanistan) or `tajik-writing` (Tajikistan).

## At a glance

| | fa-IR | fa-AF (Dari) | tg (Tajik) |
|---|---|---|---|
| Other codes | `fa`, `pes` | `prs` (CLDR maps it to `fa_AF`) | `tg-Cyrl`, `tg-TJ`, `tgk` |
| Script, direction | Perso-Arabic, RTL | Perso-Arabic, RTL | Cyrillic, LTR |
| Default digits | Persian ۰۱۲۳۴۵۶۷۸۹ (`arabext`) | Persian ۰–۹ | Latin 0–9 |
| Decimal, group | `٫` U+066B, `٬` U+066C | same as fa | `,` and no-break space |
| Currency | ریال (IRR); tomans in everyday prices | افغانی `؋` (AFN) | сомонӣ, `сом.` (TJS) |
| Main calendar | Solar Hijri (`persian`) | Solar Hijri; lunar Hijri in government letters since 2021 | Gregorian |
| Week starts | Saturday | Saturday | Monday |
| Weekend | Friday | Thursday and Friday | Saturday and Sunday |
| Plurals (ICU) | `one` (0 and 1), `other` | same | same |

## Iran (fa-IR)

- **Solar months:** فروردین، اردیبهشت، خرداد، تیر، مرداد، شهریور، مهر، آبان،
  آذر، دی، بهمن، اسفند.
- **Gregorian months:** ژانویه، فوریه، مارس، آوریل، مه، ژوئن، ژوئیه، اوت،
  سپتامبر، اکتبر، نوامبر، دسامبر.
- **Lunar months:** محرم، صفر، ربیع‌الاول، ربیع‌الثانی، جمادی‌الاول،
  جمادی‌الثانی، رجب، شعبان، رمضان، شوال، ذیقعده، ذیحجه.
- **Weekdays:** شنبه، یکشنبه، دوشنبه، سه‌شنبه، چهارشنبه، پنجشنبه، جمعه.
- **Date patterns (Solar Hijri):** short `y/M/d` (۱۴۰۵/۸/۱۹), long
  `d MMMM y` (۱۹ آبان ۱۴۰۵), full `y MMMM d, EEEE`.
- **Money:** CLDR's symbol is ریال. Prices people read are usually in
  tomans (۱ تومان = ۱۰ ریال). Pick one per product, say which, and never mix
  them on one screen.
- **Minus sign:** CLDR puts a left-to-right mark before `−` so the sign
  stays on the correct side; keep it when you format negatives by hand.

## Afghanistan (fa-AF)

- **Solar months:** حمل، ثور، جوزا، سرطان، اسد، سنبله، میزان، عقرب، قوس،
  جدی، دلو، حوت.
- **Gregorian months:** جنوری، فبروری، مارچ، اپریل، می، جون، جولای، اگست،
  سپتمبر، اکتوبر، نومبر، دسمبر.
- **Spellings that differ from Iran:** دالر امریکا (not دلار آمریکا),
  تاجکستان (not تاجیکستان).
- **Currency:** afghani, sign `؋`, code AFN.
- **Calendar choice:** ask for official text; consumer copy uses the solar
  year or Gregorian dates with the Dari month names above.

## Tajikistan (tg)

- **Months:** январ, феврал, март, апрел, май, июн, июл, август, сентябр,
  октябр, ноябр, декабр.
- **Weekdays:** Душанбе, Сешанбе, Чоршанбе, Панҷшанбе, Ҷумъа, Шанбе,
  Якшанбе.
- **Date patterns:** short `dd/MM/yy`, long `dd MMMM y`, full
  `EEEE, dd MMMM y`.
- **Persian solar month names** exist in Tajik (фарвардин … исфанд) for
  cultural dates such as Наврӯз; everyday dates are Gregorian.
- **Letters:** the alphabet needs ғ ӣ қ ӯ ҳ ҷ; see `tajik-writing`.

## Plural messages

All three locales use the same CLDR rule: `one` for 0 and 1, `other` for
everything else. Persian nouns stay singular after a number anyway
(«۳ فایل», «3 файл»), so both branches often read the same:

```
{count, plural, one {# فایل} other {# فایل}}
```

Keep both branches; translation tools and linters expect them.

## Checks before shipping

1. `dir="rtl"` and `lang="fa"` or `lang="fa-AF"` on Persian pages;
   `lang="tg"` and LTR for Tajik.
2. Numbers go through the locale formatter. Don't swap digits by hand
   inside codes, URLs, phone numbers or version strings.
3. The calendar and currency match the audience (tomans or rials in Iran,
   afghani in Afghanistan, somoni in Tajikistan).
4. Month and weekday names come from the right locale. Iranian month names
   in an Afghan product are the most common mistake.

## Sources

- Unicode CLDR, https://github.com/unicode-org/cldr: `common/main/fa.xml`,
  `fa_AF.xml`, `tg.xml`, `supplemental/plurals.xml`,
  `supplemental/supplementalData.xml`.
