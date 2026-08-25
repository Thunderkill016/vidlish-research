---
id: RQ-004-SOURCE-DIGEST
title: Retrieval and spacing source digest
status: verified-initial-cycle
research_question: RQ-004
last_verified: 2026-08-25
---

# RQ-004 source digest — retrieval, spacing and review scheduling

## Research question

What retrieval schedule gives useful delayed retention while keeping time-on-task reasonable for a near-A0 language learner?

## Source set and extraction

### `SRC-0003` — Kim & Webb, spaced-practice meta-analysis

- 98 effect sizes from 48 L2 experiments (N = 3,411).
- Spaced practice produced a medium-to-large average benefit over massed practice.
- Shorter and longer spacing were similar on immediate tests, while longer spacing was stronger on delayed tests.
- Equal and expanding spacing were statistically equivalent overall.
- Learning target, number of sessions, practice/activity type, feedback timing and retention interval helped explain heterogeneity.

**Use for Nếp:** strong evidence for spacing and for rejecting one universal relative-spacing ritual.

### `SRC-0004` — Nakata, within-session repeated retrieval

- Japanese learners practiced L2 word pairs with different retrieval frequencies.
- Five and seven retrievals produced higher raw posttest performance than one and three.
- When time-on-task was controlled, one retrieval produced the largest gain per unit time.

**Use for Nếp:** repeated retrieval helps, but repetition count must be judged against learner time rather than treated as a target KPI.

### `SRC-0037` — Nakata, expanding versus equal spacing

- Manipulated relative spacing and absolute spacing for L2 word pairs.
- Found only a limited advantage for expanding spacing while the amount of spacing had a larger effect.
- The result sits inside a mixed literature later synthesized by `SRC-0003`.

**Use for Nếp:** do not hard-code “expanding is scientifically best.”

### `SRC-0038` — Nakata, retrieval formats

- Compared recognition, recall, hybrid and productive-recall practice.
- Recall formats were stronger when productive orthographic knowledge was the criterion.
- Recognition could be efficient when spelling/productive form was not required.

**Use for Nếp:** the review task should be selected from the capability claim, not from a single generic flashcard format.

### `SRC-0039` — Nakata, feedback timing

- Compared immediate versus delayed feedback while controlling lag to final test.
- Found little evidence that one feedback timing universally improved L2 vocabulary learning.

**Use for Nếp:** capture retrieval before reveal, then prefer low-friction correction; do not introduce artificial feedback delay as dogma.

### `SRC-0040` — Rowland, testing-effect meta-analysis

- Large general-learning meta-analysis comparing testing/retrieval with restudy.
- Retrieval practice generally improved later retention.
- Initial recall tests often produced stronger testing benefits than recognition, and successful/effortful retrieval mattered.

**Scope limit:** not specific to Vietnamese A0 English learning. Used for the memory mechanism, not for exact Nếp interval rules.

### `SRC-0041` — Pan & Rickard, transfer meta-analysis

- 192 transfer effect sizes from 122 experiments.
- Retrieval practice produced positive average transfer relative to non-testing reexposure, but effects varied substantially by transfer type and training conditions.

**Use for Nếp:** retrieval can contribute to transfer, but a successful scheduled review cannot itself be labeled `transferred`.

### `SRC-0042` / `SRC-0043` — MaiMemo memory-model scheduling research

- Built predictive memory models and optimized review schedules on very large real-world longitudinal logs.
- The research objective is recall/memorization efficiency and review cost.

**Use for Nếp:** supports adaptive memory scheduling as an engineering layer.

**Boundary:** the model outcome is memory recall, not listening comprehension, spontaneous speaking, pragmatic competence or changed-context language transfer.

### `SRC-0044` — FSRS engineering documentation and benchmark

- FSRS uses a difficulty/stability/retrievability-style memory model and predicts card recall from review history.
- The open benchmark evaluates recall-prediction accuracy on large Anki review logs.
- It is useful engineering evidence, but not a peer-reviewed randomized test showing that FSRS causes better English learning for Nếp learners.

**Use for Nếp:** FSRS remains a reasonable scheduler implementation candidate, but it must stay behind a product adapter and version pin.

## Evidence boundaries

This cycle did **not** establish:

- a universal `1d → 3d → 7d → 14d` schedule;
- that expanding spacing is always superior;
- that a specific FSRS desired-retention value is optimal for Nếp;
- that `Hard/Good/Easy` self-ratings are valid language-assessment labels;
- that predicted recall probability equals mastery;
- that one due date can represent all modalities and capabilities of a lexical item.
