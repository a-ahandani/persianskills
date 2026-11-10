# Thesis and Paper Structure

Contents: Principle: function before template; Traceability backbone; Title; Abstract; Introduction; Literature review / related work; Conceptual/theoretical framework; Methodology / materials and methods; Results; Discussion; Conclusion; Recommendations; Appendices and supplementary material; Paragraph and section architecture; Engineering and computer-science adaptation; Structural issue severity.

## Principle: function before template

A thesis or paper is not correct merely because it has conventional chapter names. Review whether each part performs its rhetorical and scientific function. Institution or venue rules control required order, front matter, length, and naming.

Do not universalize:

- a fixed five-chapter thesis;
- fixed page counts;
- a mandatory number of research questions or contributions;
- venue-specific abstract formulas;
- a requirement that literature be from only a particular recent time window.

Older templates are useful scaffolds, not current institutional authority.

## Traceability backbone

Build a traceability table for substantive review:

| Element | Where introduced | Where operationalized | Where answered | Where concluded |
|---|---|---|---|---|
| Problem/gap | Introduction/literature | Method/design | Results/discussion | Conclusion |
| RQ/Hypothesis | Introduction | Measures/analysis | Results | Discussion/conclusion |
| Contribution | Introduction | Method/system/theory | Evidence | Conclusion |
| Limitation | Scope/method | Analysis | Discussion | Conclusion/future work |

Flag missing links, changed wording that changes the construct, and questions answered only implicitly.

## Title

A title should identify the central subject and, when useful, method, population/context, or study type. Review for:

- unsupported claims (`بهینه`, `قطعی`, `جامع`, `هوشمند`);
- unnecessary opening phrases;
- acronyms or jargon not intelligible to the intended audience;
- a scope broader than the study;
- mismatch between Persian and English titles;
- inconsistent terminology relative to the abstract and glossary.

Do not rewrite a title to a generic template when the field has established naming conventions.

## Abstract

The abstract must be self-contained enough to recover:

- problem/context;
- objective or research question;
- essential method/design and data/population;
- principal results with informative quantities where appropriate;
- conclusion/implication within scope.

Review for:

- background that consumes the abstract without stating the study;
- method with no result;
- claims not present in the main text;
- vague result words without metrics;
- citations, footnotes, undefined abbreviations, or unexplained symbols unless explicitly permitted;
- numbers that disagree with results/tables;
- Persian and English abstracts that are not semantically equivalent.

Word limits and one-paragraph requirements are venue/institution rules, not universal prose rules. Apply the controlling guide.

## Introduction

Retain the useful functional guidance found in the Tehran thesis template:

1. define the problem and context;
2. explain why it matters;
3. identify the unresolved gap or limitation;
4. state the objective, research question, or hypothesis;
5. summarize the approach only as needed for orientation;
6. state contributions accurately;
7. delimit scope and assumptions where necessary;
8. provide a manuscript roadmap when useful or required.

Flag introductions that:

- begin broadly but never narrow to a researchable problem;
- claim a gap without literature support;
- confuse motivation with evidence;
- list contributions that are not evaluated later;
- reveal results only through vague praise;
- duplicate the entire literature review;
- describe chapter order mechanically when a concise logical roadmap would suffice.

## Literature review / related work

The strongest reusable guidance from the Tehran template is synthesis: classify and relate prior work, identify limitations or unresolved questions, and position the current study. Do not produce a source-by-source catalogue.

Review for:

- explicit organizing dimensions (method, theory, population, task, chronology, evidence quality);
- fair representation of prior work;
- comparison of assumptions, data, outcomes, and limitations;
- disagreement and negative evidence;
- connection from synthesis to the research gap;
- current foundational and relevant recent sources, with recency determined by the field—not a fixed rule;
- duplicate claims or citation dumping;
- novelty claims inconsistent with the surveyed literature.

A literature review may be integrated into the introduction or distributed across chapters. Judge function, not heading name.

## Conceptual/theoretical framework

Where applicable, require:

- defined constructs;
- relations among constructs;
- assumptions and boundary conditions;
- operational implications;
- distinction between borrowed theory and the author’s extension;
- a diagram that agrees with the prose and hypotheses.

Do not allow a framework section to become a glossary of unrelated definitions.

## Methodology / materials and methods

Retain and strengthen the Tehran template’s core criteria: justify methodological choices, describe the work so it is reproducible/auditable, and explain validation.

Depending on discipline, recover:

- design and rationale;
- setting, population, sampling, inclusion/exclusion;
- data sources and collection;
- instruments, measures, preprocessing, coding;
- model/algorithm/system architecture;
- variables, outcomes, estimands, hypotheses;
- baselines and ablations;
- statistical or computational analysis;
- hyperparameters, seeds, hardware/software/versioning where relevant;
- validation, robustness, sensitivity, and error analysis;
- ethics, consent, privacy, security, and data governance when relevant;
- deviations from preregistration/protocol;
- limitations inherent in design.

Flag rationale stated as result, hidden researcher degrees of freedom, and implementation details that make replication impossible.

## Results

Retain the Tehran template’s central function: present findings that answer the research questions. Strengthen it with traceability and quantitative consistency.

Review for:

- order aligned with RQs/hypotheses, not merely the order analyses were run;
- clear identification of analysis population/sample;
- estimates, units, uncertainty, and denominators;
- distinction between confirmatory, exploratory, and post-hoc analyses;
- tables/figures that add information rather than duplicate prose;
- prose that states the takeaway and exact values without narrating every table cell;
- null, negative, and anomalous findings;
- no causal interpretation beyond the design;
- no method introduced for the first time unless transparently labeled and justified.

Venue traditions differ on whether limited interpretation belongs in Results. Use the project profile.

## Discussion

Retain the Tehran template’s useful boundaries: interpret results using evidence and literature; avoid speculation presented as fact; do not overgeneralize.

A disciplined discussion normally:

1. answers the main question in relation to the results;
2. explains plausible mechanisms or interpretations with calibrated certainty;
3. compares findings with prior work;
4. analyzes discrepancies and alternative explanations;
5. states theoretical, practical, or engineering implications;
6. discusses limitations and threats to validity;
7. defines the boundary of generalization.

Flag:

- a repetition of Results with no interpretation;
- new unreported analyses or data;
- citations used to override contradictory current results;
- limitations that are ritual disclaimers with no consequence;
- recommendations unsupported by the design;
- speculation without linguistic markers or evidence.

## Conclusion

Retain the Tehran template’s useful elements: summarize what was established, state novelty/contribution proportionately, give implications, limitations, and defensible future work. The conclusion must not introduce new evidence, methods, or literature-dependent claims that were never developed.

Check alignment with:

- title and abstract;
- RQs/hypotheses;
- contribution list;
- principal quantitative findings;
- limitations;
- stated scope.

Do not turn “future work” into a list of generic possibilities. Link each item to a demonstrated limitation, open question, or next validation step.

## Recommendations

When the artifact includes policy, clinical, educational, or engineering recommendations, separate:

- evidence-supported recommendation;
- implementation condition;
- stakeholder and setting;
- expected benefit;
- cost/risk/trade-off;
- uncertainty and monitoring requirement.

A recommendation is not equivalent to a research conclusion.

## Appendices and supplementary material

Verify that appendices/supplements:

- are referenced from the main text;
- contain necessary detail without hiding central evidence;
- use consistent labels, terminology, and notation;
- preserve anonymization and permissions;
- remain buildable and accessible;
- are included or excluded according to submission rules.

## Paragraph and section architecture

For each section, write a one-sentence function summary. For each paragraph, identify its main move. Flag:

- a section whose paragraphs do not serve the stated function;
- duplicated arguments across chapters;
- headings with only one trivial paragraph;
- headings that promise content not delivered;
- transitions based only on sequence (`در ادامه`) rather than logic;
- paragraphs that require evidence located much later;
- definitions introduced after first substantive use.

## Engineering and computer-science adaptation

For CS/EE theses and papers, additionally trace:

- problem formulation and assumptions;
- symbols and dimensions;
- algorithm inputs/outputs and complexity;
- data split and leakage controls;
- baseline selection and tuning budget;
- ablations and sensitivity;
- seed/run aggregation and variance;
- compute/hardware/software environment;
- reproducibility assets;
- distinction among simulation, benchmark, prototype, and deployment;
- failure cases and operational constraints.

Do not let polished prose hide an under-specified experiment.

## Structural issue severity

- `BLOCKER`: required section/object missing, research question not answerable from reported work, submission structure violates controlling rules.
- `MAJOR`: gap–method–result–conclusion chain is broken; evidence is in the wrong rhetorical category; important limitation absent.
- `MINOR`: local ordering, transition, or heading problem.
- `STYLE`: optional reorganization with no effect on scientific recoverability.
