# Research Map

## Research tracks

| Track | Core question | Current status | Product dependency |
| --- | --- | --- | --- |
| R01 Second-language acquisition | What mechanisms and constraints matter for adults near A0? | seeded | whole curriculum |
| R02 Vocabulary & chunks | What should be learned, in what contexts, and how is knowledge evidenced? | RQ-001 initial synthesis complete | starter catalogue, review |
| R03 Listening | How should perception, segmentation and comprehension progress? | RQ-003 initial synthesis complete | audio-first sessions |
| R04 Retrieval & spacing | How should recall and delayed review be designed without pretending one scheduler proves mastery? | RQ-004 initial synthesis complete | review engine |
| R05 Speaking/output | When and how should controlled production expand into guided interaction? | RQ-006 controlled speaking + RQ-015 interaction initial syntheses complete | speaking tasks, conversation engine |
| R06 Pronunciation | What improves intelligibility, especially for Vietnamese learners? | RQ-007 initial synthesis complete | pronunciation layer |
| R07 Reading/writing | How should receptive and productive literacy support the same communicative goals? | RQ-013 reading + RQ-014 writing initial syntheses complete | A0/A1 literacy engine |
| R08 Assessment | How should `understood`, `recalled`, `transferred`, `retained` be measured? | RQ-005 initial transfer synthesis complete | progress model |
| R09 Video-based learning | When is authentic video usable, and which scaffolds help rather than replace listening? | RQ-009 readiness + RQ-010 support + RQ-011 temporal-repair syntheses complete | later source path |
| R10 Vietnamese learners | Which L1-specific problems deserve targeted support? | RQ-002 general L1 scaffold synthesis complete; Vietnamese-specific calibration open | personalization |
| R11 Motivation/product behavior | Which session designs cause useful return without substituting engagement for learning? | open | UX and retention |
| R12 AI/technology | Where can ASR/LLMs/TTS help, and where do reliability/privacy limits dominate? | RQ-008 ASR + RQ-014 writing AI + RQ-015 interaction AI evidence seeded; broader calibration open | AI features |
| R13 Grammar & constructions | How should form, meaning and use be learned together and evidenced beyond rule recall? | RQ-012 initial synthesis complete | curriculum, lesson engine, speaking/writing/review |
| R14 Interaction & pragmatics | How should learners manage turns, responses, repair and socially appropriate language in real interaction? | RQ-015 initial synthesis complete | conversation engine, roleplay, transfer |
| R15 Fluency & automaticity | How should accurate and meaningful language become faster and less effortful without turning raw speed into mastery? | open | listening, speaking, reading, interaction, review |

## Priority research questions

### P0 — before expanding the A0 engine

- `RQ-001`: What counts as independent evidence that an A0 learner knows a word/chunk? → **initial synthesis complete** (`SYN-VOC-002`, `FEAT-VOC-001`, `EXP-001`)
- `RQ-002`: What amount/type of Vietnamese scaffold supports comprehension without becoming the task itself? → **initial synthesis complete** (`SYN-SCF-001`, `FEAT-SCF-001`, `EXP-002`)
- `RQ-003`: How should short listening tasks separate sound perception from meaning comprehension? → **initial synthesis complete** (`SYN-LIS-002`, `FEAT-LIS-001`, `EXP-003`)
- `RQ-004`: What retrieval schedule gives useful delayed retention while keeping time-on-task reasonable? → **initial synthesis complete** (`SYN-REV-001`, `FEAT-REV-001`, `EXP-004`)
- `RQ-005`: What changed-context probe is feasible enough to measure transfer repeatedly? → **initial synthesis complete** (`SYN-TRN-001`, `FEAT-TRN-001`, `EXP-005`)

### P1 — before expanding speaking and pronunciation

- `RQ-006`: Which controlled speaking tasks are valid for near-A0 learners? → **initial synthesis complete** (`SYN-SPK-001`, `FEAT-SPK-001`, `EXP-006`)
- `RQ-007`: Which pronunciation targets most affect intelligibility for Vietnamese L1 learners? → **initial synthesis complete** (`SYN-PRN-001`, `FEAT-PRN-001`, `EXP-007`)
- `RQ-008`: What can ASR score reliably for this population, if anything? → **initial synthesis complete** (`SYN-ASR-001`, `FEAT-ASR-001`, `EXP-008`)

### P2 — before making video central to any stage

- `RQ-009`: What vocabulary coverage and speech characteristics make a short authentic clip usable? → **initial synthesis complete** (`SYN-VID-002`, `FEAT-VID-002`, `EXP-009`)
- `RQ-010`: When should English captions, Vietnamese support, transcript and replay appear? → **initial synthesis complete** (`SYN-CAP-001`, `FEAT-VID-001`, `EXP-010`)
- `RQ-011`: Does auto-pause improve learning or simply fragment comprehension? → **initial synthesis complete** (`SYN-PAU-001`, `FEAT-VID-003`, `EXP-011`)

### P3 — before treating grammar as a comprehensive learning dimension

- `RQ-012`: How should near-A0 learners learn and demonstrate grammar/construction knowledge without reducing grammar to rule memorization and decontextualized drills? → **initial synthesis complete** (`SYN-GRM-001`, `FEAT-GRM-001`, `EXP-012`)

### P4 — before expanding literacy from sentences to independent text production

- `RQ-013`: How should near-A0 learners progress from supported sentence-level reading to independent connected-text reading without confusing word recognition, comprehension, fluency and support-assisted success? → **initial synthesis complete** (`SYN-READ-001`, `FEAT-READ-001`, `EXP-013`)
- `RQ-014`: How should near-A0 learners progress from controlled written production to independent meaningful writing, with feedback that improves future writing rather than merely correcting the current text? → **initial synthesis complete** (`SYN-WRI-001`, `FEAT-WRI-001`, `EXP-014`)

### P5 — before calling speaking a real interaction capability

- `RQ-015`: How should near-A0 learners progress from controlled speaking to real turn-by-turn interaction, including response relevance, turn-taking, clarification/repair and pragmatic appropriateness, without letting AI roleplay hide comprehension or production weaknesses? → **initial synthesis complete** (`SYN-INT-001`, `FEAT-INT-001`, `EXP-015`)

### P6 — before treating faster performance as fluent language use

- `RQ-016`: How should Nếp develop fluency/automaticity across listening, reading, speaking and interaction without confusing faster performance on practiced material with flexible retained use? → **open**

## Explicitly unresolved product assumptions

- Session length that fits the target learner's real schedule.
- Exact support-fading threshold.
- Exact speaking support-fading / task-unlock threshold.
- Exact pronunciation target priority / practice dose for Vietnamese near-A0.
- Listener-panel mix and minimum intelligibility criterion for pronunciation validation.
- Exact ASR provider/model mix and maintenance policy.
- Exact caption/support fading policy and transcript/replay thresholds for Vietnamese learners.
- Exact auto-pause trigger, pause-boundary, duration and temporal-support fading policy.
- Exact construction sequencing for Vietnamese near-A0 learners.
- Exact explanation timing and Vietnamese/English grammar-support policy.
- Exact exemplar count, lexical variation and abstraction threshold for each construction.
- Exact interpretation-to-production and controlled-to-transfer progression thresholds.
- Exact grammar corrective-feedback policy by construction, error type and learner state.
- Exact reading message/microtext/graded-text length progression for Vietnamese near-A0.
- Exact lexical and construction readiness bands for each reading stage.
- Exact reading audio/gloss/translation fading policy.
- Exact repeated-reading dose and criteria for using repeated reading as repair rather than routine.
- Exact point at which reading-strategy instruction becomes worth the learning time.
- Exact sustained/extensive-reading unlock threshold, text-choice freedom and accountability policy.
- Exact reading fluency metrics and any useful rate targets for Vietnamese adults.
- Exact balance of practical, narrative, dialogue and informational reading material.
- Exact transition from writing reconstruction to independent sentence production.
- Exact writing sentence-frame / word-bank fading thresholds.
- Exact micro-writing length and proposition load for Vietnamese near-A0.
- Exact use of Vietnamese in writing planning versus feedback explanation.
- Exact writing feedback priority and maximum issue count per draft.
- Exact self-repair-prompt versus direct-correction policy.
- Exact comparator/model timing and number of revision cycles before a new writing task.
- Exact AI/AWE assistance limits, confidence gates and false-correction thresholds in writing.
- Exact writing component weights, if any composite score is ever justified.
- Exact practical writing-genre order and mobile typing/mechanics policy.
- Exact first interaction stage for true A0 learners and turns per stage.
- Exact interaction response-latency expectations by task/device.
- Exact listener-support/backchannel teaching timing.
- Exact repair repertoire, sequence, engineered-breakdown frequency and difficulty.
- Exact partner rephrasing/rescue thresholds that should count as interaction support.
- Exact pragmatic-function order and treatment of cultural variation in appropriateness.
- Exact AI interaction strictness/accommodation policy and whether intentional misunderstanding is useful for repair practice.
- Exact automated response-contingency and pragmatic-scoring thresholds.
- Minimum human-listener/human-partner validation sample and AI-to-human transfer criteria.
- Exact interaction review schedule and delayed-probe interval.
- Exact machine-feedback confidence / false-correction thresholds outside writing.
- Exact automated feature detectors safe enough for Vietnamese near-A0.
- Exact authentic-video lexical-coverage bands and learner × clip readiness thresholds.
- Exact authentic-video window length / segmentation policy.
- Exact speech-load and visual-grounding weights for Vietnamese near-A0.
- Exact transfer novelty ladder and probe-sampling frequency for near-A0.
- Best beginner voice/ accent mix.
- Whether learners value and return for delayed review.
- Exact review workload / desired-retention policy for the target learner.
- Whether learning gains are large enough to support willingness to pay.

These remain product experiments even if related educational literature exists.
