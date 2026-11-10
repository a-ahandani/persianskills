---
name: persian-book-translation
description: >-
  Translate a whole book or long literary text into Persian with a
  consistent voice: a style sheet and name glossary before the first
  chapter, chapter-by-chapter passes, narration vs dialogue register,
  poetry and wordplay, footnotes, and a final consistency sweep. Includes
  RTL EPUB basics (page direction, lang, Sahel font, ZWNJ). Use for novels,
  non-fiction books, long-form essays or any multi-chapter translation into
  Persian, or when the user wants a Persian EPUB.
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/edyt-app/persianskills
  version: 0.1.0
  inspired-by: m4tinbeigi-official/hermes-literary-translation-mastery (literary book translation and EPUB typesetting skills); written from scratch, no text copied
---

# Persian book translation

A book is translated hundreds of times over: once per sentence, and the
reader notices every place where the voice drifts. Consistency is the
work; decide it up front and check it at the end.

Load `persian-localization` for meaning-over-words, `persian-writing` for
orthography and documents, and `persian-translation-review` for the
review pass.

## Before chapter one

Write a style sheet the translator follows and updates:

1. **Audience and variety:** Iranian Persian unless the publisher says
   Dari or Tajik.
2. **Narration register:** literary standard (نوشتاری). Decide the past
   tense habits and whether to use «می‌بود»-style archaisms (usually not).
3. **Dialogue register:** spoken forms for speech («می‌رم», «نمی‌دونم»)
   or standard written forms. Pick one per book; mixed choices read as
   mistakes. Formality between characters (شما vs تو) follows their
   relationship and changes only when it changes in the story.
4. **Names glossary:** every person, place and invented term with one
   Persian spelling, decided on first appearance. Transliterate by sound,
   not letters (Joan → جوآن, not ژوآن, unless the name is French).
5. **Units, dates and money:** keep the original's (miles stay mile,
   dollars stay dollars); explain only where a reader would be lost.
6. **Footnotes:** when to use them (untranslatable wordplay, cultural
   references) and their format «ـ م.» for translator's notes.

## Per chapter

1. Read the whole chapter before translating it.
2. Translate by paragraph, keeping the paragraph and dialogue breaks.
3. Keep each character's voice: an uneducated narrator doesn't get
   polished Persian; a formal one doesn't slide into slang.
4. Idioms: find the Persian idiom with the same weight, or say it plainly.
   Never translate an idiom word for word.
5. Wordplay and poetry: translate the effect. If it can't carry over,
   translate the sense and add a short footnote.
6. Update the style sheet with every new name or decision.

## Final sweep

- Search each glossary name across the book for stray spellings.
- Check dialogue register and شما/تو for each main character.
- Run the review checklist from `persian-translation-review` on a sample
  of each chapter, and on every passage that changed late.
- Run `persian-writing`'s linter in report mode; fix ZWNJ and punctuation.

## RTL EPUB basics

- `<html lang="fa" dir="rtl">` on every XHTML file, and in the OPF:
  `<spine page-progression-direction="rtl">` and `<dc:language>fa</dc:language>`.
- Embed the font (EPUB readers often lack Persian fonts). Use Sahel
  (SIL OFL, github.com/rastikerdar/sahel-font): body in Sahel 400, headings
  in Sahel 700 or 900; declare `@font-face` with the embedded files.
- Keep real ZWNJ characters; some conversion tools strip them. Check a
  sample with a search for «می» followed by a space.
- `text-align: justify` needs `text-justify: inter-word` or Persian
  readers see uneven gaps; never add tatweel (ـ) to justify.
- Validate with epubcheck before handing over.

## Handover

Give the publisher the translated text, the style sheet with the names
glossary, the list of footnotes and open questions, and a note on which
parts a native editor should read first.
