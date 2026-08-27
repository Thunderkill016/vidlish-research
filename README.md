# Vidlish Research

> Evidence base for deriving **Nếp** from research before committing to a teaching method, curriculum or product implementation.

This repository is **not** the product codebase. It is the project's research and decision layer.

## Current phase — meta-foundation before Nếp Method

`RQ-001` through `RQ-021` produced substantial feature-level evidence. A subsequent meta-audit found that several high-leverage foundations are still incomplete, especially:

- competing SLA/instructional theories;
- target-needs and capability selection;
- language-assessment validity and learner-state inference;
- corrective feedback;
- individual differences / anxiety / motivation / self-regulation;
- corpus-informed beginner content selection;
- evidence grading, contradiction and update methodology.

Therefore the current integrated Nếp v1 documents are **provisional hypotheses**, not the final teaching method and not implementation authority.

Read first:

1. [`00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md`](./00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md) — what a sufficiently comprehensive research program must cover.
2. [`07-syntheses/META-001-research-coverage-validity-audit.md`](./07-syntheses/META-001-research-coverage-validity-audit.md) — what the first 21 RQs cover well and what is still missing.
3. [`decisions/ADR-005-research-first-reset.md`](./decisions/ADR-005-research-first-reset.md) — why research now precedes any new build.
4. [`RESEARCH_MAP.md`](./RESEARCH_MAP.md) — research tracks and open questions.

The required order is now:

```text
VERIFIED SOURCES
  ↓
CLAIMS + COMPETING EVIDENCE
  ↓
FOUNDATIONAL / SKILL SYNTHESIS
  ↓
NẾP METHOD
  ↓
CURRICULUM SPECIFICATION
  ↓
PRODUCT SPECIFICATION
  ↓
NEW IMPLEMENTATION
  ↓
LEARNER OUTCOME DATA
  ↓
UPDATE THE KNOWLEDGE BASE
```

## Research flow

For an individual research question or product hypothesis:

```text
SOURCE
  ↓
CLAIM
  ↓
EVIDENCE QUALITY + DIRECTNESS + LIMITS
  ↓
SYNTHESIS / COMPETING EXPLANATIONS
  ↓
LEARNING PRINCIPLE OR OPEN ASSUMPTION
  ↓
EXPERIMENT / VALIDATION
  ↓
RESULT
  ↓
UPDATE THE KNOWLEDGE BASE
```

A paper, book, benchmark or opinion is not a feature requirement by itself. Likewise, a collection of individually sensible features is not automatically a validated teaching method.

## Why this repo exists

The earlier Vidlish application accumulated multiple AI-assisted product directions. This repository exists so that pedagogy can be reconstructed from evidence rather than inherited from implementation.

It allows:

- research to grow independently of legacy application code;
- agents to retrieve structured evidence instead of relying on persuasive prose;
- claims, assumptions and product decisions to remain distinct;
- competing theories and contradictory findings to be represented explicitly;
- every later curriculum/product decision to trace back to evidence and uncertainty;
- learner experiments to revise beliefs without rewriting history.

## Current target learner

Initial research focuses on a Vietnamese-speaking adult beginning near zero / Pre-A1 and progressing toward independent everyday/work English use. This is a research/product scope, not a claim that every Vietnamese learner has identical needs.

The final target-capability set remains an open research question until needs-analysis work is completed.

## Evidence levels

| Level | Meaning |
| --- | --- |
| **A — Strong** | Multiple high-quality syntheses / meta-analyses / converging evidence relevant to the claim. |
| **B — Moderate** | Several relevant controlled studies or one strong synthesis with meaningful scope limitations. |
| **C — Preliminary** | Limited studies, indirect evidence, small samples, or weak transfer to the target learner/context. |
| **D — Hypothesis** | Plausible mechanism with insufficient direct evidence for the concrete product claim. |
| **E — Product assumption** | Product/design decision that must be tested with learners; not presented as scientific evidence. |

Evidence level is attached to a **claim**, not to a whole source.

`META-001` found that this compact scale is not sufficient for final method synthesis. New foundation work must also preserve separate judgments of methodological quality, population directness, construct directness, replication/consistency and transfer to the product context.

## Repository map

- [`RESEARCH_MAP.md`](./RESEARCH_MAP.md) — research tracks and open questions.
- [`AGENTS.md`](./AGENTS.md) — mandatory rules for AI agents working with this knowledge base.
- [`00-foundations/`](./00-foundations/) — SLA/ISLA field coverage, frameworks and learning-model hypotheses.
- [`01-skills/`](./01-skills/) — listening, vocabulary, speaking, pronunciation, reading, writing.
- [`02-video-learning/`](./02-video-learning/) — captions, transcripts, replay and video-specific questions.
- [`04-learners/`](./04-learners/) — target learner constraints and Vietnamese-specific research.
- [`05-products/`](./05-products/) — provisional product synthesis/history plus benchmark rules; not current build authority.
- [`06-evidence/`](./06-evidence/) — source registry and evidence handling rules.
- [`07-syntheses/`](./07-syntheses/) — RQ syntheses, meta-audits and eventually `SYN-METHOD-*`.
- [`08-product-principles/`](./08-product-principles/) — evidence-linked principles and anti-patterns.
- [`09-vidlish-features/`](./09-vidlish-features/) — research specs for candidate features; feature existence does not imply it belongs in the final method/product.
- [`10-experiments/`](./10-experiments/) — experiment plans; they remain hypotheses until result artifacts exist.
- [`decisions/`](./decisions/) — durable research/product decision records.
- [`data/`](./data/) — machine-readable sources, claims, principles and feature links.
- [`templates/`](./templates/) — required note formats.

## Provisional pre-meta-foundation product artifacts

The following documents integrated `RQ-001`–`RQ-021` before `META-001` identified missing foundations:

- [`07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md`](./07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md)
- [`05-products/nep-v1-executable-product-spec.md`](./05-products/nep-v1-executable-product-spec.md)
- [`05-products/nep-v1-runtime-architecture.md`](./05-products/nep-v1-runtime-architecture.md)
- [`05-products/nep-v1-learner-model-evidence-contract.md`](./05-products/nep-v1-learner-model-evidence-contract.md)
- [`05-products/nep-v1-build-slices.md`](./05-products/nep-v1-build-slices.md)

Keep them as useful hypotheses and design history. Do **not** treat them as the final Nếp Method or instructions to begin a new build.

## Research workflow

1. Define a research question and its decision relevance.
2. Map competing positions before choosing search terms that favor one answer.
3. Search for high-quality sources and record provenance.
4. Extract narrowly worded claims; do not summarize a whole paper into one sweeping conclusion.
5. Record population, task, outcome, effect direction, delayed/transfer evidence, limitations and target-population directness.
6. Separate methodological quality from directness to the target learner/product.
7. Record contradictory/null evidence and moderators, not only support.
8. Synthesize across sources and competing explanations.
9. Translate only justified conclusions into principles; keep product-specific choices as assumptions.
10. Design validation where literature cannot answer the concrete product question.
11. Update machine-readable indexes and preserve revision history.

## Current learner-evidence hypothesis

Existing research has found it useful to keep at least these task/time evidence categories distinct:

- `understood` — meaning comprehension under recorded conditions;
- `recalled` — retrieval/use without the full answer visible;
- `transferred` — performance in a changed or unseen context;
- `retained` — performance after a meaningful delay.

These categories are **not accepted as four independent psychological traits**. `RQ-024` must establish what learner-state inferences they can validly support and with what uncertainty.

Completion, streaks, watch time, number of cards, SRS state, AI confidence or feature usage are not automatically evidence of any of those outcomes.

## Relationship to `Thunderkill016/vidlish`

`Thunderkill016/vidlish` is now treated as a **legacy prototype**, not the pedagogical source of truth.

It can later contribute selectively reusable engineering infrastructure, production lessons or code patterns. Its existing curriculum, UX, feature labels and learner-state logic do not constrain the new research-derived method.

No legacy implementation behavior is evidence of teaching efficacy.

## Next milestone

Close the meta-foundation RQs defined by `META-001`, then produce:

```text
SYN-METHOD-001 — Nếp Method v0
```

Only after that synthesis passes the gates in `ISLA_FIELD_COVERAGE_FRAMEWORK.md` should the project freeze a curriculum specification and design a new implementation.