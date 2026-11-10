# Citations, Evidence, Figures, Tables, Equations, and Quantitative Consistency

## General rule

Scholarly objects are part of the argument, not decoration. Review their semantic relation to the prose and their technical integrity. Never “fix” a mismatch by changing a number, equation, or citation without verifying the authoritative source.

## Citations and bibliography

### Citation need

Flag claims that plausibly require support:

- non-common factual assertions;
- definitions attributed to a field or authority;
- prior-method descriptions;
- prevalence, historical, performance, or comparative claims;
- borrowed theory, instrument, dataset, algorithm, or scale;
- direct quotations and translated quotations;
- claims of novelty or absence of prior work.

Do not add a fabricated or merely plausible citation. State the claim that needs support.

### Citation fit

When sources are available, verify:

- entailment: the source supports the actual proposition;
- scope: population, setting, method, period, and outcome match;
- attribution: the correct authors/source are named;
- polarity: supporting versus contradicting evidence is not reversed;
- primary/secondary status is represented accurately;
- quotation wording and page/location are correct;
- retracted/corrected/superseded status when material;
- translation is faithful and marked according to policy.

### Citation placement

A citation should attach unambiguously to the claim it supports. Flag citations placed after a paragraph containing several unrelated claims, or citation clusters whose mapping cannot be recovered.

Do not impose one citation macro/style universally. Follow the venue, bibliography package, and project profile.

### Bibliographic integrity

Check:

- duplicate keys and duplicate works under different keys;
- missing required fields;
- inconsistent author/name encoding;
- incorrect year, title, venue, volume, pages, DOI, URL;
- title capitalization/protection in BibTeX/Biber;
- Persian/Arabic script direction and sorting;
- cited-but-missing and uncited entries, according to policy;
- exact matching between in-text names/year and bibliography;
- bibliography style compliance.

Automated metadata lookup may propose corrections but must not overwrite verified records silently.

## Figures

A figure should have a clear argumentative purpose and be interpretable with its caption plus necessary context.

Review:

- first in-text reference precedes or appropriately accompanies the figure;
- reference order and numbering;
- caption identifies what is shown, conditions, groups, abbreviations, and uncertainty where needed;
- axes, units, scales, legends, sample sizes, and error bars;
- colors/patterns remain distinguishable and accessible;
- panel labels agree with prose (`الف`, `ب` or `a`, `b` per policy);
- image resolution and legibility at final size;
- no screenshot artifacts, placeholder text, or confidential data;
- source/permission/attribution when reused or adapted;
- consistency between figure values and prose/tables;
- no causal implication created by visual design;
- alt text or accessibility description when required.

Do not require every caption to reproduce the entire method. “Self-contained” means sufficient for correct interpretation, not maximal length.

## Tables

Use a table when structured comparison or exact values are more readable than prose. Review:

- descriptive title/caption;
- row/column headings with units;
- definition of abbreviations and symbols;
- consistent decimal precision justified by measurement;
- denominators and sample sizes;
- missing-value notation;
- totals and percentages;
- statistical markers and footnotes;
- alignment and RTL/LTR readability;
- explicit identification of best/baseline values without misleading emphasis;
- no duplicate information unless repetition serves a clear reading need;
- values match prose, figures, appendices, and source output.

A mathematically correct table can still mislead through selected denominators, truncated comparisons, or unexplained exclusions.

## Equations and mathematical notation

Check each displayed equation for:

- introduction before use;
- grammatical integration into the sentence;
- punctuation after the display when required by sentence syntax;
- equation number and reference consistency;
- definition of every nonstandard symbol;
- domains, dimensions, indices, and units;
- distinction among scalar, vector, matrix, set, random variable, estimate, and realization;
- consistent bold/italic/roman conventions;
- no symbol overload or silent redefinition;
- assumptions and boundary conditions;
- consistency between equation, algorithm, implementation description, and results.

Do not edit mathematical expressions as prose. A suspected mathematical correction is `SCIENTIFIC/MEANING-SENSITIVE` or `BLOCKER` and requires verification.

## Algorithms, pseudocode, and code listings

Review:

- inputs, outputs, initialization, termination;
- variable names matching equations/prose;
- deterministic versus stochastic steps;
- indexing boundaries;
- random seed and sampling;
- undefined helper procedures;
- complexity claims;
- line references and caption;
- syntax highlighting/direction for mixed text;
- licensing or attribution for adapted code.

Do not “clean up” pseudocode into a different algorithm.

## Units, quantities, and numerical style

Apply the project’s unit standard and digit policy. Check:

- number and unit separated appropriately;
- SI symbols and capitalization;
- nonbreaking spacing in TeX where needed;
- decimal separator and thousands grouping;
- ranges and negative signs;
- percentage denominator;
- significant figures/measurement precision;
- consistent unit conversion;
- exact versus approximate equality;
- `p`, confidence/credible interval, standard deviation/error, and effect-size notation;
- no mixed Persian/Latin digits inside one quantity.

Do not convert technical notation or official identifiers merely to match prose digits.

## Quantitative consistency pass

Build a ledger for important values:

| Quantity | Definition | Source of truth | Abstract | Main text | Table/Figure | Conclusion |
|---|---|---|---|---|---|---|

Compare:

- sample counts before/after exclusions;
- train/validation/test sizes;
- percentages and denominators;
- metric values and direction;
- confidence intervals;
- baseline and proposed-method labels;
- number of experiments/runs/seeds;
- model parameters/hyperparameters;
- dates and study duration;
- units and conversion factors.

Flag rounding differences only when they are inconsistent, misleading, or outside the declared precision.

## Statistical reporting integrity

Depending on the analysis, check:

- assumptions and diagnostics;
- exact model/test;
- estimate and uncertainty;
- sample size and missingness;
- multiplicity;
- preregistered versus exploratory status;
- model selection and tuning leakage;
- effect-size interpretation;
- practical threshold;
- robustness/sensitivity;
- uncertainty across random seeds/runs;
- distinction between standard deviation, standard error, and confidence interval.

Do not infer “no effect” solely from a non-significant p-value. Do not infer equivalence without an equivalence/non-inferiority design or appropriate interval argument.

## Cross-reference integrity

For every figure, table, equation, appendix, theorem, algorithm, and section:

- label exists and is unique;
- reference resolves;
- object type is correct;
- numbering/order agrees with visible output;
- referenced content actually supports the sentence;
- subfigure/subtable references identify the correct panel;
- capitalization and Persian object term follow project style.

An unreferenced object is not automatically critical: appendices, required forms, or self-contained supplementary items may be legitimate. Classify by purpose and venue rule.

## Captions and prose relationship

The prose should answer “why this object matters”; the caption should answer “what exactly is shown and how to read it.” Flag:

- prose that merely says “Figure 4 shows the results”;
- caption that asserts an interpretation absent from evidence;
- method details split inconsistently between caption and text;
- abbreviations defined only in one location when the other must be standalone;
- visual labels not mentioned in the caption;
- contradictory naming between caption and text.

## Severity guidance

- `BLOCKER`: incorrect/fabricated citation, central value contradiction, unresolved required reference, equation/notation error that changes the method.
- `MAJOR`: unsupported claim, misleading figure/table, missing denominator, substantial citation-scope mismatch.
- `MINOR`: local caption ambiguity, formatting inconsistency, recoverable unit/label issue.
- `STYLE`: optional presentation improvement with no interpretive effect.
