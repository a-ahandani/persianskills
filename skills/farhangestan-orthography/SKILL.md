---
name: farhangestan-orthography
description: >-
  Copyedit Persian spelling and spacing by the Academy of Persian Language and
  Literature's official «دستور خطّ فارسی» (new edition, 1401), with the book's
  page for every rule: full space vs ZWNJ vs joined, «می‌، ها، تر، به، بی، هم،
  که، را، چه», «است» and attached pronouns, ezafe «هٔ», indefinite «ای» and
  «گی», hamza seats (مسئله، رئیس، سؤال), tanvin, ة and alef maqsura, compound
  words, compound prepositions and conjunctions, and the Academy's preferred
  forms for words with two spellings (اتاق، بلیت، زغال). Use when copyediting
  Persian for publication, applying or checking a style sheet, or when the
  user mentions فرهنگستان، دستور خط، رسم‌الخط، نیم‌فاصله، جدانویسی، پیوسته‌نویسی
  or شیوه‌نامه.
license: MIT
metadata:
  author: persianskills (Edyt)
  source: https://github.com/edyt-app/persianskills
  version: 1.0.0
  based-on: "فرهنگستان زبان و ادب فارسی، «دستور خطّ فارسی (ویراست جدید)»، چاپ اوّل ۱۴۰۱، ISBN 978-622-5305-22-9"
  based-on-url: https://apll.ir/wp-content/uploads/2023/07/Dastour-e-Khat-17.04.1402.pdf
---

# Farhangestan orthography

This skill applies the spelling rules of the Academy of Persian Language and
Literature (فرهنگستان زبان و ادب فارسی) as published in «دستور خطّ فارسی»,
new edition (چاپ اوّل ۱۴۰۱; PDF dated 17.04.1402). Every rule here is
summarized in our own words and cites the book's page. The book is copyrighted
by the Academy, so its text and full word lists are not copied here; read the
official PDF for the exact wording:
https://apll.ir/wp-content/uploads/2023/07/Dastour-e-Khat-17.04.1402.pdf

Load `persian-writing` for prose style and the cleanup scripts. This skill
decides spelling and spacing.

## Which file to read

| Question | File | Book pages |
|---|---|---|
| Spacing types, joining letters, letters and signs | `references/principles-and-letters.md` | 7–33 |
| را، که، چه، این، هر، هیچ، به، بی، می، هم، تر، ها؛ است، pronouns, «ای»، «گی»، ezafe | `references/words-and-affixes.md` | 34–48 |
| Hamza, ة، و as ā, alef maqsura, tanvin, tashdid, vowel marks | `references/hamza-and-arabic.md` | 48–57 |
| Compound words, numbers, compound prepositions and conjunctions | `references/compounds-and-spacing.md` | 58–71 |
| Words with two or more spellings | `references/multi-spelling-words.md` | 72–85 |

## The three spacing outcomes (pp. 22–23)

Every joining question ends in one of three outcomes:

- **Full space:** between independent words («این کتاب»، «کتاب را»).
- **Apart:** the parts touch with no space. After a joining letter put a ZWNJ
  (U+200C, «نیم‌فاصله»): «می‌رود»، «کتاب‌ها»، «هم‌وطن». After a non-joining letter
  (ا د ذ ر ز ژ و, or a silent final ه) nothing is needed («بی‌فاصله»):
  «هوادار»، «پرفروش». In Unicode a silent ه still joins, so «خانه‌ها» and
  «خسته‌ام» need the ZWNJ.
- **Joined:** one word with no ZWNJ: «آنچه»، «بلکه»، «پیشرفت»، «کتابخانه».

## Rules that cover most edits

| Case | Write | Page |
|---|---|---|
| «می» and «همی» before a verb | «می‌رود»، «می‌افکند» | 39 |
| «را» | separate word: «کتاب را»; only «چرا»، «مرا» joined | 35 |
| «که» after a word | «چنان‌که»، «چون‌که»; joined only «آنکه»، «اینکه»، «بلکه» | 35 |
| «اینکه» vs «این‌که» | conjunction joined; "this person who" with ZWNJ | 34 |
| «چه» before a word | space, except «چرا»، «چطور»، «چقدر»، «چگونه» | 34 |
| «به» | preposition and phrasal verbs: space («به خانه»، «به کار بردن»); adverbs and compound prepositions: ZWNJ («به‌سختی»، «به‌وسیلهٔ»); verbs: joined («بروم») | 38 |
| «بی» | «بی‌تردید»; 11 joined words («بیکار»، «بیچاره»، «بیزار»…) | 39 |
| «هم» | «هم‌وطن»; 32 joined words («همکار»، «همسایه»، «همراه»…) | 40 |
| «-تر»، «-ترین» | «بزرگ‌تر»، «بزرگ‌ترین»; joined «بهتر، بیشتر، کمتر، کهتر، مهتر» | 40 |
| «-ها» | apart recommended; required after silent ه, foreign words, names, many-tooth words, consonantal ی | 40–41 |
| «است» | separate after a consonant or silent ه («خسته است»); short «ست» only after ا، و، vowel ی | 42–43 |
| pronouns after silent ه | «خانه‌ام، خانه‌ات، خانه‌اش» but «خانه‌مان، خانه‌تان، خانه‌شان» | 44–45 |
| indefinite vs relational «ی» | «خانه‌ای» (a house) vs «خانگی» (domestic) | 46 |
| ezafe after silent ه | «خانهٔ او» | 47 |
| hamza | «مسئله»، «جرئت»، «هیئت»، «مسئول»، «سؤال»، «رئیس»، «تئاتر»; «توأم» | 49–53 |
| «رییس، ارایه، جزیی، قرایت» | wrong; write «رئیس، ارائه، جزئی، قرائت» | 42 |
| final ā + ء | «انشاء/ انشا» both correct; ezafe «اعضای بدن» | 51 |
| tanvin | always «ـاً»: «واقعاً»، «جزئاً»، «نسبتاً» | 56 |
| prefixes | non-joining end: no space («بازآفرینی»، «فرایند»); joining end: ZWNJ («برون‌مرزی»، «تک‌درس») | 36–37 |
| compound verbs | space before the light verb («تصمیم گرفتن»); derived words apart («تصمیم‌گیری»); nouns joined («پیشرفت») | 67–68 |
| compound prepositions | «براساسِ»، «به‌وسیلهٔ»، «علاوه‌بر»، «پیش‌از»; three parts spaced: «با توجّه به» | 69–70 |
| compound conjunctions | «درحالی‌که»، «ازآنجاکه»، «بنابراین»; «به‌طوری که» | 70–71 |
| numbers | «چهارصد»، «دوهزار»; «بیست و یک»; «یک‌چهارم»; «سی‌سالگی» | 65–66 |
| two-spelling words | look up pp. 73–85: «اتاق»، «بلیت»، «زغال»، «طومار»، «غدغن» | 72–85 |

## Workflow

1. **Agree the scope.** These rules are for prose. Leave Quranic verses,
   quoted Arabic, poetry, old texts and quotations in their original spelling
   (pp. 13, 21, 72). If the publication has its own style sheet, it wins where
   it differs, and say so.
2. **Fix the required rules everywhere.** Use the table above and the
   reference files. Each rule's status is marked REQUIRED, BOTH ALLOWED or
   PREFERRED.
3. **Leave both-allowed forms alone,** or make them consistent within the
   document if the user wants that: «کتابها/ کتاب‌ها»، «انشاء/ انشا»،
   «یکصد/ یک‌صد»، «آمریکا/ امریکا».
4. **Decide by meaning where the book does:** «اینکه/ این‌که»، «بجا»، «بیخود»،
   «کلانتر»، «تاق/ طاق»، «تراز/ طراز»، «حکومتِ نظامی/ حکومت‌نظامی».
5. **Don't invent rules.** A compound the book doesn't list is not settled by
   it (p. 58), and a two-spelling word that isn't listed keeps its spelling.
   Flag it instead of correcting it.
6. **Report by rule, not by edit:**

   ```
   «می» + verb, ZWNJ (ص ۳۹): ۱۸ مورد
   همزه: مسأله ← مسئله، هیأت ← هیئت (ص ۴۹–۵۰): ۴ مورد
   «را» جدا (ص ۳۵): ۷ مورد
   چنداملایی: بلیط ← بلیت (ص ۷۴): ۲ مورد
   به تشخیص نویسنده: «اینکه/ این‌که» در بند ۳ (ص ۳۴)
   ```

## Accuracy notes

- Examples were transcribed from the page images because the PDF's text layer
  is broken. ZWNJ positions were judged from letter shapes; check against the
  official PDF if a case is disputed.
- Where these notes add an interpretation the book doesn't state, they say
  "our reading" or "our note".
- The edition matters: the first edition (1381) left most compound spacing to
  taste; this edition sets rules for it (p. 18).
