# EXP-024 — Learner-state inference validity

**Status:** planned validation program  
**Depends on:** RQ-024, RQ-023  
**Purpose:** determine which short in-product observations predict later independent, delayed and changed-context capability strongly enough to justify learner-state updates and product decisions.

## 1. Primary question

For Vietnamese-speaking learners near Pre-A1/A1, which combinations of task, support, repetition, scorer and observation history validly predict later target capability?

## 2. Unit of validation

Do not validate one global `mastery` variable.

Validate an explicit inference:

```text
observations under conditions X
→ claim Y
→ decision Z
```

Example:

```text
3 first-seen audio-only successes
on parallel short request items
→ likely independent current listening capability
→ reduce listening scaffold on next parallel item
```

## 3. Capability families

Sample multiple capability types because one evidence rule may not transfer across constructs:

- receptive lexical/form-meaning access;
- first-pass listening comprehension;
- productive short-chunk retrieval;
- short functional writing;
- controlled interaction/repair;
- pronunciation/intelligibility where scoring validity permits.

## 4. Evidence-condition factors

Systematically vary or observe:

### Exposure
- first-seen;
- exact replay;
- retry after failure;
- previously trained exemplar;
- new parallel exemplar.

### Support
- none;
- non-answer-bearing replay/time support;
- L2 keyword cue;
- L2 full text/model;
- Vietnamese micro-gloss;
- full translation/model where relevant.

### Response mode
- recognition;
- cued recall;
- independent production;
- interactional response.

### Novelty
- same item;
- lexical substitution;
- changed speaker/voice;
- changed surface wording;
- changed scenario;
- changed interaction continuation.

### Scorer
- deterministic rule where possible;
- trained human;
- ASR;
- purpose-built automated scorer;
- LLM/hybrid where proposed.

Store scorer model/version.

## 5. Criterion probes

### Criterion A — parallel current capability

Use new parallel items under independent conditions.

Tests generalization beyond the exact event.

### Criterion B — delayed retention

Probe after predefined retention intervals.

Use more than one interval if practical so the product does not optimize for one arbitrary horizon.

### Criterion C — changed-context transfer

Use new contexts/exemplars that preserve the intended capability while changing surface cues.

### Criterion D — target-task performance

Where feasible, use tasks derived from RQ-023 target needs rather than only isolated item tests.

## 6. Automated-scoring validation

For any automated evaluator used to update learner state:

Measure:
- agreement with trained human ratings;
- disagreement distribution;
- false accept / false reject rates;
- calibration if confidence is exposed;
- subgroup effects, including Vietnamese L1 and proficiency range;
- sensitivity to device/audio quality where relevant;
- model/provider/version drift;
- prediction of later criterion performance.

Human agreement is not the sole criterion.

Disagreement cases should be manually analyzed for:
- human error;
- rubric ambiguity;
- model bias;
- construct mismatch;
- unusual but communicatively acceptable language.

## 7. Competing learner-state models

Compare at minimum:

### Model A — naive boolean

```text
correct → mastered
incorrect → not mastered
```

### Model B — count threshold

```text
N recent correct responses → mastered
```

### Model C — evidence-conditional

Uses:
- modality;
- support;
- first-seen status;
- exposure;
- task diversity;
- delay;
- changed context;
- scorer reliability.

### Model D — probabilistic evidence-conditional

Like C, but explicitly represents uncertainty and evidence aging if justified.

The experiment does not assume D will win merely because it is more sophisticated.

## 8. Primary outcome

Prediction/calibration of later **independent target capability**.

At minimum report:

```text
false positive:
model says capability present
but criterion probe fails
```

```text
false negative:
model withholds capability
but criterion probe succeeds
```

Because overclaiming and underclaiming have different educational costs, report them separately.

## 9. Secondary outcomes

- delayed-retention prediction;
- changed-context transfer prediction;
- learner minutes spent on assessment/probes;
- unnecessary review caused by false negatives;
- premature scaffold removal caused by false positives;
- learner frustration/abandonment from over-testing;
- scorer arbitration cost.

## 10. Decision-stakes analysis

Test different thresholds for different decisions.

Examples:

### Low stakes
- select one harder/easier next example;
- choose whether to offer a hint.

### Medium stakes
- reduce a scaffold family;
- schedule less review.

### High stakes
- skip prerequisite capability;
- claim delayed retention;
- claim transfer/mastery-like status.

Hypothesis:

```text
higher decision cost
→ higher evidence requirement
```

but exact thresholds must be calibrated empirically.

## 11. Support-response analysis

Do not only evaluate whether support increased immediate correctness.

Ask whether response to support predicts later independent success.

For example:

```text
failed independently
→ succeeds with micro-gloss
→ later independent success?
```

versus:

```text
failed independently
→ needs full model
→ later independent success?
```

This can determine whether support history is useful as an emerging-capability signal.

## 12. Required output

`EXP-024` should ultimately produce:

- validated evidence features by capability family;
- task-sampling requirements;
- decision-specific confidence thresholds;
- support-provenance interpretation rules;
- delayed-retention horizons used by the product;
- changed-context probe requirements;
- automated scorer validity/limitations by model version;
- false-positive/false-negative cost estimates;
- evidence-state transition policy;
- cases where the system must remain uncertain.

## 13. Falsification

The evidence-conditional learner model should be rejected or simplified if it does not predict later independent/delayed/changed-context performance meaningfully better per learner minute than a simpler model.

Likewise, any automated scorer should be excluded from capability-state decisions if its errors, subgroup behavior or drift make the intended inference unreliable even if it appears convenient or engaging.
