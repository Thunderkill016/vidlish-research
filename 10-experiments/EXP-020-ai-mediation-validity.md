# EXP-020 — Role-gated AI mediation validity

**Experiment ID:** `EXP-020`  
**Research question:** `RQ-020`  
**Feature:** `FEAT-AIG-001`

## Question

Does role-gated AI mediation improve delayed, changed-context English learning per learner minute for Vietnamese near-A0/A1 adults without increasing false feedback, false evidence, synthetic-speech dependence or privacy exposure?

## Why this experiment exists

Existing research supports useful average effects for chatbots and shows promising narrow uses of LLM assessment and TTS. It does not establish that Nếp should allow one AI system to generate, teach, correct, score, speak and update learner state without separate validation.

## Population

Target Vietnamese-speaking adults near A0 / low A1 in mobile-first use. Record baseline vocabulary/listening, prior chatbot use and device/audio conditions. Dialect/background is optional and only used when relevant.

## Arms

### A — Curated / deterministic baseline

Curated tasks, human audio where available, deterministic answer keys, existing validated domain rules and no free-form LLM scoring.

### B — Unrestricted AI

LLM may generate variants, explain, give feedback, evaluate and converse; TTS may be freely used with only basic safety/schema handling.

This tests the attractive assumption:

```text
better model
→ let it handle the learning loop
```

### C — Role-gated AI

Use `FEAT-AIG-001`: role declaration, curriculum constraints, deterministic validation, bounded feedback scopes, no unvalidated mastery update, complete model/prompt/rubric/TTS provenance, natural/human transfer probes, privacy-minimized context and regression-tested configurations.

### D — Gated AI + selective escalation

Same as C plus a second checker, deterministic parser, sampled human reference or no-judgment path for uncertain high-value decisions.

Keep D only if added validity is worth cost/latency.

## Content domains

Include vocabulary/chunks, controlled constructions, short writing, short listening, controlled speaking/interaction and changed-context transfer. Do not let essay writing stand in for the multimodal product.

## TTS subtest

Match semantic content across human recording versus TTS.

Measure immediate comprehension, word/chunk recognition, later unseen human-speech recognition, support dependence and an effort/friction proxy.

Critical question:

```text
learning with TTS
→ later understand new human speech?
```

## Feedback subtest

Use a human-adjudicated research set containing true errors, acceptable variants, no-error responses, ambiguous cases, Vietnamese-L1 likely errors and grammar/chunk/pragmatic distinctions.

Measure precision, recall, false-correction rate, abstention rate and issue-type coverage. Do not report precision alone.

## Evaluator subtest

For AI scoring, compare to independent human/rule references; measure absolute agreement and ranking separately; inspect severity, score compression and halo behavior; analyze by task/construct; repeat calls where stochasticity matters.

A rater must pass critical slices, not only aggregate correlation.

## Conversation subtest

Compare AI-interaction success with later different-model / less-accommodating interaction and a human-rated or human-partner sample where feasible.

Track whether the chatbot silently repairs intent, rephrases the learner, supplies missing language, ignores unclear pronunciation or accepts pragmatically odd responses.

## Drift test

Freeze a regression bank. After model/provider/prompt/rubric updates, rerun it, compare aggregate metrics and inspect critical slices. Block evidence authority when preregistered regression thresholds fail.

Include at least one model or prompt migration if feasible.

## Primary learning outcome

```text
delayed changed-context capability gain
---------------------------------------
learner learning minutes
```

Use tasks not generated from the learner's just-seen examples.

## Reliability guardrails

- false corrective-feedback rate;
- false positive learner-error rate;
- missed-issue rate where reference labels exist;
- AI-created curriculum/prerequisite violation rate;
- evaluator disagreement rate;
- unsupported mastery-update count;
- TTS-to-human transfer gap;
- AI-to-less-accommodating interaction transfer gap.

## Operational guardrails

- inference cost per learner;
- cost per retained/transfer gain;
- latency and fallback rate;
- third-party data classes/volume sent;
- raw learner-data retention;
- learner reports of clearly wrong feedback.

## Decision logic

C beats A only if learning gain/minute improves, or equivalent learning is delivered with materially better useful practice/cost, while false evidence and false correction stay under threshold.

B beats C only if unrestricted AI provides meaningfully better learning/cost without materially worse false correction, evidence validity, support dependence, transfer or privacy exposure.

D beats C only if escalation reduces harmful errors enough to justify extra complexity/cost.

## Falsification

Simplify or remove `FEAT-AIG-001` if gated AI does not improve learning or useful scalability over curated flows, if gates add friction without reducing meaningful error, or if model drift makes evidence-producing AI too costly to maintain.

Narrow authority if one construct shows clustered false correction, if a model is reliable as generator but not evaluator, if TTS learning fails to transfer to natural speech, or if chatbot success fails to transfer to less-accommodating/human interaction.

## Must preregister

- sample size / stopping rule;
- assignment procedure;
- delay intervals;
- reference-rater procedure;
- false-correction tolerance;
- authority allowed per arm;
- exact model/provider/prompt/rubric versions;
- TTS voice(s);
- migration/drift threshold;
- cost accounting;
- missing-data/dropout handling.

## Success condition

The winner is the **smallest AI authority layer** that improves real learning and useful practice while preserving evidence integrity.

This experiment is not intended to prove that “AI works.” It is intended to discover what AI is allowed to do in Nếp.
