---
id: FEAT-GRM-001
title: Meaning-linked construction learning engine
status: research-backed-candidate
research_question: RQ-012
---

# Feature research spec — Meaning-linked construction learning engine

## Learner problem

Learners can memorize grammar rules and succeed on fill-in-the-blank exercises while still failing to understand or use the same pattern in speech, reading, writing or interaction.

Near-A0 learners also cannot be expected to infer all grammar from uncontrolled exposure or to produce complex patterns before they can reliably map form to meaning.

## Target capability

Understand and use a grammatical construction for a communicative purpose across new examples, with progressively less support and after delay.

## Research basis

- `SYN-GRM-001`
- `CLM-GRM-001` through `CLM-GRM-016`
- `PRN-133` through `PRN-148`
- `FEAT-SCF-001`
- `FEAT-LIS-001`
- `FEAT-TRN-001`
- `FEAT-SPK-001`
- `FEAT-REV-001`

## Construction representation

```ts
type Construction = {
  id: string;
  label: string;
  formPattern: string;
  communicativeFunctions: string[];
  meanings: string[];
  contexts: string[];
  exemplars: string[];
  productiveSlots: string[];
  prerequisites: string[];
  contrasts: string[];
  modalityTargets: Array<"listening" | "reading" | "speaking" | "writing">;
};
```

The schema should permit both relatively fixed chunks and more abstract patterns.

## Candidate learning state

```ts
type ConstructionEvidence = {
  recognizedForm?: number;
  mappedFormToMeaning?: number;
  interpretedNewExample?: number;
  producedControlled?: number;
  producedChangedContext?: number;
  realTimeProcessing?: number;
  retainedAfterDelay?: number;
};
```

These are evidence dimensions, not guaranteed latent traits.

## Support provenance

Every attempt records whether the learner had:

```text
no support
choices
model visible
English explanation
Vietnamese explanation
highlighted form
partial prompt
full reformulation
```

A success after a rule or model is revealed cannot be backfilled as unsupported construction use.

## Default lesson loop

```text
1. MESSAGE / CONTEXT
   learner first encounters understandable input

2. INTERPRET
   task forces relevant form–meaning processing

3. NOTICE
   target form is made inspectable after evidence is captured

4. EXPLAIN IF NEEDED
   smallest useful explanation / contrast

5. INTERPRET AGAIN
   new exemplar, reduced support

6. CONTROLLED PRODUCTION
   substitution / completion / bounded response

7. CHANGED-CONTEXT USE
   new lexical items, speaker, scenario or modality

8. DELAYED REVIEW
   unseen interpretation and/or production
```

The UI does not need to display these technical labels.

## Example

Target:

```text
I want + NOUN
```

Sequence:

```text
hear: "I want water."
→ choose intended meaning
→ inspect "I want ..."
→ hear/read "I want coffee."
→ complete "I want ___."
→ café scenario: ask for tea
→ next-day new scenario: ask for a ticket
```

Do not award the same evidence for each step.

## Structured interpretation task rule

When a construction is being assessed for form–meaning mapping, the answer should depend on processing the target form rather than be solvable from an unrelated content word, picture or temporal adverb alone.

## Explanation policy

Explanation may appear:

- after an initial meaningful attempt;
- after repeated form–meaning confusion;
- proactively for a construction shown by product data to benefit from it.

The exact trigger is experimental.

Explanation should be:

- short;
- tied to the current message;
- contrastive only when useful;
- followed immediately by another interpretation/use attempt.

Do not turn a five-second clarification into a grammar lecture.

## Example distribution

Candidate strategy:

```text
few high-clarity / high-frequency exemplars
→ controlled lexical variation
→ changed contexts
→ increasingly novel compatible uses
```

Do not hard-code a universal exemplar count from usage-based theory.

## Feedback policy

```text
learner output
→ determine whether error blocks target evidence
→ if likely retrievable: prompt
→ if missing/unstable: bounded model or explanation
→ retry
→ later changed example
```

All feedback is logged.

## Progress behavior

Progress should say things such as:

```text
Can understand “I can + action” in new short sentences — independent
Can use “I can + action” with a prompt — guided
Can use it in a changed situation — not enough evidence
```

Do not display:

```text
Past tense: 83% mastered
```

unless the underlying mastery model is separately validated.

## Falsification

The feature is weakened if:

- rule-first drill produces equal or better delayed unseen interpretation and production per minute;
- integrated lessons increase time without meaningful transfer gains;
- learners can pass construction tasks through lexical cues without processing the target form;
- construction-level scores fail to predict later use;
- explanation/support dependence does not fade;
- changed-context tasks mostly measure vocabulary rather than the construction.

## Experiment

See `EXP-012`.
