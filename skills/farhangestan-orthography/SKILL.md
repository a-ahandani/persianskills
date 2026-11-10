---
name: farhangestan-orthography
description: >-
  Copyedit Persian against the spelling rules of the Academy of Persian
  Language and Literature (فرهنگستان زبان و ادب فارسی, «دستور خط فارسی»):
  joined vs separate writing (می‌، ها، تر، ترین، به، ضمیرها), ezafe after
  silent ه, indefinite «ای» and «یی», hamza in Arabic loans, tanvin, and a
  house style sheet for the choices the Academy leaves open. Use when
  copyediting Persian for publication, setting a style guide for a magazine,
  site or company, or when the user mentions فرهنگستان, دستور خط, رسم‌الخط or
  شیوه‌نامه.
license: MIT
metadata:
  version: 0.1.0
  inspired-by: Byte-Magazine/skills (byte-virastari, a magazine house style based on the Academy's rules); written from scratch, no text copied
---

# Farhangestan orthography

The Academy's «دستور خط فارسی» is the standard reference for Persian
spelling in Iran. It fixes some rules and allows two forms for others;
for those, a publication picks one and writes it into its style sheet.

This is a working summary. For a disputed case, check the official text
on the Academy's site (apll.ir). Load `persian-writing` for ZWNJ
mechanics and the cleanup scripts.

## Fixed rules

| Rule | Write | Not |
|---|---|---|
| «می» and «همی» before verbs: separate, with ZWNJ | می‌روم، همی‌گفت | میروم، می روم |
| «ب» and negative «ن»، «م» on verbs: joined | بروم، نرفت، مرو | به روم، نه رفت |
| «تر» and «ترین»: separate, with ZWNJ | بزرگ‌تر، بزرگ‌ترین | بزرگتر |
| …except these, always joined | بهتر، بیشتر، کمتر، کهتر، مهتر | به‌تر، بیش‌تر |
| Plural «ها» after silent ه: separate | خانه‌ها | خانهها |
| Attached pronouns after silent ه | خانه‌ام، خانه‌ات، خانه‌اش، خانه‌مان | خانم، خانهام |
| Indefinite «ی» after silent ه | خانه‌ای | خانه‌یی، خانهء |
| Indefinite «ی» after «ا» and «و» | جایی، بازویی | جائی |
| Ezafe after «ا» and «و» | دانای راز، بازوی چپ | دانا راز |
| «است» after silent ه keeps its «ا» | خسته است | خسته‌ست |
| Persian «ی» and «ک», never Arabic «ي» and «ك» | یک، کتاب | يك، كتاب |

## Hamza and Arabic forms

- **Hamza on a seat** in common loans: مسئله، مسئول، رئیس، تأثیر، تأمین،
  مؤسسه، مؤلف. Don't drop it (مساله، تاثیر) in edited text.
- **Final hamza after «ا»** is dropped in Persian: املا، انشا، اجرا، اعضا
  (not املاء).
- **Tanvin** stays in the adverbs readers know: فوراً، تقریباً، اتفاقاً،
  نسبتاً.
- **Arabic «ة»** becomes «ه» or «ت» as the Persian word is spelled:
  رحمت، نتیجه.

## Choices to fix in a style sheet

The Academy allows both forms for these. Pick one, write it down, apply
it everywhere.

| Choice | Option A | Option B |
|---|---|---|
| Plural «ها» after a joining letter | کتاب‌ها (ZWNJ, most common) | کتابها |
| Ezafe after silent ه | خانهٔ من (Academy form) | خانه‌ی من (safest in UI fonts) |
| Common compounds | کتاب‌خانه، دانش‌گاه | کتابخانه، دانشگاه |
| «این» / «آن» compounds | این که، آن چه | اینکه، آنچه |
| Digits in running text | ۱۴۰۵ | 1405 (technical text only) |

## Copyediting procedure

1. Agree the style sheet first (the table above plus product names and
   terms). If the publication has one, follow it over this skill.
2. Fix the fixed rules everywhere without asking.
3. Apply the style sheet choices; don't flip a choice the author made
   consistently unless the style sheet says so.
4. Leave quotations, names, titles of works and poetry in their original
   spelling.
5. Report counts per rule so the author sees the pattern, not 200
   separate edits.

## Sources

- فرهنگستان زبان و ادب فارسی، «دستور خط فارسی»: https://apll.ir
