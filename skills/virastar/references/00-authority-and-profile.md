# Authority Resolution and Project Profile

## Why authority must be resolved first

Editing Persian scholarly writing combines rules from different domains. They are not interchangeable:

- **Orthography** answers how Persian words and morphemes are written.
- **Punctuation and typography** depend partly on editorial convention and medium.
- **Institutional formatting** answers what a university or journal requires.
- **Scientific style** answers how strongly a claim may be stated and how evidence should be organized.
- **Project house style** settles recurring choices that more than one authority permits.

A correct review identifies the source of each requirement. Never write “according to Persian grammar” when the basis is only a university template or editor preference.

## Precedence

Use this order unless the user explicitly changes it:

1. The user’s current, explicit instruction.
2. Current university, faculty, department, journal, publisher, or funder requirements.
3. Supervisor-approved decisions and project-specific profile.
4. Project terminology register, glossary, and already established consistent practice.
5. Academy of Persian Language and Literature rules within their actual scope.
6. IranDoc or recognized discipline-level guidance when controlling rules are silent.
7. General editorial judgment.

### Conflict handling

When sources conflict:

- identify both sources;
- state which one controls and why;
- do not silently normalize the manuscript to the editor’s preference;
- record the decision in the project decision log;
- apply the decision consistently thereafter.

An old template may remain useful for workflow and examples, but it cannot override a newer official guide.

## Project profile

Look for `editorial/project-profile.toml`. If absent, infer a provisional profile and state the assumptions.

Important fields:

- artifact: thesis, dissertation, paper, report, proposal;
- degree and discipline;
- institution, faculty, department, journal;
- source format and build command;
- current official guide and its date/version;
- citation system;
- digit policy;
- preferred form of ezafe after final `ه`;
- plural `ها` policy;
- quotation-mark policy;
- first-use bilingual terminology policy;
- first-person/passive-voice policy;
- spelling dictionary or approved terminology source;
- protected LaTeX macros and environments;
- terminology register and decision log paths.

Do not invent missing institutional rules. Mark them `unknown` or `provisional`.

## Infer house style from evidence

When no explicit rule controls:

1. sample several clean, author-approved sections;
2. count competing forms rather than relying on one occurrence;
3. prefer the dominant form only when it is linguistically defensible;
4. avoid learning inconsistency as house style;
5. record the inferred decision and confidence.

Examples of inferable choices:

- `خانهٔ` vs `خانۀ` vs `خانه‌ی`;
- Persian or Latin digits in prose;
- English term in parentheses or a footnote at first use;
- author–date or numeric citation syntax;
- `شکل` vs `تصویر` for figure labels;
- whether the methods section uses present or past tense.

## Authority labels for findings

Use one or more labels:

- `USER` — direct instruction;
- `INSTITUTION` — current official institutional rule;
- `VENUE` — journal/publisher/conference requirement;
- `SUPERVISOR` — recorded supervisor decision;
- `PROJECT` — project profile or terminology register;
- `ACADEMY` — Academy orthography/spelling;
- `IRANDOC` — IranDoc thesis-writing guidance;
- `DISCIPLINE` — accepted discipline/reporting convention;
- `UNICODE` — encoding or bidirectional-text integrity;
- `EDITORIAL` — reasoned editorial judgment.

## What not to do

- Do not enforce every convention found in a sample thesis template.
- Do not treat a journal’s author guide as universal Persian grammar.
- Do not convert all digits because the prose is Persian.
- Do not replace every English technical term with an Academy equivalent.
- Do not claim the Academy has settled punctuation or every compound spelling.
- Do not call the dominant manuscript form correct when it is consistently wrong.
