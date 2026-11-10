# Academic Style, Claims, Evidence, and Statistics

Contents: What “academic” means here; Register and precision; Claim ladder; Causality; Statistical significance; Quantifiers, modality, and scope; Comparative and superiority claims; Novelty and contribution claims; Generalization and external validity; Results, interpretation, and recommendation; Evidence and citation fit; Negative results and limitations; Paragraph-level academic prose; Translationese; “Humanizing” and anti-AI heuristics; Rewrite protocol for a meaning-sensitive sentence.

## What “academic” means here

Academic Persian should be precise, traceable, proportionate to the evidence, and readable by the intended disciplinary audience. It does not need to sound ceremonial, bureaucratic, impersonal, archaic, or translated from English.

Prefer information-bearing prose over prestige signals. Do not rewrite a clear technical sentence merely to make it sound “more academic.”

## Register and precision

Review for:

- conversational fillers or unsupported evaluative language;
- vague nouns such as `موضوع`, `مسئله`, `امر`, `حالت`, or `چیز` when a technical noun is available;
- vague verbs such as `انجام دادن` or `داشتن` when the exact operation matters;
- undefined evaluative adjectives such as `مناسب`, `قابل‌قبول`, `چشمگیر`, `قوی`, `بهینه`, `کارآمد`;
- bureaucratic scaffolding that delays the proposition;
- abrupt colloquial shifts in an otherwise formal manuscript.

Expressions such as `لازم به ذکر است`, `شایان توجه است`, `در راستای`, `در خصوص`, `در رابطه با`, `مورد بررسی قرار گرفت`, and `می‌باشد` are review candidates—not universal grammatical errors. Remove or replace them when they add no meaning, obscure agency, or recur mechanically.

## Claim ladder

Calibrate wording to the strength of the design and evidence. The exact Persian verb depends on context, but this ladder is useful:

| Strength | Typical Persian wording | Required basis |
|---|---|---|
| Logical/mathematical proof | `اثبات می‌کند`, `نشان می‌دهیم که ... برقرار است` | Valid formal proof under stated assumptions |
| Strong empirical demonstration | `نشان می‌دهد`, `نشان داد` | Direct, replicated or well-controlled evidence within scope |
| Evidential support | `از ... پشتیبانی می‌کند`, `حاکی از آن است` | Results increase plausibility but do not establish universally |
| Tentative interpretation | `نشانگر`, `می‌تواند بیانگر`, `احتمالاً`, `پیشنهاد می‌کند` | Limited, indirect, exploratory, or uncertain evidence |
| Compatibility only | `با ... سازگار است` | Result does not contradict the proposition; alternatives remain |

Do not substitute one rung for another as a stylistic variation. Repetition of the scientifically correct verb is preferable to semantic drift.

## Causality

Flag causal language unless the study has an appropriate identification strategy or intervention design.

Causal candidates include:

- `باعث شد`;
- `موجب شد`;
- `سبب شد`;
- `اثر گذاشت`;
- `بهبود داد` when improvement is attributed to a treatment;
- `کاهش داد` / `افزایش داد` when only association was measured.

Association-safe alternatives include:

- `با ... همراه بود`;
- `با ... همبستگی داشت`;
- `در گروه/شرط ... مقدار بیشتری مشاهده شد`;
- `پس از تعدیل ... رابطه باقی ماند`.

Do not weaken a genuinely causal result merely because cautious language sounds safer. Verify design, assumptions, comparison, and estimand.

## Statistical significance

Use `معنادار` or `معنی‌دار` according to the project’s chosen spelling only for statistical significance, and only when the inferential analysis supports it. Record the chosen term consistently.

Do not use statistical-significance language as a synonym for:

- large;
- important;
- useful;
- noticeable;
- practically consequential.

For practical importance, report effect size, absolute difference, uncertainty interval, decision threshold, or domain-specific consequence.

Check that every significance statement identifies, where relevant:

- the comparison or coefficient;
- test/model;
- direction;
- estimate and unit;
- uncertainty interval;
- exact or thresholded p-value;
- multiplicity adjustment;
- analysis population and sample size.

The venue may not require every item in every sentence, but the manuscript must make them recoverable.

## Quantifiers, modality, and scope

Treat these as scientific content:

- all/some/most/none;
- always/often/may/can;
- necessary/sufficient;
- only/at least/at most;
- approximately/exactly;
- under the tested conditions/in general;
- statistically/practically;
- training/test/external data.

During editing or translation, preserve the scope of:

- negation;
- modal verbs;
- hedges;
- frequency adverbs;
- conditions and exceptions;
- universal or existential quantification.

A small word-order change can turn “not all methods” into “all methods did not,” or move `تنها` to a different constituent. Mark such edits `MEANING-SENSITIVE`.

## Comparative and superiority claims

Words such as `بهتر`, `برتر`, `بهینه`, `پیشرفته‌تر`, `دقیق‌تر`, `کارآمدتر`, `مقاوم‌تر`, and `سریع‌تر` require an explicit comparison frame.

Recover or request:

- comparator/baseline;
- metric;
- dataset, population, or environment;
- operating point or budget;
- statistical uncertainty or run-to-run variability;
- computational hardware and measurement protocol when speed/resources are claimed;
- conditions under which the ranking holds.

Replace “the proposed method performs better” with a measurable claim, not with more ornate wording.

Reserve `state of the art`, `بهترین`, and `برای نخستین بار` for claims supported by a current and sufficiently broad comparison/search. Otherwise scope the statement: `در میان روش‌های بررسی‌شده`, `در مجموعه‌داده‌های این مطالعه`, or `تا آنجا که در منابع بررسی‌شده یافتیم`.

## Novelty and contribution claims

A contribution statement should say what is new, relative to what, and why it matters. Distinguish:

- a new problem formulation;
- a new method or theoretical result;
- a new dataset/tool/system;
- a new empirical finding;
- a replication, negative result, or synthesis;
- an engineering integration rather than an algorithmic novelty.

Flag novelty claims that merely restate implementation work, use undefined adjectives, or conflict with the literature review.

Do not manufacture novelty by removing citations or narrowing descriptions of prior work.

## Generalization and external validity

Flag movement from a bounded study to an unbounded conclusion:

- one institution → all students;
- one dataset → real-world deployment;
- simulation → physical system;
- retrospective association → prospective benefit;
- benchmark accuracy → educational effectiveness;
- short-term outcome → durable learning.

A defensible conclusion names the population, setting, task, period, and assumptions actually studied, then separately states hypotheses for broader use.

## Results, interpretation, and recommendation

Keep these rhetorical moves distinct:

1. **Result:** what was measured or derived.
2. **Interpretation:** what the result may mean.
3. **Comparison:** how it relates to prior work or a baseline.
4. **Limitation:** what remains uncertain.
5. **Recommendation:** what action, if any, follows.

Do not rewrite an interpretation as a result, or a recommendation as an established fact.

## Evidence and citation fit

For a cited claim, check:

- whether the source actually supports the proposition;
- whether the source population/method matches the claim’s scope;
- whether a review is being cited for a primary result or vice versa;
- whether a citation cluster hides disagreement among sources;
- whether the sentence attributes a claim to the correct author;
- whether a direct quotation, paraphrase, or translation is clearly identified.

Never fabricate a supporting citation. When source access is unavailable, write `citation support not verified` rather than assuming fit.

## Negative results and limitations

Do not soften a null, failed, or negative result into success language. Preserve:

- failed hypotheses;
- confidence intervals crossing a decision threshold;
- non-convergence;
- sensitivity to initialization or seed;
- missing data or exclusions;
- non-replication;
- limitations imposed by measurement, sample, implementation, or design.

Likewise, do not exaggerate uncertainty until a real result becomes unreadably timid.

## Paragraph-level academic prose

A strong analytical paragraph usually performs a coherent function:

- establishes a claim or question;
- presents evidence/reasoning;
- interprets it;
- qualifies it;
- links it to the section argument.

This is not a rigid five-sentence template. Flag paragraphs that:

- contain several unrelated topics;
- start with generic metadiscourse but never state a claim;
- list citations source by source without synthesis;
- end with a new unsupported assertion;
- use transitions that misstate the logical relation;
- repeat the same proposition in inflated wording.

## Translationese

Common candidates include:

- noun-heavy calques where Persian prefers a clause;
- unnecessary explicit subjects copied from English;
- repeated `این مطالعه ...` at every sentence;
- English modifier order reproduced in Persian;
- literal renderings of discourse markers;
- overuse of passive constructions because the English source is passive;
- false friends or imported polysemy in technical terms.

Repair translationese only after reconstructing the source proposition. A natural Persian sentence that changes modality, agency, or relation is not a good translation.

## “Humanizing” and anti-AI heuristics

Do not use folklore about AI-generated text as an authority. The following may justify ordinary editing when they impair prose:

- empty metadiscourse;
- formulaic repetition;
- gratuitous headings;
- unsupported grand claims;
- monotonous sentence openings;
- excessive symmetry or triads;
- inflated abstractions.

But punctuation choices, em dashes, a three-item list, transition words, or one rhetorical pattern are not evidence of authorship. Edit the defect, not an imagined origin.

## Rewrite protocol for a meaning-sensitive sentence

Before proposing wording:

1. state the atomic proposition(s);
2. identify actor, action/relation, object, condition, comparison, time, and uncertainty;
3. determine the evidence level;
4. preserve terms, numbers, symbols, citations, and negation;
5. write the smallest Persian revision that improves clarity;
6. explain any remaining ambiguity.

When two scientifically plausible interpretations exist, offer alternatives and request an author decision in the issue report.
