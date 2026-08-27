# RQ-028 — Evidence grading, contradiction and update protocol

**Status:** initial meta-foundation synthesis complete  
**Date:** 2026-08-27  
**Claims:** `CLM-META-001`–`CLM-META-022`  
**Protocol:** `00-foundations/EVIDENCE_GRADING_PROTOCOL.md`

## 1. Research question

> How should the knowledge base separately grade methodological quality and directness, represent competing/null findings and boundary conditions, and revise earlier syntheses when stronger/newer evidence appears?

## 2. Main conclusion

The old model:

```text
claim
→ evidence level A/B/C/D/E
```

is too compressed for the decisions Nếp intends to make.

The new minimum model is:

```text
SOURCE SET
    ↓
ATOMIC CLAIM
    ↓
MULTIDIMENSIONAL APPRAISAL (EVA)
    ├─ methodological quality
    ├─ population directness
    ├─ construct directness
    ├─ replication / consistency
    └─ product-transfer directness
    ↓
CONTROVERSY / BOUNDARY CHECK (CTR)
    ↓
SYNTHESIS WITH EXPLICIT UNCERTAINTY
    ↓
METHOD CONSTRAINT OR VALIDATION HYPOTHESIS
```

No arithmetic average is permitted to turn these axes into a false precision score.

## 3. Why this changes the research program

Before RQ-028, a claim such as:

```text
explicit instruction = A
```

could look stronger than the actual product inference warranted.

After RQ-028 it can be represented as:

```text
methodological quality: high
population directness: low
construct directness: moderate
replication consistency: moderate
product-transfer directness: low
```

This does not weaken the underlying literature. It states the correct scope of inference.

## 4. Methodological quality is not directness

A well-conducted study with a different population or outcome can still be valuable.

But it cannot silently become direct evidence for Nếp's target.

Likewise, a small direct Vietnamese near-A0 study may have:

```text
population directness: high
methodological quality: low/moderate
```

Neither source should automatically dominate the other. Synthesis needs both dimensions.

## 5. Population directness is a first-class issue

The sampling synthesis in RQ-028 reinforces a major risk found during the meta-audit: much L2 evidence comes from younger/intermediate university populations.

Nếp's intended target initially is:

```text
Vietnamese-speaking adult
near zero / Pre-A1
limited real-world English ability
primarily self-study product
```

Therefore many strong general SLA findings will legitimately enter `SYN-METHOD-001` as:

```text
well-supported general constraint
+
low/moderate target-population directness
+
target-validation requirement
```

That is scientifically preferable to either ignoring the literature or pretending it directly studied Nếp users.

## 6. Construct directness follows RQ-024

RQ-024 established that validity concerns the inference, not merely the test label.

RQ-028 makes this a confidence dimension.

Examples:

```text
controlled form recognition
→ direct for recognition
→ indirect for spontaneous production

immediate posttest
→ direct for immediate performance
→ indirect for retention

trained-item performance
→ indirect for transfer
```

Therefore a method rule requiring real-world ability cannot inherit high confidence from a study whose outcome did not elicit that ability.

## 7. Replication and consistency

Confidence increases when a finding survives:

- independent teams;
- multiple operationalizations;
- replications;
- reasonable sensitivity analyses;
- relevant settings/populations.

But consistency is not paper count.

Multiple reports from one sample, one laboratory or one measurement family do not constitute independent convergence.

## 8. Product-transfer directness

This is the axis most likely to prevent another Vidlish-style mistake.

Examples:

```text
teacher-led classroom intervention
→ useful pedagogical evidence
→ indirect for AI-mediated mobile self-study
```

```text
ASR agrees with human raters
→ evidence about scoring relation
→ not automatically evidence that using that score improves learning
```

```text
Nếp target learner
+ Nếp-like task
+ delayed changed-context outcome
→ high product-transfer directness
```

Product experiments therefore complement rather than replace SLA research.

## 9. First-class controversies

RQ-028 introduces `CTR-*` records.

This fixes a major failure mode of narrative AI synthesis:

```text
find evidence A
find evidence B
write smooth paragraph
→ disagreement disappears
```

Instead:

```text
competing positions
+ supporting claims
+ boundary conditions
+ current resolution
+ what would change our mind
```

remain queryable.

Initial records prove the mechanism on three real disputes:

- `CTR-SLA-001` explicit instruction vs spontaneous/implicit ability;
- `CTR-CF-001` prompts vs recasts/supplied correction;
- `CTR-CONT-001` lexical threshold vs continuous/modality-sensitive coverage.

## 10. Null and negative evidence

RQ-028 rejects positive-result curation.

A future research digest must preserve credible null/negative findings and explain plausible interpretations.

This is especially important for an AI-run research program because an agent prompted to "find the best method" can otherwise preferentially collect confident positive conclusions.

## 11. Updating the knowledge base

Scientific knowledge is provisional.

A claim may move through:

```text
ACTIVE
→ NARROWED / REVISED
→ SUPERSEDED
```

without deleting the historical record.

Resynthesis triggers:

1. stronger/newer synthesis;
2. important replication disagreement;
3. more direct target-population evidence;
4. direct Nếp experiment;
5. changed validity interpretation;
6. major methodological/bias reassessment;
7. controversy-state change.

## 12. Consequence for stable IDs

RQ-028 adds:

```text
EVA-*  evidence appraisal
CTR-*  controversy record
```

The repository validator must verify their references.

Machine validity still means only:

```text
references are structurally consistent
```

not:

```text
scientific conclusion is true
```

## 13. Consequence for the old A–E system

Do not delete `A–E`; too many existing claims use it and it remains a useful shorthand.

But from now on:

```text
A–E = retrieval shorthand
EVA = confidence explanation
CTR = disagreement/boundary representation
```

For a core `SYN-METHOD-001` rule, `A` alone is insufficient.

## 14. Method-synthesis promotion gate

Before a statement is called a **high-confidence core Nếp Method rule**, require:

```text
verified source lineage
+ narrow claim(s)
+ claim-level appraisal
+ valid construct link
+ population/product directness stated
+ controversy checked
+ uncertainty/boundaries stated
+ falsification/validation path
```

Statements that fail this gate may still appear as:

- provisional constraints;
- candidate policies;
- unresolved alternatives;
- target-validation questions.

They must not be hidden behind authoritative language.

## 15. What RQ-028 does not solve

It does not:

- magically remove researcher/AI judgment;
- guarantee searches are exhaustive;
- produce universal numeric confidence;
- make indirect evidence useless;
- replace expert critique;
- replace direct learner experiments;
- imply all RQ-001–RQ-027 claims have already been reappraised.

The final point matters.

`SYN-METHOD-001` should strategically reappraise the **claims necessary for the core method**, not blindly score hundreds of claims before synthesis.

## 16. Decision

Mark RQ-028 **initial meta-foundation synthesis complete** once registry validation/CI confirms the new `EVA-*` and `CTR-*` graph.

This closes the planned P12 literature/methodology blocker.

It does **not** mean the English-learning method is proven.

It means the repository finally has a defensible process for deciding which findings are strong enough, direct enough and consistent enough to enter the method—and for exposing uncertainty where they are not.

Next gate after successful audit: `SYN-METHOD-001 — Nếp Method v0`.
