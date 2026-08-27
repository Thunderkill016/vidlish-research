# RQ-026 — Individual differences, affect and self-regulated learning

**Status:** initial meta-foundation synthesis complete  
**Date:** 2026-08-27  
**Claims:** `CLM-ID-001`–`CLM-ID-020`  
**Evidence digest:** `06-evidence/RQ-026-source-digest.md`

## 1. Research question

> Which learner differences materially affect learning/participation, and which adaptations are justified rather than personalization theater?

## 2. Main conclusion

Learner differences matter, but the evidence rejects the shortcut:

```text
measure difference
→ personalize instruction
```

The required chain is stricter:

```text
learner variable
→ valid construct
→ plausible mechanism
→ treatment-relevant difference
→ reversible adaptation
→ better learner outcome
```

If the last step is not demonstrated, the personalization is not justified.

## 3. Three classes of learner information

### 3.1 Current state / context

Examples:

- anxiety during a task;
- willingness to communicate;
- self-efficacy for a capability;
- current SRL behavior;
- available time;
- device/audio constraints;
- recent overload/support dependence.

These are often the most actionable because they can change quickly and can be observed repeatedly.

### 3.2 Background / relatively stable moderators

Examples:

- prior schooling and literacy;
- language-learning aptitude components;
- working-memory measures;
- prior language experience.

These may help explain variation but should normally act as priors or moderators rather than permanent route labels.

### 3.3 Unsupported labels

Examples:

- visual learner;
- auditory learner;
- fixed personality curriculum;
- inferred neurotype from clickstream behavior.

These must not drive pedagogy without treatment-interaction evidence.

## 4. Personalization hierarchy

Candidate order for research and later system design:

```text
TARGET CONSTRUCT
↓
DECLARED CONSTRAINT / ACCESS NEED
↓
REPEATED OBSERVED PERFORMANCE STATE
↓
AFFECT / WTC / SELF-EFFICACY / SRL STATE
↓
VALIDATED COGNITIVE MODERATOR
only when treatment interaction is supported
↓
PREFERENCE
lowest authority unless independently validated
```

This prevents a preference from overriding the skill being learned.

For example:

```text
learner prefers reading
```

cannot justify removing listening from a listening target.

## 5. Anxiety and willingness to communicate

The evidence supports caring about anxiety and WTC because they are meaningfully associated with achievement, perceived competence, motivation and actual language use.

But the product must preserve the distinction:

```text
language capability
≠
willingness to expose that capability in this task
```

A learner can know enough to answer but avoid a socially risky or open-ended task.

A candidate adaptation may reduce task social risk or openness while retaining the target modality.

What it must not do:

```text
anxiety detected
→ silently lower English expectations forever
```

## 6. Self-efficacy

Self-efficacy is related strongly enough to achievement to monitor, but confidence can be both cause and consequence of success.

Therefore the target is not maximum confidence.

The target is:

```text
confidence calibrated to demonstrated capability
```

Useful mechanisms may include:

- selecting attainable but nontrivial tasks;
- showing evidence-backed progress;
- providing actionable feedback;
- exposing successful independent retrieval/use.

Empty praise is not an evidence-based self-efficacy intervention.

## 7. Motivation

Motivation is multidimensional.

Autonomous motivation is positively associated with L2 achievement, but motivational constructs often predict intended effort more strongly than objective achievement.

Therefore:

```text
motivation
→ participation/support decisions

motivation
-X→ mastery update
```

A learner who wants English intensely but repeatedly fails a listening probe still has a listening evidence gap.

## 8. Self-regulated learning

SRL should not be treated only as a learner trait.

The intervention evidence supports teaching and scaffolding:

- goal setting;
- planning;
- monitoring;
- strategy selection;
- reflection.

However, SRL support should remain lightweight and instrumental.

Nếp should not turn language learning into project-management homework.

## 9. Aptitude and working memory

### Aptitude

Language aptitude predicts some L2 outcomes and contains separable components.

More importantly for personalization, aptitude × treatment interactions have been observed.

That makes aptitude scientifically more relevant than learning styles.

But the current evidence is not enough for a full product route:

```text
aptitude score
→ permanent lesson method
```

because treatment interactions are domain-specific and traditional aptitude tests have construct-coverage problems.

### Working memory

Working memory has a robust but modest relation to L2 outcomes.

Nếp should therefore prefer observing actual task overload to administering a broad working-memory test merely to label the learner.

Example:

```text
long utterance fails
short equivalent succeeds repeatedly
→ candidate processing-load issue
```

This observation is more directly actionable than:

```text
WM score = low
```

## 10. Prior literacy and schooling

Prior literacy must not be conflated with English proficiency.

Candidate representation:

```text
English listening capability
English speaking capability
English reading capability
English writing capability
L1 print literacy / schooling familiarity
```

A learner with limited literacy may have usable oral language and require a different literacy path.

Conversely, a highly educated learner can be an English beginner while possessing strong metalinguistic and study skills.

## 11. Neurodiversity and accessibility

Current foreign-language intervention evidence is too sparse for Nếp to infer a diagnosis and select a neurotype curriculum.

The safer rule is:

```text
explicit accessibility need
or
repeated observable barrier
→ accommodation
→ re-evaluate outcome
```

Examples may include:

- adjustable timing;
- reduced visual clutter;
- keyboard/audio alternatives;
- task chunking;
- caption/transcript availability where compatible with the target construct;
- learner-controlled sensory settings.

These are access decisions, not evidence of English mastery.

## 12. Reversible adaptation contract

Every nontrivial adaptive decision should eventually be representable as:

```ts
type AdaptationEvidence = {
  trigger: string;
  targetConstruct: string;
  adaptation: string;
  evidenceBasis: string[];
  expectedEffect: string;
  costOrRisk: string;
  expiresAtOrRecheck: string;
  observedOutcome?: string;
};
```

Key property:

```text
adaptation can expire
```

The system should continuously earn the right to keep personalizing.

## 13. Rule for trait-based adaptation

A stable learner characteristic should change instructional treatment only when all of the following are defensible:

1. the trait measure has sufficient validity;
2. the trait is relevant to the target construct;
3. there is evidence of learner-characteristic × treatment interaction;
4. the candidate treatment is feasible and safe;
5. the adaptation improves relevant outcomes relative to a simpler policy.

This standard intentionally rejects most personalization theater.

## 14. Vietnamese near-A0 implications

Direct Vietnamese adult studies suggest a useful design distinction:

```text
strong goal / motivation
+
low confidence
+
limited time
+
limited speaking environment
```

can coexist.

Therefore a single `motivationScore` is structurally inadequate.

At minimum, later target research should distinguish:

- why the learner wants English;
- available study time;
- confidence/WTC by task;
- actual capability evidence;
- prior educational/literacy background;
- practice environment / access constraints.

## 15. Explicitly rejected policies

RQ-026 rejects as current scientific defaults:

```text
VARK / learning-style routing
personality-based curriculum routing
one motivation score as learner quality
a low aptitude score as a learning ceiling
working-memory score as permanent difficulty level
clickstream-based neurodevelopmental diagnosis
low participation = low English ability
low confidence = low English ability
high confidence = mastery
```

## 16. What remains uncertain

RQ-026 does not identify exact thresholds or the best adaptive algorithm.

Open product questions include:

- when an anxiety/WTC signal is strong enough to change task conditions;
- how often to recheck self-efficacy;
- which SRL prompts are useful without adding burden;
- whether aptitude testing creates enough incremental value to justify cost;
- how to infer processing-load problems from performance without overdiagnosis;
- which accessibility controls should be universal versus personalized.

These are assigned to `EXP-026` and later target-user data.

## 17. Constraint carried into Nếp Method synthesis

The future method must treat personalization as a **validated adaptation layer**, not as the organizing theory of learning.

The learning mechanism remains grounded in target capability and evidence.

Personalization changes conditions only where the evidence justifies it.
