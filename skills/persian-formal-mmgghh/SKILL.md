---
name: persian-formal-mmgghh
description: Rules for writing formal, professional, and official Persian — administrative letters (نامه اداری), reports, engineering/tech docs, contracts, proposals, articles, and bilingual Persian/English business documents. Covers register, syntax, terminology, orthography (نیم‌فاصله), punctuation, numbers, and RTL markdown.
when_to_use: Any Persian text that is formal, official, administrative, professional, academic, financial, or legal; also when translating English business/technical text into Persian or writing technical documentation.
---

# Formal & Technical Persian Writing

This is the standard register for professional and formal documents. Colloquial (شکسته) forms, administrative jargon, and lazy transliterations are strictly forbidden (e.g., use می‌روم, never می‌رم).

---

## 1. Sentence Structure & Grammar

- **SOV Order**: Persian is Subject-Object-Verb. Keep verbs at the end of the sentence. Shift them only for deliberate rhetorical emphasis.
- **Conciseness & Sentence Length**: Limit sentences to ~25 words. Split multi-clause chains connected by verbose conjunctions (e.g., replace long «با توجه به اینکه … لذا …» chains with clear, distinct sentences).
- **Active Voice Dominance**: Prefer the active voice. Use passive voice only when the agent is unknown or irrelevant—never as an artificial politeness device.
  - *Incorrect:* «گزارش توسط تیم فنی آماده شد.»
  - *Correct:* «تیم فنی گزارش را آماده کرد.»
- **Object Marker (`را`) Placement**: Keep `را` immediately following its direct object. Do not allow long modifiers or subordinate clauses to strand `را`.
  - *Incorrect:* «پیشنهادی که هفته گذشته مطرح شده بود را بررسی کردیم.»
  - *Correct:* «پیشنهاد مطرح‌شده در هفته گذشته را بررسی کردیم.»
- **Paragraphing**: Focus on one topic per paragraph (3–5 sentences maximum).

---

## 2. Word Choice, Vocabulary & Anti-Calques

### Word Replacement Matrix
Avoid archaic, overly complex, or redundant administrative terminology:

| به‌جای | بنویس |
|---:|---:|
| می‌باشد | است، هست |
| گردید، گردیده است | شد، شده است |
| نمودن (به‌جای فعل اصلی) | کردن |
| توسطِ … انجام شد | … انجام داد |
| مورد بررسی قرار گرفت | بررسی شد |
| در رابطه با | درباره‌ی، در مورد |
| جهتِ | برایِ |
| بایستی، می‌بایست | باید |
| علی‌رغم | به‌رغمِ، با وجودِ |
| گزارشات، پیشنهادات، آزمایشات | گزارش‌ها، پیشنهادها، آزمایش‌ها |
| اساتید | استادان |
| گاهاً، تلفناً، زباناً | گاهی، تلفنی، شفاهی |

### Plurals & Redundancy Rules
- **Native Plurals**: Apply Persian plural suffixes (`-‌ها` / `-ان`) to Persian words. Do not apply Arabic plural forms to non-Arabic base words (*گزارشات* → *گزارش‌ها*).
- **Arabic Loanwords**: Recognized standard Arabic broken or sound plurals (e.g., *استثنائات*, *مراحل*) are accepted in formal contexts.
- **No Double Plurals**: Never apply `-ها` to an already pluralized word (*مدارک‌ها* → *مدارک*).
- **Tanwin Rules**: Never apply Arabic Tanwin (`ـً`) to native Persian words (*زباناً* → *شفاهی*).
- **Eliminate Redundancy (حشو)**:
  - «بازگشت مجدد» → «بازگشت»
  - «تقریباً حدودِ» → «حدودِ»
  - «سؤال پرسید» → «پرسید»
- **Consistency**: Use a single standard term for each concept throughout a document. Varying terms for variety causes ambiguity in legal, technical, and financial writing.

### Technical & Engineering Terminology
Use consistent translations for common software, engineering, and business terms:

| English Term | Standard Persian Equivalent (بنویس) | Avoid Transliteration / Incorrect (ننویس) |
|---:|---:|---:|
| API / Endpoint | رابط برنامه‌نویسی / نقطه‌ی پایانی | اندپوینت |
| Authentication | احراز هویت | اتنتیکیشن |
| Authorization | سطح دسترسی / مجوزدهی | اتوریزیشن |
| Feature | قابلیت / ویژگی | فیچر |
| Production Environment | محیط عملیاتی | محیط پروداکشن / محیط تولید |
| Stage / Environment | محیط / مرحله | استیج |
| Token | توکن | نشانه |
| User Interface (UI) | رابط کاربری | یوآی |

---

## 3. Orthography (دستور خط)

- **Zero-Width Non-Joiner (ZWNJ / نیم‌فاصله)**: Use ZWNJ (`U+200C`)—never a full space—in:
  - Verb prefixes: `می‌` / `نمی‌` (`می‌رود`)
  - Plural suffix: `ها` (`کتاب‌ها`)
  - Comparative/Superlative suffixes: `تر` / `ترین` (`بزرگ‌تر` — note: `بهتر`, `کمتر`, `بیشتر` are written solid)
  - Indefinite suffix: `ای` (`خانه‌ای`)
  - Compound nouns/adjectives: (`دانش‌آموز`, `سی‌ساله`)
- **Preposition `به`**:
  - Keep prepositional `به` separate: `به تهران رفت`.
  - Prefix `به` in adverbs/adjectives takes ZWNJ: `به‌ویژه`, `به‌طور کلی`, `به‌جز`.
- **Ezāfe on Silent `ه` (هٔ / ه‌ی)**:
  - Write as `ه` + ZWNJ + `ی`: `خانه‌ی من`.
  - The Academy standard `خانهٔ من` is equally valid for publishers/government requirements. **Do not mix both styles in the same document.** Never use a full space (`خانه ی من`).
- **Hamza in Loanwords**:
  - Arabic words ending in hamza drop the character in Persian compound forms: `املا`, `انشا`, `ابتدا` → `املای من`.
  - Arabic plural forms with hamza are written cleanly: `استثنائات`.
- **Persian Letterforms Only**:
  - Use exclusively Persian `ی` (`U+06CC`) and `ک` (`U+06A9`).
  - Never use Arabic `ي` (`U+064A`) or `ك` (`U+0643`).
- **Plural `-گان` after a silent `ه`** (drop the `ه`): Write `تشنگان`, not `تشنه‌گان`.

---

## 4. Punctuation (نشانه‌گذاری)

- **Persian Punctuation Marks**: Use `،` `؛` `؟` `«` `»` instead of `,` `;` `?` `"` `"`.
- **Spacing Rules**:
  - No space *before* `. ، ؛ : ؟ !` and exactly one space *after*.
  - Quotes and Brackets: No space inside, one space outside → `«نقل‌قول»` ، `(توضیح)`.
- **Parentheses vs. Dashes**:
  - Supplementary, optional, or explanatory content goes in parentheses: `سود خالص (پس از کسر مالیات) ۱۲٪ افزایش یافت.`
  - Reserve em-dashes (`—`) for complete interjected clauses.
  - Use short dashes (`-`) strictly for numeric or date ranges: `۱۳۹۸-۱۴۰۲`.
- **Semicolons (`؛`)**: Use to separate long related independent clauses or list items that already contain internal commas.
- **Colons (`:`)**: Introduce lists, formal quotes, or explanations.
- **Guillemets (`« »`)**: Enclose direct quotes, titles, and the first occurrence of a specialized technical term. Use `[ ]` only for editorial insertions inside quotes.
- **Forbidden Punctuation**:
  - No commas directly after conjunctions: avoid `و،`, `اما،`, `اگر،`, `که،`.
  - Limit exclamations or questions to a single mark: never use `!!!` or `?!`.

---

## 5. Numbers, Dates & Bilingual Text

- **Persian Digits**: Always use Persian digits (`۰۱۲۳۴۵۶۷۸۹`) within Persian body text.
- **Separators**:
  - Decimal separator: `/` (`۳/۵`).
  - Thousands separator: `٬` (`۱٬۲۵۰٬۰۰۰`).
- **Units and Quantities**: Include a space between numbers and nouns (`۲۵ تومان`); use ZWNJ in numeric adjectives (`۲۵تومانی`).
- **Dates**: Format Jalali dates as `۱۴۰۴/۰۶/۱۱`. Explicitly label calendar types if both Gregorian and Jalali appear together.
- **Bilingual Terminology**:
  - Provide the original English term in parentheses at first mention, then use the Persian translation consistently: `حسابداری تعهدی (accrual accounting)`.
  - Wrap Latin code snippets, filenames, variables, and URLs in `backticks` to prevent RTL display scrambling.
  - Keep punctuation adjacent to a Latin word formatted as Persian punctuation.

---

## 6. Markdown Formatting & RTL Layout

- **Table Alignment**: Explicitly right-align every table column using `---:` in the separator row for all Persian content tables.
- **Spacing**: Ensure a blank line precedes every list and follows every section heading.
- **HTML Container**: For web/HTML output, wrap the document in `<div dir="rtl">` and apply CSS `direction: rtl; text-align: right;`.

---

## 7. Official Administrative Letters (نامه اداری)

Follow the standard structure:
1. Recipient title and honorific
2. Salutation: `با سلام و احترام،` or `احتراماً،`
3. Primary purpose stated clearly in the first sentence (avoid burying requests under extended *ta'arof*)
4. Body text: concise, one request per paragraph
5. Formal closing: `با تشکر و احترام،`
6. Sender identity: Name, Role, Date

**Honorific Guidelines**:
- Address individuals as `جناب آقای …` or `سرکار خانم …`.
- Address organizational bodies/roles as `ریاست محترمِ …` or `مدیریت محترمِ …`.
- Keep official correspondence to a single page whenever possible.

---

## 8. Quality Control Checklist (Before Delivery)

Before finalizing any document, run the following verification steps:
- [ ] **ZWNJ Verification**: Check for accidental spaces in ` می ` and ` ها ` (replace with ZWNJ).
- [ ] **Forbidden Words Check**: Confirm no instances of `می‌باشد`, `گردید`, `نمودن`, or `توسط` remain.
- [ ] **Digit Check**: Ensure no Latin digits (`0-9`) appear in standard Persian prose.
- [ ] **Letterform Check**: Ensure no Arabic `ي` or `ك` characters leaked into the text.
- [ ] **RTL Table Alignment**: Verify all Markdown tables include right-alignment specifiers (`---:`).
