# LaTeX and XePersian Safety

## Review the workspace, not only the root file

Before editing prose in a LaTeX project, discover the dependency graph:

- root document(s);
- `\input`, `\include`, `\subfile`, and generated inclusions;
- document class and style files;
- preamble and macro files;
- bibliography resources;
- glossary/acronym/terminology files;
- figure/table/data assets;
- appendices and supplementary files;
- build scripts, `latexmkrc`, Makefile/Justfile, CI configuration;
- compiled PDF and log files when available.

A root `.tex` file can contain almost no prose. Never claim full-manuscript review without resolving included files.

## Establish the toolchain

Record:

- engine: XeLaTeX/LuaLaTeX/other;
- Persian package and version, especially XePersian;
- bibliography backend: BibTeX/Biber;
- glossary/index backend: xindy/makeindex/other;
- build command and number/order of passes;
- font availability and fallback behavior;
- required shell-escape or external tools;
- current warnings/errors baseline.

Do not modernize packages or toolchain during language editing unless explicitly requested.

## Protected scholarly spans

Never perform blind prose replacements inside:

- command names and environment names;
- labels, citation keys, glossary keys, index keys;
- URLs, DOIs, file paths, email addresses;
- inline/display math;
- code/listings/verbatim/minted environments;
- bibliography database fields unless that field is deliberately reviewed;
- generated files;
- macro definitions whose arguments have unknown semantics;
- comments that are intentionally excluded, except draft-residue review.

Text arguments of commands such as section headings, captions, footnotes, and emphasis may be editable, but parse them conservatively.

## Macro preservation

Before replacing visible text, check whether it is emitted by a macro. Preserve:

- semantic terminology macros;
- method/model-name macros;
- unit macros;
- cross-reference macros;
- citation macros;
- RTL/LTR wrappers;
- glossary/acronym commands;
- custom punctuation/spacing macros.

Prefer correcting the single authoritative macro definition when the same visible error is intentionally generated everywhere, but only after verifying all call sites.

Do not inline macros merely to make editing easier.

## XePersian-specific directionality

Follow the project’s established commands and package guidance for Latin/RTL spans. Typical mechanisms may include `\lr{...}`, `\rl{...}`, `\LTRfootnote{...}`, Latin environments, and language-aware font commands, but exact commands depend on the project.

Check rendered output for:

- reversed model names or acronyms;
- misplaced punctuation at script boundaries;
- parenthesis order;
- citations adjacent to English text;
- footnote direction;
- English abstract/title page direction;
- equations and units embedded in Persian sentences;
- list labels and table columns;
- hyperlink direction and line breaks.

Do not insert Unicode directional overrides as a substitute for semantic TeX commands.

## ZWNJ and TeX source

A ZWNJ in ordinary Persian text is a character-level orthographic device. Do not replace it with arbitrary TeX spacing commands. Conversely, do not run ZWNJ normalization inside macro keys, code, math, or file names.

Check for:

- invisible duplicate ZWNJ;
- ZWNJ adjacent to braces or command boundaries that breaks joining;
- copy-pasted nonbreaking or zero-width spaces with unintended semantics;
- Persian words split across macros in a way that prevents correct shaping.

Repairs that change brace/macro boundaries require compilation and rendered inspection.

## Fonts and glyph coverage

Verify that chosen Persian and Latin fonts:

- contain required glyphs;
- distinguish Persian Yeh/Kaf correctly;
- render digits and mathematical symbols as intended;
- provide bold/italic forms or deliberate substitutes;
- are embedded in the final PDF when required;
- do not silently fall back inconsistently;
- respect institution requirements.

Do not distribute or expose proprietary font files. Record font names/configuration only.

## Bibliography and glossary

Check:

- bibliography files are loaded exactly once as intended;
- keys resolve and are unique;
- Persian and Latin entries render and sort correctly;
- author names and titles preserve source fidelity;
- glossary/acronym entries compile and sort;
- first-use behavior matches the terminology policy;
- stale generated glossary/index files are not masking errors;
- build instructions reproduce the output from a clean state.

A formatting problem in a bibliography style is not safely repaired by manually changing every entry.

## Figures and floats

Review source and PDF together:

- asset path and extension;
- missing/placeholder/draft figures;
- label placement relative to caption;
- subfigure labels and references;
- float placement far from first reference;
- unreadable text after scaling;
- RTL caption alignment and punctuation;
- table direction and numeric column alignment;
- ad-hoc `\vspace`/negative spacing used to force layout;
- venue-specific float restrictions.

Layout hacks are candidates, not automatic errors. Determine whether they are necessary and stable.

## Cross-references and labels

Check:

- duplicate or empty labels;
- inconsistent label naming only when project policy exists;
- unresolved `??` in log/PDF;
- correct object type in references;
- ranges and multiple references;
- hyperref targets;
- references to deleted/moved objects;
- reference macros compatible with Persian wording and pluralization.

Do not rename labels during prose editing unless requested; label renames have repository-wide impact.

## Comments and draft residue

Search for:

- `TODO`, `FIXME`, `XXX`, `TBD`;
- editorial comments;
- colored review annotations;
- `\marginpar`, notes, change-tracking commands;
- hidden text or conditionals;
- dummy figures/tables;
- copied venue instructions;
- placeholder citations/text;
- disabled sections that still affect claims or numbering.

Classify residue by whether it appears in source only or in the final PDF.

## Build-and-verify protocol

Before edits, when feasible:

1. build from the documented command;
2. save baseline exit status, warnings, and output hash/pages;
3. identify pre-existing failures.

After edits:

1. rebuild from a clean enough state to expose dependency problems;
2. distinguish introduced errors from baseline errors;
3. inspect changed pages in the PDF;
4. verify no unresolved references/citations;
5. verify glossary/index/bibliography generation;
6. report commands and outcomes.

Never say “compiles successfully” without running the build or being given a reliable build result.

## Source-versus-PDF review

Source review can detect:

- malformed commands;
- missing assets;
- duplicate keys/labels;
- terminology and prose issues;
- dangerous manual spacing;
- unresolved dependency graph.

PDF review is necessary for:

- actual bidirectional rendering;
- line/page breaks;
- float placement;
- clipped tables/figures;
- font substitution;
- visible comments/draft marks;
- caption and footnote layout;
- page-level consistency.

State clearly when no compiled PDF was available.

## Safe-edit boundary

Usually safe after verification:

- Persian Yeh/Kaf normalization in plain prose;
- obvious typos inside ordinary text arguments;
- approved local wording changes that leave command structure intact.

Meaning- or structure-sensitive:

- moving citations across clauses;
- changing captions that encode experimental conditions;
- altering terminology/glossary macros;
- modifying equations, units, or labels;
- changing RTL/LTR wrappers;
- touching class/style/package configuration;
- global regex replacement across `.tex` files.
