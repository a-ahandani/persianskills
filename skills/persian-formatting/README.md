<div align="center">

# 🇮🇷 Persian Typography, Natural Voice & Universal RTL Skill for AI
### Comprehensive Standards, De-AI-ing Guidelines & Cross-Platform RTL Rules for AI Coding Assistants

**Built for modern AI agents and LLMs:**  
Google Antigravity • Claude Code • Cursor • GitHub Copilot • Windsurf • ChatGPT • Claude.ai

[![Persian Documentation](https://img.shields.io/badge/Language-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-green.svg)](README.fa.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/PouyaRN/persian-formatting-skill/pulls)
[![RTL Supported](https://img.shields.io/badge/RTL-100%25-orange.svg)](#)

[**🇮🇷 مشاهده مستندات فارسی (Persian Documentation)**](README.fa.md) • [English Documentation](README.md)

</div>

---

## 📌 Why is this skill essential?

While modern Large Language Models (GPT-4o, Claude 3.7, Gemini 2.5) understand Persian well, they consistently struggle with stylistic nuances, typographic conventions, and layout engineering:

1. **Robotic & Translated Tone:** Excessive repetition of passive/archaic verbs like `"می‌باشد"` instead of `"است"`, clichéd filler openers (`"لازم به ذکر است"`, `"شایان ذکر است"`, `"در دنیای پرشتاب امروزی"`), and translationese phrasing.
2. **Broken BiDi & Text Direction:** Mixed Latin/Persian sentences get mangled in markdown and chat bubbles (parentheses flip, numbers jump to the wrong side of sentences).
3. **Glyph Disconnection via `letter-spacing`:** AI assistants frequently inject CSS `letter-spacing` into Persian/Arabic headings, breaking the connected cursive ligatures of the alphabet.
4. **Excel CSV Encoding Corruption:** Exported Persian CSV files open as garbled question marks (`????`) in Microsoft Excel due to missing UTF-8 Byte Order Marks (BOM).
5. **Client-side Missing Fonts:** Rendered HTML documents and PDFs fail or degrade on devices that do not have local Persian fonts installed.

This skill equips AI models with battle-tested guardrails to produce natural, grammatically sound, typographically pleasing, and layout-safe Persian text, code, and documents.

---

## 🚀 Quick Setup Across Platforms

| Platform | Setup Instructions |
| :--- | :--- |
| **Google Antigravity** | Copy [`SKILL.md`](SKILL.md) to `~/.gemini/config/skills/persian-formatting/SKILL.md` or `.agent/skills/` in your repository. |
| **Cursor IDE** | Copy [`rules/persian.mdc`](rules/persian.mdc) to `.cursor/rules/persian.mdc` or append its content to `.cursorrules`. |
| **Claude Code (Anthropic)** | Copy [`SKILL.md`](SKILL.md) to `.claude/skills/persian-formatting/SKILL.md` or append [`rules/CLAUDE.md`](rules/CLAUDE.md) to your project's `CLAUDE.md`. |
| **GitHub Copilot** | Copy [`rules/copilot-instructions.md`](rules/copilot-instructions.md) into `.github/copilot-instructions.md` in your project root. |
| **Windsurf** | Copy [`rules/windsurfrules`](rules/windsurfrules) into `.windsurfrules` in your repository. |
| **ChatGPT / Claude Web** | Paste sections 1 to 4 of [`SKILL.md`](SKILL.md) into **Custom Instructions** or your project's system prompt. |

---

## 🌟 Core Pillars & Capabilities

### 1. Natural Voice & De-AI-ing (انسانی‌سازی لحن)
* **Elimination of `"می‌باشد"`:** Automatically replaces 95% of passive/archaic occurrences with natural, conversational `"است"` or context-appropriate active verbs.
* **Stripping Robotic Clichés:** Removes generic preamble phrases (`"لازم به ذکر است"`, `"شایان ذکر است"`, `"همان‌طور که می‌دانید"`).
* **Character Normalization:** Enforces authentic Persian characters (`ی` and `ک`) instead of Arabic variants (`ي` and `ك`).

### 2. Frontend & CSS Safety Guardrails
* **Strict `letter-spacing` Prohibition:** Prevents AI from applying letter spacing to Persian fonts, safeguarding natural script ligatures.
* **Sensitive Input Direction:** Forces `dir="ltr"` on numeric/alphanumeric inputs (phone numbers, national IDs, bank cards, IBANs, passwords, OTPs) to eliminate cursor jumping.
* **CSS Logical Properties:** Automatically prefers `margin-inline-start`, `padding-inline-start`, and `border-inline-start` (and Tailwind `ms-*`, `me-*`, `ps-*`, `pe-*`) for native bidirectional support.
* **Universal Web Font Fallback:** Integrates the open-source **Sahel** font (SIL OFL 1.1) via the jsDelivr CDN in all standalone HTML layouts so outputs look pristine on every client machine.

### 3. BiDi & Layout Isolation
* **Chat Encapsulation:** Encloses responses in an explicit RTL container for platforms supporting HTML styling.
* **Token Isolation:** Isolates Latin terms, code symbols, and acronyms using backticks, `<bdi>`, or `<span class="en-font" dir="ltr">`.
* **Accurate Typography:** Enforces Zero-Width Non-Joiners (ZWNJ / نیم‌فاصله), Persian quotation marks («...»), and authentic decimal separators (`۴٫۵` instead of `۴.5`).

### 4. Data Encoding & Headless PDF Generation
* **Excel Compatibility:** Guarantees **UTF-8 with BOM** (`utf-8-sig` in Python, `\uFEFF` in JS) for CSV files to prevent Excel character corruption.
* **Cross-Platform Chrome Headless:** Provides validated commands for Windows, macOS, and Linux to convert Persian HTML to vector-perfect PDFs.

---

## 💻 HTML & Print-Ready Template

When creating Persian documents or PDF reports, the AI utilizes this resilient boilerplate:

```html
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Persian Document</title>
    <!-- Sahel via jsDelivr, Fira Code via Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/sahel-font@v3.4.0/dist/font-face.css">
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        body {
            direction: rtl;
            text-align: right;
            font-family: 'Sahel', Tahoma, sans-serif;
            /* Sahel has no ss01 digit set; Persian numerals come from the Sahel FD build (dist/Farsi-Digits/) */
            letter-spacing: normal !important; /* Critical: prevent breaking cursive ligatures */
            line-height: 1.8;
            margin: 0;
            padding: 24px;
            color: #1e293b;
            background-color: #ffffff;
        }
        .en-font, [dir="ltr"] {
            direction: ltr;
            text-align: left;
            display: inline-block;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .code-font, code, pre {
            direction: ltr;
            text-align: left;
            font-family: 'Fira Code', 'Source Code Pro', Consolas, monospace;
            unicode-bidi: isolate;
        }
        @page {
            size: A4 portrait;
            margin: 12mm 15mm;
        }
    </style>
</head>
<body dir="rtl">
    <!-- Content goes here -->
</body>
</html>
```

### Exporting to PDF via Headless Chrome:
* **Windows (PowerShell):**
  ```powershell
  & "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="output.pdf" "input.html"
  ```
* **macOS:**
  ```bash
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="output.pdf" "input.html"
  ```
* **Linux:**
  ```bash
  google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="output.pdf" "input.html"
  ```

---

## 📂 Repository Structure

```text
├── SKILL.md                  # Universal skill file for AI agent engines
├── README.md                 # English documentation and architecture
├── README.fa.md              # مستندات کامل به زبان فارسی
├── LICENSE                   # MIT License
└── rules/                    # Ready-to-use rule snippets for coding tools
    ├── persian.mdc           # Cursor IDE rule file
    ├── CLAUDE.md             # Claude Code instruction file
    ├── copilot-instructions.md # GitHub Copilot configuration
    └── windsurfrules         # Windsurf Cascade rule file
```

---

## 🤝 Contributing

Contributions, feedback, and edge-case reports are warmly welcomed! If you encounter specific AI hallucinations, broken ligatures, or missing tool adapters, please feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free for personal and commercial use.
