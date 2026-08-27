# Evidence Grading & Contradiction Protocol

**Status:** RQ-028 initial protocol  
**Applies to:** all future high-impact claims, syntheses and `SYN-METHOD-001`  
**Date:** 2026-08-27

## 1. Purpose

The repository previously used a compact `A–E` evidence label. That label is useful for quick retrieval but can hide the reason a claim is trustworthy or indirect.

Example:

```text
high-quality meta-analysis
+ university intermediate learners
+ controlled grammar test
+ classroom treatment
```

may be strong evidence for a narrow instructional effect while remaining weak evidence for:

```text
Vietnamese adult near Pre-A1
+ mobile self-study
+ spontaneous speaking
+ delayed transfer
```

Therefore Nếp must separate **quality** from **directness**.

## 2. The five mandatory appraisal axes

Each high-impact claim should eventually receive an `EVA-*` record.

### 2.1 Methodological quality

Question:

> How trustworthy is the research process for the inference being used?

Candidate values:

```text
high
moderate
low
unclear
```

Consider, as appropriate to design:

- design fit to question;
- controls/comparison;
- sample size/power/precision;
- measurement reliability/validity;
- analysis appropriateness;
- handling of dependent observations;
- risk of selective reporting;
- transparency/reproducibility;
- quality of a synthesis's search/coding/modeling.

Do not reduce journal prestige to methodological quality.

### 2.2 Population directness

Question:

> How similar are the studied learners to the population for the current claim?

For core Nếp Method claims the target is initially:

```text
Vietnamese-speaking adults
near zero / Pre-A1
self-directed or lightly guided learning
```

Candidate values:

```text
high       direct target population or close replication
moderate   adult EFL/ESL with meaningful similarities
low        materially different proficiency/age/L1/setting
unknown    insufficient sample information
```

Population directness is claim-specific. A universal cognitive mechanism may require less L1 directness than a Vietnamese pronunciation rule.

### 2.3 Construct directness

Question:

> Does the outcome actually measure the construct claimed?

Examples:

```text
word recognition
≠ productive recall

typed recall
≠ speaking

controlled grammar judgment
≠ spontaneous interaction

immediate performance
≠ delayed retention
```

Use RQ-024 to judge the inference chain.

### 2.4 Replication / consistency

Question:

> Is the pattern repeated across studies, methods and settings, and what does heterogeneity mean?

Candidate values:

```text
high
moderate
low
unclear
```

Consider:

- independent replication;
- multiple research teams;
- meta-analytic consistency;
- heterogeneity;
- credible moderator patterns;
- null/negative findings;
- sensitivity to analytic choices.

Do not use publication count as a substitute for replication.

### 2.5 Product-transfer directness

Question:

> How directly does the evidence test the decision Nếp intends to make?

Examples:

```text
classroom teacher feedback study
→ indirect for AI-mediated 5-minute self-study

TTS intelligibility study
→ indirect for using TTS as durable listening mastery evidence

Vietnamese near-A0 mobile experiment
→ high product-transfer directness
```

This axis prevents a strong academic result from silently becoming a product fact.

## 3. Optional certainty summary

An `EVA-*` record may contain a short `certainty_summary`, but it must not be calculated by averaging ordinal axes.

Allowed examples:

```text
high
moderate
low
very-low
high-for-direction-moderate-for-threshold
```

The rationale is mandatory when the summary is not obvious.

## 4. The legacy A–E label

Existing `evidence_level` values remain for backward compatibility.

Interpret them only as a compact claim-level shorthand:

- `A` strong research support for the narrow claim;
- `B` moderate support;
- `C` synthesis/product inference grounded in evidence;
- `D` hypothesis requiring direct validation;
- `E` product assumption / very weak support.

From RQ-028 onward:

```text
A–E alone
≠ sufficient confidence representation
```

Any statement entering `SYN-METHOD-001` as a high-confidence method rule must be accompanied by multidimensional appraisal or an explicit reason appraisal is not yet possible.

## 5. Controversies are first-class records

Use `CTR-*` when credible evidence supports materially different interpretations or policies.

A controversy record must include:

```text
id
title
status
claim_ids
source_ids
competing_positions
boundary_conditions
current_resolution
would_change_if
```

Possible status values:

```text
open
open-moderated
open-bounded
provisionally-resolved
superseded
```

Do not mark a controversy resolved because one side has more papers.

Resolve/narrow it by examining:

- study quality;
- construct/outcome differences;
- population differences;
- task/treatment differences;
- timing/dosage;
- replication;
- publication bias;
- target-product directness.

## 6. Null and negative evidence

Null/negative findings must remain discoverable.

Do not write:

```text
study did not support current idea
→ omit from digest
```

Instead record whether the null result may reflect:

- true absence/small effect;
- imprecision/low power;
- construct mismatch;
- weak manipulation;
- population boundary;
- measurement ceiling/floor;
- contradictory replication.

A null result is not automatically evidence of no effect, but it is evidence that belongs in the synthesis.

## 7. Source quality versus claim quality

One source can support claims at different levels.

Example:

```text
source directly studies reading comprehension
→ high construct directness for reading claim

same source used to justify conversation policy
→ low construct directness
```

Therefore `EVA-*` attaches primarily to a **claim**, while source-level quality remains part of its rationale.

## 8. Updating and superseding claims

Never silently rewrite history when evidence changes.

Use this lifecycle:

```text
ACTIVE
↓
NARROWED / REVISED
↓
SUPERSEDED
```

A superseded claim remains in version history and should point to the newer synthesis/claim where practical.

Triggers for mandatory review include:

1. new high-quality meta-analysis/systematic review;
2. credible direct/approximate replication disagreement;
3. new Vietnamese near-A0 evidence;
4. evidence directly testing the Nếp product context;
5. construct-validity evidence changing interpretation;
6. major publication-bias or methodological reassessment;
7. contradiction record changing status.

## 9. Evidence propagation into method/product decisions

Never propagate the strongest source grade upward.

Bad:

```text
one A-level source
→ PRN high confidence
→ feature high confidence
```

Required reasoning:

```text
claim appraisal
+ controversy state
+ target directness
+ alternative explanations
→ synthesis confidence
→ method constraint / hypothesis
```

If one necessary premise has very low directness, expose that weakness.

## 10. Research synthesis workflow

For high-impact RQs:

```text
1. define question / target inference
2. search broadly, including contradictory/null evidence
3. verify source metadata
4. record atomic claims
5. appraise important claims on separate axes
6. create controversy records where needed
7. synthesize boundary conditions
8. state what would change the conclusion
9. create experiment/target-validation plan for unresolved product choices
10. update RESEARCH_MAP
```

## 11. AI-specific safeguards

An AI agent may search, extract, compare and propose appraisals.

It must not:

- invent metadata or findings;
- assign `high` because a paper is famous;
- infer population directness from title only;
- hide contradictory evidence;
- mechanically average appraisal dimensions;
- declare a controversy closed without explicit synthesis;
- treat its own prior summary as source evidence.

## 12. Minimum gate for `SYN-METHOD-001`

Before a statement becomes a **core high-confidence Nếp Method rule**, require:

```text
traceable claim(s)
+ verified sources
+ construct fit
+ explicit population/product directness
+ contradiction check
+ confidence rationale
```

Lower-directness evidence can still support a provisional method constraint, but it must be labeled as provisional and paired with a falsification/target-validation plan.

## 13. Philosophy

The repository is not trying to manufacture certainty.

It is trying to make this visible:

```text
WHAT WE KNOW
WHY WE THINK IT
WHERE IT APPLIES
WHERE IT MAY FAIL
WHAT WOULD CHANGE OUR MIND
```

That is the evidence standard required before Nếp is allowed to turn research into a learning method.
