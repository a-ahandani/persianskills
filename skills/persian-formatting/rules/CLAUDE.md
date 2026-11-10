# Persian Typography & Universal RTL Guidelines

When generating Persian (Farsi) text, documentation, UI components, or chat output:

1. **Natural Tone (De-AI-ing):**
   - Avoid robotic phrasing and unnecessary passive verbs. Replace "می‌باشد" with "است" or "هست".
   - Eliminate filler openings ("لازم به ذکر است", "شایان ذکر است", "در جهان پرشتاب امروزی").
   - Always use standard Persian letters (`ی`, `ک`) instead of Arabic ones (`ي`, `ك`).

2. **RTL & Mixed Content Isolation:**
   - In rich chat/HTML rendering, wrap Persian output in:
     `<div dir="rtl" style="text-align: right; direction: rtl; font-family: 'Sahel', Tahoma, sans-serif;">`
   - Isolate English terms, code identifiers, and acronyms using backticks, `<span class="en-font" dir="ltr">`, or `<bdi>`.
   - Never start a paragraph with a Latin word or number.
   - Enforce ZWNJ (نیم‌فاصله) on prefixes ("می‌شود"), suffixes ("گزارش‌ها"), and compounds ("پایگاه‌داده").
   - Attach punctuation (، ؟ ؛ .) to the previous word. Use Persian quotation marks (« »).

3. **Frontend & Styling Safety:**
   - Never apply `letter-spacing` to Persian text (it breaks cursive glyph connections).
   - Use CSS Logical Properties (`margin-inline-start`, `border-inline-start`, `ms-*`, `me-*`).
   - Force `dir="ltr"` on numeric/sensitive input fields (phone, national ID, card number, password, email).

4. **File Encoding & Exports:**
   - Always export Persian CSV files as UTF-8 with BOM (`utf-8-sig` in Python, `\uFEFF` in JS) so Microsoft Excel opens them correctly.
   - For PDF generation, use Chrome Headless with `--headless=new`.
