---
name: persian-localization
description: >-
  Translate and localize product copy, UI strings, websites, emails and blog
  posts into Persian so it reads as if a native team wrote it, not as a
  translation from English. Picks the right variety first (Iranian Persian,
  Dari for Afghanistan, Tajik in Cyrillic for Tajikistan), then applies
  meaning-over-words rules, a list of English calques that native readers
  reject, and safe handling of placeholders, ICU plurals, bidi and digits in
  i18n files. Use whenever you translate English into Persian, Farsi, Dari or
  Tajik, review a Persian translation, write fa/fa-IR/fa-AF/prs/tg locale
  files, or a native speaker says a Persian string "sounds translated",
  "is literal" or "doesn't make sense".
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/edyt-app/persianskills
  version: 0.1.0
  based-on: Lessons from shipping edyt.app in Persian, reviewed by a native Persian speaker
---

# Persian localization

One rule serves all the others: **translate what the English means, not the
words it uses.** A reader should not be able to tell the text was written in
English first.

Load alongside:
- `persian-writing` for Persian prose, orthography, register and documents.
- `dari-writing` when the audience is in Afghanistan or is Afghan.
- `tajik-writing` when the audience reads Tajik in Cyrillic.

## Step 1: pick the variety

Ask, or read it from the project (locale code, country, market):

| Audience | Write | Locale codes | Script |
|---|---|---|---|
| Iran, most of the Iranian diaspora | Iranian Persian (Farsi) | `fa`, `fa-IR` | Perso-Arabic, RTL |
| Iranian communities in the Gulf (Bahrain, UAE, Kuwait) | Iranian Persian, with local currency and dates | `fa` | Perso-Arabic, RTL |
| Afghanistan, Afghan diaspora, Hazara communities | Dari | `fa-AF`, `prs` | Perso-Arabic, RTL |
| Persian speakers in Pakistan (Afghan and Hazara communities) | Dari, with Pakistani formats | `fa-AF` | Perso-Arabic, RTL |
| Tajikistan, Tajik speakers in Uzbekistan and Russia | Tajik | `tg`, `tg-Cyrl` | Cyrillic, LTR |

"Persian" or "Farsi" with no country means Iranian Persian. Never ship one
variety to another's audience: tomans, Iranian month names and Iranian
slang are wrong for Afghan readers, and Perso-Arabic script is unreadable for
most Tajik readers.

## Step 2: know the job of the string

Before writing, find where the string renders: heading, button, error, hint,
email subject. Write what a native product team would put in that slot. If
the English uses an idiom that Persian does not have, drop the idiom and name
the action plainly.

Then reread the Persian **without the English beside it**. If a native
speaker would stop and think "this came from English", rewrite it.

## Calques native readers reject

The first three were corrected by a native reviewer on a live product; the
rest follow the same pattern and were flagged in the same review across
languages. The pattern matters more than the list: English verbs used as
metaphors rarely survive.

| English | Literal (wrong) | Why it fails | Natural |
|---|---|---|---|
| Welcome back (sign-in heading) | «دوباره خوش آمدید» | «خوش آمدید» greets a guest who just arrived; adding «دوباره» does not make it "nice to see you again". Persian sign-in pages name the action | «ورود به …» (the product name) |
| catch mistakes | «اشتباه‌ها را می‌گیرد» | Mistakes are not "caught" in Persian, they are found | «اشتباه‌ها را پیدا می‌کند» |
| pricing plan | «طرح رایگان»، «طرح سالانه» | «طرح» reads as "design" or "project" | «اشتراک رایگان»، «اشتراک سالانه» |
| one click away | «یک کلیک فاصله» | Distance metaphor does not exist | «با یک کلیک» |
| lives in (software) | «در … زندگی می‌کند» | Software does not live | «در … کار می‌کند» or «در … هست» |
| sounds like you | «شبیه صدای شما» | Writing has no sound in Persian | «به لحن خودتان» |

Words that carry the same risk: catch, land, hit (send), grab, jump in, back,
ship, look, sounds like, away, lives. Reread every verb that came from one.

Some idioms do exist natively and are fine. Check the phrase in Persian, not
the English phrase.

## Product copy rules

- **Glossary first.** One Persian word per product term, used everywhere.
  Read the project's existing locale file before translating and reuse its
  words. If a term is new or the file is inconsistent, ask and record the
  decision.
- **Product and brand names stay Latin** inside Persian sentences. Keys and
  shortcuts come from placeholders, never typed out.
- **Same copy rules as the English:** no em dashes, no filler, no invented
  social proof. Translate only what was asked; do not reword nearby strings
  in passing.
- **Letters:** Persian «ی» (U+06CC) and «ک» (U+06A9), never Arabic «ي» and
  «ك». A real zero-width non-joiner (U+200C) in «می‌شود»، «پیام‌ها»،
  «نوشته‌تان», never a space and never nothing. After a joining letter the
  pronoun attaches directly: «حسابتان»، «اشتراکتان».
- **Ezafe after «ه»:** pick one form for the whole project and keep it.
  «صفحه‌ی» (ZWNJ + «ی») is safest in UI because every font renders it;
  «صفحهٔ» (U+0654) is the academic form. Never mix them.
- **Digits:** Persian digits (۰–۹) in prose for Iranian and Afghan readers,
  unless the project has decided otherwise. Keep Latin digits inside codes,
  URLs, versions and prices written next to a currency symbol that is Latin.
- **Quotes:** «گیومه», not "straight quotes".

## i18n files: what never to touch

- Keep `{variables}`, ICU `plural`/`select` blocks, `<tags>` and keys exactly
  as in the source. Persian, Dari (`fa-AF`) and Tajik all use the CLDR
  plural categories `one` and `other`.
- Never run an automatic cleanup that rewrites quotes, digits or punctuation
  (for example `persian_cleanup.py --edit`) on JSON, YAML, PO or frontmatter.
  It changes characters inside placeholders. Run lint in report mode only.
- A missing key often falls back to English silently. Never drop a key on
  purpose.

## Bidi: Latin words inside Persian

Inside a page that sets `dir="rtl"`, a Latin product name in a sentence is
fine. Where the direction is guessed from the first letter (chat apps, push
notifications, meta titles and descriptions, social cards, plain-text email
subjects), a line that opens with a Latin word displays backwards. Start
those lines with a Persian word: «دانلود Edyt» not «Edyt دانلود».

## Reviewing an existing translation

1. One language and one section at a time, next to the source.
2. Flag only: literal translations and calques, two words for one product
   term, wrong tone or formality, changed or missing meaning, broken
   placeholders. Not matters of taste.
3. Report so a native reviewer can approve line by line:

   | Key or file:line | Current | Suggested | Why |
   |---|---|---|---|

4. Change nothing until a native speaker approves. A model reviewing a
   model's translation catches literal phrasing but is not a native review;
   say so in the handoff.

## When a native speaker corrects you

1. Fix the string, then search the same locale for the same phrase or idiom
   and fix those too.
2. Check whether the same English idiom was translated literally elsewhere.
3. Add the wrong and right versions to the project's never-use list so the
   correction outlives the conversation.
