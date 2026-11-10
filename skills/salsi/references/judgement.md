# Worked examples

Contents: Accept; Reject; Ambiguous — decide from context; A note on quantity.

Every example below is a real finding from `salsi scan`. What matters is not the
verdict but the reason — the same reasoning applied to a finding you have not
seen before should give you the right answer.

---

## Accept

### The field already writes the Persian word

> این **سیستم** روی سه **سرور** اجرا می‌شود و **فایل‌های** پیکربندی را از
> **دیتابیس** می‌خواند.

→ **سامانه**, **کارساز**, **پرونده‌های**, **پایگاه داده**

Persian technical writing uses all four. Nothing is lost, and the sentence
becomes more readable, not less.

### The loanword adds nothing

> کاربران به **تدریج** با آن آشنا می‌شوند.

→ **کم‌کم**

`کم‌کم` is ordinary Persian that every reader knows. There is no cost.

### The suffix follows along cleanly

> **فایل‌ها** را **دانلود کنید**.

→ **پرونده‌ها** را **بارگیری کنید**.

Note the verb keeps the reader's inflection. `بارگیری کردن` dropped in
unchanged would have been wrong.

---

## Reject

### It is the term of art

> این **الگوریتم** از یک **پروتکل** رمزنگاری استفاده می‌کند.

The lexicon has entries for both. Do not use them. A reader in this field knows
these words precisely; a coined replacement makes the sentence *less* exact.

### The suggestion is a different word

> سه **سرور** در این اتاق هست.  →  سه **شادمانی** در این اتاق هست.

The lexicon keys on spelling. `سُرور` "joy" and `server` are written the same
way. The `sense` label said `سُرور به چم خوشحالی` — that was the warning.

Always read the sense label. This is the single most common way an automated
rewrite goes wrong.

### Nobody would recognise it

> رعایت **حریم** خصوصی کاربران.  →  رعایت **بژکما**ی کاربران.

Formally correct, practically unusable. A word that sends the reader to a
dictionary has failed at the one job prose has.

### It is a quotation

> فردوسی می‌گوید: «توانا بود هر که دانا بود»

Never edit inside a quotation, even to "improve" it.

### It is inside code

> مقدار `system.config.path` را عوض کنید.

`salsi` excludes inline code automatically. When editing by hand, watch for
identifiers that happen to be Persian-adjacent.

### The trade is bad

> این کار **ریسک** دارد. → این کار **خطرِ احتمالیِ زیان** دارد.

One word became three. Keep the original, or find a one-word equivalent.

---

## Ambiguous — decide from context

`استرس` has two senses in the lexicon:

| Context | Choose |
| --- | --- |
| مهندسی، مکانیک، مقاومت مصالح | `تنش` |
| روان‌شناسی، سلامت، زندگی روزمره | `دلهره` |

Pass `--topic مکانیک` or `--topic روانی` and the matching sense is ranked first.
If the context does not tell you, leave the word alone and say why.

---

## A note on quantity

Scanning a normal Persian article at `standard` level flags roughly one word in
six. Accepting all of them would produce something no one wants to read.

A good pass on a technical document changes **a handful of words**. If your diff
touches every other line, you have gone too far — go back and keep only the
changes that a reader of that document would call an improvement.
