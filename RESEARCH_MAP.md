# Research Map

## Research tracks

| Track | Core question | Current status | Product dependency |
| --- | --- | --- | --- |
| R01 Second-language acquisition | What mechanisms and constraints matter for adults near A0? | seeded | whole curriculum |
| R02 Vocabulary & chunks | What should be learned, in what contexts, and how is knowledge evidenced? | RQ-001 initial synthesis complete | starter catalogue, review |
| R03 Listening | How should perception, segmentation and comprehension progress? | RQ-003 initial synthesis complete | audio-first sessions |
| R04 Retrieval & spacing | How should recall and delayed review be designed without pretending one scheduler proves mastery? | RQ-004 initial synthesis complete | review engine |
| R05 Speaking/output | When and how should controlled production expand into guided interaction? | RQ-006 initial synthesis complete | speaking tasks |
| R06 Pronunciation | What improves intelligibility, especially for Vietnamese learners? | RQ-007 initial synthesis complete | pronunciation layer |
| R07 Reading/writing | How should receptive and productive literacy support the same communicative goals? | open | later A0/A1 packs |
| R08 Assessment | How should `understood`, `recalled`, `transferred`, `retained` be measured? | RQ-005 initial transfer synthesis complete | progress model |
| R09 Video-based learning | When is authentic video usable, and which scaffolds help rather than replace listening? | RQ-009 readiness + RQ-010 support + RQ-011 temporal-repair syntheses complete | later source path |
| R10 Vietnamese learners | Which L1-specific problems deserve targeted support? | RQ-002 general L1 scaffold synthesis complete; Vietnamese-specific calibration open | personalization |
| R11 Motivation/product behavior | Which session designs cause useful return without substituting engagement for learning? | open | UX and retention |
| R12 AI/technology | Where can ASR/LLMs/TTS help, and where do reliability/privacy limits dominate? | RQ-008 initial ASR validity synthesis complete | AI features |

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

## Explicitly unresolved product assumptions

- Session length that fits the target learner's real schedule.
- Exact support-fading threshold.
- Exact speaking support-fading / task-unlock threshold.
- Exact pronunciation target priority / practice dose for Vietnamese near-A0.
- Listener-panel mix and minimum intelligibility criterion for pronunciation validation.
- Exact ASR provider/model mix and maintenance policy.
- Exact caption/support fading policy and transcript/replay thresholds for Vietnamese learners.
- Exact auto-pause trigger, pause-boundary, duration and temporal-support fading policy.
- Exact machine-feedback confidence / false-correction thresholds.
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
