# GitHub Copilot Instructions for Persian Language & RTL

- **Tone & Natural Phrasing:** Write natural Persian without robotic patterns. Avoid "می‌باشد", prefer "است". Drop cliché phrases like "لازم به ذکر است". Use Persian `ی` and `ک`.
- **RTL & Text Direction:** For Persian markdown, start with a Persian word. Isolate English terms and code variables in backticks or `<span class="en-font" dir="ltr">`.
- **Typography & Orthography:** Enforce proper ZWNJ (نیم‌فاصله) for verbs and compound nouns. Persian punctuation (، ؟ ؛) must stick to the previous word with a trailing space.
- **Frontend & CSS:** Do NOT apply `letter-spacing` on Persian fonts. Use CSS logical properties (`margin-inline-start`, `padding-inline-start`). Set `dir="ltr"` on numeric/phone/email input fields.
- **Data & Excel:** Always encode Persian CSV data with UTF-8 BOM (`utf-8-sig`) for Excel compatibility.
