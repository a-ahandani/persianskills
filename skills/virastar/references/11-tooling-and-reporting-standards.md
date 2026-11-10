# Tooling and Discipline-Specific Reporting Standards

## Tools are detectors, not authorities

Persian NLP and normalization tools can accelerate candidate discovery, but their output is not automatically correct scholarly editing. They are optimized for different tasks: corpus normalization, tokenization, search, spell-checking, speech preprocessing, or generic prose—not preservation of quotations, terminology, equations, citation keys, and TeX semantics.

Useful tool families include:

- **Hazm** and similar Persian NLP toolkits: normalization, tokenization, lemmatization, POS/dependency analysis;
- **Virastyar** and related Persian proofreading libraries: spelling, punctuation, character standardization, morphology;
- **Parsivar**, ParsiNorm, ViraPart, and other research systems: preprocessing, ZWNJ, punctuation, ezafe, or task-specific normalization;
- lightweight Persian character/digit libraries in Python, JavaScript, PHP, and other ecosystems;
- Unicode-aware diff, grep, and code-point inspection tools;
- TeX build/log tools such as `latexmk`, Biber/BibTeX, xindy/makeindex, and PDF inspection.

Before integrating any tool, inspect its current version, license, model/data assumptions, normalization options, and maintenance status.

## Safe integration pattern

```text
read-only scan → candidate report → protected-span filtering → editorial review → approved patch → build/render verification
```

Do not run an aggressive normalizer in-place over a thesis repository.

At minimum protect:

- direct quotations and archival spelling;
- Arabic passages;
- equations and math environments;
- code/listings/verbatim;
- citations, labels, glossary keys, bibliography keys;
- URLs, DOIs, identifiers, file names;
- official product/model/dataset names;
- bibliography titles when source fidelity controls;
- custom macro definitions and generated files.

## Evaluating a normalizer or checker

Create a gold test set containing:

- correct and incorrect `می‌/نمی‌`, `ها`, `تر/ترین`, `بی`, and compounds;
- Arabic quotations beside Persian prose;
- mixed Persian/English technical terminology;
- TeX commands and math;
- citations, DOIs, paths, code, and version strings;
- alternative permitted ezafe and compound styles;
- statistical text and quantities;
- proper names;
- direct quotations;
- known false positives from the actual manuscript.

Measure separately:

- character-level precision/recall;
- word-boundary precision/recall;
- false changes to protected spans;
- semantic/terminological drift;
- reproducibility across versions;
- diff review burden.

For thesis editing, high precision and low semantic risk are normally more valuable than maximal recall.

## Unicode inspection

When an invisible-character issue is suspected, report:

- code point and Unicode name;
- neighboring characters;
- source file/line/column;
- whether it occurs in a protected span;
- rendered behavior;
- proposed semantic replacement.

Do not diagnose directionality from visual appearance alone. Use code-point inspection and the compiled PDF.

## TeX validation stack

Use the project’s own build first. Optional checks may include:

- `latexmk`/engine exit status and clean rebuild;
- log scanning for undefined references/citations, missing glyphs, overfull/underfull boxes, font substitution, and package errors;
- bibliography/glossary/index regeneration;
- `chktex` or similar syntax/style checks, with project-specific suppressions;
- asset existence and PDF font embedding checks;
- visual PDF comparison of changed pages.

A TeX linter’s style warning is not a Persian-language rule.

## Citation metadata tools

Crossref, DOI registries, publisher pages, library catalogs, and reference managers can help validate metadata. Use them to compare records, not to overwrite a verified bibliography automatically. Titles, author names, dates, corrections/retractions, and Persian transliterations need human verification.

## Reporting guidelines by study design

The general skill must load the reporting standard relevant to the research design when one exists. Examples include:

- randomized trials, observational studies, systematic reviews, diagnostic studies, qualitative research, case reports, animal research, and implementation studies;
- psychology/education measurement and statistical-reporting standards;
- engineering/CS venue author guides, reproducibility checklists, artifact policies, dataset/model documentation, and ethics statements.

Treat such standards as `DISCIPLINE` or `VENUE` authority. Do not apply a medical reporting checklist to an ML benchmark or an IEEE convention to every Persian thesis.

## Computer science and machine learning checks

For ML/AI work, consider current venue/project requirements for:

- data provenance, consent, licenses, and splits;
- leakage and preprocessing;
- baselines, tuning budgets, and fairness of comparison;
- random seeds, number of runs, aggregation, uncertainty;
- ablations and sensitivity;
- compute/hardware/software versions;
- hyperparameter and checkpoint selection;
- reproducibility code/data/model availability;
- limitations, risks, misuse, and societal impact;
- distinction between benchmark, simulation, prototype, and deployment claims.

These are scientific checks, not Persian copyediting, but the Persian prose must represent them accurately.

## Maintenance rule

Pin or record tool versions in the project profile/CI. When updating a normalizer or parser:

1. rerun the gold test set;
2. compare new false positives and changed outputs;
3. review license/model changes;
4. update suppressions and source audit;
5. do not silently change the manuscript’s established orthography.
