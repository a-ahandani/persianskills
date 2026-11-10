# Review and Apply Protocol

Contents: Core workflow; Review levels; Issue dimensions; Category prefixes; Required issue format; Executive summary; Approval language; Stale-file protection; Patch discipline; Verification; Direct-edit exception.

## Core workflow

```text
scope → authority → context → passes → issue report → approval → stale check → patch → verification
```

The report-first protocol is the default because Persian copyediting can accidentally change technical meaning, terminology, equations, and claim strength.

## Review levels

Keep these levels distinct:

| Level | Focus | Typical examples |
|---|---|---|
| L0 Mechanical | Unicode, spacing, file integrity | Arabic `ي/ك`, malformed ZWNJ, missing asset |
| L1 Copyedit | Orthography, grammar, syntax | punctuation, ambiguous referent, malformed clause |
| L2 Substantive | Clarity, cohesion, terminology | paragraph flow, inconsistent term, translationese |
| L3 Scientific | Claims and evidence | causal overreach, unsupported “best,” significance misuse |
| L4 Structural | Manuscript architecture | missing gap, results/discussion conflation, conclusion drift |

Do not resolve an L3 or L4 problem through an unannounced L1 rewrite.

## Issue dimensions

### Severity

- `BLOCKER`: risks invalid submission, corrupted files, fabricated/incorrect scholarship, or materially false interpretation.
- `MAJOR`: important scientific, logical, structural, or clarity problem.
- `MINOR`: local correctness or readability issue that does not materially change the argument.
- `STYLE`: optional or house-style improvement.

### Confidence

- `HIGH`: rule and diagnosis are clear from available context.
- `MEDIUM`: likely issue, but context or house style could change the judgment.
- `LOW`: plausible concern requiring author/venue confirmation.

### Layer

- `MECHANICAL`
- `LINGUISTIC`
- `SCIENTIFIC`
- `STRUCTURAL`
- `VENUE`

### Edit risk

- `SAFE`: mechanical/local correction with no plausible semantic change.
- `MEANING-SENSITIVE`: wording may alter scope, agency, modality, chronology, or terminology.
- `STRUCTURAL`: paragraph/section reorganization or addition/removal of content.

These dimensions are independent. A `STYLE/HIGH/SAFE` finding is not more urgent than a `MAJOR/MEDIUM/MEANING-SENSITIVE` one.

## Category prefixes

- `WS` workspace
- `UNI` Unicode/encoding
- `ORTH` orthography
- `PUNCT` punctuation/typography
- `GRAM` grammar
- `SYN` syntax and ambiguity
- `TERM` terminology/acronyms
- `TRANS` translation fidelity
- `STYLE` academic register
- `CLAIM` claim strength/causality
- `EVID` evidence/statistics
- `STRUCT` paragraph/section/chapter structure
- `CITE` citations/bibliography
- `FIG` figures/captions
- `TABLE` tables
- `EQ` equations/notation
- `LATEX` TeX/XePersian
- `QC` rendered-output/final checks

## Required issue format

```markdown
### CLAIM-004 — Unsupported causal wording

- Severity: MAJOR
- Confidence: HIGH
- Layer: SCIENTIFIC
- Edit risk: MEANING-SENSITIVE
- Authority: DISCIPLINE, EDITORIAL
- Location: `chapters/results.tex:118`
- Original: «استفاده از روش پیشنهادی باعث افزایش یادگیری دانشجو شد.»
- Diagnosis: The design reports an observational association and does not identify a causal effect.
- Why it matters: The sentence overstates what the data support.
- Proposed repair: Use association language and name the measured outcome and conditions, or provide the causal identification argument.
- Candidate wording: «در داده‌های این مطالعه، استفاده از روش پیشنهادی با افزایش ... همراه بود.»
- Depends on: EVID-007
```

Quote only enough text to identify the issue.

## Executive summary

At minimum include:

- files/sections reviewed;
- controlling profile and unresolved assumptions;
- counts by severity;
- three to five highest-risk patterns;
- whether the manuscript can be edited mechanically or needs author decisions first;
- missing context that limits confidence.

## Approval language

Recognize selectors such as:

```text
apply ORTH-001 TERM-003 CLAIM-002
apply all BLOCKER and MAJOR except STRUCT-004
apply SAFE/HIGH findings
apply file:chapters/method.tex severity:MINOR
skip STYLE-*
discard TRANS-006
```

When a selector is ambiguous, choose the narrowest safe interpretation and state it in the change summary.

## Stale-file protection

Before applying an approved issue:

1. re-read the target file;
2. compare its hash or the surrounding span with the reviewed version;
3. if unchanged, patch it;
4. if locally changed but the issue remains, refresh the patch against current text;
5. if the meaning or structure changed, mark the issue stale and re-audit it.

Never force an old patch onto a changed manuscript.

## Patch discipline

- Apply only approved issues.
- Keep changes local unless structural work was approved.
- Preserve author voice and discipline terminology.
- Do not “improve” adjacent sentences silently.
- Do not reorder citations to make prose easier without checking citation semantics.
- Do not change a number, sign, unit, equation, statistical result, label, or citation key as a side effect of language editing.
- Make atomic changes that are easy to review in a diff.

## Verification

After editing:

1. rerun static checks;
2. rebuild the manuscript when possible;
3. inspect errors and warnings introduced by the patch;
4. compare affected rendered pages when a PDF is available;
5. verify terminology and symbol consistency;
6. report applied, skipped, stale, and remaining findings.

## Direct-edit exception

When the user explicitly requests direct copyediting or rewriting:

- apply `SAFE` and clearly justified language changes;
- preserve a compact change log;
- mark meaning-sensitive alternatives rather than silently selecting one when evidence is insufficient;
- never use the request for “better prose” as permission to invent scientific content.
