# Alyce Intervention V3 Source

Source id: `alyce_intervention_v3`

Base package:

- Kaggle output slug: `alycemiki/intervention-command-w-ffa`
- Local source: `external/kaggle_outputs/alycemiki__intervention-command-w-ffa/submission_extracted`
- Package type: multi-file submission with `main.py` and `orbit_lite/`

V3 changes:

- Preserves the full Alyce Intervention package structure.
- Keeps the original v15 planner mechanisms: dynamic ROI, full safe-drain options, floor-sized fleets, regroup fade, comet handling, and 4P FFA anti-snowball bonuses.
- Adds a narrow 4P-only soft scoring penalty for far low-production neutral targets and far low-production enemy targets that are not owned by the current leader.

Reason:

- Local replay review found that V1/V2 losses were not caused by full-drain itself.
- Non-winning 4P games more often spent tempo on far low-value neutrals early and fragmented far low-value enemy pressure midgame.
- V3 is therefore a candidate-level score adjustment rather than a broad reserve/action deletion filter.

Attribution:

- Original public Kaggle output belongs to Alyce Miki.
- This repository records the modification path for local evaluation and does not claim the public output score as our own official score.
