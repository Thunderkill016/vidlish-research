---
id: SYN-GRM-001
title: Grammar as learned form–meaning–use constructions
status: initial-synthesis
research_question: RQ-012
last_verified: 2026-08-25
---

# RQ-012 — Grammar/constructions for near-A0 learners

## Decision summary

Nếp should teach grammar as **usable form–meaning–use patterns**, not as a catalogue of rules and not as exposure with no requirement to process form.

Candidate sequence:

```text
meaningful message/context
        ↓
interpret meaning
        ↓
notice the form that carries the meaning
        ↓
brief explanation / contrast when useful
        ↓
structured interpretation on new examples
        ↓
controlled production / substitution
        ↓
changed-context production
        ↓
delayed unseen interpretation + production
```

The explanation is a scaffold. Rule recall is not mastery.

## Why Nếp should not become a traditional grammar course

Meta-analytic research consistently shows that focused L2 instruction can accelerate learning and that explicit treatments often produce strong gains (`SRC-0119`, `SRC-0120`, `SRC-0121`, `SRC-0122`). That does **not** imply this product rule:

```text
explain rule first
→ grammar worksheet
→ mark grammar mastered
```

The research base is sensitive to outcome measurement. Selected-response, grammaticality-judgment and tightly constrained tasks can reflect explicit/controlled knowledge more strongly than spontaneous use. Therefore Nếp must preserve what kind of evidence an assessment actually supplies.

## Interpret before demanding free production

Comprehension-based and production-based instruction both improve grammar learning. Meta-analytic comparisons suggest that comprehension/processing instruction is especially useful for receptive form–meaning knowledge, while production practice becomes important for productive knowledge and can show delayed advantages (`SRC-0123`, `SRC-0124`).

For a near-A0 learner, this suggests:

```text
Do not start with:
"Produce a correct present-tense sentence."

Start with:
Which message does this form mean here?
```

Then move toward production once the form–meaning relation is sufficiently available.

Example:

```text
Audio/context:
"I want water."

Meaning task:
What does the speaker want?

Notice:
I want + THING

New interpretation:
"I want coffee."

Controlled production:
I want ___ .

Changed context:
You are at a café. Ask for tea.

Later:
new speaker + new object + no displayed pattern
```

## Structured input is more than highlighting

Processing Instruction research targets how learners interpret forms while attention is on meaning. Its useful product lesson is not that Nếp must copy a branded teaching method exactly. It is that grammar activities can require the target form to be **necessary for successful interpretation**.

Bad task:

```text
Read: Yesterday I walked home.
Question: Where did I go?
```

The learner can answer without processing `-ed`.

Better diagnostic task when testing past-time form–meaning mapping:

```text
I walk home.
I walked home.

Which one describes a completed past event?
```

The exact task must still be communicatively sensible and level-appropriate.

Textual bolding/underlining alone is insufficient as a learning mechanism (`SRC-0125`). Salience can direct attention, but the learner must process what the form contributes.

## Use constructions as curriculum units

A useful product abstraction is a construction:

```ts
type Construction = {
  id: string;
  form: string;
  function: string;
  meanings: string[];
  contexts: string[];
  exemplars: string[];
  productiveSlots: string[];
  prerequisites: string[];
  contrasts: string[];
  receptiveTasks: string[];
  productiveTasks: string[];
  transferVariants: string[];
};
```

Examples near A0:

```text
I want + NOUN
I like + NOUN / -ing
I can + VERB
This is + NOUN
There is + NOUN
Do you + VERB ...?
Where is + NOUN?
I'd like + NOUN
```

These are not claimed as a final curriculum ordering. The point is representational: form and communicative function stay linked.

Usage-based research supports viewing morphology, chunks and syntactic frames as learned form–function pairings shaped by repeated meaningful exposure, frequency, contingency, salience and prior-language attention (`SRC-0126`). A targeted construction study also supports integrating attention to form and core meaning rather than relying on metalanguage or frequency alone (`SRC-0131`).

## Exemplars before unrestricted abstraction

Near-A0 learners should encounter a small set of highly interpretable exemplars before being expected to generalize broadly.

Candidate path:

```text
I want water.
I want coffee.
I want a ticket.
        ↓
I want + [thing]
        ↓
novel compatible nouns / situations
```

Do not infer that raw repetition count is enough. Frequency interacts with variation, salience, meaning and contingency (`SRC-0126`). The exact exemplar distribution is an experimentable product parameter.

## Explicit explanation: bounded support, not forbidden and not sovereign

A near-A0 learner may benefit from a short Vietnamese or simple-English explanation when a pattern is difficult to infer. The literature does not justify either extreme:

```text
Never explain grammar.
```

or:

```text
Grammar learning = memorizing explanations.
```

Candidate Nếp rule:

```text
meaning first when feasible
→ learner processes examples
→ smallest explanation that resolves confusion
→ immediately return to interpretation/use
```

Store whether explanation was shown before success.

## Grammar evidence model

Do not store:

```text
construction.known = true
```

Store multiple dimensions:

```text
recognized_form
mapped_form_to_meaning
interpreted_new_example
produced_controlled
produced_changed_context
processed_in_real_time
retained_after_delay
```

And preserve support state:

```text
with_rule_visible
with_model_visible
with_choices
with_L1_explanation
unsupported
```

## Rule knowledge is useful evidence — just not enough

Metalinguistic explanation or error correction can show explicit knowledge. It can help instruction and diagnosis. But measurement research shows explicit, automatized and implicit knowledge are difficult to separate and that even commonly used time-pressured tasks may draw on more than one knowledge system (`SRC-0127`, `SRC-0128`).

Therefore UI labels should remain behavioral:

```text
"Can interpret this pattern without help"
"Can use it in a new situation"
```

not speculative latent labels such as:

```text
"Implicit grammar mastery: 82%"
```

unless such a model is independently validated.

## Corrective feedback belongs inside use

Corrective-feedback meta-analyses show that feedback can produce durable L2 development (`SRC-0129`, `SRC-0130`). But the literature does not establish one best feedback type for every learner, construction and modality.

Candidate near-A0 feedback ladder:

```text
production attempt
→ preserve meaning/intelligibility first
→ if target construction error matters:
    prompt self-repair when learner likely has the form
    OR provide bounded model/reformulation when learner lacks it
→ retry
→ changed example later
```

This is a product synthesis, not a universal empirical law. Feedback policy deserves its own later calibration if needed.

## Integration across skills

A construction should not live only in a Grammar tab.

```text
LISTENING
recognize pattern in speech

READING
interpret pattern in text

SPEAKING
produce it for a purpose

WRITING
generate/modify it

INTERACTION
respond to another speaker using it

REVIEW
retrieve and transfer after delay
```

This is how grammar becomes part of a comprehensive English system rather than an isolated school subject.

## Product decision

Create `FEAT-GRM-001` — **Meaning-linked construction learning engine**.

Its mastery model must require more than rule recall. `EXP-012` will test whether the integrated form–meaning–use loop provides better delayed unseen interpretation and production per learning minute than rule-first drill or meaning-only exposure.

## Open assumptions

- exact order of interpretation and production for each construction;
- when a Vietnamese explanation should appear;
- how many exemplars precede abstraction;
- how much lexical variation is useful near A0;
- which constructions should be taught as chunks before analysis;
- feedback choice by error/learner state;
- construction sequencing for Vietnamese adults;
- thresholds for moving from controlled to changed-context production.
