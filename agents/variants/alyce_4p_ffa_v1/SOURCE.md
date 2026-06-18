# Alyce 4P FFA V1 Source

Source date: 2026-06-18

## Lineage

This variant is derived from the local reproduction:

```text
agents/public/alyce_intruder_repro
```

The reproduced public source is:

```text
Kaggle code: alycemiki/light-ver-1200-simple-orbit-intruder
Title: [Light ver. & 1200+] Simple Orbit Intruder
Author: Alyce Miki
URL: https://www.kaggle.com/code/alycemiki/light-ver-1200-simple-orbit-intruder
```

Attribution remains attached to Alyce Miki and the referenced
`slawekbiel/producer-orbit-wars-utils` lineage.

## Local Modification

This is not an unmodified public output. It is a local research variant built
from two project reports:

```text
reports/TXT_BASED_4P_IMPROVEMENT_DESIGN_20260618.md
reports/ALYCE_52_REPLAY_REVIEW_20260618.md
```

Code changes are intentionally limited to `main.py`. The bundled `orbit_lite/`
engine/model helpers remain copied from the reproduced Alyce package.

## Strategy Delta

The variant keeps 2P/3P behavior on the original path and enables a 4P-only FFA
safety layer:

- live player-strength / leader proxy;
- approximate reaction ETA map;
- 4P source reserve cap for valuable or pressured sources;
- trap-neutral rejection;
- contested-neutral hold/surplus gate;
- safe-neutral bonus;
- source depletion penalty;
- hold-gated leader asset bonus;
- low-value rear enemy penalty;
- direct threat-neighbor bonus.

The variant does not add opponent-name hardcoding, neural training, network
access, local file reads, or replay access at runtime.

## Packaging Notes

This is a multi-file candidate. To submit it, package `main.py` and the
`orbit_lite/` directory at archive root.

Do not submit until local 2P/4P validation shows no regression and a separate
submit confirmation card is written.
