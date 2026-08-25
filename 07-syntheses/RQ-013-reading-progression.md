---
id: SYN-READ-001
title: Reading progression from word access to sustained independent comprehension
status: initial-synthesis
research_question: RQ-013
last_verified: 2026-08-25
---

# RQ-013 — Reading progression for near-A0 learners

## Decision summary

Nếp should treat reading as a progression across **written-form access, language comprehension, connected-text understanding and fluency**, not as a single `reading_score` and not as a sequence of translation exercises.

Candidate progression:

```text
short high-clarity messages
        ↓
connected microtexts
        ↓
graded short texts
        ↓
sustained easy reading
        ↓
increasingly authentic texts
```

At every stage:

```text
independent first attempt
→ record what the learner can read unaided
→ smallest useful support if needed
→ continue reading for meaning
→ later reduced-support / unseen text
```

Audio, glosses and strategy prompts are scaffolds. Success with them visible is not independent-reading success.

## Reading is not one skill

Meta-analytic work shows that L2 reading comprehension depends on multiple interacting components, including decoding/written-word access, vocabulary, grammar/construction knowledge and broader language comprehension (`SRC-0134`, `SRC-0135`).

Therefore Nếp should separate at least:

```text
written_form_recognition
lexical_access
construction_interpretation
sentence_understanding
connected_text_gist
connected_text_detail
reading_fluency
sustained_reading
```

This avoids two common errors:

```text
reads words aloud quickly
→ assumed to understand text
```

and:

```text
answers a gist question using one familiar keyword
→ assumed to read independently
```

## Start with understandable connected meaning, not isolated sentences forever

Sentence-level tasks are useful for establishing vocabulary and constructions, but a comprehensive system must teach learners to maintain meaning across sentences.

Near-A0 candidate path:

### Stage R0 — bounded messages

```text
Hello. I'm Mai.
I live in Hanoi.
```

Targets:
- recognize known written forms;
- understand one short proposition;
- connect text to an already learnable message.

### Stage R1 — connected microtexts

```text
I'm Mai. I live in Hanoi. I work in a café.
```

Targets:
- maintain a referent across sentences;
- combine known vocabulary/constructions;
- answer gist/detail without translation of every word.

### Stage R2 — graded short texts

Short narratives/dialogues/descriptions with high learner-specific lexical and construction readiness.

Targets:
- process several connected ideas;
- tolerate a small number of unknowns;
- use bounded lookup only when needed;
- reread strategically without being forced to inspect every sentence.

### Stage R3 — sustained easy reading

Repeated exposure to easy/graded texts for meaning and volume. Extensive-reading meta-analyses support positive effects across reading and other language outcomes (`SRC-0132`, `SRC-0133`).

The product implication is not "unlock a giant library and tell the learner to read anything." Text selection should remain level-aware and friction should be low enough to preserve reading flow.

### Stage R4 — increasingly authentic reading

As lexical/construction coverage, comprehension and fluency improve, introduce authentic messages, posts, instructions, articles and stories in locally usable windows. Authenticity is not a reason to ignore readiness.

## Lexical coverage is a readiness feature, not a magic threshold

Reading comprehension generally improves as more words in a text are known (`SRC-0136`, `SRC-0088`). Figures such as 95% or 98% are useful anchors from specific research traditions, but should not become:

```ts
if (coverage >= 0.98) unlock();
```

Coverage interacts with:
- text genre and purpose;
- importance of unknown words;
- construction difficulty;
- background knowledge;
- learner inferencing ability;
- desired comprehension criterion;
- available support.

Nếp should compute **learner × text readiness**, not one universal reading level.

## Easier text is often the correct learning material

Extensive-reading evidence and direct text-difficulty research support the value of reading material that is comfortably comprehensible (`SRC-0133`, `SRC-0140`). Near-A0 learners do not need to struggle through authentic paragraphs to prove that the reading is "real."

Product rule:

```text
if a learner must stop every line,
translate repeatedly,
or cannot maintain the message,
the text is probably functioning as an intensive decoding task,
not sustained reading.
```

Both intensive and extensive reading can have a place, but the system should know which task it is giving.

## Glosses and Vietnamese support: preserve flow, preserve provenance

Existing gloss meta-analyses (`SRC-0025`, `SRC-0017`, `SRC-0024`) support accessible form/meaning help during L2 reading. The RQ-002 rule still applies: support should solve a bounded problem without silently becoming the task.

Candidate support policy:

```text
first attempt / first phrase
→ no full translation
→ tap unknown word/chunk if meaning blocks progress
→ show bounded Vietnamese or simple-English gloss
→ continue text
```

Avoid default line-by-line bilingual display for independent-reading measurement.

Store:

```text
gloss_opened
translation_opened
support_scope
support_language
unknown_item
position_in_text
```

Then distinguish:

```text
independent_text_understanding
understanding_after_gloss
understanding_after_translation
```

## Audio-assisted reading: optional bridge, not permanent reading mode

Reading-while-listening can support word-form/sound mapping and some learners may benefit, but the broad meta-analysis found only a trivial overall comprehension advantage over reading-only and no reliable advantage when reading-only was self-paced (`SRC-0139`).

Therefore:

```text
text + audio success
≠
independent reading success
```

Candidate uses:
- early orthography↔sound mapping;
- fluency repair;
- first encounter with a graded text when word recognition is slow;
- optional accessibility/support;
- repeated-reading variant.

Then fade audio and test the learner on a new text without it.

Vietnamese EFL studies show repeated/audio-assisted reading can improve fluency/rate (`SRC-0141`, `SRC-0142`), but the exact dose and near-A0 benefit must be tested directly.

## Reading fluency is not words per minute

Reading fluency includes efficient, accurate processing that supports comprehension; rate is only one observable component (`SRC-0143`).

Nếp should never optimize:

```text
maximize WPM
```

while comprehension collapses.

Candidate fluency evidence:

```text
reading_time
word/phrase regressions when measurable
accuracy on meaning probes
first-pass gist
support use
reread count
```

Useful derived metric:

```text
comprehended words / minute
```

but even that is task-dependent and should not become a universal proficiency score without validation.

## Repeated reading belongs in repair/fluency practice, not every text

Repeated reading can improve fluency and has population-relevant evidence from Vietnamese learners (`SRC-0141`, `SRC-0142`). However, repeated exposure also makes a text familiar, so faster rereading does not prove transfer to unfamiliar text.

Store:

```text
exposure_index
first_read_time
repeat_read_time
first_read_comprehension
repeat_read_comprehension
```

Then test unfamiliar parallel text.

## Strategy instruction: useful later and targeted, not a near-A0 burden

Meta-analyses support L2 reading-strategy instruction (`SRC-0137`, `SRC-0138`), but effects vary and delayed evidence is relatively sparse in some syntheses.

Near A0, linguistic bottlenecks often dominate. Nếp should not teach a 10-strategy checklist before learners can understand basic sentences.

Candidate policy:

```text
observe recurring reading failure
→ introduce one strategy that addresses it
→ immediately apply it to a real text
→ later test without strategy prompt
```

Examples when appropriate:
- use title/context to set purpose;
- reread a sentence after gist failure;
- infer a noncritical unknown instead of opening every gloss;
- identify referent across sentences;
- use text structure at later proficiency.

## Reading evidence model

```ts
type ReadingAttempt = {
  textId: string;
  textStage: "message" | "microtext" | "graded" | "extended" | "authentic";
  firstSeen: boolean;
  audioVisible: boolean;
  glossCount: number;
  translationCount: number;
  rereadCount: number;
  readingMs: number;
  gistCorrect?: boolean;
  detailCorrect?: boolean;
  targetFormAccess?: number;
  lexicalCoverageEstimate?: number;
  constructionCoverageEstimate?: number;
};
```

Learner model should infer evidence cautiously rather than directly equating these fields with mastery.

## Product integration

Reading should reuse, not duplicate, other engines:

```text
Vocabulary Engine
        ↓
Construction Engine
        ↓
Reading Readiness
        ↓
Connected Text
        ↓
bounded support from Scaffold Engine
        ↓
Transfer / Review
```

A word or construction learned through listening/speaking should become readable; reading encounters should also feed later recall/use without making every unknown word a flashcard automatically.

## Product decision

Create `FEAT-READ-001` — **Adaptive reading progression engine**.

It should select the shortest connected text that meaningfully stretches the learner, preserve independent-first evidence, offer bounded help, and progressively increase connected-text length/novelty while tracking fluency separately from comprehension.

## Open assumptions

- exact lexical/construction readiness bands for each reading stage;
- microtext length near A0;
- when to introduce graded extensive reading;
- optimal amount of repeated reading;
- whether audio should be optional, system-triggered or scheduled;
- reading-rate targets for Vietnamese adults;
- when strategy instruction becomes worth the time;
- how much free text choice to permit at each stage;
- how to balance fiction, dialogue, practical and informational text;
- whether on-demand Vietnamese glosses preserve enough independent processing.
