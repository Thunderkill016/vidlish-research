# EXP-028 — Evidence grading and contradiction protocol audit

**Status:** planned repository-methodology audit  
**Depends on:** RQ-028  
**Unit of analysis:** high-impact claims/syntheses in `vidlish-research`

## Purpose

RQ-028 changes how Nếp represents confidence. The protocol itself can fail by being too subjective, too expensive, too coarse, or unable to distinguish strong direct evidence from strong but indirect evidence.

This audit tests whether the protocol improves research decisions before it is relied on broadly in `SYN-METHOD-001`.

## Audit sample

Select a stratified sample of important claims from at least these domains:

- foundational SLA mechanisms;
- vocabulary/content selection;
- listening;
- speaking/output;
- grammar/constructions;
- corrective feedback;
- pronunciation/ASR;
- assessment validity;
- individual differences;
- AI/TTS/product mediation.

Include deliberately mixed cases:

```text
strong + direct
strong + indirect
weak + direct
heterogeneous / disputed
product inference
null/negative evidence
```

## Procedure

### Pass 1 — independent appraisal

At least two independent reviewers/agents appraise each selected claim on:

```text
methodological_quality
population_directness
construct_directness
replication_consistency
product_transfer_directness
```

They must provide rationale and may abstain when evidence is insufficient.

### Pass 2 — disagreement analysis

Do not merely calculate agreement.

For each disagreement, classify cause:

- unclear anchors;
- incomplete source access;
- different interpretation of construct;
- different target-population assumptions;
- different treatment of replication/heterogeneity;
- genuine reasonable judgment difference.

Revise protocol anchors only when disagreement exposes a systematic ambiguity.

### Pass 3 — controversy capture

Independently ask reviewers to identify important unresolved disagreements in the literature.

Measure whether `CTR-*` records:

- capture the actual competing positions;
- preserve null/negative evidence;
- identify meaningful boundary conditions;
- avoid false resolution;
- state useful revision triggers.

### Pass 4 — decision consequence

Compare method statements produced under:

A. legacy `A–E` only;
B. `A–E + EVA`;
C. `A–E + EVA + CTR`.

Blind reviewers judge whether each statement appropriately calibrates:

- scope;
- confidence;
- directness to Nếp users;
- construct validity;
- unresolved uncertainty;
- need for target validation.

## Primary success criterion

The protocol succeeds if B/C materially reduce **overconfident method promotion** relative to A without making every useful finding impossible to act on.

Operationally track:

```text
false-high-confidence rate
+
missed-usable-evidence rate
+
review time / claim
```

No single metric should dominate.

## Secondary outcomes

- inter-reviewer agreement by appraisal axis;
- proportion of disagreements resolved by clearer evidence versus subjective negotiation;
- number of previously hidden controversies found;
- number of A-level legacy claims downgraded in target/product directness;
- number of modest studies retained because they are unusually direct;
- appraisal time;
- percentage of claims where source access is insufficient;
- resynthesis triggers generated.

## Failure conditions

Simplify or revise the protocol if:

- reviewers cannot reliably distinguish axes;
- directness axes duplicate each other in practice;
- appraisals depend mainly on paper prestige/type rather than method/content;
- controversy records become generic prose with no decision value;
- review cost is so high that critical claims are skipped;
- the protocol mechanically downgrades all non-Vietnamese research to unusable;
- high-confidence method wording remains unchanged despite clearly indirect evidence.

## Scope control

Do **not** appraise every historical claim before drafting the method.

Instead:

```text
candidate core method statement
→ trace necessary claims
→ appraise those claims
→ check controversies
→ promote / narrow / label provisional
```

This keeps the protocol usable while protecting high-impact decisions.

## Result artifact

When executed, create a result artifact separate from this plan containing:

- sampled claim IDs;
- independent appraisals;
- disagreement log;
- revised anchors if any;
- method-promotion errors found;
- protocol changes;
- final decision on readiness for continued use.

Until that result exists, `EXP-028` is a validation plan, not proof that the protocol is reliable.
