# Rubric

Score each criterion 0, 1 or 2. The total is out of 40. The verdict comes
from SKILL.md step 6, not from the score alone: a single wrong core rule can
reject a skill that scores well elsewhere.

## Contents

- The skill (static review)
- The output (behavior test)
- Grading Persian output

## The skill (static review)

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Persian specificity | Mostly generic advice | Some Persian rules among generic ones | Nearly all content is about Persian |
| Accuracy | A wrong core rule | Minor errors or unverified claims | Every checked claim holds |
| Sources | None | Some claims sourced | Rules tied to the Academy, CLDR or named references |
| Variety awareness | Assumes Iran without saying so | Says it covers Iran only | Handles Dari or Tajik where they differ, or routes to those skills |
| Examples | Missing or wrong | Present, some mechanical errors | Correct, natural, with ZWNJ and Persian letters |
| Actionability | Vague goals | Rules without a procedure | Clear steps the agent can follow and check |
| Uniqueness | Duplicates an existing skill | Partly new | Covers something no other skill does |
| Standard | Many problems | A few | Passes the validator |
| Safety and tools | Unsafe or broken scripts | Scripts untested | Scripts tested and documented, or no scripts needed |
| Description | Wouldn't trigger reliably | Triggers, but too broad or vague | Says what and when, with real trigger words |

## The output (behavior test)

Compare the output with and without the skill for each prompt.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Script mechanics | Errors the base output didn't have | Same as without the skill | Fewer errors than without the skill |
| Orthography | Breaks the Academy's rules | Mixed | Follows them, or the house style the skill sets |
| Register | Wrong for the task | Inconsistent | Fits the task and stays consistent |
| Naturalness | Calques, AI tells, translated feel | Some | Reads as written by a native writer |
| Variety | Wrong variety for the audience | Mixed signals | Right words, calendar, currency and script |
| Meaning | Facts changed or invented | Small drift | Facts and meaning kept |
| Task fit | Ignores what was asked | Partly does it | Does what was asked, in the requested format |
| Improvement | Worse than without the skill | No difference | Clearly better |
| Triggering | Loaded when it shouldn't, or missed | Mostly right | Loaded exactly on the right prompts |
| Efficiency | Slower, longer or noisier with no gain | Similar | Same quality or better with less effort |

## Grading Persian output

Mechanical, checked by `fa_lint.py --check`:
- Persian «ی» (U+06CC) and «ک» (U+06A9); no Arabic «ي» or «ك».
- ZWNJ in «می‌»، «‌ها»، «‌تر»، «‌ترین» and the other cases the Academy requires.
- Persian punctuation «،» «؛» «؟» and «» quotes in Persian prose.
- Digits as the locale expects (Persian digits for Iran and Afghanistan in
  prose, Latin digits for Tajik and in code).

By reading:
- Calques of English idioms (catch mistakes, welcome back, one click away);
  see `persian-localization`.
- AI tells: «لازم به ذکر است»، «در راستای»، «از اهمیت ویژه‌ای برخوردار است»،
  rule-of-three lists, em dashes in Persian prose; see `persian-writing`.
- Register slips: colloquial forms in formal text or the reverse.
- Variety slips: «بیمارستان» for an Afghan reader, Perso-Arabic script for a
  Tajik reader, tomans in Afghanistan.

Model grading catches the mechanical and obvious problems. Flag the outputs a
native speaker should still read.
