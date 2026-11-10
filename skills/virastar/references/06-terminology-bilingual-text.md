# Terminology, Bilingual Text, and Academic Translation

Contents: Terminology is a controlled system; TOML terminology register; Choosing a Persian technical term; Concept consistency, not string consistency alone; First-use policy; Acronyms and abbreviations; Names, titles, and transliteration; Mixed-direction text; Translation modes; Literalness versus naturalness; English-source hazards; Persian-to-English back-check; Terminology consistency report; Glossary and index integration; Editing safety.

## Terminology is a controlled system

A technical manuscript should not vary terminology merely to avoid repetition. Establish a terminology register and use one preferred Persian form for one concept unless the manuscript intentionally distinguishes senses.

Each entry should record:

- concept ID;
- preferred Persian term;
- accepted variant(s);
- rejected/confusable variant(s);
- English/source-language term;
- acronym;
- definition or disambiguation note;
- first-use form;
- domain and source/authority;
- grammatical behavior (plural, ezafe, derived adjective/verb);
- capitalization/spelling for Latin text;
- status: proposed, approved, deprecated.

The register controls the manuscript after author/supervisor approval.

## TOML terminology register

Store project terminology in a schema-versioned TOML document with `[glossary]` metadata and `[[entries]]` records. Use a stable `id`; default `concept_id` to the same value. Require `english`, `persian`, and `status`. Use arrays—not delimiter-packed strings—for variants and notes.

```toml
[glossary]
schema_version = 1
name = "Thesis terminology"

[[entries]]
id = "signed_kl_policy_guidance"
concept_id = "signed_kl_policy_guidance"
english = "signed-KL policy guidance"
persian = "هدایت سیاستیِ KL علامت‌دار"
preferred_fa = "هدایت سیاستیِ KL علامت‌دار"
acronym = "KL"
accepted_variants = ["هدایت KL علامت‌دار", "همجوشی علامت‌دار"]
rejected_variants = ["وزن استقرار منفی"]
notes = ["A negative signed coefficient is not a negative deployment weight."]
status = "approved"
```

The loader also accepts optional definition, first-use, authority, grammatical-behavior, capitalization, category, plural-English, definition-reference, alias, and source-page fields. Use `status = "reference"` for an attributed source that offers candidates without establishing a project preference. A custom exact English match overrides bundled reference entries; absent that match, the lookup tool may return the bundled candidates with their source and status.

## Choosing a Persian technical term

Use this decision order:

1. project-approved term or glossary;
2. controlling institution/venue terminology;
3. established disciplinary usage;
4. Academy-approved equivalent, assessed against current field usage;
5. transparent translation or transliteration with a definition;
6. source-language term when translation would reduce precision or recognizability.

Avoid automatic linguistic purism. Also avoid unnecessary English when a precise, established Persian term exists.

## Concept consistency, not string consistency alone

The same English word can denote different concepts, and different English phrases can denote one concept. Audit semantic mapping, not only token counts.

Examples requiring explicit decisions:

- `accuracy`: دقت طبقه‌بندی, صحت, accuracy of measurement;
- `precision`: precision metric vs measurement precision;
- `policy`: سیاست in governance vs خط‌مشی/سیاست in reinforcement learning;
- `model`: statistical model, conceptual model, software model;
- `significant`: statistically significant vs important.

Do not globally replace a string without sense disambiguation.

## First-use policy

Follow the project profile. Common defensible patterns include:

- Persian term followed by English term in parentheses;
- Persian term with English term in a footnote;
- English term followed by Persian definition when the English form is dominant;
- acronym introduced after the full Persian and/or English name.

Example pattern:

`مدل مارکوف پنهان (Hidden Markov Model; HMM)`

Do not repeat the English equivalent at every occurrence. Do not introduce an acronym that is never reused.

## Acronyms and abbreviations

Check:

- definition at first substantive use in abstract and main text as required;
- one expansion per acronym;
- collision between acronyms;
- Persian and English abstract consistency;
- plural/possessive treatment of Latin acronyms;
- correct LTR rendering;
- glossary/acronym-list alignment;
- no acronym in a title unless standard and permitted.

Acronyms often need separate first-use handling in abstract, main text, figure captions, or supplementary material because these may be read independently.

## Names, titles, and transliteration

Preserve authoritative spellings for:

- author names;
- organizations;
- software, model, dataset, and benchmark names;
- standards;
- product names;
- titles of cited works.

Do not transliterate a proper name inconsistently. Record the chosen Persian form and exact Latin form. When uncertainty affects identity or citation retrieval, leave the Latin form visible.

Distinguish:

- translation of a generic descriptor;
- transliteration of a proper name;
- official localized name;
- author-provided spelling.

## Mixed-direction text

In source files, protect Latin spans using the project’s approved mechanism, for example XePersian commands such as `\lr{...}` or semantic macros. Do not insert manual spaces or bidirectional override characters merely to make one editor view look correct.

Inspect:

- parentheses around Latin terms;
- punctuation at RTL/LTR boundaries;
- model names with hyphens/slashes;
- ranges, signs, and percentages;
- citations adjacent to Latin text;
- code and command-line fragments;
- English title pages and abstracts.

Visual order in a source editor is not reliable evidence of stored character order. Verify rendered output.

## Translation modes

### Faithful academic translation into Persian

Preserve:

- propositions and logical relations;
- claim strength and uncertainty;
- negation and quantifier scope;
- actor/agency;
- chronology and tense/aspect where semantically relevant;
- definitions and distinctions;
- numbers, units, symbols, equations, citations, references, and labels;
- paragraph/section function;
- quotation status.

Naturalize syntax only after these invariants are secured.

### Translation audit

Compare source and target by units, not only sentences. Build an alignment table with:

- source span;
- Persian span;
- status: equivalent, omission, addition, mistranslation, scope drift, term drift, citation/number drift;
- severity and confidence;
- proposed repair.

Pay special attention to:

- hedges (`may`, `might`, `likely`, `suggest`);
- exclusives and focus (`only`, `primarily`);
- comparatives and baselines;
- conditionals and exceptions;
- causal versus associative language;
- statistical terms;
- deontic language (`must`, `should`, `recommended`);
- negative results;
- antecedents of pronouns;
- passive-agent ambiguity.

## Literalness versus naturalness

A faithful translation is not necessarily word-for-word. Use this priority:

1. scientific and logical equivalence;
2. terminology equivalence;
3. rhetorical function;
4. natural Persian syntax and register;
5. surface resemblance.

When naturalization requires choosing among source ambiguities, report the ambiguity instead of silently resolving it.

## English-source hazards

Review literal renderings of:

- noun stacks;
- participial modifiers;
- dummy subjects (`it is ...`);
- passive chains;
- broad verbs (`address`, `capture`, `leverage`, `support`);
- discourse markers (`however`, `therefore`, `indeed`);
- `respectively`;
- article-based definiteness;
- modal perfects;
- scope of `not`, `only`, and `all`;
- slash constructions and hyphenated compounds.

The Persian repair must be based on the intended relation, not a one-to-one dictionary substitution.

## Persian-to-English back-check

For high-risk translated passages, create a compact semantic back-check rather than stylistic back-translation:

- claim;
- subject/agent;
- relation/action;
- object/outcome;
- comparison;
- condition;
- uncertainty;
- evidence/citation.

Any mismatch is a translation issue even when the Persian reads fluently.

## Terminology consistency report

Useful report columns:

| Concept | Preferred | Observed variants | Locations | Decision | Risk |
|---|---|---|---|---|---|

Classify variants as:

- legitimate sense distinction;
- first-use form;
- abbreviation;
- inflected/derived form;
- inconsistent synonym;
- mistranslation;
- spelling/Unicode variant.

Do not count legitimate morphology as inconsistency.

## Glossary and index integration

For LaTeX projects, check:

- glossary key exists;
- displayed Persian and English forms match the register;
- first use expands the term as intended;
- plural forms render correctly;
- glossary entries are actually used;
- unused/duplicate keys are reported;
- sorting/transliteration configuration is reproducible;
- manual term text has not drifted from macro output.

## Editing safety

Treat term replacement as `MEANING-SENSITIVE` unless the mapping is one-to-one and project-approved. Never perform a global replacement across:

- citation keys;
- labels;
- macro names;
- URLs/DOIs;
- code;
- quoted source text;
- bibliography titles;
- equations or variable names.
