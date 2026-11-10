# Test prompts

Write prompts from the skill's own description, then add cases from the
categories below that fit it. Each prompt needs an expected outcome written
down before you run it.

## Contents

- How to write the set
- Prompt bank by skill type
- Running the comparison

## How to write the set

- 6 to 10 prompts in total.
- Half should clearly trigger the skill.
- Two or three sit at its edge, such as a related task in another variety or
  register.
- Two should not trigger it, such as an English-only task or a different
  Persian task.
- Mix the language of the request: Persian, English asking for Persian output,
  and Finglish where the skill claims to handle it.
- Use realistic inputs: a pasted draft, a UI string file, a paragraph to
  translate. A one-line toy prompt hides most problems.

## Prompt bank by skill type

Writing and editing:
- Paste a 150-word Persian paragraph full of AI tells and ask to make it
  natural. Expect: tells removed, facts kept, register kept.
- Ask for a formal letter to an organization. Expect: correct letter form,
  no colloquial verbs.

Translation and localization:
- Ask to translate ten UI strings with `{variables}` and an ICU plural into
  fa-IR. Expect: placeholders untouched, `one`/`other` kept, no calques.
- Ask for the same strings for Afghan users. Expect: Dari words and
  months, afghani.

Orthography:
- Paste text with «میشود»، «کتابها»، «مسأله»، «رییس»، «ترا». Expect:
  «می‌شود»، «کتاب‌ها»، «مسئله»، «رئیس»، «تو را», each with the Academy's page.

Dari and Tajik:
- Ask for a short product announcement for readers in Kabul. Expect:
  «شفاخانه»-style vocabulary where relevant, solar months حمل…حوت or
  Gregorian with Dari month names.
- Ask for the same in Tajik. Expect: Cyrillic with ғ ӣ қ ӯ ҳ ҷ, сомонӣ, no
  Russian loans where Tajik words exist.

Typography and RTL:
- Ask for an HTML page with a Persian paragraph containing an English
  product name and a URL. Expect: `dir="rtl"`, `lang="fa"`, isolated LTR runs,
  Sahel or the project's font.

Calendar and locale:
- Ask what date 1405/8/19 is in the Gregorian calendar and how to show it in
  a fa-IR UI. Expect: 10 November 2026, a CLDR-style format, Persian digits.

Should not trigger:
- An English-only coding question.
- A Persian question the skill doesn't cover (for example a writing skill
  asked for a currency conversion).

## Running the comparison

1. Run every prompt in a fresh context without the skill, and again with the
   skill loaded or installed.
2. Save both outputs side by side.
3. Run `fa_lint.py --check` on each Persian output.
4. Grade with `rubric.md`, then count the prompts where the skill made the
   output better, the same or worse.
5. Record which prompts loaded the skill.
