# Nếp Method Validation Contract

**Status:** active  
**Applies to:** `SYN-METHOD-001 — Nếp Method v0`  
**Target population:** Vietnamese-speaking adults beginning near zero / Pre-A1  
**Purpose:** define what evidence is required before the integrated method, curriculum, or product may make stronger efficacy claims.

---

## 1. Why this contract exists

`SYN-METHOD-001` is an evidence-backed synthesis, not a completed efficacy study.

The repository must not make this invalid jump:

```text
components have supporting literature
→ integrated Nếp Method is proven effective
```

The integrated method must earn its own evidence with the intended population and intended learning conditions.

---

## 2. Validation hierarchy

### Gate V0 — Research traceability

Required before curriculum derivation:

- every core method claim is traceable to `CLM-*` evidence;
- important method-level claims have an `EVA-*` appraisal when confidence/directness matters;
- active disagreements that could change the method are represented by `CTR-*` records;
- unresolved exact policies remain labeled hypotheses;
- CI passes all stable-ID and method-reference checks.

Passing V0 means only:

> the method is auditable enough to derive a curriculum hypothesis.

It does **not** mean the method has demonstrated learner efficacy.

### Gate V1 — Target-needs validation

Before fixing a broad beginner curriculum, validate the first target capabilities with intended learners and relevant domain evidence.

Use the RQ-023 contract:

```text
learner target situations
+ target tasks
+ frequency / importance / difficulty / training need
+ authentic discourse or artefacts where feasible
```

A published CEFR profile, textbook sequence, corpus list, owner preference, or AI rationale cannot substitute for this gate.

### Gate V2 — Construct-faithful vertical slices

Before scaling content, implement only a small number of capabilities end-to-end.

Each slice must preserve:

```text
target capability
→ elicited behavior in the target modality
→ original independent attempt when relevant
→ support / feedback provenance
→ repair attempt
→ changed-context probe
→ delayed probe when retention is claimed
→ conservative learner-state inference
```

A slice fails V2 if the software label overclaims the behavior actually elicited—for example typing labeled as speaking, supported success labeled independent, or same-item repetition labeled transfer.

### Gate V3 — Owner dogfood / instrumentation sanity

The owner may use the slice longitudinally to detect:

- broken or confusing tasks;
- obvious content irrelevance;
- feedback failures;
- evidence-state bugs;
- support dependence;
- review/orchestration problems;
- unacceptable effort or friction.

Dogfooding can reject a bad design quickly.

Dogfooding **cannot** establish population efficacy or a universal curriculum rule.

### Gate V4 — Target-population pilot

Test with Vietnamese-speaking adults near the intended starting range.

At minimum, record separately:

- prior English exposure;
- literacy/formal-schooling background where relevant;
- target goals/constraints;
- support used;
- task modality;
- scorer provenance;
- immediate performance;
- delayed performance;
- changed-context performance.

Do not pool away true beginners if more experienced learners dominate the sample.

### Gate V5 — Comparative learning test

Compare the Nếp slice with one or more **credible simpler baselines**, matching learning time or opportunity as closely as practical.

The baseline must be strong enough that Nếp cannot win merely by receiving more practice, more time, or more feedback.

Primary educational criterion:

```text
independent
+ delayed
+ changed-context
+ capability-relevant performance
──────────────────────────────────
learning time
```

Secondary outcomes may include:

- immediate learning;
- time to first useful capability;
- support dependence;
- false mastery / false routing;
- repair success;
- abandonment / effort;
- confidence / WTC, kept separate from mastery;
- implementation cost where it changes practical viability.

### Gate V6 — Replication / expansion

A positive result on one capability does not validate the whole method.

Before broad claims, replicate across meaningful variation such as:

- more than one capability family;
- receptive and productive demands;
- different content items;
- different learner subgroups;
- different sessions/time horizons;
- unfamiliar changed-context probes.

Only then may curriculum/product scope expand with stronger confidence.

---

## 3. Method-level falsification rules

A Nếp component should be modified, narrowed, or removed if target evidence shows that it:

- does not improve the intended delayed/changed-context outcome over a simpler credible policy;
- consumes materially more learner time for equivalent learning;
- increases support dependence without later independent benefit;
- causes systematic false-positive learner-state decisions;
- harms a relevant skill while optimizing an easier proxy;
- creates avoidable anxiety/effort/abandonment without educational benefit;
- benefits only a subgroup while being imposed globally;
- depends on an automated scorer whose validity is insufficient for the decision being made.

A literature-supported component is not immune to target-population falsification.

---

## 4. Evidence semantics during validation

Never collapse these conditions:

```text
first-seen
repeated
supported
independent
immediate
delayed
same-context
changed-context
AI-scored
human/listener-scored
```

The validation dataset must retain enough provenance to reconstruct what the learner actually did.

No experiment may promote post-feedback correction into evidence that the pre-feedback attempt was correct.

---

## 5. What counts as a method win

A Nếp design is not a winner because it produces:

- higher completion;
- more session time;
- more XP/streaks;
- better same-session quiz scores;
- more corrected answers after reveal;
- faster repeated-task performance;
- higher AI scores alone.

The method earns stronger confidence only when the relevant **independent capability** improves, especially under delayed and changed-context conditions when those claims are intended.

---

## 6. Decision states

Every validation question should end in one of these states:

```text
RETAIN
MODIFY
NARROW
REJECT
UNRESOLVED
```

`UNRESOLVED` is preferable to inventing certainty.

Negative and null results must be retained in the repository and may trigger a new `CTR-*`, revised `EVA-*`, claim status change, or method revision.

---

## 7. Change control for `SYN-METHOD-001`

A material change to a core method constraint must include:

1. the claim(s) or target learner result motivating the change;
2. an updated evidence/directness appraisal when appropriate;
3. the relevant controversy/boundary condition if evidence conflicts;
4. what previous statement is being narrowed, replaced, or rejected;
5. the validation consequence for curriculum/product work already derived from it.

Do not silently rewrite the method to match implementation convenience.

---

## 8. Current decision

`SYN-METHOD-001` may be used as the **provisional pedagogical source of truth for curriculum derivation and validation design** after V0 passes.

It must not yet be marketed or documented as:

> scientifically proven to be the optimal way to learn English.

The next research-to-build chain is:

```text
Nếp Method v0
→ direct target-needs confirmation
→ curriculum contract
→ first high-value capability slices
→ construct-faithful implementation
→ dogfood
→ target-population comparative validation
→ revise / expand
```
