---
name: persian-typography
description: >-
  Starts Persian typography and design work by establishing the purpose,
  medium, locale and editing scope, and routes to the web, documents or review
  skill. Preserves the source text exactly: ZWNJ
  («نیم‌فاصله»), Persian ک and ی, logical order, names and numbers. Use when
  starting any Persian typesetting, layout or design task, or when the user
  writes «حروف‌چینی فارسی» or «طراحی فارسی».
license: Apache-2.0
metadata:
  author: L&Co. LLC
  source: https://github.com/landco-llc/kumihan
  upstream-commit: 1b27c93
  version: "0.1.0"
  changes: Description and instructions made English only (the Persian half of the bilingual text removed), file paths marked as code, and how to run the static checker added.
---

# Persian typography: start here

Begins Persian typography and design by establishing the purpose, medium, locale and editing scope.

1. Read `references/contract.md`, then `assets/rule-catalog.json` and `assets/sources.json`. Choose the medium from the actual purpose and audience.
2. For new Iranian Persian content, propose fa-IR as the default locale. Do not infer the Persian language from Arabic-script glyphs alone. fa-AF (Dari) and Tajik are separate.
3. Choose the mode: study, build, refine or read-only audit. Preserve source bytes, metadata, ZWNJ (نیم‌فاصله), ZWJ, Persian Kaf ک and Yeh ی, combining marks, numbers, names and version strings.
4. Do not insert automatic Tatweel, reverse logical strings, split joined text into per-letter spans, force decorative calligraphy or output uniform templates. Make design choices from the context.
5. Apply the FA rules and locale guidance that fit. For LTR URLs, emails, codes and version strings inside RTL text, isolate them with markup without rewriting the original content.
6. Use `scripts/check_source.py` for bounded static evidence only: `python3 scripts/check_source.py page.html` checks one HTML file, and adding `--candidate edited.html` compares the candidate's bytes with the source. Run rendered, copy and native evidence separately when available. The scenarios in `evals/acceptance.json` are examples, not proven passes.
7. Report observed results with `assets/report-schema.json`, listing unverified checks explicitly. In an audit, never edit the target files.

Once the medium is chosen, load its skill: `persian-typography-web` for sites and interfaces, `persian-typography-documents` for documents, slides and print, or `persian-typography-review` for a read-only audit.

Package creation does not check provider import, real host invocation or native-language certification.
