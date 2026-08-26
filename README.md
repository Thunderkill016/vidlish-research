# Vidlish Research

> Evidence base for building **Nếp / Vidlish** into an English-learning product that can explain *why* each learning feature exists, what evidence supports it, what is still uncertain, and how the product should test the claim.

This repository is **not** the product codebase. It is the product's research and decision layer.

## Core flow

```text
SOURCE
  ↓
CLAIM
  ↓
EVIDENCE QUALITY
  ↓
LEARNING PRINCIPLE
  ↓
PRODUCT IMPLICATION
  ↓
VIDLISH / NẾP FEATURE
  ↓
EXPERIMENT
  ↓
RESULT
  ↓
UPDATE THE KNOWLEDGE BASE
```

A paper, book, benchmark or opinion is not a feature requirement by itself. A product feature must be traceable through this chain.

## Why this repo exists

The current Vidlish codebase already contains useful A0 research and a product master plan. This repository separates that knowledge from implementation so that:

- research can grow without being buried in application code;
- agents can retrieve small, structured notes instead of a giant document;
- claims, assumptions and product decisions do not get mixed together;
- every learning feature can link back to evidence and explicit uncertainty;
- experiments can change product beliefs without rewriting history.

## Current target learner

Initial research focuses on a Vietnamese-speaking adult beginning near A0 and progressing toward independent everyday/work English use. This is a product scope, not a claim that every learner has identical needs.

## Evidence levels

| Level | Meaning |
| --- | --- |
| **A — Strong** | Multiple high-quality syntheses / meta-analyses / converging evidence relevant to the claim. |
| **B — Moderate** | Several relevant controlled studies or one strong synthesis with meaningful scope limitations. |
| **C — Preliminary** | Limited studies, indirect evidence, small samples, or weak transfer to the target learner/context. |
| **D — Hypothesis** | Plausible mechanism with insufficient direct evidence for the concrete product claim. |
| **E — Product assumption** | Product/design decision that must be tested with learners; not presented as scientific evidence. |

Evidence level is attached to a **claim**, not to a whole source.

## Repository map

- [`RESEARCH_MAP.md`](./RESEARCH_MAP.md) — research tracks and open questions.
- [`AGENTS.md`](./AGENTS.md) — mandatory rules for AI agents working with this knowledge base.
- [`00-foundations/`](./00-foundations/) — frameworks and learning model.
- [`01-skills/`](./01-skills/) — listening, vocabulary, speaking, pronunciation, reading, writing.
- [`02-video-learning/`](./02-video-learning/) — captions, transcripts, replay and video-specific questions.
- [`04-learners/`](./04-learners/) — target learner constraints and Vietnamese-specific research.
- [`05-products/`](./05-products/) — integrated product decision/handoff specs plus benchmark rules.
- [`06-evidence/`](./06-evidence/) — source registry and evidence handling rules.
- [`07-syntheses/`](./07-syntheses/) — cross-source conclusions and integrated system synthesis.
- [`08-product-principles/`](./08-product-principles/) — principles and anti-patterns derived from evidence.
- [`09-vidlish-features/`](./09-vidlish-features/) — research specs for concrete product features.
- [`10-experiments/`](./10-experiments/) — product experiments that can confirm or reject assumptions.
- [`decisions/`](./decisions/) — durable research/product decision records.
- [`data/`](./data/) — machine-readable sources, claims, principles and feature links.
- [`templates/`](./templates/) — required note formats.

## Nếp v1 integrated product handoff

`RQ-001` through `RQ-021` are now integrated into an implementation-facing product layer rather than remaining only as independent research feature specs.

Start with:

1. [`05-products/nep-v1-executable-product-spec.md`](./05-products/nep-v1-executable-product-spec.md) — what Nếp v1 is and how the learner experiences it.
2. [`05-products/nep-v1-runtime-architecture.md`](./05-products/nep-v1-runtime-architecture.md) — engine/service boundaries and runtime contracts.
3. [`05-products/nep-v1-learner-model-evidence-contract.md`](./05-products/nep-v1-learner-model-evidence-contract.md) — what learner evidence means and what the runtime may infer.
4. [`05-products/nep-v1-build-slices.md`](./05-products/nep-v1-build-slices.md) — implementation order for proving the first complete learning loop before expanding content.

Cross-RQ synthesis:

- [`07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md`](./07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md)

Accepted architecture decisions:

- [`decisions/ADR-002-capability-evidence-runtime.md`](./decisions/ADR-002-capability-evidence-runtime.md)
- [`decisions/ADR-003-progressive-placement-bootstrap.md`](./decisions/ADR-003-progressive-placement-bootstrap.md)
- [`decisions/ADR-004-ai-is-mediated-not-authoritative.md`](./decisions/ADR-004-ai-is-mediated-not-authoritative.md)

These docs do not replace the application codebase. They define the product/evidence contracts that implementation should preserve.

## Research workflow

1. Open a research question (RQ).
2. Search for high-quality sources and record provenance.
3. Extract narrowly worded claims; do not summarize a whole paper into one sweeping conclusion.
4. Record population, task, outcome, effect direction, limitations and transfer risk.
5. Assign evidence level to the claim.
6. Synthesize across sources.
7. Translate the synthesis into a product implication.
8. If the implication is still a product assumption, design an experiment instead of presenting it as truth.
9. Update `data/*.json` so agents can retrieve the relationship programmatically.

## Product contract

Research should help Nếp answer four separate questions about learning evidence:

- `understood` — did the learner comprehend the target input?
- `recalled` — could the learner retrieve/use the target without the full answer visible?
- `transferred` — could the learner use/understand it in a changed or unseen context?
- `retained` — could the learner still do it after a delay?

Completion, streaks, watch time, number of cards, or an SRS schedule are not automatically evidence of any of those outcomes.

## First research priorities

1. A0 adult second-language acquisition.
2. Vocabulary/chunk acquisition and coverage.
3. Listening perception and comprehension.
4. Retrieval practice and spaced review.
5. Output progression from controlled to guided use.
6. Pronunciation for intelligibility, including Vietnamese-specific difficulties.
7. Graded reading/audio and when authentic input becomes usable.
8. Caption/subtitle/replay behavior once video becomes appropriate.
9. Assessment of transfer and retention.
10. Motivation, session design and return behavior as product questions, not substitutes for learning outcomes.

## Relationship to `Thunderkill016/vidlish`

The application repository remains the implementation source of truth. This repository owns research rationale. Product documents should link to stable research IDs rather than duplicate full research notes.

Initial content here was normalized from the existing Vidlish A0 research dossier and master plan. It should be expanded source-by-source rather than copied forward as one monolithic document.
