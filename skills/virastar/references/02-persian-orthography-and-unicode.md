# Persian Orthography, Unicode, and Punctuation

Contents: Scope and authority; Character normalization; Three spacing states; High-confidence morpheme rules; Compounds; Ezafe; Diacritics, hamza, and tashdid; Punctuation policy; Digits and mixed-script text; Quotations and foreign text; Automation boundary.

## Scope and authority

The Academy’s *Dastur-e Xatt-e Fārsi* is the primary general authority for Persian orthography and spelling. Its own scope is important:

- it regulates obligatory spelling and spacing cases;
- it deliberately leaves many compound-writing choices to lexical convention and writer/editor judgment;
- it does not by itself settle the whole of punctuation, Persian rendering of foreign words, or transliteration.

Therefore, classify rules as:

- `obligatory/academy-backed`;
- `lexical—consult spelling dictionary`;
- `project/house style`;
- `context-dependent`.

## Character normalization

### Persian and Arabic code points

In Persian prose, prefer:

- Persian Yeh `ی` (U+06CC), not Arabic Yeh `ي` (U+064A);
- Persian Kaf `ک` (U+06A9), not Arabic Kaf `ك` (U+0643).

Exceptions:

- faithful Arabic quotations;
- exact bibliographic titles or names whose source spelling must be preserved;
- code, identifiers, URLs, citation keys, and data fields.

Do not normalize protected technical spans blindly.

### Hidden controls

Flag:

- repeated ZWNJ;
- ZWNJ next to ordinary whitespace or punctuation where it cannot join morphemes;
- stray ZWJ;
- directional overrides/embeddings inserted into source text;
- tatweel/kashida used as manual justification.

Bidirectional controls may be legitimate in rare technical contexts; report their code point and surrounding span before removing them.

## Three spacing states

Persian digital text distinguishes:

1. full word space;
2. ZWNJ/half-space between morphemes whose visual joining must be interrupted;
3. no inserted character when a naturally non-joining letter already creates the required visual separation.

Do not confuse a visual gap with an ordinary space.

## High-confidence morpheme rules

### Verbal prefixes `می‌` and `نمی‌`

Use ZWNJ between the prefix and verb stem:

- `می‌رود`
- `نمی‌دانیم`
- `می‌تواند`

Do not change the noun `می` or unrelated words beginning with `می` by regex alone.

### Negative prefix `بی‌`

The negative/privative prefix normally takes ZWNJ or the equivalent no-space behavior required by letter joining:

- `بی‌توجه`
- `بی‌نتیجه`

But independent prepositional `بی` takes a full space, and lexicalized exceptions exist. Diagnose the grammatical role before editing.

### Compound-forming `هم‌`

Compound-forming `هم‌` generally follows compound spacing rules, but many lexicalized words have established joined spellings. Independent `هم` remains a separate word. Consult the Academy spelling dictionary or project register rather than auto-rewriting every `هم` sequence.

### Comparative and superlative `تر/ترین`

Use ZWNJ or the natural no-space equivalent with the preceding word, except lexicalized forms such as established joined spellings. Do not alter a sequence without confirming that `تر` is a suffix rather than an independent token or part of a name.

### Plural `ها`

Academy guidance recognizes more than one written realization in some contexts and recommends the separated/ZWNJ form for educational and text-processing reasons. Some contexts require separation. Project policy should choose a consistent default, but an attached form is not automatically a grammatical error.

Safe editorial default when the institution is silent:

- prefer `کتاب‌ها`, `داده‌ها`, `روش‌ها`;
- report attached forms as consistency candidates rather than universally wrong;
- require ZWNJ where lexical shape, foreign words, proper names, or readability make separation necessary.

## Compounds

There is no defensible rule that “all compounds take ZWNJ.” Use this decision process:

1. Is the form explicitly covered by an Academy rule?
2. Is it listed in the Academy spelling dictionary?
3. Is it a fixed discipline term in the project register?
4. Is one form overwhelmingly established in the field and linguistically defensible?
5. If more than one form remains possible, select and record house style rather than call alternatives incorrect.

Avoid aggressive cleanup tools that split or join compounds without lexical context.

## Ezafe

Ezafe is usually not written after ordinary consonant-final words. After final silent `ه`, digital Persian permits competing editorial forms in practice. The manuscript must follow the controlling institution/project choice consistently, for example:

- `خانهٔ پژوهشگر`
- `خانۀ پژوهشگر`
- `خانه‌ی پژوهشگر`

Do not normalize among these until the profile establishes the accepted form. Do not use a plain Latin apostrophe or a detached Arabic hamza as a substitute.

## Diacritics, hamza, and tashdid

- Use vowel marks and tashdid only when required by the controlling guide or when they prevent ambiguity/misreading.
- Do not fully vocalize ordinary academic prose.
- For lexical hamza and Arabic-origin spelling, consult an authoritative spelling dictionary; do not “simplify” by sound alone.
- Preserve exact forms in names, quotations, and source titles when bibliographic fidelity controls.

## Punctuation policy

Punctuation is an editorial/typographic layer, not fully determined by the Academy orthography guide.

In Persian prose, normally use:

- comma `،`;
- semicolon `؛`;
- question mark `؟`;
- guillemets `«…»` for ordinary quotations, unless the project specifies another system.

Spacing:

- no ordinary space before comma, semicolon, colon, question mark, exclamation mark, or full stop;
- normally one space after sentence/internal punctuation;
- no spaces immediately inside parentheses or guillemets;
- punctuation belongs to the sentence, so place it relative to citations, equations, and parentheses according to grammar—not merely visual direction.

Exceptions include decimal markers, file names, code, URLs, DOI strings, version numbers, bibliographic conventions, and mathematical notation.

## Digits and mixed-script text

Do not enforce “Persian text means Persian digits everywhere.” Use profile/context:

- prose, dates, and ordinary counts may use Persian digits when required;
- equations, variables, source code, commands, identifiers, model names, dataset names, versions, URLs, DOI/ISBN strings, and official Latin titles normally preserve Latin forms;
- never mix digit scripts inside one number;
- keep decimal separators, thousands grouping, signs, units, and ranges internally consistent;
- inspect RTL rendering, because a semantically correct sequence may display confusingly.

## Quotations and foreign text

- Preserve quotation language and spelling unless the task includes editing the quotation itself.
- Distinguish direct quotation, translated quotation, and paraphrase.
- Do not silently modernize quoted historical spelling.
- Put Latin technical spans in an appropriate LTR mechanism in TeX/HTML; visual direction must not alter the stored characters.

## Automation boundary

Safe automatic candidates:

- Persian/Arabic Yeh and Kaf normalization in unprotected Persian prose;
- tatweel removal;
- repeated malformed ZWNJ cleanup;
- obvious whitespace corruption.

Require human/model judgment for:

- compounds;
- `بی`, `هم`, `تر/ترین`, and plural `ها` beyond high-confidence contexts;
- ezafe form;
- punctuation around equations/citations;
- digit conversion;
- transliteration and technical term replacement.
