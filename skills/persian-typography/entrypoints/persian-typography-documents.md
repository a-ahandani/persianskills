---
name: persian-typography-documents
description: >-
  Composes and reviews Persian documents and presentations (Word,
  PowerPoint, PDF, print and graphics) while preserving the source text and
  checking the output: shaping, reading order, ZWNJ («نیم‌فاصله») and
  copy-paste round trips. Part of KUMIHAN (تراز). Use when creating,
  formatting or exporting a Persian document, slide deck, PDF or print
  piece, or when the user writes «سند فارسی», «ارائه فارسی» or
  «حروف‌چینی».
license: Apache-2.0
metadata:
  author: L&Co. LLC
  source: https://github.com/landco-llc/kumihan
  upstream-commit: 1b27c93
  version: "0.1.0"
  changes: Description and instructions made English only (the Persian half of the bilingual text removed), file paths marked as code, and how to run the static checker added.
---

# KUMIHAN (تراز): Persian documents and presentations

Composes Persian documents and presentations with source preservation and output checks.

1. Read `references/contract.md` and `references/documents.md`, then `rules/catalog.json` and `sources.json`. Choose the medium from the actual purpose and audience.
2. For new Iranian Persian content, propose fa-IR as the default locale. Do not infer the Persian language from Arabic-script glyphs alone. fa-AF (Dari) and Tajik are separate.
3. Choose the mode: study, build, refine or read-only audit. Preserve source bytes, metadata, ZWNJ (نیم‌فاصله), ZWJ, Persian Kaf ک and Yeh ی, combining marks, numbers, names and version strings.
4. Do not insert automatic Tatweel, reverse logical strings, split joined text into per-letter spans, force decorative calligraphy or output uniform templates. Make design choices from the context.
5. Apply the FA rules and locale guidance that fit. For LTR URLs, emails, codes and version strings inside RTL text, isolate them with markup without rewriting the original content.
6. Use `runtime/check_source.py` for bounded static evidence only: `python3 runtime/check_source.py page.html` checks one HTML file, and adding `--candidate edited.html` compares the candidate's bytes with the source. Run rendered, copy and native evidence separately when available. The scenarios in `fixtures/acceptance.json` are examples, not proven passes.
7. Report observed results with `schemas/report.schema.json`, listing unverified checks explicitly. In an audit, never edit the target files.

Package creation does not check provider import, real host invocation or native-language certification.
