---
id: RQ-008-SOURCE-DIGEST
title: Source digest for ASR and automated pronunciation validity
research_question: RQ-008
last_verified: 2026-08-25
---

# RQ-008 source digest

## High-signal evidence

| Source | Why it matters | Scope limit |
| --- | --- | --- |
| `SRC-0077` | Meta-analysis: ASR practice can improve pronunciation; explicit feedback and segmental targets perform better | Learning effectiveness ≠ score validity; only 15 primary studies |
| `SRC-0078` | Direct ASR-vs-human intelligibility comparison; agreement varies by speaker/task | Taiwanese L1, small speaker sample |
| `SRC-0079` | Demonstrates conflict between robust ASR recognition and pronunciation assessment | Google ASR / target setup; not Vietnamese-specific |
| `SRC-0080` | Technical review of automatic pronunciation assessment, MDD, GOP, prosody, data/evaluation challenges | Broad technical review, not one validated product |
| `SRC-0082` | Peer-reviewed Whisper accent benchmark; Vietnamese among highest-error accent groups | Corpus/model-version bound; possible training-data overlap uncertainty |
| `SRC-0083` | Current 2026 five-system L2 benchmark; Vietnamese high error across systems | L2-ARCTIC has few speakers per L1 and read-speech emphasis |
| `SRC-0084` | Shows WER can fail as pronunciation proxy when advanced ASR recognizes through variation | Korean child learners, read speech |

## Supporting evidence

| Source | Contribution | Scope limit |
| --- | --- | --- |
| `SRC-0081` | PRISMA review: ASR learning tools focus more on segmentals; prosodic assessment remains difficult | Review through 2023 |
| `SRC-0085` | L1 phonology predicts categories of ASR errors | Otter/Speech Accent Archive; system-specific |
| `SRC-0086` | Whisper confidence/transcription-distance can contain learner-speech signal | Italian L1; small corpus; not a human-feedback replacement |
| `SRC-0072` | Prior Vietnamese case comparison of Otter and human listeners | Very small speaker/listener sample |

## Evidence not accepted as proof

- vendor claims of “human-level pronunciation scoring” without target-population validation;
- one correlation coefficient without calibration/error analysis;
- ASR benchmark accuracy on native English;
- WER measured against a prompt when the learner did not actually produce the prompt exactly;
- a model's confidence value interpreted as a probability of correct pronunciation;
- a generic “AI pronunciation score” with undisclosed construct or training data.

## Search conclusions

The literature supports **useful ASR-assisted practice** more strongly than it supports **ASR as a pronunciation judge**. The strongest product implication is therefore architectural: separate machine observation from validated educational evidence.
