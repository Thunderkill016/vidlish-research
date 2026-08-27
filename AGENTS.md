# AGENTS.md — Research rules

These rules apply to every human or AI agent editing this repository.

## 1. Never invent evidence

Do not create citations, DOI values, publication details, effect sizes, quotes or URLs from memory when they cannot be verified. If a source cannot be verified, mark it `unverified` and do not use it to raise confidence.

## 2. Separate five different things

Never collapse these into one statement:

1. **Source finding** — what a source actually reports.
2. **Claim** — a narrow proposition supported or challenged by evidence.
3. **Synthesis** — what multiple sources jointly suggest.
4. **Product implication** — what the evidence makes reasonable to build.
5. **Product assumption** — what still needs to be tested in Nếp.

## 3. Preserve uncertainty

Always record population, proficiency, intervention, comparison, outcome and limitations when they matter. A result on university EFL students is not automatically evidence for Vietnamese adults near A0.

## 4. Prefer evidence hierarchy, but match the question

Prefer systematic reviews, meta-analyses, high-quality handbooks/guidelines, replications and controlled studies. Product usability questions still require product experiments; a meta-analysis cannot decide the best button interaction for Nếp.

Do not confuse hierarchy with directness. A high-quality meta-analysis can still be indirect for the target population, construct or self-study context.

## 5. Record competing evidence before resolving a controversy

For contested instructional questions, do not search only for evidence supporting the current product idea.

Record:

- competing positions;
- supporting and contradictory/null evidence;
- outcome measures used;
- proficiency/population/task moderators;
- methodological limitations;
- what evidence would change the current synthesis.

A clean synthesis is not evidence that the underlying literature is unanimous.

## 6. Separate evidence quality from directness

The compact `A–E` claim label may remain, but meta-foundation work must separately consider when possible:

- methodological quality;
- directness to the target population;
- directness to the target construct/outcome;
- replication/consistency;
- transfer directness to the intended product context.

Do not mechanically average these into one score.

`00-foundations/EVIDENCE_GRADING_PROTOCOL.md` owns the detailed appraisal protocol. High-impact method claims should receive an `EVA-*` assessment and be checked against any relevant `CTR-*` controversy before being promoted into `SYN-METHOD-001`.

## 7. CEFR is descriptive, not a teaching algorithm

CEFR can define communicative activities, proficiency descriptors and can-do goals. Do not treat CEFR levels, grammar profiles or inventory coverage as proof of a learning sequence or scheduling algorithm.

## 8. Needs and language-use evidence precede curriculum content

Do not choose the first capabilities, words, chunks or constructions solely because they appear in a framework, textbook, frequency list or prior implementation.

Content selection must eventually combine target-needs evidence with appropriate corpus/usage, learnability and prerequisite evidence.

## 9. Product benchmarks are not efficacy studies

Duolingo, Speak, ELSA, Babbel, Busuu, LingQ, Memrise and other products may inspire hypotheses or interaction patterns. A competitor feature does not become a learning principle merely because it exists.

## 10. Do not infer mastery from engagement

Streaks, completion, watch time, clicks, session count and review scheduling can measure behavior. Do not label them comprehension, recall, transfer, retention or proficiency without a validated relationship.

## 11. Attempt before reveal when the goal is retrieval

If a feature claims to practice retrieval, the full answer cannot already be visible. Recognition, comprehension and retrieval are different task types and must be labeled correctly.

## 12. A skill claim requires a task that actually elicits that skill

Typing is not speaking. Reading an answer aloud is not independent spoken retrieval. Translation recall with the communicative intention already supplied is not automatically spontaneous transfer. A realistic scenario label does not guarantee ecological or construct validity.

Task labels must describe the observable behavior actually elicited.

## 13. Assessment validity is an inference problem

Do not assume a task is valid because it looks realistic or because a schema calls it `listening`, `speaking`, `transfer`, `fluency` or `mastery`.

Always ask:

```text
what construct?
→ what task observation?
→ what scoring process?
→ what support/contamination?
→ what inference?
→ how far may it generalize?
```

`RQ-024` owns the comprehensive validity framework. Preserve conservative learner-state claims when validity evidence is incomplete.

## 14. Do not over-generalize Vietnamese learner research

Vietnamese-specific phonology, grammar, processing or strategy findings can guide candidate interventions. Never turn one study into a stereotype about all Vietnamese learners.

Population evidence is a prior. Individual learner evidence should be able to override it.

## 15. AI-generated content requires provenance and gates

A model may propose examples, feedback, summaries or variants, but it cannot be the authority for source facts, learner readiness or mastery. Generated learning assets require deterministic checks and/or editorial/empirical validation appropriate to their risk.

Do not use AI confidence or persuasive rationale as pedagogical evidence.

## 16. Research comes before the new implementation

`ADR-005` is active.

The current order is:

```text
verified research
→ competing-evidence synthesis
→ Nếp Method
→ curriculum specification
→ validation slices
→ product specification
→ implementation
```

The existing Vidlish application is a legacy prototype, not a pedagogical source of truth.

The pre-meta-foundation documents in `05-products/` and `SYN-SYS-001` are provisional. They may not override the accepted Method.

## 17. Do not turn a local result into a global method

Never infer:

```text
one supported mechanism
→ universal teaching method
```

or:

```text
many individually plausible features
→ optimal integrated system
```

Integration requires explicit evidence/controversy synthesis and target validation.

## 18. Experiment plans are not results

`EXP-*` files define falsifiable plans. They do not support a product claim until corresponding learner data/results exist.

Do not write `validated`, `proven`, `effective` or equivalent merely because an experiment is well designed.

## 19. Every feature research spec must include

- learner problem;
- target capability;
- linked research claims;
- mechanism;
- proposed behavior;
- risks / alternative explanations;
- what would falsify the assumption;
- experiment or validation plan;
- learning metric separate from engagement metric.

## 20. Stable IDs

Use these prefixes:

- `SRC-` source
- `CLM-` claim
- `SYN-` synthesis
- `PRN-` product principle
- `FEAT-` feature research spec
- `RQ-` research question
- `EXP-` experiment / validation plan
- `ADR-` decision record
- `EVA-` multidimensional evidence assessment
- `CTR-` controversy / contradiction record

Never reuse an ID after deletion. Deprecate instead.

## 21. Machine-readable files are indexes, not replacements

`data/*.json` contains concise representations for retrieval and validation. Markdown notes remain the place for nuance, contradictions, limitations and reasoning.

A graph that passes referential validation is not automatically scientifically valid.

`EVA-*` and `CTR-*` records make evidence quality/directness and unresolved disagreement machine-readable; they still require substantive human/agent reasoning and source verification.

## 22. Evidence governance is active

`RQ-028` and `00-foundations/EVIDENCE_GRADING_PROTOCOL.md` are active.

High-impact method/curriculum claims should separate evidence quality from target directness with `EVA-*` appraisal where decision risk warrants it. Credible disagreements that can change a decision should remain visible as `CTR-*` records.

Null, negative and boundary-condition evidence must not be deleted simply because it makes the synthesis less clean.

## 23. `SYN-METHOD-001` is the provisional pedagogical source of truth

After the P12/P13 audit, `07-syntheses/SYN-METHOD-001-nep-method-v0.md` is the current pedagogical parent for new curriculum work.

This means:

- curriculum rules must be derivable from the Method or be explicitly labeled validation hypotheses;
- `SYN-SYS-001`, the legacy Vidlish curriculum and old `05-products/` plans cannot override the Method;
- implementation convenience cannot silently weaken construct/evidence boundaries;
- the Method itself remains falsifiable and may be narrowed or revised by target learner results;
- changes to core Method constraints must follow `00-foundations/NEP_METHOD_VALIDATION_CONTRACT.md` change control.

The Method is **not** a claim of integrated efficacy or optimality.

## 24. Do not jump from Method directly to a full app

The next order is:

```text
SYN-METHOD-001
→ direct target-needs confirmation
→ curriculum contract
→ small construct-faithful capability slices
→ dogfood
→ Vietnamese near-A0 pilot
→ comparative delayed/changed-context validation
→ revise
→ broader product specification
```

Do not build hundreds of lessons, a complete CEFR path, or a broad feature surface before the first capability slices pass the relevant validation gates.
