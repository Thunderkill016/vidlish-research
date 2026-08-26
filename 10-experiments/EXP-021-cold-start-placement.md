# EXP-021 — Cold-start placement decision validity

**Experiment ID:** `EXP-021`  
**Research question:** `RQ-021`  
**Feature:** `FEAT-ONB-001`

## Question

Can Nếp reach a useful starting decision for Vietnamese near-A0/A1 adults with substantially less onboarding burden than a longer placement battery, without increasing harmful over-placement/under-placement or reducing first-week learning gain?

## Population

Vietnamese-speaking adults spanning:

- true/near-zero English;
- Pre-A1-like partial knowledge;
- low A1;
- stronger learners who could otherwise be bored by foundation content.

Recruit enough true beginners; do not let the sample be dominated by university learners already above A1.

## Reference decision

Create a higher-burden reference profile using a curated battery plus early-session evidence.

The reference should sample at least:

- written lexical recognition;
- aural lexical recognition;
- short listening comprehension;
- short reading comprehension;
- construction meaning;
- low-support recall;
- targeted productive evidence where feasible.

The final reference route should also incorporate first-session/early-session evidence so the experiment evaluates **placement usefulness**, not agreement with another imperfect test alone.

## Arms

### A — Long curated baseline

A longer fixed or balanced multistage placement battery before learning begins.

Purpose: high-information reference product experience.

### B — Self-report + ultra-short screen

Concrete self-assessment plus only a few objective items.

Purpose: test the attractive product assumption that onboarding can be nearly eliminated.

### C — Progressive adaptive bootstrap

Use `FEAT-ONB-001`:

```text
prior
→ common anchors
→ targeted frontier probes
→ uncertainty-aware decision
→ learning
```

### D — Progressive bootstrap + early-session recalibration

Same as C, but the system deliberately treats the first several normal learning tasks as additional validated placement evidence and can accelerate or remediate immediately.

This is the preferred architecture if it improves decisions without making the learner feel continuously tested.

## Primary outcomes

### 1. Downstream route validity

Measure after early sessions:

```text
overplacement event rate
underplacement event rate
route correction rate
```

Operationalize before launch.

Candidate over-placement indicators:

- cannot understand prerequisite input even with expected support;
- repeated failure across independent tasks;
- support use far above route expectation;
- immediate fallback to earlier capability required.

Candidate under-placement indicators:

- repeated high-confidence success on prerequisites;
- known-content skipping triggered repeatedly;
- first-session tasks produce negligible information because they are too easy;
- rapid multi-node acceleration required.

### 2. Learning efficiency

Primary product metric:

```text
delayed / changed-context capability gain
────────────────────────────────────────
onboarding minutes + learning minutes
```

Do not optimize placement accuracy while ignoring the time stolen from learning.

### 3. Time to first useful learning value

```text
signup
→ first genuine learning task completed
```

### 4. Decision stability

Compare initial recommended route with the route supported after early validated evidence.

A system that constantly reverses itself is not well calibrated even if it eventually learns the user.

## Secondary outcomes

- onboarding completion;
- voluntary abandonment;
- item count;
- time per item;
- rapid guessing / disengagement proxy;
- learner-rated clarity and difficulty;
- self-report vs direct-evidence disagreement;
- listening/text profile divergence;
- percentage of learners requiring productive probes;
- `unknown` constructs remaining at lesson start;
- support dependence during first sessions.

## Slice analysis

At minimum analyze separately:

- true beginner / near-zero;
- partial beginner;
- low A1;
- stronger-than-target entrant;
- low versus high prior formal English study;
- mobile audio quality / headphone availability;
- learners whose written ability substantially exceeds listening ability.

The overall mean can hide catastrophic placement failure for the true beginner slice.

## Important falsification tests

Reject the progressive bootstrap if:

- it substantially shortens onboarding but increases first-session failure;
- it systematically under-places stronger learners;
- its low-end classification is unstable;
- it uses self-assessment to skip direct evidence incorrectly;
- early calibration produces many reversals;
- learning gain per total minute is not better than the longer baseline.

Reject mandatory speaking/writing at signup if removing them does not worsen downstream route validity enough to justify their friction.

## Candidate stopping experiment

Compare variants such as:

```text
fixed minimum + confidence threshold + hard maximum
vs
fixed small item count
vs
module-level multistage routing
```

Do not preregister universal numeric thresholds from literature. Calibrate them on Nếp data.

## Minimum preregistration requirements

Before running:

- target sample size and power rationale;
- exact target learner inclusion criteria;
- reference placement procedure;
- route boundaries being tested;
- operational definitions of over/under-placement;
- maximum acceptable route-correction rate;
- onboarding burden ceiling;
- primary delayed/changed-context probe;
- handling of missing/abandoned onboarding;
- ASR/AI role if any;
- item exposure and calibration plan.

## Decision rule

Adopt the smallest placement architecture that gives a stable enough next-learning decision and improves total learning efficiency.

The winner is **not** the arm with the shortest onboarding.

The winner is the arm that gets the learner into useful learning fastest **without paying for that speed later through bad routing**.
