# Targeted Agent Design

Date: 2026-06-16

Goal:

Build a targeted Orbit Wars agent around a stable base strategy, with opponent
profiling used only as a scoring and budget modifier.

Implemented first pass:

| Component | Path | Role |
|---|---|---|
| Physics helpers | `src/orbitwars_agent/physics.py` | distance, angle, ETA, sun intersection, orbit prediction |
| World model | `src/orbitwars_agent/world_model.py` | parse observation, infer likely fleet targets |
| Opponent profiler | `src/orbitwars_agent/opponent_profiler.py` | track new enemy fleets and produce tendency scores |
| Counter policy | `src/orbitwars_agent/counter_policy.py` | convert profiles into safe strategy modifiers |
| Candidate agent | `src/orbitwars_agent/adaptive_agent.py` | fallback-safe action generator |
| Candidate entry | `agents/adaptive_agent/main.py` | future tar.gz submission entry |

Profile dimensions:

- `neutral_rusher`
- `enemy_rusher`
- `turtle`
- `center_greedy`
- `production_greedy`
- `big_stack`
- `comet_greedy`
- `overcommitter`

Design constraint:

The profiler must not hard-switch the entire strategy. It adjusts reserve,
defense, expansion, attack, comet, counterattack, and commit-ratio weights.

Current limitation:

The candidate agent is a scaffold, not yet selected for submission. It needs
local tournament evaluation against public agents before replacing the official
starter or a public strong baseline.

