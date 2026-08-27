# EXP-026 — Evidence-backed personalization versus personalization theater

**Related RQ:** RQ-026  
**Status:** planned  
**Population:** Vietnamese-speaking adults near zero / Pre-A1, with subgroup reporting by prior schooling/literacy and current English experience

## 1. Question

> Does adapting learning conditions from validated, changing learner-state evidence improve learning and participation compared with one-size-fits-all instruction or preference/style-based personalization?

## 2. Why this experiment exists

RQ-026 found evidence that anxiety, WTC, self-efficacy, SRL, aptitude, working memory, prior literacy and practical constraints matter.

But:

```text
variable predicts outcome
≠
variable tells us which lesson to give
```

The experiment tests whether personalization adds **incremental value** beyond a simpler high-quality learning policy.

## 3. Conditions

### A — Fixed evidence-based learning policy

All learners receive the same target-capability sequence and support policy, except mandatory accessibility controls.

No affective/cognitive personalization.

### B — Preference/persona personalization

Learners complete a short preference/style/persona questionnaire.

Surface instructional presentation is matched to those reported preferences where feasible.

This condition represents common commercial personalization and is a deliberate falsifiable comparator, not a recommended policy.

It must not remove the modality required by the target construct.

### C — State-adaptive personalization

Uses only reversible signals such as:

- repeated observed overload/support dependence;
- task-specific anxiety/WTC/self-efficacy;
- available time;
- practice environment;
- declared access constraints;
- demonstrated SRL difficulties.

Examples:

- reduce open-endedness before reducing target difficulty;
- split high-load input after repeated processing failure;
- offer a smaller valid session when time is constrained;
- add planning/monitoring scaffolds when evidence suggests SRL breakdown;
- preserve target modality and learning criterion.

### D — State adaptive + validated moderator candidate

Same as C, plus one preregistered stable moderator only where prior literature predicts a learner × treatment interaction.

Candidate example for a narrow grammar sub-study:

- validated aptitude component × explicit/implicit instructional support.

This arm exists to test whether trait measurement adds value beyond direct performance-state adaptation.

## 4. Primary learning outcome

```text
delayed changed-context capability gain
───────────────────────────────────────
onboarding + learning minutes
```

Measured on parallel tasks not seen during treatment.

## 5. Secondary outcomes

Learning:

- independent first-seen performance;
- delayed retention;
- changed-context transfer;
- support dependence;
- modality-specific performance.

Participation/affect:

- useful return;
- task completion;
- voluntary speaking attempts;
- WTC by task type;
- task anxiety;
- calibrated self-efficacy;
- abandonment.

Personalization quality:

- adaptation frequency;
- adaptation reversal rate;
- adaptation benefit/harm rate;
- false adaptation rate;
- time/cognitive burden of questionnaires;
- subgroup disparities.

## 6. Calibration outcome

Self-efficacy should be evaluated for **calibration**, not maximum score.

Candidate metric:

```text
| predicted success probability - observed success rate |
```

A treatment that increases confidence while accuracy falls is not a success.

## 7. Misadaptation events

Record explicitly:

```text
adaptation triggered
→ target construct
→ learner evidence before
→ changed condition
→ learner evidence after
```

Candidate failure classes:

- unnecessary simplification;
- reduced exposure to target modality;
- permanent route caused by temporary state;
- preference match that lowers learning;
- high-anxiety learner protected from all productive challenge;
- low early performance misread as low capacity.

## 8. Accessibility

Declared accessibility needs are not randomized away.

Required access accommodations must remain available across all arms.

EXP-026 evaluates pedagogical personalization, not whether learners should be denied accessibility.

## 9. Trait testing gate

Any aptitude/working-memory measure added to D must demonstrate:

1. construct validity appropriate to the intended use;
2. acceptable burden;
3. preregistered treatment interaction;
4. incremental predictive/adaptive value over direct learner-performance evidence.

If it does not improve decisions, remove the test.

## 10. Analysis

Primary comparison:

```text
C vs A
```

Does evidence-driven state adaptation improve learning efficiency without harming retention/transfer?

Critical red-team comparison:

```text
B vs A
```

Does preference/persona matching provide any actual learning benefit?

Incremental-complexity comparison:

```text
D vs C
```

Does trait/moderator measurement justify its extra complexity?

Analyze separately by:

- near-zero versus nonzero starting capability;
- prior formal schooling/literacy;
- high/low initial speaking anxiety;
- available study time;
- task family;
- modality.

## 11. Decision rule

Do **not** ship an adaptive rule because learners say they like it.

A personalization rule becomes a candidate for production only if it shows one or more of:

```text
learning gain/minute ↑
transfer/retention ↑
useful participation ↑ without learning loss
support dependence ↓
accessibility/friction improves without construct contamination
```

and does not create unacceptable subgroup harm or labeling effects.

If B performs no better than A, preference/style routing is explicitly rejected for Nếp.

If D performs no better than C, do not collect the extra stable-trait measurement.

## 12. Falsification

RQ-026's product synthesis is weakened if:

- state-adaptive rules fail to improve learning or useful participation;
- adaptation burden offsets benefit;
- rules repeatedly lower task challenge without later recovery;
- learner-state measures are too unstable/unreliable for decisions;
- direct performance evidence outperforms all affective/cognitive personalization signals.

A negative result is useful: it supports a simpler system.
