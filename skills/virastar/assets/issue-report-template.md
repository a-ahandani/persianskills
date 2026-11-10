# Virastar Manuscript Audit

## Scope

- Artifact:
- Files/sections reviewed:
- Root file:
- Compiled PDF reviewed: yes/no
- Review mode:
- Date/revision/hash:

## Authority and assumptions

- User instruction:
- Institution/venue guide and version:
- Faculty/department supplement:
- Project profile:
- Terminology register:
- Inferred conventions:
- Unresolved authority questions:

## Executive summary

| Severity | Count |
|---|---:|
| BLOCKER | 0 |
| MAJOR | 0 |
| MINOR | 0 |
| STYLE | 0 |

Highest-risk patterns:

1.
2.
3.

Recommended approval order:

1. scientific/meaning decisions;
2. terminology decisions;
3. safe orthographic/mechanical corrections;
4. optional style changes.

## Findings

### CLAIM-001 — Descriptive title

- Severity: MAJOR
- Confidence: HIGH
- Layer: SCIENTIFIC
- Edit risk: MEANING-SENSITIVE
- Authority: DISCIPLINE, EDITORIAL
- Location: `chapters/results.tex:118`
- Reviewed hash/span:
- Original: «...»
- Diagnosis:
- Why it matters:
- Proposed repair:
- Candidate wording:
- Depends on:
- Status: open

## Cross-document consistency

### Terminology

| Concept | Preferred form | Variants found | Locations | Decision |
|---|---|---|---|---|

### Claims and values

| Claim/value | Source of truth | Abstract | Body | Table/figure | Conclusion |
|---|---|---|---|---|---|

### Symbols and acronyms

| Item | Definition | First use | Variants/collisions | Decision |
|---|---|---|---|---|

## Quality rubric

| Dimension | Score (0–4) | Evidence | Required action |
|---|---:|---|---|
| Authority/compliance |  |  |  |
| Orthography/Unicode |  |  |  |
| Grammar/syntax |  |  |  |
| Terminology/translation |  |  |  |
| Academic register |  |  |  |
| Claims/evidence |  |  |  |
| Structure/traceability |  |  |  |
| Scholarly objects |  |  |  |
| LaTeX/rendered output |  |  |  |

## Limits of review

-

## Approval syntax

```text
apply ORTH-001 ORTH-004 TERM-002
apply all SAFE/HIGH except STYLE-*
apply BLOCKER and MAJOR; discard STYLE-*
```
