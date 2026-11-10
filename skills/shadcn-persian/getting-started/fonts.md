---
title: "Fonts"
description: "Choose a Persian font stack - a Persian-first Sahel build paired with Geist, Farsi digits from the Sahel FD build, plus local-font notes for Next.js."
---

Persian text renders best with a proper Arabic-script typeface. The resilient choice is a **Persian-first stack**: put a Persian font like _Sahel_ first, then a Latin font like Geist for Latin letters and digits.

## 1. The stack we recommend

Use a Persian font first, then Geist, so Persian glyphs come from the Persian family and Latin/digits fall through where they don't:

```css
:root {
  --font-sans: "Sahel", "Geist", system-ui, sans-serif;
  --font-mono: "Geist Mono", ui-monospace, monospace;
}
```

### Use a Sahel build without Latin and without Persian digits

For the most flexible pairing, prefer the **Sahel WOL build** (`dist/Without-Latin/`, no Latin glyphs) over the **Sahel FD** build (`dist/Farsi-Digits/`), so digits stay Latin (0-9) instead of forcing Persian digits:

- Because it has no Latin, every Latin character automatically falls to Geist — so mixed Persian/English text and code look consistent.
- Because it is not the FD build, digits stay Latin, so you aren't locked into ۰-۹ everywhere. Turn on Persian digits **only where you want them** with the digit utilities ([Normalize Persian Digits](/docs/utilities/normalize-persian-digits), `toPersianDigits` from [Persian Date](/docs/utilities/persian-date)), rather than having the base font decide for you.

This keeps body copy, filenames, prices, and form values under your control instead of the font's.

## 2. Farsi digits come from the Sahel FD build, not `ss01`

Some Persian fonts put Farsi digits behind a stylistic set, but Sahel does not, so `font-feature-settings: "ss01"` does nothing for its digits. When you want the base font itself to draw ۰-۹, use the **Sahel FD** family from `dist/Farsi-Digits/`. The jsDelivr `font-face.css` only declares `Sahel`, so declare `Sahel FD` yourself:

```css
@font-face {
  font-family: "Sahel FD";
  src: url("https://cdn.jsdelivr.net/gh/rastikerdar/sahel-font@v3.4.0/dist/Farsi-Digits/Sahel-FD.woff2") format("woff2");
  font-weight: 400;
}

body {
  font-family: "Sahel FD", "Geist", system-ui, sans-serif;
}
```

PersianLabs/ui components don't override the base font, so whatever you set on your base keeps applying to them.

> The scaffolded projects ship Vazirmatn with its `ss01` digit setting. When you switch them to Sahel, drop `ss01` and pick the Sahel or Sahel FD family instead. Estedad, the other scaffold option, uses `ss20`.

## 3. Adding a local font in Next.js

If you self-host the font files (recommended for offline/perf), load them with `next/font/local`. Set `adjustFontFallback: false` so Next.js doesn't generate a Latin metric fallback that can fight the Arabic metrics:

```tsx
// app/layout.tsx
import localFont from "next/font/local"

const sahel = localFont({
  src: "./fonts/Sahel-VF.woff2",
  weight: "400 900", // the variable build has no Light and no Latin; Geist covers Latin
  style: "normal",
  variable: "--font-sahel",
  adjustFontFallback: false,
})

const geist = localFont({
  src: "./fonts/Geist.woff2",
  variable: "--font-geist",
  adjustFontFallback: false,
})
```

```css
:root {
  --font-sans: "Sahel", "Geist", system-ui, sans-serif;
}
```

The same `adjustFontFallback: false` applies to Google-font loading through `next/font/google` when you're layering an Arabic script next to a Latin one — it prevents metric fallback mismatches between the two families.

## 4. If you're not using `next/font`

Load the CSS manually and set the same tokens:

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/rastikerdar/sahel-font@v3.4.0/dist/font-face.css"
/>
```

```css
body {
  font-family: "Sahel", "Geist", system-ui, sans-serif;
}
```

## 5. Numerals and tabular alignment

Values that must align numerically — prices, counts, tables — should use `tabular-nums`. The components already do:

```tsx
<span className="tabular-nums">۱۲۳٬۴۵۶</span>
```

## 6. Mixing Persian and code

Commands, URLs, and code stay LTR and use your mono font (see [RTL → LTR islands](/docs/rtl#3-ltr-islands-in-an-rtl-page)). The install blocks across the docs set this up for you.

## Next steps

- [RTL](/docs/rtl) — wire up the text direction.
- [Typography](/docs/components/typography) — the heading and paragraph styles the library expects.
