---
name: persian-translation-review
description: >-
  Translate into Persian in two separate roles, a translator and then an
  independent reviewer, and reconcile the two before handing over. The
  reviewer compares the Persian against the source line by line for
  meaning, omissions, calques, terminology, register and mechanics, and
  reports findings in a table the user can approve. Use for any translation
  into Persian, Dari or Tajik that matters (product UI, marketing, legal,
  documentation, books), or when the user asks to check or review an
  existing Persian translation.
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/edyt-app/persianskills
  version: 0.1.0
  inspired-by: jwiegley/claude-prompts (persian skill, translator and reviewer team); written from scratch, no text copied
---

# Persian translation review

One pass of translation catches most errors a translator can see. A
second reader who did not write the draft catches the rest: the omitted
clause, the calque that felt fine while writing, the term that drifted.

Load `persian-localization` for the meaning-over-words rules and the
calque list, and the writing skill for the target variety
(`persian-writing`, `dari-writing` or `tajik-writing`).

## Roles

Run them as separate steps. If your agent can start subagents, give the
reviewer a fresh one that sees the source and the draft but not the
translator's reasoning.

1. **Translator:** writes the Persian for the target reader. Keeps a short
   note of choices that need a decision (a term with two options, an idiom
   dropped, a sentence reordered).
2. **Reviewer:** reads the Persian alone first, as a reader would, and
   marks anything that sounds translated. Then compares line by line with
   the source.
3. **Reconcile:** the translator accepts or rejects each finding with a
   reason; open questions go to the user.

## Reviewer checklist

For each line or segment:

- **Meaning:** same claim, same strength. «ممکن است» is not «حتماً»; a
  negative stays negative.
- **Omissions and additions:** nothing dropped, nothing invented.
- **Calques:** idioms and metaphors translated word for word
  (catch, land, hit, back, away, lives in, sounds like).
- **Terminology:** one Persian term per source term, matching the
  project's glossary.
- **Register and address:** شما vs تو is consistent; formal and
  colloquial forms aren't mixed.
- **Variety:** Iranian, Dari or Tajik words and formats as the audience
  needs (months, currency, spelling).
- **Mechanics:** ZWNJ, «ی» and «ک», digits, punctuation, untouched
  placeholders and tags.

Flag problems only, not matters of taste. A finding needs a concrete
reason a native reader would stumble.

## Report

| # | Source | Current Persian | Suggested | Why |
|---|---|---|---|---|
| 1 | Welcome back | دوباره خوش آمدید | ورود به … | «خوش آمدید» greets a new arrival; sign-in pages name the action |

End with counts (accepted, rejected, open) and the open questions. Say
plainly that a model reviewing a model's translation is not a native
review; for anything public, a native speaker should read the final text.

## When the user corrects a line

Fix it, search the rest of the text for the same pattern, and add the
wrong and right forms to the project's never-use list so the next
translation starts from it.
