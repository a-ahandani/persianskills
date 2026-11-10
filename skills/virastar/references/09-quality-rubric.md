# Quality Rubric and Completion Gates

## Purpose

Use this rubric to summarize manuscript quality and decide whether an audit, editing pass, or final check is complete. Scores support diagnosis; they do not replace issue-level evidence.

## Scoring scale

Score each dimension from 0 to 4:

- `0 — not assessable or fundamentally absent`
- `1 — serious defects; central meaning/recoverability at risk`
- `2 — usable but recurrent major problems`
- `3 — sound with local correctable problems`
- `4 — submission-ready for this dimension under the controlling profile`

Do not average away a blocker. Report blockers separately.

## Dimensions

### A. Authority and compliance

- controlling institution/venue guide identified;
- project decisions recorded;
- current rules distinguished from old templates;
- required front/back matter and formatting recoverable.

### B. Unicode and orthography

- Persian Yeh/Kaf and ZWNJ integrity;
- high-confidence morpheme rules;
- compounds handled lexically rather than by blanket rule;
- punctuation/digits/ezafe consistent with profile;
- no harmful hidden controls.

### C. Grammar and syntactic clarity

- agreement and valency;
- unambiguous referents and scope;
- manageable clause/noun-phrase structure;
- coherent tense/aspect and agency;
- parallel coordination and list grammar.

### D. Terminology and bilingual consistency

- one concept–one approved term;
- first-use and acronym policy;
- source/target equivalence;
- proper names and official Latin forms;
- glossary/register alignment and mixed-direction rendering.

### E. Academic register and readability

- precise information-bearing prose;
- no recurrent empty bureaucracy or translationese;
- paragraph cohesion and explicit logical relations;
- author voice preserved;
- no “humanizer” artifacts or ornamental rewriting.

### F. Scientific claims and evidence

- causal and inferential language calibrated;
- significance and practical importance distinguished;
- comparator, metric, scope, and uncertainty recoverable;
- novelty/generalization proportionate;
- negative results and limitations represented honestly.

### G. Structure and argument traceability

- problem/gap/RQ/contribution alignment;
- method operationalizes the question;
- results answer it;
- discussion interprets rather than invents;
- conclusion matches evidence and scope.

### H. Citations and scholarly objects

- citation need, fit, and placement;
- bibliography integrity;
- figures/tables/captions interpretable and consistent;
- equations/notation defined;
- values/units/statistics agree across manuscript.

### I. LaTeX/XePersian and rendered output

- recursive workspace integrity;
- reproducible build;
- resolved references/citations/glossary;
- safe macros and directionality;
- acceptable fonts, floats, tables, footnotes, and visible PDF output;
- no draft residue.

## Phase-specific completion gates

### Audit complete

- requested files and dependencies were actually reviewed;
- assumptions and missing context are stated;
- findings have stable IDs and required dimensions;
- no file was changed;
- high-risk patterns and blockers are summarized;
- optional style is separated from obligation.

### Approved edit complete

- approved selector is recorded;
- stale-file check passed or affected findings were refreshed;
- only approved changes were applied;
- diff was inspected;
- static checks/build were rerun when available;
- applied, skipped, stale, and remaining findings are listed.

### Translation complete

- all source units are represented;
- no addition/omission/claim drift remains unresolved;
- terminology register was followed;
- numbers, citations, equations, and labels match;
- Persian is natural without changing scientific content;
- unresolved source ambiguity is disclosed.

### Final QC complete

- current official guide/profile is identified;
- zero unresolved `BLOCKER` findings;
- every remaining `MAJOR` issue is either repaired or explicitly accepted by the author;
- build succeeds, or external build limitations are stated precisely;
- rendered PDF pages were inspected when available;
- title/abstract/introduction/conclusion and principal values agree;
- bibliography, glossary, cross-references, figures, tables, equations, and appendices are resolved;
- draft residue is absent from final output.

## Suggested report summary

```markdown
## Quality summary

| Dimension | Score | Main evidence | Blocking decision |
|---|---:|---|---|
| Authority/compliance | 3/4 | UT 1403 guide identified; faculty appendix missing | confirm faculty cover page |
| Orthography/Unicode | 2/4 | 41 Arabic Yeh/Kaf; mixed plural policy | safe normalization available |
| Claims/evidence | 2/4 | two causal overclaims; one metric mismatch | author/statistical review |
| ... | ... | ... | ... |

Overall status: not submission-ready / conditionally ready / ready under stated scope.
```

Avoid an unsupported single “quality percentage.”

## Stop conditions

Stop automatic editing and escalate in the report when:

- the intended scientific meaning is not recoverable;
- source and target translations disagree on a major claim;
- a value differs across authoritative locations;
- a citation appears fabricated or cannot be matched;
- a mathematical correction would be required;
- the current institutional rule cannot be identified and the choice affects submission;
- build changes would alter package/toolchain behavior;
- an approved patch is stale after substantive file changes.
