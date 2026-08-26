---
id: SYN-CUR-001
title: Comprehensive over time, integrated by capability
status: initial-synthesis
research_question: RQ-017
last_verified: 2026-08-26
---

# RQ-017 — Integrated curriculum sequencing

## Decision summary

Nếp should not organize learning as independent skill silos and should not force every session to contain every language dimension.

The curriculum should be organized around **useful communicative capabilities/scenarios**, with prerequisite-aware microtasks that draw on only the skills needed for the learner's next step.

The governing rule is:

```text
comprehensive over time
+ integrated around use
+ diagnostic underneath
```

not:

```text
every lesson = listening + speaking + reading + writing + grammar + vocabulary + pronunciation
```

## Why capability is the organizing unit

The CEFR action-oriented model (`SRC-0001`) treats learners as language users and organizes learning toward real-life communicative action. Reception, production, interaction and mediation can occur together in a task/scenario.

For Nếp, a capability might be:

```text
order one drink
understand a simple price
say where you live
ask for repetition
reply to a simple availability question
write a short practical message
```

A capability is more useful than a `Grammar Unit 7` or `Speaking Lesson 12`, because the target already specifies what English must eventually do.

## Capability does not erase component learning

Communicative capability depends on component knowledge:
- vocabulary/chunks;
- constructions;
- phonological form;
- sound perception;
- reading/writing form where relevant;
- pragmatic function;
- retrieval efficiency.

Therefore the curriculum must be both:

```text
top-down: useful can-do
```

and:

```text
bottom-up: prerequisite language/evidence
```

The learner should not be asked to perform a rich scenario simply because the scenario is authentic.

## Course balance is measured across time

Nation's Four Strands (`SRC-0007`) provides a valuable course-audit frame:
- meaning-focused input;
- meaning-focused output;
- language-focused learning;
- fluency development.

However, the rough 25/25/25/25 split is a course heuristic, not a per-lesson prescription.

Nếp should audit strand balance over a configurable horizon such as multiple sessions or weeks.

Example:

```text
Session 1: mostly input + language focus
Session 2: retrieval + guided output
Session 3: interaction + changed-context use
Session 4: review + fluency + short reading
```

The four sessions can be balanced as a sequence even if no single session is.

## Near-A0 needs bounded integration

For a learner with very little English, too many novel demands in one task make failure uninterpretable.

If a task simultaneously contains:
- unknown words;
- unknown construction;
- fast unfamiliar speech;
- new pronunciation contrast;
- free speaking;
- multiple interaction turns;
- no scaffold;

then failure cannot tell the system what the learner needs next.

Candidate rule:

```text
ONE main new learning burden
+ familiar supporting language
+ bounded support
```

This is a product synthesis from task-complexity evidence and existing Nếp evidence, not a claim that research proves exactly one novel variable is universally optimal.

## Sequence complexity by controlled dimensions

Task sequencing research (`SRC-0186`, `SRC-0187`, `SRC-0189`) supports taking complexity seriously and gives partial support to simple-to-complex sequences.

Nếp should model task complexity explicitly instead of using a vague level label.

Candidate dimensions:

```ts
type TaskComplexity = {
  lexicalNovelty: number;
  constructionNovelty: number;
  inputLength: number;
  inputRate: number;
  propositionCount: number;
  inferenceDemand: number;
  outputLength: number;
  interactionTurns: number;
  partnerOrVoiceNovelty: number;
  supportReduction: number;
  timePressure: number;
  contextNovelty: number;
};
```

A task becomes harder by changing a limited subset, allowing both learner adaptation and interpretable evidence.

## Simple → complex does not mean easy forever

More complex tasks can elicit richer language, and the learner ultimately needs real-world complexity.

The sequence should resemble:

```text
stabilize useful form/meaning
→ perform simple meaningful task
→ vary content
→ reduce support
→ add turns/elements
→ change context/partner/input realization
→ combine capabilities
```

not:

```text
stay on isolated beginner drills until an arbitrary vocabulary threshold
```

Authentic use is approached gradually.

## Input and output should be complementary

`SRC-0123` shows comprehension-based and production-based instruction can both support learning, with different outcome/time patterns.

Therefore Nếp should reject both extremes:

```text
input only until learner is "ready"
```

and:

```text
free speaking from minute one regardless of prerequisites
```

Near-A0 default:

```text
processable input
→ meaning decision
→ notice useful language
→ supported retrieval
→ constrained production
→ changed production/interaction
```

The relative amount of input/output changes with learner state and target capability.

## Planning is a legitimate scaffold

Task-planning evidence (`SRC-0188`) supports allowing learners preparation before demanding real-time output.

Candidate beginner planning supports:
- preview the scenario goal;
- hear/read one comprehensible model;
- select among known chunks;
- organize one or two propositions;
- rehearse once;
- see a limited word bank.

But Nếp records this as support provenance.

```text
successful with word bank
≠
successful independently
```

## Tasks are an integration frame, not a religion

TBLT syntheses (`SRC-0183`, `SRC-0184`) suggest meaningful task use can support L2 outcomes.

But methodological critiques (`SRC-0184`, `SRC-0185`) show that:
- studies disagree on what counts as a task;
- inclusion criteria change the estimated effect;
- program implementations vary greatly.

Therefore Nếp should not brand every exercise a `task` or infer that a task-based architecture is automatically superior.

Use task/scenario framing where it helps transfer and coherence, then test Nếp's implementation directly.

## Integrated learning; separate evidence

A single micro-scenario can activate multiple systems.

Example:

```text
CAN-DO: buy a drink

listen:
"Small or large?"

understand:
choose size

chunk/construction:
"I'd like..."

pronunciation:
intelligible target phrase

speak:
"I'd like a small coffee."

interaction:
answer follow-up

later reading:
understand a short menu/message

later writing:
type a simple order/message
```

The session may feel unified, but the Evidence Engine stores:

```text
listening understood
chunk recalled
construction transferred
speech intelligible
interaction contingent
reading understood
writing produced
```

No single `lesson passed` flag replaces these dimensions.

## Primary and secondary modalities

Each learning unit should declare a primary capability/modal bottleneck and optional supporting modalities.

Example:

```yaml
primary:
  capability: understand_simple_choice_question
  modality: listening
secondary:
  - spoken_response
  - chunk_retrieval
```

This reduces accidental overload and helps the Evidence Engine know what success means.

## Spiral rather than one-and-done coverage

A capability should return in multiple modes and contexts over time.

Example:

```text
Day 1: hear + understand request pattern
Day 2: retrieve + say it
Day 4: use it with changed object
Day 7: read it in a short exchange
Day 10: interact with a new follow-up
Day 14: write a related practical message
```

The dates are illustrative, not fixed scheduling rules.

Spiral reuse helps make the curriculum comprehensive without demanding all modalities in one sitting.

## Skill unlocks are evidence-based, not level-tab based

Do not unlock a whole `Speaking A1` section because a learner completed a number of lessons.

Unlock the next challenge when prerequisite evidence is sufficient.

Conceptually:

```text
known-enough language
+ understood task pattern
+ support below threshold
→ next complexity increment
```

Different learners may reach reading, writing, interaction or authentic video expansion at different times.

## Capability graph

Candidate structure:

```ts
type CapabilityNode = {
  id: string;
  canDo: string;
  scenarios: string[];
  prerequisites: {
    capabilities: string[];
    vocabulary: string[];
    chunks: string[];
    constructions: string[];
    listeningTargets?: string[];
    pronunciationTargets?: string[];
  };
  modalities: string[];
  complexityBands: string[];
  transferFamilies: string[];
};
```

Edges represent prerequisites, not arbitrary lesson numbers.

## Unit generation contract

For each session/unit, the Curriculum Engine should decide:

1. What useful capability is being advanced?
2. What is the current learner bottleneck?
3. Which prerequisites are stable enough?
4. What is the smallest task that exposes the next useful challenge?
5. Which support is permitted on first attempt?
6. Which evidence will the attempt produce?
7. What changed-context probe follows?
8. What should be delayed rather than crammed into this session?

## Candidate session assembly

```text
learner state
→ choose capability
→ choose bottleneck
→ generate/select bounded input/task
→ first attempt
→ diagnose
→ targeted micro-learning
→ retry with less support
→ changed-content probe
→ persist evidence
→ schedule delayed/other-modality continuation
```

This is more adaptive than a fixed lesson template while remaining constrained enough to validate.

## Global balance dashboard for the engine

Internal curriculum audit can track rolling exposure/practice:

```text
meaning-focused input minutes
meaning-focused output minutes
language-focused learning minutes
fluency minutes

listening opportunities
reading opportunities
speaking opportunities
writing opportunities
interaction opportunities
```

These are curriculum-health indicators, not learner mastery scores.

## Avoid compensatory masking

Integrated tasks create a danger: a strong skill can hide a weak one.

Examples:
- reading captions hides listening weakness;
- memorized speech hides comprehension weakness;
- AI partner rescue hides production weakness;
- translation hides independent reading weakness.

Therefore support provenance and component evidence remain mandatory.

## Assessment alignment

Every capability needs:

```text
training task
≠ exact assessment item
```

but:

```text
same target capability
+ changed content/context
```

Assessment should include enough unfamiliarity to test transfer while preserving prerequisite fairness.

## Product decision

Create `FEAT-CUR-001` — **Adaptive capability curriculum orchestrator**.

It should:
- organize curriculum around practical capabilities;
- maintain a prerequisite graph;
- select one primary bottleneck at a time;
- compose modality-specific engines instead of duplicating them;
- track task complexity dimensions;
- increase complexity gradually;
- use planning/scaffolds with provenance;
- audit Four-Strands balance over a rolling horizon;
- spiral capabilities across modalities over time;
- keep evidence separate even when the learner experience is integrated;
- require changed-context and delayed evidence before strong progression claims.

## Open assumptions

- exact first capability set for Vietnamese adults near A0;
- exact capability prerequisite graph;
- exact number of active capabilities at once;
- exact rolling horizon for strand balance;
- exact target strand distribution by stage;
- exact number of modalities per session;
- exact complexity increment policy;
- exact criteria for switching the primary modality;
- exact planning/scaffold dose;
- exact order of reading/writing introduction relative to listening/speaking;
- exact task-first vs model-first policy;
- exact learner-choice policy;
- exact evidence threshold for capability expansion;
- exact rules for merging several capabilities into a larger scenario.

These are `EXP-017` variables, not literature truths.
