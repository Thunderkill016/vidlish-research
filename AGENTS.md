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
5. **Product assumption** — what still needs to be tested in Nếp/Vidlish.

## 3. Preserve uncertainty

Always record population, proficiency, intervention, comparison, outcome and limitations when they matter. A result on university EFL students is not automatically evidence for Vietnamese adults near A0.

## 4. Prefer evidence hierarchy, but match the question

Prefer systematic reviews, meta-analyses, high-quality handbooks/guidelines, replications and controlled studies. Product usability questions still require product experiments; a meta-analysis cannot decide the best button interaction for Nếp.

## 5. CEFR is descriptive, not a teaching algorithm

CEFR can define communicative activities, proficiency descriptors and can-do goals. Do not treat CEFR levels as proof of a learning sequence or scheduling algorithm.

## 6. Product benchmarks are not efficacy studies

Duolingo, Language Reactor, LingQ, Readlang, Anki and other products may inspire interaction patterns. A competitor feature does not become a learning principle merely because it exists.

## 7. Do not infer mastery from engagement

Streaks, completion, watch time, clicks, session count and review scheduling can measure behavior. Do not label them comprehension, recall, transfer, retention or proficiency without a validated relationship.

## 8. Attempt before reveal when the goal is retrieval

If a feature claims to practice retrieval, the full answer cannot already be visible. Recognition, comprehension and retrieval are different task types and must be labeled correctly.

## 9. Do not over-generalize Vietnamese learner research

Vietnamese-specific phonology, grammar or strategy findings can guide candidate interventions. Never turn one study into a stereotype about all Vietnamese learners.

## 10. AI-generated content requires provenance and gates

A model may propose examples, feedback or variants, but it cannot be the authority for source facts, learner readiness or mastery. Generated learning assets require deterministic checks and/or editorial review appropriate to their risk.

## 11. Every feature research spec must include

- learner problem;
- target capability;
- linked research claims;
- mechanism;
- proposed behavior;
- risks / alternative explanations;
- what would falsify the assumption;
- experiment or validation plan;
- learning metric separate from engagement metric.

## 12. Stable IDs

Use these prefixes:

- `SRC-` source
- `CLM-` claim
- `SYN-` synthesis
- `PRN-` product principle
- `FEAT-` feature research spec
- `RQ-` research question
- `EXP-` experiment
- `ADR-` decision record

Never reuse an ID after deletion. Deprecate instead.

## 13. Machine-readable files are indexes, not replacements

`data/*.json` contains concise representations for retrieval and validation. Markdown notes remain the place for nuance, limitations and reasoning.
