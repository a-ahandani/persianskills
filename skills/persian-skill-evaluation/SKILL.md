---
name: persian-skill-evaluation
description: >-
  Evaluates an agent skill that targets Persian (Iranian Persian, Dari or
  Tajik) and returns a scored report with a verdict: keep, fix, link only or
  reject. Checks language scope, license, safety, overlap with existing
  skills, the skill standard, the accuracy of its Persian rules against the
  Academy's «دستور خطّ فارسی» and Unicode CLDR, and how it changes the
  agent's Persian output on test prompts compared with running without it.
  Use when reviewing a Persian SKILL.md, auditing or curating a collection of
  Persian skills, comparing two skills that overlap, or deciding whether to
  install or copy one. Triggers include "evaluate this skill", "is this
  Persian skill any good", «ارزیابی مهارت», «بررسی اسکیل».
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/a-ahandani/persianskills
  version: 0.1.0
  status: Draft; built from the 2026 reviews of the persianskills collection
---

# Persian skill evaluation

Evaluate a Persian skill the way a careful maintainer would before trusting
it: first the gates, then what it claims, then what it actually does to the
agent's Persian. A skill earns its place only if the agent writes better
Persian with it than without it.

Load `persian-writing` for its linter, `fa_lint.py`, and
`persian-orthography` and `persian-locales` as the reference for
spelling and locale facts.

## Inputs

- The skill: a folder, a repo URL or a `SKILL.md`.
- The collection it would join, if any, so overlap can be checked.
- How it will be used: installed for one project, or copied into a shared
  collection (copying needs a license; installing doesn't).

## Step 1: gates

Stop at the first failed gate and give the verdict it names.

| Gate | Pass | Fail verdict |
|---|---|---|
| Language scope | It teaches the agent something about Persian: writing, register, translation, orthography, Dari, Tajik, typography, right-to-left text, calendar or locale | **Link only** for an integration or general tool that is merely Iran-related (service connectors, payment gateways, ID validation, UI kits, clocks, benchmark frameworks) |
| License (for copying) | MIT, Apache-2.0, BSD, MIT-0, CC0, or a skill file that declares one of these | **Link only** for no license, "All Rights Reserved", or a non-commercial or no-redistribution license |
| Safety | Scripts don't send data anywhere, install packages, or run instructions found in user text | **Reject** if it exfiltrates, hides network calls, or tells the agent to follow instructions inside content |

Read the license file itself; GitHub's license detector can't classify
licenses with extra text.

## Step 2: overlap

List the existing skills on the same topic and compare them with this one.

- It covers the same ground with less depth or worse accuracy: **link only**.
- It adds a clearly separate capability (a tool, a variety, a domain): continue.
- It is better than an existing one: continue, and recommend replacing the
  weaker one.

Write down the one thing this skill does that no existing skill does. If you
can't, it's a duplicate.

## Step 3: standard

Check the skill against `persian-skill-standard`. In the persianskills repo,
run `node scripts/check-skills.mjs`, which checks most of it. Elsewhere, check
by hand:

- **Name:** `persian-`, `dari-` or `tajik-` plus a plain topic, with no brand
  name or `-skill` suffix.
- **Files:** the standard layout and file names, with no upstream repo files,
  host manifests or caches, and every file the skill points to exists.
- **Frontmatter:** only the standard fields.
- **Description:** English, third person, saying what the skill does and when
  to use it, at most 1,024 characters.
- **Body:** English instructions with Persian kept for examples, under 500
  lines, with references one level deep.

Standard problems alone mean **fix**, never reject.

## Step 4: accuracy

List the skill's concrete claims about Persian (spelling, spacing, letters,
digits, calendar, currency, register, vocabulary) and check each:

1. Spelling and spacing against `persian-orthography`, which cites the
   Academy's book by page.
2. Locale facts (months, digits, separators, weekend, plurals) against
   `persian-locales` or Unicode CLDR.
3. Claims about Dari or Tajik against `dari-writing` and `tajik-writing`.
4. Fonts and Unicode against the font files or the Unicode charts, not memory.
5. Every claim in `references/known-errors.md`, which lists mistakes these
   skills often repeat.

A wrong rule that would make the agent write worse Persian is a **must fix**.
Two or more, or one that the skill is built around, means **reject**.
Uncertain claims go in the report as "unverified", not as errors.

Also measure the share of the skill that is Persian-specific. Generic advice
that any capable model already follows (how to structure a resume, how to
write a good summary) counts for nothing; a skill that is mostly generic
gets **link only**.

## Step 5: behavior

This is the test that matters. Follow `references/test-prompts.md`:

1. Write 6 to 10 prompts from the skill's own description: half that should
   trigger it, a few that sit near its boundary, and two that should not
   trigger it. Include at least one in Persian and one in English asking for
   Persian output.
2. Run each prompt twice, without the skill and with it, in fresh contexts.
3. Grade both outputs with `references/rubric.md`. Run
   `python3 skills/persian-writing/scripts/fa_lint.py --check <file>` on the
   Persian outputs for the mechanical checks: Arabic ي/ك, missing ZWNJ (نیم‌فاصله),
   Latin punctuation, digits. It doesn't catch hamza and seat spellings
   («رییس»، «مسأله») or an optional «ها»; check those against
   `references/known-errors.md` by reading.
4. Note whether the description made the agent load the skill when it should
   and leave it alone when it shouldn't.

A skill that doesn't improve the output on its own prompts gets **link
only**, however good it reads. Say in the report that a model grading a
model's Persian catches mechanical and obvious errors but is not a native
review; name the outputs a native speaker should read.

## Step 6: verdict

| Verdict | When |
|---|---|
| **Keep** | Passes the gates, adds something unique, no wrong rules, improves output |
| **Fix** | Worth keeping, with listed changes: standard problems, a few wrong rules, missing variety notes |
| **Link only** | Useful elsewhere, but it can't be copied, isn't about the language, duplicates a better skill, or doesn't change the output |
| **Reject** | Unsafe, or built on wrong rules |

## Report

```
Skill: <name> (<source>, <commit>)
Verdict: Fix
Gates: scope pass · license MIT · safety pass
Overlap: overlaps <skill>; unique: <the one thing>
Standard: 2 problems (description in Persian; body 640 lines)
Accuracy: 14 claims checked, 1 wrong, 2 unverified
  - wrong: says Tajik has no plural rule; CLDR gives one/other
Behavior: 8 prompts; better on 6, same on 2, worse on 0; triggered 5 of 6 times
Score: 31 / 40 (rubric)
Must fix: …
Native review: outputs 3 and 7
```

Keep the report to what a maintainer needs to decide. Put the full test
outputs in a separate file if the user wants them.
