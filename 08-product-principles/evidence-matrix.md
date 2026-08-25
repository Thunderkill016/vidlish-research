# Evidence matrix

This file is a human-readable bridge between research and product. Machine-readable equivalents live in `data/`.

| Claim / synthesis | Evidence | Confidence | Product implication | Status |
| --- | --- | --- | --- | --- |
| CEFR describes broader communicative modes than four isolated skills. | CEFR Companion Volume | high | Track concrete can-do/capability profiles. | accepted |
| Spaced practice supports L2 vocabulary retention. | meta-analytic literature | high | Keep delayed review. | accepted |
| Repeated retrieval helps vocabulary learning. | controlled + synthesis literature | high | Require attempt-before-reveal in recall tasks. | accepted |
| Listening needs perception/segmentation/comprehension work, not exposure alone. | listening pedagogy + meta-analysis | moderate | Build bounded audio tasks before long authentic media. | accepted |
| Captions can scaffold L2 video learning. | captioned-video research | moderate | Progressive caption support is reasonable. | accepted with scope limits |
| Always-on bilingual subtitles are optimal for Nếp A0. | none sufficient | low | Do not hard-code as truth; experiment. | open |
| Auto-pausing every unknown word improves learning. | none sufficient | low | Experiment before shipping as default. | open |
| FSRS state means a learner has mastered an item. | no | rejected | Use FSRS for scheduling only. | rejected |
| Global ASR pronunciation score is valid for Vietnamese near-A0 learners. | insufficient | low | Do not launch as mastery/proficiency score. | open/rejected for current scope |
| A lexical item is not adequately represented by one known/unknown flag. | construct + assessment literature (`SRC-0008`, `SRC-0009`, `SRC-0014`) | moderate-high | Derive graded lexical state from attempts. | accepted |
| Recognition success establishes recall/productive ability. | evidence contradicts this (`SRC-0008`, `SRC-0010`, `SRC-0016`) | low/rejected | Recognition-only tasks cannot mark recall/productive state. | rejected |
| Immediate success establishes retention. | meta-analyses show delayed decline (`SRC-0011`, `SRC-0012`) | high evidence against | Require delayed re-demonstration. | rejected |
| Nếp evidence categories are four independent psychological vocabulary dimensions. | construct evidence does not support this claim (`SRC-0009`) | low/rejected wording | Keep them as task/time evidence categories only. | rejected as scientific claim |
| Partial phrase/first-letter cues prove independent chunk production. | collocation measurement review (`SRC-0015`) | moderate evidence against | Store cue level; label as scaffolded evidence. | rejected |
| Strategic L1/multilingual support can aid L2 learning relative to English-only instruction. | `SRC-0019`–`SRC-0023`; newer meta-analyses positive but heterogeneous | moderate-high | Allow principled Vietnamese support near A0. | accepted with scope limits |
| L1 lexical gloss/explanation is useful for beginners. | meta-analyses `SRC-0017`, `SRC-0018`, `SRC-0024`, `SRC-0025` | high | Use concise Vietnamese meaning support when English-only definitions add unnecessary difficulty. | accepted |
| One universal percentage of Vietnamese is optimal. | no sufficient evidence | low | Do not hard-code a 10/20/30% rule. | rejected/open |
| Vietnamese should disappear after exactly 300 independently produced words. | no direct evidence | low | Treat 300 as a product hypothesis, not a scientific threshold. | open/rejected as fact |
| Full translation visible during a scored comprehension task proves English comprehension. | task/measurement evidence contradicts this inference | high evidence against | Hide answer-bearing translation for independent probes; log support. | rejected |
| Immediate scaffolded accuracy proves the scaffold improves long-term learning. | delayed evidence sparse; gloss outcomes are test-sensitive | low/rejected | Evaluate delayed unsupported performance. | rejected |
| Written vocabulary knowledge proves the learner can recognize the same word in speech. | diagnostic/predictive listening evidence (`SRC-0030`–`SRC-0032`) | moderate-high evidence against | Collect aural lexical evidence separately. | rejected |
| Decoding/word recognition and message comprehension are identical. | `SRC-0032`, `SRC-0033`, `SRC-0034` | high evidence against | Store separate decoding and comprehension evidence. | rejected |
| Explicit decoding training can improve L2 listening outcomes. | systematic review/meta-analysis `SRC-0026` | high | Include bounded bottom-up diagnostic/practice tasks. | accepted with heterogeneity |
| Phonetic perception training alone proves listening comprehension. | HVPT meta-analysis measures perception (`SRC-0029`) | rejected inference | Use perception training as one component, then test message comprehension/transfer. | rejected |
| Transcript-visible success is independent audio-only comprehension. | listening assessment + support-provenance logic (`SRC-0034`) | high evidence against | Hide answer-bearing text before independent listening probe. | rejected |
| Strict dictation is a pure measure of listening perception. | decoding/assessment studies use written responses (`SRC-0026`, `SRC-0032`–`SRC-0034`) | moderate evidence against | Record/tolerate orthographic demands or use lower-writing-burden probes. | rejected as pure measure |
| One universal replay count or decoding percentage defines A0 listening mastery. | no sufficient evidence | low | Keep as product calibration question. | rejected/open |
| Spaced practice improves delayed L2 retention relative to massed practice. | L2 meta-analysis `SRC-0003` | high | Keep delayed review in the core engine. | accepted |
| Longer spacing is always better immediately and after delay. | `SRC-0003` shows retention-horizon interaction | high evidence against | Judge schedule against the intended delay. | rejected |
| Expanding spacing is universally superior to equal spacing. | `SRC-0003`, `SRC-0037` | high evidence against universal claim | Do not hard-code expanding intervals as doctrine. | rejected |
| More within-session retrieval is always more efficient. | `SRC-0004` | moderate-high evidence against | Optimize retained performance per minute. | rejected |
| Retrieval format can be ignored when scheduling review. | `SRC-0038` + RQ-001 evidence model | high evidence against | Select task from the needed capability/evidence lane. | rejected |
| Delayed corrective feedback is universally better for L2 vocabulary. | `SRC-0039` | moderate evidence against | Feedback after attempt can be prompt; exact timing is not a fixed rule. | rejected |
| Retrieval practice generally improves retention over restudy. | meta-analysis `SRC-0040` | high | Use attempt-based review when the learner can retrieve meaningfully. | accepted with scope limits |
| Retrieval practice alone proves transfer. | transfer meta-analysis `SRC-0041` shows conditional effects | high evidence against inference | Require actual changed-context evidence. | rejected |
| Adaptive memory models can optimize review timing/cost. | `SRC-0042`, `SRC-0043` | moderate-high | Keep an adaptive scheduler behind a versioned adapter. | accepted as engineering strategy |
| FSRS predicted retrievability or stability means English mastery. | `SRC-0042`–`SRC-0044` target recall prediction/scheduling, not language capability | high evidence against | Separate scheduler state from capability evidence. | rejected |
| One FSRS desired-retention value is scientifically optimal for Nếp. | no direct Nếp evidence | low | Calibrate via `EXP-004`. | open/rejected as fact |
| Exact trained-context success proves transfer. | transfer meta-analysis + contextual-learning evidence (`SRC-0041`, `SRC-0045`, `SRC-0048`) | high evidence against | Label exact retests retention/trained-context only. | rejected |
| Unseen parallel contexts can provide transfer evidence when the target relation is preserved and other difficulty is controlled. | `SRC-0041`, `SRC-0045`, `SRC-0048` | moderate-high | Build changed-context probes with explicit novelty metadata. | accepted with task limits |
| More contextual diversity is always better for beginners. | direct L2 evidence `SRC-0046`, `SRC-0047` contradicts a universal rule | high evidence against | Increase novelty gradually; do not maximize context changes near A0. | rejected |
| Familiar-context fluency proves decontextualized word knowledge. | `SRC-0045`, `SRC-0046`, `SRC-0048`, `SRC-0049` | moderate-high evidence against | Sample performance in unseen contexts. | rejected |
| A new-context multiple-choice item proves speaking/independent production. | productive-task evidence `SRC-0052`, assessment boundary `SRC-0053` | high evidence against | Require productive transfer samples for productive claims. | rejected |
| Open conversation is required to measure every A0 transfer target. | no sufficient evidence; productive assessment is costly/confounded | low/rejected | Use controlled production when it better isolates the target; reserve open transfer for later/sampling. | rejected as default |
| Arbitrarily increasing difficulty necessarily improves transfer. | `SRC-0050`, `SRC-0051`, `SRC-0047` show conditional/mixed effects | high evidence against | Use bounded desirable difficulty after prerequisites are stable. | rejected |
| Reusing the same unseen probe repeatedly remains fresh transfer evidence. | testing/retrieval evidence (`SRC-0040`, `SRC-0041`) | high evidence against | Track first exposure; later attempts are review/retention, not first unseen transfer. | rejected |
| One fixed transfer novelty level/frequency is optimal for Vietnamese near-A0. | no direct validation | low | Calibrate with `EXP-005`. | open |
| Pre-A1 speaking requires broad spontaneous conversation before it counts as speaking. | CEFR Pre-A1 (`SRC-0001`) contradicts this framing. | rejected | Begin with meaningful short/formulaic production and bounded interaction. | rejected |
| Comprehension success will automatically become productive speaking without production practice. | comparative instruction meta-analysis `SRC-0054` | high evidence against | Include actual oral retrieval when production is a target capability. | rejected |
| Low-proficiency learners should only read/listen to model answers before speaking. | low-proficiency planning study `SRC-0055`; planning synthesis `SRC-0056` | moderate evidence against | Allow bounded productive planning and record its support conditions. | rejected |
| Planning/support can improve oral performance without changing what a speaking attempt demonstrates. | `SRC-0055`–`SRC-0057` | high evidence against | Store planning mode, answer visibility and support provenance. | rejected |
| Repeating the exact same speaking task proves spontaneous speaking transfer. | task-repetition meta-analysis `SRC-0058` + transfer boundary `SRC-0041` | high evidence against | Repetition is practice; use first-seen changed tasks for transfer. | rejected |
| Completely open conversation is required to observe interactional ability. | standardized interactive-task evidence `SRC-0059` | moderate evidence against | Use bounded scripted Q&A/role-play for early interaction diagnostics. | rejected |
| Corrective feedback should always immediately supply the correct oral form. | oral-CF meta-analysis `SRC-0060` | moderate evidence against | Give a brief self-repair opportunity when the target is plausibly retrievable. | rejected as universal rule |
| Formulaic sequences are illegitimate because they are not fully generative speech. | CEFR + formulaic-sequence review `SRC-0001`, `SRC-0061` | moderate-high | Use useful chunks early while keeping formulaic and generative evidence distinct. | rejected |
| One speech-rate/fluency number proves overall speaking mastery. | planning/task evidence `SRC-0056`–`SRC-0059` | low/rejected | Keep fluency as one task-conditioned signal alongside task success and language evidence. | rejected |
| ASR/pronunciation scores are validated mastery gates for Vietnamese near-A0 speaking. | RQ-006 found no sufficient validation; RQ-007/RQ-008 pending | insufficient | Do not ship global automated speaking mastery scoring yet. | open/rejected for current scope |
