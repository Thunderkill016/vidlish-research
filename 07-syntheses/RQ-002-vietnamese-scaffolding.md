---
id: SYN-SCF-001
title: Vietnamese scaffolding near A0
status: initial-synthesis
research_question: RQ-002
last_verified: 2026-08-25
---

# RQ-002 — Vietnamese scaffolding near A0

## Research question

What amount and type of Vietnamese scaffold can help a near-A0 learner understand and
learn English without letting the Vietnamese support replace the English task?

## Decision summary

Nếp should use **strategic, progressive Vietnamese support**, not an English-only policy
and not always-on translation.

The default product model is:

```text
English target/context
    ↓
independent first attempt when the task is measurable
    ↓
smallest support needed to restore access
    ↓
Vietnamese micro-gloss / instruction / contrastive note as needed
    ↓
return attention to English
    ↓
later retry with less support
```

This is a product synthesis. The literature supports the usefulness of L1/multilingual
scaffolding, especially for beginners and vocabulary meaning access, but it does **not**
supply a universal percentage of L1 or a validated Nếp fading threshold.

## What the evidence supports

### 1. English-only is not a scientific requirement for beginners

Recent meta-analytic evidence finds positive average outcomes for multilingual or
translanguaging approaches relative to monolingual approaches across represented L2
settings (`SRC-0020`, `SRC-0021`). Controlled beginner studies also show that principled
L1 inclusion can coexist with, and in those studies improve, productive L2 outcomes
(`SRC-0022`, `SRC-0023`).

This does not mean all L1 use is beneficial. It means Nếp should not create artificial
difficulty merely to preserve an English-only ideology.

### 2. The clearest early use case is fast access to lexical meaning

Two meta-analytic lines converge on the usefulness of L1 lexical support:

- L1 glosses can outperform L2 glosses, with a particularly large relative advantage for
  beginners in one meta-analysis (`SRC-0017`);
- L1 verbal lexical explanation outperformed L2 explanation in both immediate and delayed
  vocabulary outcomes (`SRC-0018`);
- broader gloss meta-analyses show that glosses facilitate word learning and that L1
  glosses can be effective (`SRC-0024`, `SRC-0025`).

For a true A0 learner, an English definition can contain more unknown language than the
word being taught. A concise Vietnamese equivalent can therefore be a lower-cost bridge
to the intended meaning.

### 3. Support must be tied to a function, not sprayed over the page

The research literature bundles many multilingual practices: translation, lexical
explanation, task planning, language comparison, note-taking, discussion, and more.
Because those mechanisms differ, Nếp should label the purpose of every scaffold.

Initial product categories:

| Scaffold type | Purpose | Example |
| --- | --- | --- |
| `instruction_vi` | understand what to do | "Nghe và chọn ý đúng" |
| `meaning_gloss_vi` | establish lexical meaning | `borrow → mượn` |
| `context_hint_vi` | clarify scenario without giving English answer | "Bạn đang hỏi mượn sạc" |
| `contrastive_note_vi` | flag useful L1–L2 difference | short word-order/pragmatic note |
| `feedback_vi` | explain why an answer failed | concise correction |
| `full_translation_vi` | rescue comprehension after failure | whole message meaning |

The last category should be more expensive in the support hierarchy because it can replace
the comprehension task if revealed too early.

### 4. Learning mode and measurement mode need different support rules

This follows from RQ-001's task-sensitive evidence model as well as the gloss literature's
sensitivity to test format.

During **teaching**, Vietnamese may be used to make meaning available efficiently.

During an **independent evidence attempt**, the exact answer-bearing Vietnamese support
must be hidden until after the attempt. If the learner succeeds only after a Vietnamese
translation appears, Nếp records scaffolded performance, not independent English
comprehension/recall.

This is not a claim that translation is harmful. It is a measurement-validity rule:
changing the cue changes what the task demonstrates.

### 5. The support ladder should be progressive disclosure, not binary on/off

Candidate ladder:

```text
S0  no answer-bearing Vietnamese support
S1  non-answer context cue / image / replay
S2  Vietnamese task instruction or narrow context hint
S3  Vietnamese micro-gloss for one target word/chunk
S4  partial meaning/paraphrase
S5  full Vietnamese translation / explicit answer-bearing help
```

Not every task uses every level. The system should request/reveal only the smallest useful
step and store the highest support level used.

### 6. Fading should be performance-driven, but the exact rule is unproven

`SRC-0017` provides evidence that the relative advantage of L1 glosses is larger at lower
proficiency. That supports the **direction** of gradual fading as English knowledge grows.

It does not validate:

```text
after 300 produced words → remove Vietnamese
```

or any other fixed threshold.

Therefore the existing "~300 words" idea is a curriculum/product hypothesis, not an
evidence-backed law. Nếp should fade support when repeated task evidence shows the learner
can perform at a lower support level, and calibrate that rule in `EXP-002`.

### 7. Immediate ease is not enough to judge a scaffold

The 2026 translanguaging meta-analysis reports very few delayed posttests (`SRC-0020`).
Gloss research also shows that results depend on immediate/delayed test and recognition/
recall format (`SRC-0017`, `SRC-0024`, `SRC-0025`).

Nếp therefore evaluates a scaffold on:

- immediate task access;
- unsupported later recall/comprehension;
- changed-context performance;
- time cost;
- dependence on repeated help.

A scaffold that makes every screen easy but leaves the learner unable to perform later is
not successful.

## Proposed Nếp scaffold policy

### Default for Stage 0 / near A0

- UI instructions may be Vietnamese or bilingual when English-only instructions would
  become a second learning task.
- Core target English remains visible/audible as the thing being learned.
- New word/chunk meaning can use a short Vietnamese gloss after the learner has had the
  intended first exposure/attempt.
- Avoid English-only dictionary definitions for first meaning access unless all definition
  language is already known.
- Full-sentence Vietnamese translation is **progressive rescue**, not default wallpaper.
- Independent recall/comprehension attempts hide answer-bearing translation.
- Every hint/reveal is logged with support type and level.

### As evidence grows

- suppress Vietnamese automatically on items/tasks where the learner repeatedly succeeds
  without it;
- keep one-tap support available during learning when failure would otherwise stop the
  session;
- reintroduce support after repeated failures, but do not overwrite the evidence as
  "independent";
- increase English paraphrases/examples only when they themselves are comprehensible.

## What we should not conclude

- "Vietnamese is always better than English."
- "Translation prevents thinking in English."
- "More Vietnamese means more learning."
- "English-only immersion is always superior."
- "A fixed 20%, 30%, or 300-word rule is scientifically established."
- "If a learner understands the Vietnamese translation, they understood the English."
- "The 2026 pooled translanguaging effect transfers unchanged to one Vietnamese adult
  using a web app."

## Product decisions unlocked

1. build scaffold provenance into learning attempts;
2. allow Vietnamese in Stage 0 without treating it as a temporary embarrassment;
3. move from always-on translation to progressive disclosure;
4. remove any hard-coded claim that support must fade at exactly 300 words;
5. distinguish `unsupported_success` from `success_after_support`;
6. make `EXP-002` a prerequisite for locking the production fading policy.

## Open questions after RQ-002

- Does a micro-gloss outperform full translation for Nếp delayed learning?
- Should the first comprehension attempt occur before *any* Vietnamese hint at true A0?
- Which scaffold level produces the best delayed learning per minute?
- How many independent successes justify suppressing a scaffold?
- Does learner-requested support work better than automatically revealed support?
- Are these effects different for audio-first vs text-first tasks?

Those are product questions, not gaps that should be filled by guessing.
