# RQ-024 source digest — language-assessment validity and learner-state inference

**RQ:** What observations under what task/support/scorer conditions justify what learner-state inference, with what uncertainty, reliability and generalizability?

**Status:** initial meta-foundation evidence digest  
**Date:** 2026-08-27  
**Registry:** `data/sources-rq024.json`, `data/claims-rq024.json`

## 1. Why RQ-024 is a foundation blocker

The existing Nếp research contains useful distinctions:

- recognition vs recall;
- supported vs unsupported success;
- first-seen vs replayed input;
- exact repetition vs transfer;
- immediate vs delayed evidence;
- human vs ASR/AI judgment.

But these distinctions were accumulated locally by feature.

RQ-024 asks the higher-order question:

```text
OBSERVATION
→ what claim is justified?
→ under which assumptions?
→ how far may the claim generalize?
→ what uncertainty remains?
→ what product decision may safely follow?
```

Without this layer, a learner model can become a collection of confident labels whose inferential basis is unclear.

## 2. Validity belongs to the claim, not to the test

### SRC-0281 — Kane (2013)

The central principle is that validation evaluates the plausibility of **interpretations and uses** based on test observations/scores.

Important implications:

- a test is not simply “valid” in the abstract;
- the same observation can support a narrow claim while failing to support a broader one;
- more ambitious claims require more evidence;
- valid score interpretation does not automatically validate a later product decision;
- consequences matter when validating use.

For Nếp:

```text
learner chose the correct meaning
```

is an observation.

It is not automatically equivalent to:

```text
learner knows this word
learner can hear this word
learner can say this word
learner retained it
learner can transfer it
```

Each arrow is an inference requiring support.

### SRC-0282 — Chapelle, Enright & Jamieson (2010)

Argument-based validation helps make intended interpretations explicit, organize needed research, and expose weak assumptions.

The value for Nếp is architectural:

```text
claim first
→ evidence needed
→ task design
```

rather than:

```text
collect telemetry first
→ invent learner-state meaning later
```

### SRC-0283 — Im, Shin & Cheng (2019)

Review of language-testing validity frameworks reinforces the use of linked inferences such as:

```text
performance
→ evaluation/scoring
→ generalization
→ extrapolation
→ decision/use/consequence
```

It also emphasizes domain analysis, multiple stakeholders/methods and consequences.

## 3. Evidence-centered design

### SRC-0284 — Mislevy & Haertel (2006)

Evidence-Centered Design (ECD) explicitly separates:

### Student model
What latent knowledge/capability is being claimed?

### Task model
What situation is constructed to elicit relevant performance?

### Evidence model
What observable aspects of the response count as evidence, how are they evaluated, and how are observations accumulated?

This maps naturally to Nếp:

```text
CAPABILITY CLAIM
↓
TASK CONDITIONS
↓
WORK PRODUCT / ATTEMPT
↓
EVALUATION
↓
EVIDENCE UPDATE
```

The important lesson is not that Nếp must copy one psychometric architecture. It is that raw events such as clicks, words recognized, ASR transcripts or completion time acquire meaning only through a defensible evidence model.

## 4. Diagnostic granularity requires construct design

### SRC-0286 — Toprak & Cakir (2021)

The study developed a diagnostic L2 reading assessment from an explicit cognitive model rather than retrofitting a generic test after the fact.

Relevant lesson:

```text
fine-grained learner profile
requires
fine-grained construct + task-to-attribute mapping
```

It is unsafe to do this:

```text
large event log
→ machine clusters behavior
→ label 17 hidden English skills “mastered”
```

unless the supposed attributes and observations have been validated.

Nếp may use a simpler evidence model than formal cognitive-diagnostic modeling, but it inherits the same validity constraint.

## 5. Scoring is not generalization

### SRC-0287 — Eskin (2022)

Writing performance varied by task even under a common assessment and rubric.

Task variation reduced score dependability while also reflecting genuine breadth in the construct.

This exposes a basic tension:

```text
use one highly standardized task
→ reliable narrow measurement

sample diverse tasks
→ broader construct representation
but more task variance
```

For Nếp, one perfect response cannot generally support a broad productive capability.

The solution is not “test everything forever.” It is to match observation count/diversity to the breadth and stakes of the claim.

## 6. Generalization is not extrapolation

### SRC-0288 — LaFlair & Staples (2017)

A high-stakes speaking assessment can produce internally consistent performance while still requiring evidence that its language/performance resembles the target domain.

Corpus/register comparison showed that extrapolation support varied across dimensions.

For Nếp:

```text
can answer Nếp role-play prompt
```

is not automatically:

```text
can handle this target interaction outside Nếp
```

The changed-context/target-domain evidence from earlier RQ-005 therefore belongs inside the validity architecture, not only inside a transfer feature.

## 7. Interaction needs interaction-sensitive evidence

### SRC-0289 — Youn (2015)

Assessment of L2 pragmatics in interaction required task-sensitive, data-driven rating criteria because interaction is co-constructed and sequential.

A generic sentence-quality score would miss important interactional behavior.

Nếp implication:

If the claim is:

```text
can repair a misunderstanding in interaction
```

then evidence should include actual contingent repair behavior, not merely a multiple-choice recognition item about the right phrase.

## 8. Independent ability versus mediated potential

### SRC-0290 — Poehner & Wang (2020)

Dynamic Assessment argues that independent performance reveals developed capability while responsiveness to mediation can reveal emerging ability.

This gives Nếp two legitimate but different evidence types:

```text
INDEPENDENT CURRENT PERFORMANCE
```

and

```text
RESPONSIVENESS TO SUPPORT / EMERGING POTENTIAL
```

The earlier Nếp rule that support-bearing success cannot be re-labeled independent mastery remains valid.

RQ-024 adds:

```text
supported success is not worthless
```

It may tell the system what kind of assistance enables development.

This requires support provenance.

## 9. Support and exposure are task conditions

The inference changes when the learner receives:

- Vietnamese translation;
- English caption/transcript;
- answer model;
- keyword cue;
- hint;
- replay;
- second attempt;
- slowed or segmented input.

These supports reveal different amounts of information.

Therefore evidence should record them rather than merely store:

```text
correct = true
```

Similarly:

```text
first-seen success
```

and

```text
success after three replays
```

can both be useful observations while supporting different claims.

## 10. Retention and transfer are claims, not scheduler labels

RQ-024 consolidates earlier RQ-004/RQ-005 boundaries into the validity argument.

### Retention

A retention claim requires a delay explicitly relevant to the claim.

```text
success now
≠
retained later
```

No universal delay is established for all Nếp capabilities.

### Transfer/generalization

A transfer claim requires a meaningful change in cue/context/exemplar/task or response conditions that corresponds to the target generalization.

```text
same sentence again
≠
transfer
```

A changed item that differs only cosmetically may still be insufficient.

The transfer probe should be designed from the target capability and target-language-use domain identified in RQ-023.

## 11. Automated scoring requires a validity argument too

### SRC-0285 — Chapelle, Cotos & Lee (2015)

Automated writing evaluation can support diagnostic assessment, but validation must address intended diagnostic interpretations and uses rather than merely algorithmic accuracy.

This is directly relevant to AI-assisted Nếp scoring:

```text
model output
→ score
```

is only the evaluation step.

It does not automatically validate:

```text
score
→ learner capability
→ curriculum decision
```

### SRC-0291 — Li, Qunhan & Mao (2026)

Meta-analysis:
- 21 empirical studies;
- 401,698 participants;
- average AI-human score difference was small/non-significant;
- heterogeneity was extremely high;
- differences were moderated by system type, proficiency level, number of human raters, agreement index and other study characteristics;
- purpose-built scoring systems aligned more closely with humans than general-purpose LLMs in the analyzed literature.

Correct interpretation:

```text
AI can be useful in scoring/diagnosis
```

not:

```text
AI score ≈ human average
→ AI is universally valid ground truth
```

### SRC-0292 — Wilson & Huang (2024)

Automated and human essay scores showed similar predictive validity in the studied ELL population, but both displayed weaker relationships for ELLs than for non-ELLs on one external outcome.

Important lesson:

```text
human scorer
≠ infallible ground truth
```

An automated scorer may reproduce weaknesses already embedded in human labels/rubrics.

Validation should therefore include:
- target construct evidence;
- subgroup analysis;
- external/target-domain outcomes;
- disagreement analysis;
not only human-machine correlation.

## 12. Existing Nếp ASR/AI research fits inside this model

RQ-008 and RQ-020 already established important constraints:

- ASR accuracy varies by accent/L1 and system;
- ASR transcription is not the same construct as pronunciation/intelligibility;
- LLM/rater behavior varies by model and implementation;
- provider/model/version provenance matters;
- model updates can change behavior.

RQ-024 promotes these from isolated technology concerns into general assessment-validity requirements.

## 13. Proposed Nếp inference chain

```text
TARGET CAPABILITY
↓
TASK + CONDITIONS
(modality, support, exposure, novelty, interlocutor)
↓
OBSERVED WORK PRODUCT / ATTEMPT
↓
EVALUATION
(rule / human / ASR / LLM + provenance)
↓
TASK-BOUND OBSERVATION
↓
GENERALIZATION ACROSS RELEVANT PARALLEL TASKS
↓
TARGET-DOMAIN EXTRAPOLATION
↓
CAPABILITY CLAIM WITH UNCERTAINTY
↓
PRODUCT DECISION
↓
LATER CONSEQUENCE / PREDICTIVE CHECK
```

For retention and transfer, additional conditions are inserted:

```text
DELAY
```

and/or:

```text
MEANINGFUL CONTEXT/TASK CHANGE
```

## 14. Proposed evidence object

Candidate research representation:

```ts
type LanguageEvidence = {
  evidenceId: string;
  learnerId: string;
  capabilityId: string;
  taskId: string;

  modality: "listen" | "read" | "speak" | "write" | "interact" | "mediate";
  responseMode: string;

  firstSeen: boolean;
  exposureIndex: number;
  supportState: string[];
  noveltyProfile?: string[];

  observedAt: string;
  delaySinceLearningMs?: number;

  scorerType: "rule" | "human" | "asr" | "llm" | "hybrid";
  scorerModel?: string;
  scorerVersion?: string;
  score?: number;
  scorerConfidence?: number;
  disagreement?: number;

  observationLabel: string;
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

This is a candidate research contract, not yet a database schema.

## 15. What RQ-024 does not establish

The literature does not give Nếp universal values for:

- number of parallel tasks needed;
- confidence threshold for a capability;
- acceptable scorer disagreement;
- retention delay;
- amount of changed context needed for transfer;
- weight of first-seen versus repeated performance;
- how much each support type discounts an inference;
- how fast evidence decays;
- when AI judgment needs human arbitration;
- false-positive versus false-negative costs.

Those are direct validation parameters for `EXP-024`.
