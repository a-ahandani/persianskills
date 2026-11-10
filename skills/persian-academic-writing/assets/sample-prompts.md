# Sample Prompts

## Full thesis audit

```text
Use persian-academic-writing in workspace-audit mode on main.tex.
Read all recursive inputs, bibliography and glossary files, the project profile,
and the compiled PDF. Do not edit. Report workspace, orthography, grammar,
terminology, scientific-claim, structure, citation, figure/table/equation, and
rendered-output findings with stable IDs. Separate current institutional rules
from Academy rules and editorial preferences.
```

## One chapter, report first

```text
Audit chapters/03-methodology.tex in context of the full thesis. Focus on
reproducibility, methodological rationale, terminology, Persian syntax, units,
notation, and claim strength. Do not rewrite or change files. Quote only the
minimum span needed for each issue.
```

## Apply selected findings

```text
Apply ORTH-001..ORTH-018, UNI-003, and TERM-006. Do not apply STYLE findings.
Re-read each target first, skip stale findings, preserve citations/macros, build
the thesis, and report the exact changes and remaining errors.
```

## English-to-Persian scholarly translation

```text
Translate this section into formal academic Persian. Preserve every proposition,
hedge, negation, comparison, number, symbol, equation, citation, and limitation.
Follow editorial/terminology-register.toml. Naturalize English syntax without
strengthening claims. List unresolved source ambiguities after the translation.
```

## Bilingual equivalence audit

```text
Compare thesis-en/04-results.tex with thesis-fa/04-results.tex. Align by claim,
not by sentence count. Report omissions, additions, mistranslations, modality or
causality drift, terminology drift, and number/citation mismatches. Do not edit.
```

## Scientific-claim audit only

```text
Review the abstract, results, discussion, and conclusion for causal overreach,
misuse of statistical significance, vague superiority, unsupported novelty,
generalization beyond the data, and inconsistent metrics. Ignore minor style
unless it changes interpretation.
```

## University of Tehran project

```text
Use the University of Tehran overlay. Treat the current Aban 1403 university
guide and faculty supplement as submission authority. Use sinamomken/tehran-thesis
only for useful chapter-function, glossary, and modular XePersian patterns—not
for old page counts, fixed structure, or formatting rules.
```

## Final QC

```text
Run final-qc. Build from the documented command, inspect the compiled PDF,
verify title/abstract/introduction/conclusion alignment, principal values,
citations, glossary, references, figures, tables, equations, RTL/LTR rendering,
fonts, floats, and draft residue. Do not claim submission readiness while any
BLOCKER remains.
```
