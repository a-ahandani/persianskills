# Persian fonts: catalog, pairing, embedding

All fonts here are SIL OFL — free for commercial use, embedding allowed.
The bundled family (Sahel, five static weights) lives in `assets/fonts/`.
The rest need `scripts/download_fonts.py` (requires GitHub access — will NOT
work in offline/allowlisted sandboxes; in that case use only what's bundled,
or ask the user to drop TTFs into the project folder).

## Catalog

| Font | Personality | Use for | Avoid for | Weights |
|---|---|---|---|---|
| **Sahel** ★bundled | Modern, clean, slightly condensed | Body text, UI, documents, dashboards, anything | — (the safe default) | 5 (Light 300–Black 900) + FD |
| **Sahel Black** ★bundled | The 900 weight as display face: heavy, poster-like | Headlines, covers, banners, campaign titles | Body text, long headings | 1 (Sahel's 900) |
| **Shabnam** | Softer, rounder sibling from the same designer | Body alternative, friendly docs | — | 5 + FD variants |
| **Samim** | Sober text face tuned for reading | Long reports, articles, books | Display sizes | 3 + FD |
| **Parastoo** | Bookish, literary, mild serif flavor | Formal letters, literary/academic docs | Modern tech branding | 2 + FD |
| **Tanha** | Thin, elegant, airy display | Pull quotes, elegant covers, invitations | Body text (too light) | 1 |
| **Gandom** | Warm, rounded, approachable | Casual brochures, kids/food/lifestyle content | Corporate formal docs | 2 + FD |

("FD" variants ship with built-in Farsi digit glyphs mapped to ASCII digits —
prefer real Persian digit characters instead; see orthography.md.)

Sources (for `download_fonts.py` or manual download):
- Sahel: github.com/rastikerdar/sahel-font, release v3.4.0 (not on Google Fonts);
  CDN: `https://cdn.jsdelivr.net/gh/rastikerdar/sahel-font@v3.4.0/dist/`
  (Farsi-digit builds under `dist/Farsi-Digits/`, family "Sahel FD")
- Others: github.com/rastikerdar/{shabnam,samim,parastoo,tanha,gandom}-font

## Pairings that work

| Deliverable | Headings | Body |
|---|---|---|
| Business proposal / invoice | Sahel Bold/Black | Sahel Regular |
| Marketing one-pager, poster | Sahel Black | Sahel |
| Long report / whitepaper | Sahel Bold | Samim or Sahel |
| Product docs / dashboard | Sahel Bold | Shabnam or Sahel |
| Literary / formal letter | Parastoo Bold | Parastoo |
| Elegant cover + quote | Tanha (display) | Sahel |

One display font per document, maximum. When in doubt: Sahel everywhere,
weights for hierarchy.

## Typography rules for Persian

- **Line height:** Persian needs more leading than Latin — 1.6–2.0 in CSS,
  `line: 312+` (≥1.3) in docx, more for headings. Tight leading clips
  ascenders and dots.
- **Size:** Persian x-height runs small; bump body ~1pt/10% over the Latin
  equivalent (11–12pt docx body, 16–18px web).
- **Never letter-space** (`letter-spacing`/character spacing) — Persian letters
  join; tracking tears the joins apart. Not even for headings. Use size/weight/
  color for emphasis instead.
- **Never fake bold/italic.** Use real weights. Italic barely exists in Persian
  type; for emphasis use bold, color, or «گیومه».
- **Kashida (کشیده):** justification by stretching connections. Word processors
  do it automatically with justify; don't insert manual ـ characters.
- **Justified text** is traditional for print Persian body; START-aligned
  (ragged left) is fine for web and modern docs. Headings: never justify.

## Embedding per format

### docx (docx-js / python-docx)
Font name exactly as the family name: `"Sahel"` (Regular; bold toggle gives
the real Bold), `"Sahel Black"` for display headings (also `"Sahel Light"`,
`"Sahel SemiBold"` — docx has no numeric weight, so non-bold weights are
separate family names).
Always with `hint: "cs"` (docx-js) or `w:rFonts w:cs=` (python-docx) — see
docx-pdf.md. The font must be installed on the converting machine
(`bash scripts/install_fonts.sh`) or LibreOffice substitutes DejaVu.

### HTML / CSS
```css
@font-face {
  font-family: "Sahel";
  src: url("fonts/Sahel.woff2") format("woff2"),
       url("fonts/Sahel.ttf") format("truetype");
  font-weight: 400; font-display: swap;
}
/* repeat per weight: Sahel-Light 300, Sahel-SemiBold 600, Sahel-Bold 700, Sahel-Black 900 */
body {
  font-family: "Sahel", "Segoe UI", Tahoma, sans-serif; /* Tahoma = classic Persian-safe fallback */
  line-height: 1.8;
}
```
Online pages can use the jsdelivr CSS (Sahel is not on Google Fonts):
`https://cdn.jsdelivr.net/gh/rastikerdar/sahel-font@v3.4.0/dist/font-face.css`
(family `Sahel`, weights 300/400/600/700/900); offline/PDF-print pages must
reference local files — copy them from `assets/fonts/`.

### pptx
Set the font on both latin and cs typefaces of every run (see pptx.md).
PowerPoint font embedding is unreliable cross-platform; if the deck must
travel, export a PDF (with fonts installed) alongside it.

### Checking a glyph exists (before using any symbol)
```python
from fontTools.ttLib import TTFont
cmap = TTFont("assets/fonts/Sahel.ttf").getBestCmap()
ok = all(ord(c) in cmap for c in "•·۱۲۳؟،؛«»٪٬")
```
Known result for the bundled fonts: • · and all Persian punctuation/digits are
present; ▪ ■ ✓ ● ◆ are NOT (they silently fall back to DejaVu in PDFs). Check
before using anything fancier than • — `verify_pdf.py` will catch the fallback
after the fact, but checking first is cheaper.
