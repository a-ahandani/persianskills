# Source Audit: Retained, Adapted, and Rejected Ideas

Contents: Method; 1. Academy of Persian Language and Literature; 2. IranDoc thesis/dissertation writing guide (`راه`); 3. University of Tehran official guidance; 4. `sinamomken/tehran-thesis`; 5. `LimHyungTae/awesome-claudecode-paper-proofreading`; 6. `ali2000hos/persian-writing`; 7. `0xRadikal/Academic-Paper-Writer-Skill`; 8. Other proofreading/agent-skill examples; 9. Persian NLP and proofreading tools; 10. Unicode and TeX standards/resources; 11. Deliberate design decisions in this skill; 12. Source-use rule for future maintenance; 13. IPL Signal Processing Glossary.

## Method

This skill does not treat any single repository as a comprehensive authority. Sources were classified by role:

- **language authority** — Persian orthography/spelling;
- **institutional guidance** — current thesis/dissertation requirements;
- **editorial workflow** — how an agent should inspect, report, and patch;
- **disciplinary writing advice** — claims, structure, figures, equations;
- **implementation examples** — LaTeX/XePersian organization and terminology tooling.

A useful idea was retained only when its scope could be stated and it did not conflict with a higher authority.

## 1. Academy of Persian Language and Literature

### Sources

- *Dastur-e Xatt-e Fārsi* / `دستور خطّ فارسی`, revised edition published by the Academy.
- Academy author/submission guidance that requires standard Persian, Academy orthography, authoritative spelling, approved terminology where applicable, and correct spacing/half-spacing.
- Academy spelling and terminology resources when available.

### Retained

- Persian orthography must be grounded in the Academy within the guide’s stated scope.
- Full space, ZWNJ/half-space, and no inserted character are distinct states.
- High-confidence morphology includes `می‌/نمی‌`, many prefix/suffix boundaries, and contexts in which plural `ها` must or preferably should be separated.
- Persian Yeh/Kaf and digital-text integrity matter.
- Lexical dictionaries are necessary for many compounds.

### Scope correction

The orthography guide itself does not settle all punctuation, transliteration, foreign-word rendering, or every compound. The skill therefore labels these as lexical, venue, project, or editorial decisions instead of inventing “Academy rules.”

## 2. IranDoc thesis/dissertation writing guide (`راه`)

### Retained

- section- and object-level guidance for titles, abstracts, citations, footnotes, figures, tables, equations, and thesis presentation;
- the principle that captions/titles must be informative and objects should support efficient interpretation;
- explicit treatment of Persian and English abstract/title components;
- the existence of multiple citation systems and the need to follow a declared one.

### Adapted

IranDoc’s numeric recommendations, font choices, citation preference, and format details are defaults only when no current institution/venue rule controls. They are not universal Persian grammar.

## 3. University of Tehran official guidance

### Retained

- current university/faculty rules override older templates;
- the manuscript must be checked against the currently published guide and any faculty/department supplement;
- guide date/version must be recorded in the project profile.

### Important update

The `tehran-thesis` repository says it implements a University of Tehran guide from September 2013. University of Tehran pages now point to a university-wide thesis/dissertation guide from Aban 1403 (October–November 2024), and some faculty pages may add local documents. Therefore, the repository is treated as historical implementation guidance, not current submission authority.

## 4. `sinamomken/tehran-thesis`

Repository: `https://github.com/sinamomken/tehran-thesis`

### Retained: content and editorial functions

The chapter examples contain valuable high-level guidance:

- **Introduction:** explain the problem, importance/motivation, research questions, brief method, and document roadmap in clear language.
- **Literature review:** classify and synthesize prior work, identify gaps/limitations, and position the current work rather than listing sources serially.
- **Methodology:** explain and justify methodological choices, provide enough detail for reproducibility, and describe validation.
- **Results:** present findings/data in a way that answers the research questions.
- **Discussion/conclusion:** interpret results in relation to evidence and literature, avoid speculation and overgeneralization, and cover contribution/novelty, implications, limitations, and future work without introducing new evidence.
- **Terminology tooling:** the `words.tex`/glossary mechanism demonstrates the value of a single terminology source of truth with Persian/English forms.
- **Project organization:** modular chapter files, XePersian, bibliography, glossary, and generated outputs justify a recursive workspace audit.

### Adapted

- chapter names/order are converted into rhetorical functions so the skill works across disciplines and integrated-paper theses;
- template examples are converted into checks, not copied as mandatory prose;
- LaTeX conventions are checked against the actual project toolchain rather than frozen to the repository’s package versions.

### Rejected as universal rules

- fixed page counts;
- a mandatory five-chapter structure;
- a blanket “last two years” literature rule;
- 2013 formatting details as current UT policy;
- any assumption that one template’s fonts, packages, citation style, or front matter applies to every faculty or venue.

## 5. `LimHyungTae/awesome-claudecode-paper-proofreading`

Repository: `https://github.com/LimHyungTae/awesome-claudecode-paper-proofreading`

### Retained: workflow

- two-phase **detect first, fix after approval**;
- stable issue numbering/IDs;
- workspace audit separated from content proofreading;
- recursive reading of LaTeX inputs, macros, bibliography, figures, and compiled PDF;
- report issues with location, explanation, severity, and repair direction;
- apply only user-approved changes;
- inspect figures/captions, claims, abstract/conclusion, values, acronyms, and notation;
- use the PDF for visible layout and unresolved annotation checks.

### Retained: scientific checks

- overclaiming and misuse of “significant”;
- claim–citation fit;
- abstract/conclusion alignment;
- figure/table/caption self-sufficiency at the level needed for interpretation;
- numerical consistency;
- notation/symbol tables and symbol drift;
- macro, label, bibliography, placeholder, and layout-hack audits.

### Adapted

- the source prompt’s conference/robotics/English-specific advice is generalized and placed below venue/project authority;
- issue numbering becomes typed stable IDs (`CLAIM-004`, `LATEX-012`);
- severity is separated from confidence, layer, authority, and edit risk;
- “critical” status depends on actual scholarly/submission impact, not a fixed checklist item;
- English grammar/tense/hyphenation rules are replaced by Persian-specific grammar and bilingual translation checks.

### Rejected as universal rules

- venue-specific limits or section formulas;
- robotics/IEEE macro conventions as general requirements;
- blanket tense formulas for Related Work or other sections;
- blanket bans on particular punctuation or stylistic forms;
- treating an unreferenced figure as automatically critical;
- fixed abstract/contribution formulas;
- any “AI-writing signal” heuristic presented as proof.

## 6. `ali2000hos/persian-writing`

Repository: `https://github.com/ali2000hos/persian-writing`

### Retained

- a dedicated Persian-writing skill benefits from modular references for orthography, style, and academic context;
- explicit attention to Persian punctuation, ZWNJ, Arabic/Persian code-point normalization, translationese, and register;
- examples make agent instructions more operational.

### Adapted/rejected

The project includes useful practical preferences but some style rules are opinionated or aimed at generic/human-sounding writing. This skill does not:

- turn every preference into a correctness rule;
- automatically remove formal constructions;
- ban punctuation/list patterns as “AI-like”;
- prioritize stylistic naturalness over scientific equivalence;
- overwrite an institution, discipline, or project glossary.

## 7. `0xRadikal/Academic-Paper-Writer-Skill`

Repository: `https://github.com/0xRadikal/Academic-Paper-Writer-Skill`

### Retained

- Persian scholarly writing needs explicit section functions, citation discipline, common-error checks, and terminology consistency;
- source-backed writing and non-fabrication are mandatory;
- discipline/venue structure must be resolved before drafting.

### Adapted/rejected

- rigid paper structures, abstract lengths, contribution counts, and citation patterns become configurable venue rules;
- generic writing advice is separated from Persian orthographic authority;
- “make it human” preferences are not used to alter scientific content.

## 8. Other proofreading/agent-skill examples

Other paper-proofreading skills were consulted for ideas such as staged review, minimal edits, configurable checklists, and verification. They are implementation references, not Persian-language authorities.

## 9. Persian NLP and proofreading tools

Tools such as Hazm, Virastyar-related libraries, Parsivar, and other Persian
normalizers were considered as implementation aids. They are useful for
character normalization, tokenization, morphology, spelling, punctuation, and
ZWNJ candidate discovery. They are not adopted as language authorities, and
no aggressive normalizer is allowed to rewrite scholarly source in place. The
skill therefore ships a narrow standard-library scanner and requires protected
spans, diff review, approval, and build verification. See
`references/11-tooling-and-reporting-standards.md`.

## 10. Unicode and TeX standards/resources

### Retained

- character identity and bidirectional behavior must be distinguished from visual appearance;
- format/control characters should be diagnosed by code point and context;
- TeX source, semantic macros, and rendered PDF must all be checked;
- automated normalization must protect math, code, keys, URLs, bibliography identifiers, and quoted source text.

## 11. Deliberate design decisions in this skill

The following are synthesis decisions rather than quotations from one source:

1. **Authority labels** prevent editorial preference from masquerading as language law.
2. **Five independent issue dimensions**—severity, confidence, layer, edit risk, authority—produce safer approvals than one severity rank.
3. **Project profile + terminology register + decision log** make permissible variation reproducible.
4. **Report-first by default** protects technical meaning and supports human editorial control.
5. **A narrow safe fixer** handles only character-level corruption; morphology, compounds, digits, punctuation, and prose remain judgment-based.
6. **Translation audit** treats modality, negation, scope, causality, and evidence strength as invariants.
7. **Final QC includes the compiled PDF**, because RTL and float/font problems cannot be established from source alone.

## 12. Source-use rule for future maintenance

When adding a new rule, record:

- exact source and version/date;
- source role and authority level;
- scope and exceptions;
- whether it is obligatory, recommended, or merely preferred;
- examples and counterexamples;
- automation safety;
- conflicts with current project/institution policy.

Do not add unattributed style folklore to the skill.

## 13. IPL Signal Processing Glossary

### Source

- *Signal Processing Glossary*, Shohreh Kasaei, Image Processing Lab (IPL), Sharif University of Technology; created August 2009, provided PDF edition dated December 1, 2025.

### Retained

- English headwords and their displayed Persian equivalents are transcribed into the bundled TOML register with source-page provenance.
- Multiple Persian equivalents remain candidates in source order; duplicate English headwords remain separate records.
- The source is useful for signal-processing, image-processing, machine-learning, and adjacent technical vocabulary lookup.

### Scope and authority correction

IPL entries have `reference` status. They do not automatically override a project glossary, supervisor-approved terminology, established disciplinary sense distinctions, or venue requirements. The first displayed Persian equivalent is not silently promoted to a preferred project term. The provided PDF contains no license statement; the repository records that fact and attributes the derived register without claiming that IPL or Sharif University endorses this skill.
