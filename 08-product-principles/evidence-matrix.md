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
