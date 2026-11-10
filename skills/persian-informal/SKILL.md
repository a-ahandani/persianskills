---
name: persian-informal
description: Guidelines for generating natural, idiomatic, friendly, and informal Persian (Farsi) — including messaging (Telegram, WhatsApp), social posts, casual emails, personal notes, and colloquial bilingual text. Ensures proper colloquial orthography (شکسته‌نویسی), spoken grammar, and correct ZWNJ usage while maintaining clarity.
when_to_use: Writing Persian text that is casual, friendly, conversational, or personal; messages to friends, family, or close colleagues; social media captions/tweets; or anything described as خودمانی, دوستانه, or روزمره.
---

# Informal Persian Writing (راهنمای نگارش فارسی گفتاری و خودمانی)

Informal Persian is warm, direct, and spoken-sounding — but still orthographically sound. Writing casually reflects a spoken register, not an excuse for sloppy spelling or grammar.

---

## 1. Tone and Grammar (لحن و نحو)

- **Write like people actually speak:** Use short sentences, natural vocabulary, and common spoken phrasing.
- **Flexible Word Order (جابه‌جایی ارکان جمله):** Spoken Persian frequently moves complements or adverbs after the main verb for emphasis or natural cadence:
  - *Spoken:* «رفتم خونه‌شون دیشب»
  - *Standard:* «دیشب رفتم خانه‌شان»
- **Consistency of Address (تو / شما):** Pick either second-person singular (`تو`) or second-person plural (`شما`) and stick to it throughout the entire interaction.
- **Avoid Administrative & Bureaucratic Jargon:** Completely eliminate bureaucratic opening or closing formulas (e.g., `احتراماً`, `خواهشمند است`, `مبذول`, `فوق‌الذکر`, `مقتضی`, `عطف به`, `پیرو`).
- **Direct Requests:** Ask directly using spoken verbs rather than formal modal formulas:
  - *Informal:* «می‌تونی تا فردا نگاش کنی؟»
  - *Formal:* «خواهشمند است تا فردا بررسی فرمایید.»
- **Emojis:** Limit to 1–2 maximum per message, matching the context and user style.

---

## 2. Colloquial Spelling Rules (شکسته‌نویسی)

Colloquial breaking follows predictable phonological patterns. Keep spelling consistent within the same document or message.

### A. Vowel Transformations (انتقال مصوت‌ها)
- **`آ` / `ا` → `او` (`ân` / `âm` → `un` / `um` sound shift):**
  - خانه → خونه
  - نان → نون
  - آرامی → آرومی
  - تهران → تهرون (In casual messaging; keep `تهران` if slightly formal/semi-casual)
  - می‌دانم → می‌دونم

### B. Verb & Pronoun Contractions (کوتاه‌سازی افعال و ضمایر)
- **Verbs:**
  - می‌روم → می‌رم
  - می‌خواهم → می‌خوام
  - می‌گویم → می‌گم
  - می‌گوید → می‌گه
  - آمد / آمدن → اومد / اومدن
  - می‌شود → می‌شه
- **Suffix Pronouns:**
  - از من → ازم
  - به او → بهش
  - با او → باهاش
  - برای او → براش
  - کتابشان → کتابشون

### C. Object Marker `را`
- **Use `رو` or `و`:**
  - After consonants: `کتاب رو بده`
  - After vowels: `اینا رو نگه دار` or `بابا رو صدا کن`
  - Colloquial contraction after consonants: `کتابو بده` (acceptable in casual chats).
- *Note:* Keep `را` in semi-official or client-facing messages where full breaking sounds too informal.

### D. What NOT to Break (کدام واژه‌ها نباید شکسته شوند؟)
- **Compound verb tenses:** Keep structural clarity in past perfect/continuous unless intentionally writing heavy dialect (`رفته بودم` stays `رفته بودم`).
- **Polite plurals:** When using polite forms (`می‌فرمایید`, `میل کنید`), do not over-break endings unnaturally.

---

## 3. Orthography, Formatting, and Typography (رسم‌الخط و تایپوگرافی)

### A. Half-Space / ZWNJ (نیم‌فاصله)
Zero-Width Non-Joiner (ZWNJ / `U+200C`) is strictly mandatory in informal Persian to prevent improper character linking:
- **Prefixes:** `می‌رم`, `نمی‌دونم`, `بی‌خیال`
- **Plural Suffixes:** `بچه‌ها`, `عکس‌ها` (or `عکسا`), `دست‌هات`
- **Comparative Suffixes:** `بزرگ‌تر`, `خوب‌تر`

Pronoun attachments join the word directly, with no ZWNJ: `کتابمون`, `کتابشون`, `دستم`. The one exception is a word ending in a silent `ه`, which keeps the ZWNJ before the attachment: `خونه‌م`, `خونه‌شون`.

### B. Correct Characters (حروف فارسی)
- Always use Persian `ی` (`U+06CC`) and `ک` (`U+06A9`).
- **NEVER** use Arabic `ي` (`U+064A`) with dots or Arabic `ك` (`U+0643`).

### C. The `ه` (Heh) vs. Kasra (`-e`) Rule — CRITICAL
- Write `ه` **only** when it represents the spoken short form of the verb `است` (`is`):
  - `دوستمه` = دوستِ من است (Correct)
  - `ماشین خوبیه` = ماشین خوبی است (Correct)
- **NEVER** use `ه` for the Ezafe construction (`-e` connection):
  - `دوستِ من` (Correct) — **NOT** `دوسته من`
  - `کتابِ جدید` (Correct) — **NOT** `کتابه جدید`
  - `شبِ جمعه` (Correct) — **NOT** `شبه جمعه`

### D. Numbers & Foreign Terms
- Persian digits (`۰-۹`) or English digits (`0-9`) are both acceptable; ensure internal consistency within a single text.
- Loanwords common in daily conversation are fully accepted (e.g., `ددلاین`, `فایل`, `اوکی`, `ایمیل`, `لینک`).
- Code, filenames, URLs, or variable names must be enclosed in `backticks`.

### E. Punctuation & Layout
- Standard Persian punctuation apply without leading spaces:
  - Comma: `،`
  - Question mark: `؟`
  - Quotes: `« »`
- Right-align all columns in Markdown tables containing Persian content using standard syntax (`---:`).

---

## 4. Register Matrix (سطوح گفتار)

| Feature | Extremely Casual (گپ دو نفره) | Casual / Friendly (دوستانه / شبکه‌های اجتماعی) | Semi-Formal / Work Chat (کاری / همکار نزدیک) | Formal (اداری / رسمی) |
| ---: | ---: | ---: | ---: | ---: |
| **Pronoun** | تو | تو / شما | شما | شما |
| **Object Marker** | -و / رو | رو | رو / را | را |
| **Verb Breaking** | می‌خوام / می‌گم / می‌شه | می‌خوام / می‌گم | می‌خواهم / می‌گویم (or slight break) | می‌خواهم / می‌گویم |
| **'Is' Verb** | ـه (خوبه) | ـه (خوبه) | است | است |
| **Tone** | 100% Conversational | Friendly & Spoken | Respectful & Clear | Bureaucratic / Standard |

---

## 5. Examples & Transformations (نمونه‌های بازنویسی)

### Example 1: Casual Slack/Telegram Message
- ❌ **Incorrect / Mixed:** سلام آقای محمدی، من امروز نمی تونم بیام. لطفا فایل رو برام ایمیل کنید. با تشکر.
- ❌ **Incorrect (Sloppy Ezafe & Arabic characters):** سلام علی جان. کتابه جدیدم رو دادم بهش، رسیـدم خونه زنگ میزنم.
- ✅ **Correct Informal:** سلام علی جان! کتابِ جدیدم رو دادم بهش. رسیدم خونه بهت زنگ می‌زنم.

### Example 2: Friendly Follow-up Email
- ❌ **Formal/Stiff:** احتراماً پیرو صحبت‌های قبلی، خواهشمند است فایل مربوطه را بررسی نموده و نتیجه را اعلام فرمایید.
- ✅ **Natural Informal:** سلام وقتت بخیر! در ادامه صحبتامون، ممنون می‌شم این فایل رو یه نگاه بندازی و نظرت رو بهم بگی.
