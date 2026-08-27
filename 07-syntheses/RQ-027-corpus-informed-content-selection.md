# RQ-027 — Corpus-informed beginner language/content selection

**Status:** initial meta-foundation synthesis complete  
**Date:** 2026-08-27  
**Claims:** `CLM-CONT-001`–`CLM-CONT-026`  
**Evidence digest:** `06-evidence/RQ-027-source-digest.md`

## 1. Research question

> Which words, chunks, constructions, functions and pragmatic routines deserve scarce beginner learning time when target needs are combined with real-language frequency, range, dispersion, coverage, formulaicity, learnability and prerequisite value?

## 2. Main conclusion

There is no defensible single list that can be sorted once and used as the beginner curriculum.

The best-supported model is:

```text
target needs / target tasks
        +
portable general-language utility
        +
representative corpus evidence
        +
learner / L1 learning cost
        +
reusable form–meaning/function value
        ↓
CONTENT PRIOR
        ↓
learner evidence + sequencing constraints
        ↓
TEACHING DECISION
```

This separates two decisions that the old Vidlish curriculum repeatedly collapsed:

```text
WHAT deserves inclusion?
≠
WHAT should be taught next?
```

Corpus evidence is strong for the first question. It is insufficient by itself for the second.

## 3. What counts as content

RQ-027 rejects a curriculum ontology containing only `word` and `grammar point`.

The minimum research-supported candidate unit types are:

```text
LEXEME / SENSE
MULTIWORD UNIT / COLLOCATION
CONSTRUCTION / FORM–FUNCTION PATTERN
PRAGMATIC / INTERACTION ROUTINE
```

These categories can overlap; they are pedagogical units, not claims about one correct mental representation of language.

### Example

A capability such as repairing misunderstanding may involve:

```text
lexeme: mean
chunk: What do you mean?
construction: What do you + VERB?
routine/function: request clarification
```

A useful curriculum may need all four levels of representation without teaching four disconnected lessons.

## 4. Content priority dimensions

RQ-027 supports a multi-criteria selector.

### 4.1 Target-task value

From RQ-023:

- Does the item occur in a high-value target task?
- Is it necessary or strongly helpful for task completion?
- How often is that task expected?
- What is the consequence of not having the language?

A lower-frequency expression can outrank a more frequent word if the former is central to a high-value target capability.

### 4.2 Portable general utility

A high-frequency, widely dispersed core is valuable because it recurs across many contexts.

This creates a strong prior for beginner content, not a fixed order.

### 4.3 Frequency + range/dispersion

Use at least:

```text
token frequency
+
range / dispersion
```

Raw frequency alone can reward domain bursts.

### 4.4 Corpus/domain/modality fit

Every corpus statistic must answer:

```text
frequency WHERE?
for WHICH modality?
in WHICH register/domain?
from WHICH sample period?
```

Conversation/listening content should not be selected from written-frequency evidence alone.

### 4.5 Formulaic/construction value

Some recurring multiword sequences are processed efficiently and carry stable functions. Some constructions support broad recombination across many target tasks.

This gives candidate priority to useful reusable patterns rather than isolated words only.

### 4.6 Coverage contribution

Coverage helps estimate how much a lexical item or pool improves access to a target corpus/material set.

But coverage is an outcome/property of a content set, not a complete pedagogical objective.

### 4.7 Learning cost / Vietnamese-L1 prior

Learning cost may be affected by:

- L1 congruency;
- phonological difficulty;
- morphology;
- semantic opacity/polysemy;
- orthography–sound mapping;
- collocational unpredictability;
- prior learner evidence.

Vietnamese population evidence remains a prior, never an individual diagnosis.

### 4.8 Generative/prerequisite value

Early content may deserve extra priority when it unlocks many useful messages or constructions.

Examples of legitimate generativity:

```text
one high-value construction
→ many target-task utterances

one interaction routine
→ repair across many situations
```

Not legitimate:

```text
traditional grammar chapter comes earlier
→ therefore prerequisite
```

## 5. Provisional selection model

Do **not** prematurely assign one universal weighted score.

Represent dimensions separately first:

```ts
type ContentCandidate = {
  id: string;
  unitType: "lexeme" | "multiword" | "construction" | "pragmatic_routine";

  targetTaskValue: number | null;
  portableUtility: number | null;

  corpus: {
    sourceIds: string[];
    modality: "spoken" | "written" | "mixed";
    register?: string;
    domain?: string;
    frequency?: number;
    range?: number;
    dispersion?: number;
    coverageDelta?: number;
    associationStrength?: number;
    countingUnit?: string;
  }[];

  formulaicOrConstructionValue?: number | null;
  generativeValue?: number | null;
  estimatedLearningCost?: number | null;
  vietnamesePrior?: string[];
  learnerGapEvidence?: string[];

  confidence: "high" | "moderate" | "low" | "unknown";
};
```

This is a research representation, not yet the product schema.

## 6. Dominance rules before numeric weighting

Some evidence should behave as a gate/override rather than an additive point score.

Candidate examples for later validation:

### Rule A — target necessity can override global frequency

If an item is essential for a high-value target task, low global frequency does not automatically exclude it.

### Rule B — corpus mismatch invalidates rank

High frequency in a corpus with poor target-domain fit should not dominate selection.

### Rule C — known content should not consume deliberate-learning time by default

Individual evidence can lower deliberate-teaching priority even for globally useful items, while still allowing recycling in context.

### Rule D — high learning cost does not always lower priority

A difficult item that is highly necessary may need **earlier/more supported learning**, not deferral.

### Rule E — content type affects evidence needed

Knowing component words cannot prove a collocation/chunk is known; recognizing a construction cannot prove productive use.

These rules remain candidates until curriculum/learner validation.

## 7. Coverage policy

RQ-027 consolidates earlier readiness work:

```text
coverage rises
→ comprehension probability generally rises
```

but:

```text
98% reading
90–95% listening in some studies
video-specific results
```

must not be collapsed into one threshold.

Therefore coverage may support:

- material matching;
- text adaptation;
- scaffold decisions;
- estimation of lexical load;

but not:

```text
vocabulary_size >= X
→ learner can use authentic English
```

## 8. Why CEFR/EVP cannot be the teaching order

The English Vocabulary Profile is useful evidence about what learners at different CEFR levels tend to know/use.

That means:

```text
EVP = descriptive learner evidence / reference
```

not:

```text
EVP A1 item 1
→ teach first
```

The same applies to grammar profiles and word-frequency lists.

## 9. Implication for Nếp curriculum architecture

RQ-023 proposed:

```text
portable capability core
↓
learner target situations
↓
domain branches
```

RQ-027 adds the language-content layer:

```text
TARGET CAPABILITY
      ↓
representative target discourse
      ↓
extract candidate
words + chunks + constructions + routines
      ↓
score / annotate by
utility + distribution + modality + coverage + cost + generativity
      ↓
filter against learner evidence
      ↓
sequence later using learning-method constraints
```

This is fundamentally different from:

```text
A1 grammar checklist
+
3000 frequent words
→ units
```

## 10. What RQ-027 rejects

The following claims are not supported as universal curriculum rules:

1. "Teach the 3,000 most frequent words first."
2. "Teach all CEFR A1 vocabulary before A2 vocabulary."
3. "Teach words strictly by corpus frequency."
4. "98% coverage is a universal comprehension threshold."
5. "Knowing the root means knowing the word family."
6. "Single words are the complete vocabulary curriculum."
7. "Native-speaker corpora automatically represent target English use."
8. "Hard Vietnamese items should simply be postponed."
9. "Corpus inclusion automatically determines lesson sequence."

## 11. Unresolved questions

RQ-027 does not establish:

- exact numeric weights among selection dimensions;
- exact first 100/500/1000 items for Nếp;
- exact target-task corpus before `EXP-023` data;
- exact optimal lexical counting unit for every product decision;
- exact balance of receptive vs productive content;
- how much low-frequency domain language belongs in the portable core;
- exact construction-generativity metric;
- direct learning-cost estimates for Vietnamese near-A0 adults.

These remain validation questions.

## 12. Decision

Mark RQ-027 **initial meta-foundation synthesis complete**.

The research-supported content rule is:

> **Nếp should select English content by triangulating target-task value with representative corpus evidence, portable utility, distribution, modality/register, multiword/construction value, coverage contribution, learning cost and generative value. No frequency list, CEFR profile or corpus ranking is allowed to become the curriculum by itself.**

Next blocker: `RQ-028 — evidence grading, contradiction and update protocol`.
