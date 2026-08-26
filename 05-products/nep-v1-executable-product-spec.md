# Nếp v1 — Executable product specification

**Status:** implementation-facing product decision layer  
**Research basis:** `SYN-SYS-001`, `RQ-001`–`RQ-021`  
**Implementation source of truth:** application repository, not this file

## 1. Product promise

Nếp helps a Vietnamese-speaking beginner build English that can be **understood, remembered and used**, not merely complete lessons.

Learner-facing promise:

> Tiếng Anh thành nếp. Hiểu thật. Nhớ lâu. Dùng được.

The product should feel like a simple guided path through useful situations. The internal system may be complex, but that complexity must not leak into the learner experience.

## 2. Target learner for v1

Primary:

- Vietnamese-speaking adult;
- near-zero / Pre-A1 / low-A1 English;
- uneven prior school English is expected;
- mobile-first usage is valid;
- may know written forms better than spoken forms;
- needs practical everyday/work English rather than an academic grammar syllabus.

This is a product scope, not an assumption that every Vietnamese learner has the same profile.

## 3. Non-goals for v1

Nếp v1 is not:

- an IELTS/TOEIC certification product;
- a full CEFR A1–C2 curriculum;
- a native-accent training system;
- a free-chat AI companion as the primary learning method;
- a video-first product;
- a flashcard/SRS product with lessons attached;
- a grammar course with gamification;
- a system that claims mastery from completion, streaks or AI scoring.

## 4. Canonical learner journey

```text
SIGN UP
  ↓
short adaptive starting check
  ↓
provisional learner profile
  ↓
TODAY
  ↓
one useful capability
  ↓
meaning → target → retrieval → changed use
  ↓
evidence update
  ↓
review / continue / stop
  ↓
later delayed recall + changed context
  ↓
capability expands
```

## 5. Required learner-facing surfaces

### 5.1 Welcome / onboarding

Goal: get enough information to start useful learning quickly.

Must:

- explain in Vietnamese what the short check is for;
- allow required audio setup;
- collect only routing-relevant prior information;
- run adaptive common anchors;
- stop when the route is good enough or burden ceiling is reached;
- begin the first real learning task immediately afterwards.

Must not:

- force a long placement battery;
- show false precision such as `A1.2 = 63%`;
- mark untested speaking/writing as weak;
- infer global ability from one grammar quiz.

Research owner: `FEAT-ONB-001`.

### 5.2 Today

This is the default home surface.

Candidate structure:

```text
Today

Continue
Order a drink
~7 min

Worth reviewing
3 items

Optional
Practice listening
```

Rules:

- one obvious primary action;
- review is integrated, not a separate guilt backlog;
- learner can see why a task matters in plain language;
- no giant course map as the required daily navigation mechanism.

### 5.3 Learning session

The session is generated from a `CurriculumUnitSpec`, not a hard-coded universal template.

Default beginner shape:

```text
context
→ meaning attempt
→ smallest useful support
→ focus target
→ independent retrieval
→ changed use
→ session close
```

A session can branch when evidence demands it.

### 5.4 Review

Review answers one question:

> What is worth trying to retrieve again now?

Rules:

- due state is scheduling metadata, not mastery;
- attempt before reveal;
- exact-item repetition is practice, not transfer;
- avoid unlimited backlog growth after absence;
- changed-context and delayed evidence are sampled explicitly.

Research owner: `FEAT-REV-001`, `FEAT-TRN-001`.

### 5.5 Progress

Primary learner-facing unit: **capability**, not grammar chapter or arbitrary XP level.

Example:

```text
Everyday basics

✓ Say who you are
✓ Ask for one simple item
△ Order a drink and answer a size question
○ Understand a basic price
```

A capability can expose simple evidence language when helpful:

```text
Understands with little help
Can say it in a familiar situation
Needs another later check
```

Avoid:

```text
Mastery 87%
English complete 14%
Speaking score 91/100
```

unless a future validated scoring model justifies such reporting.

### 5.6 Recovery after a break

Candidate experience:

```text
Welcome back
Let's check one thing you used before.
```

Then:

```text
small retrieval / comprehension task
→ estimate current state
→ repair / continue
```

Do not require the learner to clear every overdue item before learning again.

Research owner: `FEAT-MOT-001`.

## 6. Product content model

### Capability

A capability is the top-level learning unit.

```ts
type Capability = {
  id: string;
  canDo: string;
  domain: string;
  scenarios: string[];
  prerequisiteIds: string[];
  targetIds: string[];
  supportedModalities: Modality[];
  transferFamilies: string[];
};
```

Example:

```yaml
id: CAP-CAFE-001
canDo: Can order one familiar drink and answer a simple size question.
domain: daily-life
scenarios:
  - cafe-counter
  - takeaway-kiosk
targets:
  chunks:
    - CH-I-WANT-001
  listening:
    - LIS-SIZE-Q-001
  constructions:
    - GRM-REQUEST-001
  vocabulary:
    - coffee
    - tea
    - small
    - large
```

### Target

Targets are smaller language/processing objects:

- word;
- chunk/formula;
- construction;
- listening contrast/message;
- pronunciation feature;
- reading pattern;
- writing function;
- pragmatic function;
- repair move.

A target is not necessarily a learner-visible object.

### Scenario

A scenario gives meaning and transfer context. Several capabilities may later combine in one scenario.

## 7. Runtime decision hierarchy

When choosing the next task:

```text
1. safety / technical availability
2. current placement/re-entry uncertainty
3. due retention risk
4. active capability prerequisite gaps
5. primary bottleneck
6. changed-context/transfer gap
7. curriculum balance starvation
8. learner-relevant scenario preference
9. estimated time/burden
```

Engagement prediction may rank among pedagogically valid choices but cannot bypass evidence requirements.

## 8. Session planner contract

Input:

```ts
type SessionPlanInput = {
  learnerSnapshotId: string;
  availableMinutes?: number;
  device: DeviceContext;
  dueEvidence: DueEvidence[];
  candidateCapabilities: CapabilityCandidate[];
  learnerPreference?: LearnerPreference;
};
```

Output:

```ts
type SessionPlan = {
  capabilityId: string;
  objective: string;
  primaryBottleneck: Bottleneck;
  primaryModality: Modality;
  taskSequence: TaskSpec[];
  supportPolicyId: string;
  evidenceContracts: EvidenceContract[];
  changedContextProbe?: ProbeSpec;
  reviewContinuations: ReviewContinuation[];
  estimatedMinutes: number;
  policyVersion: string;
};
```

The planner must be deterministic enough that a product engineer can inspect *why* the session was chosen.

## 9. Canonical task contract

```ts
type TaskSpec = {
  id: string;
  family: string;
  capabilityId: string;
  targetIds: string[];

  inputMode: Modality;
  responseMode: Modality | "selection" | "none";

  novelty: "trained" | "parallel" | "changed-context" | "new";
  purpose: "learn" | "practice" | "evidence" | "repair";

  answerBearingSupportAllowedBeforeAttempt: boolean;
  allowedSupportIds: string[];

  scorerPolicyId: string;
  evidenceContracts: EvidenceContract[];
};
```

Every task must have an explicit purpose. A practice task cannot silently be promoted into independent evidence.

## 10. Support policy

All major supports are versioned policies.

Candidate support types:

- Vietnamese meaning support;
- image/context grounding;
- replay;
- slower replay when validated;
- English caption;
- transcript;
- word bank;
- sentence frame;
- model answer;
- planning time;
- rehearsal;
- pronunciation cue/comparator;
- partner rephrase;
- AI hint.

Support events are logged before scoring evidence.

## 11. Core v1 capability loop

For a new capability, candidate sequence:

```text
A. COMPREHEND
short meaningful input
→ learner attempts meaning

B. DIAGNOSE / SUPPORT
if needed, reveal smallest useful support

C. LEARN TARGET
notice useful word/chunk/construction/sound mapping

D. RETRIEVE
answer-bearing model hidden
→ learner retrieves target

E. USE
bounded new slot / changed scenario

F. STORE
record evidence separately by claim and support condition

G. RETURN
later delayed/parallel attempt
```

This is a default, not an immutable lesson script.

## 12. Listening behavior

Use `FEAT-LIS-001`.

If learner misses spoken input, distinguish candidate causes:

```text
meaning unknown
written target unknown
written target known but audio form missed
segmentation problem
speech rate/load problem
support dependency
```

Do not immediately solve every listening failure with a transcript.

## 13. Vocabulary/chunk behavior

Use `FEAT-VOC-001`.

Evidence states must distinguish at least:

```text
recognized
understood
recalled
used_changed_context
retained
```

Chunk learning is preferred when the chunk is a useful communicative unit, not merely because multiword strings are fashionable.

## 14. Construction/grammar behavior

Use `FEAT-GRM-001`.

Grammar enters as a meaningful construction.

Bad primary experience:

```text
Present Simple rule
→ choose 20 verb forms
```

Candidate experience:

```text
I want tea.
I want water.
What do you want?
→ notice request pattern
→ retrieve it
→ change slot / scenario
```

Explicit Vietnamese explanation can be used when useful, but explanation success is not construction mastery.

## 15. Speaking behavior

Use `FEAT-SPK-001`.

Candidate ladder:

```text
SP0 rehearsal
SP1 bounded oral completion
SP2 independent short utterance
SP3 controlled recombination
SP4 guided one-turn interaction
SP5 bounded multi-turn interaction
SP6 open interaction later
```

Learner UI should not show these labels.

Rule:

```text
visible exact model during response
→ rehearsal/supported production
```

not independent speaking evidence.

## 16. Pronunciation behavior

Use `FEAT-PRN-001`.

Pronunciation is attached to useful words/chunks/messages.

Priority:

```text
message identity / intelligibility risk
> accent imitation
```

Do not create a compulsory tour through all English phonemes.

## 17. Reading/writing behavior

Use `FEAT-READ-001`, `FEAT-WRI-001`.

They attach to the same capabilities.

Example:

```text
spoken café capability
→ later read short menu/message
→ later type one practical response
```

Do not force each capability through all modalities immediately.

## 18. Interaction behavior

Use `FEAT-INT-001`.

Interaction evidence needs contingency:

```text
partner says X
→ learner response meaningfully depends on X
```

A memorized monologue inside a chat UI is not interaction mastery.

## 19. Fluency behavior

Use `FEAT-FLU-001`.

Fluency work is a consolidation mode, not the first exposure mode.

Do not optimize raw speed at the cost of meaning or accuracy.

## 20. Video behavior

Use `FEAT-VID-002`, `FEAT-VID-001`, `FEAT-VID-003` only when clip/learner readiness is adequate.

Video is an input source, not the product architecture.

Nếp v1 must work without authentic video being central.

## 21. AI behavior

Every AI use declares a role:

```text
content_candidate_generator
hint_rephraser
feedback_candidate
conversation_partner
classifier
scoring_assistant
TTS_input_source
```

Each role has a policy defining:

- allowed inputs;
- learner data exposed;
- deterministic validators;
- confidence/abstention behavior;
- whether output can affect learner evidence;
- version/provenance requirements.

Use `FEAT-AIG-001` and `FEAT-ASR-001`.

## 22. Product state machine

```text
NEW
↓
PLACEMENT_BOOTSTRAP
↓
ACTIVE_LEARNING
├─→ REVIEW_DUE
├─→ TRANSFER_CHECK
├─→ PREREQUISITE_REPAIR
├─→ CAPABILITY_EXPANSION
├─→ BREAK_RECOVERY
└─→ RECALIBRATION
```

These are runtime states, not learner labels.

## 23. Required analytics separation

### Learning/evidence analytics

- unsupported comprehension;
- independent recall;
- changed-context success;
- delayed retention;
- support dependence;
- route corrections;
- prerequisite repairs.

### Product behavior analytics

- onboarding completion;
- session completion;
- voluntary continuation;
- return rate;
- notification response;
- time spent;
- feature use.

Do not merge these into one success metric.

## 24. v1 shipping scope

### Required for coherent v1

- onboarding + progressive placement;
- capability catalogue + prerequisite graph;
- learner evidence store;
- curriculum/session orchestration;
- listening;
- vocabulary/chunks;
- Vietnamese scaffolding;
- constructions/grammar;
- guided speaking;
- pronunciation on relevant targets;
- review;
- changed-context transfer;
- progress by capability;
- recovery after absence;
- AI reliability gate for every AI-enabled path.

### Can ship in limited form

- reading;
- writing;
- bounded interaction;
- fluency consolidation.

### Do not block v1

- full authentic-video pipeline;
- unrestricted AI conversation;
- complex social/leaderboard systems;
- CEFR certification;
- comprehensive pronunciation scoring;
- advanced writing evaluation.

## 25. First content slice

Do not author 100 units before proving the runtime.

Build a small capability set with enough variation to exercise the engines.

Candidate 8-capability slice:

1. greet and say name;
2. understand/answer `How are you?` in bounded forms;
3. ask for one familiar item;
4. order one drink and answer a size choice;
5. understand a simple price;
6. say a basic need/problem (`I need help`, `I don't understand`);
7. ask for repetition/clarification;
8. understand and respond to one simple everyday message.

These are **candidate product content**, not evidence-backed universal first-eight ordering. They must be refined against the capability research and target-learner testing.

## 26. Definition of done for a capability slice

A capability is ready for product testing only when it has:

- clear can-do outcome;
- scenarios;
- target inventory;
- prerequisite assumptions;
- first-exposure tasks;
- independent retrieval opportunity;
- changed-context probe family;
- delayed review hooks;
- support rules;
- scorer/evidence contract;
- known Vietnamese risk priors where relevant;
- AI/TTS provenance if used;
- falsification metric.

## 27. Product-level success criterion

Nếp v1 should be judged primarily by whether target learners improve on useful delayed changed-context capabilities per learner minute, while onboarding/session burden stays acceptable.

A beautiful UI, high streak rate or long usage time is not sufficient if this learning criterion fails.
