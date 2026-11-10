---
name: telegram-persian-enforcer
description: >-
  Makes every text sent in Telegram fluent, correctly spelled, fully native
  Persian: chat replies in groups, channels and direct messages, automated
  output, reports, summaries, error messages and task results. Goes beyond a
  mental guideline with a required script, scripts/check_persian.py, that
  checks each draft for leftover Latin words and digits before sending and
  must actually be run with a code tool, not imagined. Use every time a reply
  is being prepared for Telegram, even if the user's message is in another
  language such as English or Finglish, even if the whole conversation so far
  was in another language, and even if the user did not ask for Persian:
  knowing that the reply is for Telegram is enough. Also applies to short
  messages, notifications, error messages and inline buttons, not only long
  replies. Triggers include «تلگرام», «کانال تلگرام», «گروه تلگرام» and
  «ربات تلگرام».
license: MIT
compatibility: The checker needs Python 3 and a code-execution tool; without one, the skill falls back to a manual review.
metadata:
  author: Ehsan Ghaffar (ehsanghaffar)
  source: https://github.com/ehsanghaffar/skills
  upstream-commit: bac8138
  version: "1.1.1"
  changes: Instructions, headings, description, script messages and comments translated from Persian into English with every Persian example kept as written, and version moved into metadata.
---

# Persian-only output for Telegram (advanced)

The goal of this skill is not just "Persian words". The goal is a message that reads as if a native Persian speaker wrote it from the start, for a Telegram audience, and not an English text translated word for word. This matters because the Telegram user should read the message as natural, readable and correct; a word-for-word machine translation (calque) stands out and lowers trust, even when its vocabulary is "Persian".

## When to use

Use this skill when replying in Telegram groups, channels or direct messages. This includes:

- chat replies (short or long)
- automated output and notifications
- reports and summaries
- task results and success or error messages
- inline keyboard button text and media captions

## Core rule

**All text addressed directly to the Telegram user must be fluent, natural Persian**, whatever the input language, the earlier language of the conversation, or the language of the sources the content came from. If the input is in another language, you may briefly acknowledge it if needed, but the final reply is Persian only, unless the user explicitly asks for another language; in that case do exactly what they asked and set this skill aside for that message.

## Advanced level: details that separate "natural" Persian from "translated" Persian

### 1. Numbers and digits

The default is Persian digits (۰۱۲۳۴۵۶۷۸۹) in fluent Persian text, not Latin digits and not Arabic digits (٠١٢...). This rule applies only to numbers that are part of Persian prose (counts, percentages, Jalali dates, amounts). Numbers inside code, IDs, version numbers (v2.4.1), links and code blocks stay untouched, because changing them breaks the content.

### 2. ZWNJ (نیم‌فاصله) and orthography

Use ZWNJ in the right places: «می‌خواهم» not «میخواهم» or «می خواهم», «کتاب‌ها» not «کتابها». This typographic detail shows the difference between professional text and hasty text.

### 3. Tone and register

Match the tone to the conversation:

- In a private chat or an informal group, natural colloquial Persian (not extreme broken spelling) fits better than formal, bookish Persian.
- In channels or formal reports, use a more formal register with no slang.
- If you are not sure, look at the tone of earlier messages from the same user or group and mirror it.

### 4. Multilingual input (quotes, sources, search output)

When the content you summarize or report is in another language (an English article or a web search result, for example), rewrite or summarize it fully in Persian; do not leave English sentences inside the Persian reply. If an exact foreign phrase is needed for accuracy (an official quote or the exact name of a law, for example), keep it short and give its Persian equivalent or an explanation right after it.

### 5. Technical terms, proper nouns and brands

- Code, terminal commands, file names, identifiers, URLs and programming variables stay untouched in their original language; the explanation around them is Persian.
- For common technical terms with no established Persian equivalent (API, «سرور», «دیتابیس»), write the word in Persian transliteration («سرور» not «Server»), except in code blocks.
- For names of foreign people, companies or products whose Latin spelling the Telegram user may not know, the first time you may give both the Persian transliteration and the original name in parentheses: «اوپن‌ای‌آی (OpenAI)».

### 6. Telegram formatting

Telegram supports limited Markdown (bold with `*متن*`, code with backticks, links). Because Persian is right-to-left, make sure formatting marks and links sit in the right place and do not scramble the text direction; for example, place an English parenthesis or link in the middle of a Persian sentence so that it does not render jumbled.

### 7. Finglish (Persian in Latin letters)

If the user writes in Finglish («salam khoobi?»), that is not another language; it is Persian typed in the Latin alphabet. The reply must still be in Persian script («سلام، خوبی؟»), not Latin or English just because the input had Latin letters.

### 8. Forwarded messages and quotes from others

When you quote text in another language from another user or from a forwarded message, summarize or translate it in your own reply; do not leave the foreign sentence as part of your reply (unless the exact quoted text is itself the topic, in which case you may quote it directly and give the Persian right after it).

## Final review before sending (self-check)

Before sending any message, review it once and check:

- Is any English or other-language sentence left in the text (other than code, URLs or IDs)?
- Are the prose numbers Persian (not Latin), and are numbers inside code or IDs untouched?
- Does the sentence structure smell of word-for-word translation? If yes, rewrite it the way a native Persian speaker would write it.
- Are the ZWNJs right?
- Does the tone match the conversation (formal or colloquial)?

This visual review is good but not enough: the eye easily skips a leftover English word, especially in long texts. That is why the next step is **not optional**.

## Automatic, required check (hard gate)

If a command tool (bash or code execution) is available, running `scripts/check_persian.py` on every message to be sent in Telegram is required: not only for long messages or reports but for every message, even one-liners. Actually run it; do not just imagine that it is "probably clean".

**Draft loop:**

1. Write the Persian draft to a file (or pass it on stdin).
2. Run:
   ```bash
   python scripts/check_persian.py --file draft.txt
   ```
3. Read the output:
   - If the last line is `RESULT: CLEAN` (exit code 0), the message is ready to send.
   - If it is `RESULT: ISSUES=N` (exit code 1), **do not send** the message. Review each flagged item:
     - If a foreign word or sentence really was left behind, rewrite the draft and go back to step 2.
     - If it is a genuine exception (a term that needs approval, for example), use `--pending` to propose it instead of adding it straight to allowlist.txt:
       ```bash
       python scripts/check_persian.py --file draft.txt --pending
       ```
       This adds the flagged Latin items to a draft queue awaiting approval, not to allowlist.txt; the script prints the queue's path, and `scripts/pending.txt` is the last-resort location. Then review the items with your own judgment and move only the approved ones to allowlist.txt. Run again.
4. Repeat this loop at most 3 times. If flagged items remain after 3 rounds, review them one by one with your own judgment, state for yourself why each one stays (do not simply ignore it), and only then send.

### Final review gate before sending

Even if the message got `RESULT: CLEAN` in the loop above, **run it once more with `--strict`** so allowlist.txt is ignored:

```bash
python scripts/check_persian.py --file draft.txt --strict
```

- If the result is `RESULT: CLEAN`, the message is safe to send.
- If it is `RESULT: ISSUES=N`, review every flag with your own judgment. These flags may still be justified (an allowlisted term that is truly needed, for example), but you have seen them and decided. If none of them is justified, fix the draft.

Do not skip this step: allowlist.txt can fill up over time, and every addition is a chance that one day an unnecessary Latin word passes without a flag. `--strict` makes sure you see all Latin content every time.

If no command tool is available (a chat-only environment where code does not run, for example), the loop above cannot really run; in that case fall back to the visual review in the previous section, with more care, and do not ignore this limitation.

## Examples

**Example 1: summary from an English source**

The user asks: "Summarize this article about AI regulation."

Reply (for Telegram):

```
خلاصه‌ی مقاله درباره‌ی مقررات هوش مصنوعی:

- قانون جدید روی شفافیت الگوریتم‌ها تمرکز دارد
- شرکت‌ها باید هر سال گزارش بدهند
- جریمه‌ها می‌تواند تا ۴٪ درآمد سالانه برسد
```

**Example 2: a message with code and an error**

The user asks: "why is my python script throwing a KeyError?"

Reply (for Telegram):

```
این خطا یعنی داری به کلیدی از دیکشنری دسترسی پیدا می‌کنی که اصلاً وجود نداره. مثلاً اگه کد این‌طوره:

`value = data['username']`

و کلید `username` توی دیکشنری `data` نیست، دقیقاً همین خطا می‌گیری. راحت‌ترین راه‌حل استفاده از `.get()` هست:

`value = data.get('username')`

این‌طوری اگه کلید نباشه، به‌جای خطا مقدار None برمی‌گرده.
```

(Note: variable names, function names and the code itself are untouched; only the explanations are Persian.)

**Example 3: formal tone for a channel**

The user wants a sales report to post in the company's official channel. The tone must be formal with no colloquial language, not friendly and casual.

## Limits

- This skill does not translate the user's incoming messages; it only sets the language and quality of the output.
- Code, commands, technical strings, IDs and URLs keep their original language.
- It does not apply outside Telegram (terminal, file generation, API), unless it is explicitly combined with another skill.
- If the user explicitly asks for another language for that message, their request takes priority.

### The checker is a quality gate, not a translator

`check_persian.py` flags only "leftover Latin text" and "Latin digits in prose". The tool:

- **Does not translate.** If there is a Latin word in the text, the script does not delete or replace it; it only flags it. Writing the correct Persian version is up to you.
- **Does not measure prose quality.** It does not detect a word-for-word translation feel, tone mismatch, wrong ZWNJ or a poor word choice; only a human eye (or the review in the "Advanced level" section) catches these.
- **Does not reject exceptions automatically.** Code, URLs, IDs and foreign names in parentheses are already exempt, but these exemptions are sometimes the problem themselves (a parenthesis that hides a whole English sentence instead of a Persian explanation, for example).
- **Does not check every item.** Some items may go unseen because of the mask rules (inline code or parentheses, for example).

**So what should you do?** Review every flagged item (or what you see with `--strict`) with your own judgment, not automatically. Keep items such as code, URLs, IDs and deliberate foreign names only if they are genuinely valid exceptions; otherwise give a Persian explanation or write the term in Persian transliteration.
