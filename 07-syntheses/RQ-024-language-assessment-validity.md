# RQ-024 — Language-assessment validity and learner-state inference

**Status:** initial meta-foundation synthesis complete  
**Date:** 2026-08-27  
**Claims:** `CLM-VAL-001`–`CLM-VAL-020`  
**Evidence digest:** `06-evidence/RQ-024-source-digest.md`

## 1. Decision summary

Nếp must stop treating learner state as a direct property read from an answer.

The correct architecture is:

```text
OBSERVATION
↓
EVALUATION
↓
INFERENCE
↓
UNCERTAINTY
↓
DECISION
```

Every arrow must be justified for the claim being made.

The most important rule from RQ-024 is:

```text
one correct response
≠
one true learner state
```

A learner state is an inference from evidence under known conditions.

## 2. Replace `mastered` with evidence-bearing claims

This is not acceptable as the foundational model:

```ts
{ word: "receipt", mastered: true }
```

because it hides:

- whether the learner saw or heard the word;
- whether the task was recognition or recall;
- whether translation/model/caption was visible;
- whether this was first exposure or the tenth retry;
- whether the evidence is immediate or delayed;
- whether a new context was used;
- who/what scored the response;
- how reliable/generalizable the observation is.

A safer conceptual model is:

```text
CAPABILITY CLAIM
+
EVIDENCE HISTORY
+
CONDITIONS
+
UNCERTAINTY
```

## 3. Evidence-state taxonomy

RQ-024 proposes six distinct states of inference.

These are **not psychological learning stages**. They are epistemic labels describing what Nếp currently has evidence to claim.

### E0 — Task-bound observation

Example:

```text
On task X,
first-seen audio,
normal speed,
no text support,
learner selected the correct intended meaning.
```

This is the strongest literal description of the event.

### E1 — Generalization candidate

There are multiple relevant observations across parallel tasks, but evidence is still insufficient to claim stable target capability confidently.

### E2 — Independent current capability

Converging unsupported evidence across sufficiently representative observations supports a current capability claim.

The exact threshold is not established and must be validated.

### E3 — Mediated/emerging capability

The learner cannot yet perform independently but succeeds or improves under known graduated support.

This is useful for adaptation but must not overwrite E2.

### E4 — Delayed-retention evidence

The target capability is successfully demonstrated after a relevant delay under conditions that do not simply reveal the answer.

### E5 — Changed-context transfer evidence

The learner succeeds on a meaningfully changed task/context representative of the intended target-domain generalization.

These can coexist.

A learner might have:

```text
E2 strong current listening evidence
E4 weak/old retention evidence
E5 no interaction transfer evidence
E3 low support need on a new construction
```

There is no need to compress this into one `mastery = 0.81` unless a downstream model has a validated reason to do so.

## 4. The core inference contract

Every capability should eventually define:

### 4.1 Target claim
What are we claiming the learner can do?

Example:

```text
Understand a short café confirmation question on first hearing.
```

Not:

```text
knows café English
```

### 4.2 Target-language-use domain
What real or pedagogically relevant domain should the claim generalize to?

This connects directly to RQ-023.

### 4.3 Eliciting task
What task gives the learner a genuine opportunity to demonstrate the capability?

### 4.4 Conditions
Record at least when relevant:

- modality;
- first-seen/repeated;
- playback rate;
- support visible;
- hint/model/translation;
- interlocutor/task type;
- response mode;
- context novelty;
- time since previous learning/exposure.

### 4.5 Evaluation rule
How does the work product become an observation?

Possible evaluators:

- deterministic rule;
- human;
- ASR;
- LLM;
- hybrid.

The evaluator is part of the evidence chain, not an invisible implementation detail.

### 4.6 Generalization warrant
Why should this observation represent more than this exact item?

### 4.7 Extrapolation warrant
Why should parallel-task performance say anything about the actual target capability/domain?

### 4.8 Decision rule
What action may the product take from the claim, and what is the cost if wrong?

## 5. Support does not erase evidence; it changes the claim

Old bad model:

```text
failed
→ show translation
→ correct
→ mastered
```

RQ-024 requires:

```text
independent attempt failed
+
translation-supported attempt succeeded
```

Possible inference:

```text
independent capability not demonstrated
meaning can be recovered under L1 support
```

That second observation is pedagogically useful.

It can help answer:
- what support works;
- how close the learner is to success;
- what to present next.

It cannot retroactively transform the original failed independent attempt into success.

## 6. First-seen versus repeated evidence

A similar rule applies to replay/retry.

```text
first hearing: fail
second exact replay: success
```

is evidence of something useful:

- additional processing time/exposure helps;
- the item may be within repair range.

But it is not evidence that the learner succeeded on first encounter.

Therefore:

```text
firstSeen
exposureIndex
replayCount
```

belong to evidence provenance.

## 7. Modality is part of the construct

Do not do this:

```text
recognizes “receipt” in written MCQ
→ listening word known
→ speaking word available
```

Instead:

```text
written recognition evidence
spoken-form recognition evidence
productive retrieval evidence
```

may be related but remain separately observable until evidence justifies an aggregate.

The same applies to grammar/constructions:

```text
can explain rule
≠
can interpret cue online
≠
can produce it under communicative pressure
```

This directly integrates RQ-022’s explicit/implicit and receptive/productive distinctions.

## 8. Generalization requires task sampling

One item can be misleading because of:

- lucky guessing;
- familiarity with one exemplar;
- prompt idiosyncrasy;
- topic knowledge;
- task difficulty;
- rating variation.

Therefore broader claims require representative observations.

The principle is not:

```text
always require N = 5
```

The principle is:

```text
claim breadth / decision stakes ↑
→ required task diversity / evidence strength ↑
```

This keeps the learner experience efficient while preserving epistemic honesty.

## 9. Transfer is an extrapolation problem

RQ-005 already separated exact repetition from transfer.

RQ-024 explains why:

```text
performance on training item
→ target-domain performance
```

is an extrapolation inference.

The system should ask:

- what changed?
- is that change meaningful?
- does it represent the target domain?
- did the learner still succeed without answer-bearing support?

Transfer therefore belongs to evidence architecture, not only to an optional final quiz.

## 10. Retention is a temporal inference

A scheduler may estimate retrievability.

That estimate is not itself retained language evidence.

To claim retention:

```text
learner must perform after delay
```

under an appropriate probe.

No universal delay is established by RQ-024.

The relevant horizon depends on:
- capability;
- product decision;
- learning objective.

This preserves the distinction:

```text
memory model prediction
≠
observed retained capability
```

## 11. Automated evaluation contract

AI/ASR can remain useful, but every automated judgment needs provenance.

Minimum research contract:

```ts
scorerType
provider
model
version
prompt/rubric version when relevant
confidence or uncertainty if meaningful
disagreement / fallback path
```

### Do not use human agreement as the only validator

A model can match human raters while both are misaligned with the intended construct or biased for a subgroup.

Validation should therefore examine:

```text
model ↔ human agreement
+
construct relevance
+
subgroup performance
+
target-domain / downstream prediction
+
disagreement cases
```

### Model drift

If the underlying service changes, old validation evidence may no longer apply fully.

Model/version should therefore be stored with evidence that depends on automated scoring.

## 12. Consequence-sensitive thresholds

Nếp should not use one confidence threshold for every action.

### Lower-stakes action

Example:

```text
choose one more practice example
```

A noisy provisional estimate may be enough.

### Higher-stakes action

Example:

```text
skip a prerequisite
stop review
claim durable mastery
unlock an advanced interaction sequence
```

requires stronger evidence.

This suggests:

```text
required evidence
∝
cost of wrong decision
+
breadth of claim
```

Exact decision costs remain empirical.

## 13. Learner model should preserve contradictions

Real evidence will conflict.

Example:

```text
Task A: independent success
Task B: independent failure
Task C: success after hint
Delayed task: failure
```

A weak learner model overwrites history with the newest boolean.

A stronger model stores the contradiction and asks why:

- task difference?
- context change?
- scorer noise?
- forgetting?
- support dependence?
- unstable acquisition?

RQ-028 will specify how the research knowledge base handles scientific contradiction; RQ-024 establishes the same need at learner-evidence level.

## 14. Candidate evidence record

Research-level, not implementation schema:

```ts
type LanguageEvidence = {
  evidenceId: string;
  capabilityId: string;
  taskId: string;

  conditions: {
    modality: string;
    responseMode: string;
    firstSeen: boolean;
    exposureIndex: number;
    supportState: string[];
    noveltyProfile?: string[];
    delaySinceLearningMs?: number;
  };

  evaluation: {
    scorerType: "rule" | "human" | "asr" | "llm" | "hybrid";
    model?: string;
    version?: string;
    score?: number;
    confidence?: number;
    disagreement?: number;
  };

  observation: string;
  inferenceTarget:
    | "task_observation"
    | "generalization_candidate"
    | "independent_current_capability"
    | "mediated_emerging_capability"
    | "delayed_retention"
    | "changed_context_transfer";

  inferenceConfidence?: number;
};
```

## 15. What this changes in earlier research

RQ-024 does not delete RQ-001–RQ-021.

It changes how their evidence language should be interpreted.

Especially:

- vocabulary evidence becomes task-conditional;
- listening diagnostic states require explicit inference bounds;
- scheduler states stay predictions, not mastery;
- speaking/pronunciation/ASR judgments require scorer validity;
- transfer probes become extrapolation evidence;
- caption/L1/replay support becomes evidence provenance;
- interaction must be elicited by contingent tasks;
- cold-start placement becomes a low-confidence routing estimate, not durable learner truth.

## 16. Strong rejection rules

Nếp Method must reject these unless future evidence overturns them:

```text
correct once
→ mastered
```

```text
recognized in one modality
→ knows in all modalities
```

```text
correct after answer-bearing support
→ independent success
```

```text
same-item retry success
→ transfer
```

```text
same-session success
→ retention
```

```text
AI score matches human score
→ valid capability judgment
```

```text
high test reliability
→ real-world extrapolation validated
```

## 17. Product-independent output of RQ-024

RQ-024 contributes an **evidence epistemology**, not UI or database design:

```text
claim
→ elicitation
→ observation
→ evaluation
→ generalization
→ extrapolation
→ uncertainty
→ decision
→ consequence check
```

The exact operational thresholds remain `EXP-024` questions.
