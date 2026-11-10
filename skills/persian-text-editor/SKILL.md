---
name: persian-text-editor
description: >-
  Edit an existing Persian draft the way a careful human editor does: read
  for meaning first, then structure, sentences, word choice and mechanics,
  and return the edited text with a short list of what changed and why.
  Keeps the author's voice, facts and register. Use when the user asks to
  edit, polish, proofread, tighten or "ویرایش" a Persian text, or says a
  Persian draft reads stiff, wordy, translated or machine-written.
license: MIT
metadata:
  version: 0.1.0
  inspired-by: SamanQasempour/persian-skills (persian-writing-mastery, natural-persian-text-editor); written from scratch, no text copied
---

# Persian text editor

An editor improves the text the author wrote. They don't write a new one.
Every change has to make the text clearer, shorter or more correct while
it still sounds like the author.

Load `persian-writing` for orthography and register rules. This skill is
the editing procedure.

## Before editing

1. **Find the job.** Who reads it, where (chat, email, article, letter,
   UI) and what it must do. If that's unclear and the text is long or
   high-stakes, ask one question first.
2. **Find the register** the author chose (رسمی، نیمه‌رسمی، محاوره) and
   keep it unless it's wrong for the job. If it is, say so and ask before
   switching.
3. **Mark what must not change:** names, numbers, dates, quotes,
   technical terms, links, legal or medical claims. Never "fix" a fact.

## The four passes

Do them in this order; each pass has one question.

1. **Meaning:** does every paragraph say one thing, in an order a reader
   can follow? Move or merge paragraphs; flag gaps or contradictions as
   questions instead of inventing content.
2. **Sentences:** split long chains joined by «و» and «که»; put the verb
   where a Persian reader expects it; prefer active verbs to
   «انجام شد / صورت گرفت»; one idea per sentence.
3. **Words:** replace padding and stock phrases with plain words:

   | Padding | Plain |
   |---|---|
   | در راستای | برای |
   | به منظور | برای |
   | مورد بررسی قرار دادن | بررسی کردن |
   | لازم به ذکر است که | (delete, or say the thing) |
   | از اهمیت ویژه‌ای برخوردار است | مهم است |
   | می‌باشد | است (outside formal letters) |

   Keep loanwords readers actually use; don't swap a common word for a
   rare Persian equivalent unless the author asks.
4. **Mechanics:** ZWNJ, Persian «ی» and «ک», punctuation spacing, digits,
   «گیومه». Run `persian-writing`'s linter in report mode if available.

## What not to do

- Don't change the register, tone or point of view without asking.
- Don't add claims, examples or flourishes the author didn't write.
- Don't rewrite a sentence that is already clear just to make it yours.
- Don't "correct" dialect or colloquial forms in dialogue or quotes.

## Output

Return the edited text first, ready to paste. Then a short change list,
grouped, so the author can accept or reject:

```
ساختار: پاراگراف ۲ و ۳ ادغام شد (هر دو درباره‌ی قیمت بودند).
جمله‌ها: ۴ جمله‌ی بلند شکسته شد.
واژه‌ها: «در راستای» ← «برای» (۳ مورد).
نگارش: نیم‌فاصله در ۱۲ جا.
پرسش: در بند آخر، تاریخ عرضه ۱۴۰۵ است یا ۱۴۰۶؟
```

For a long document, edit one section, show it, and ask before doing the
rest. For a one-line fix, skip the change list.
