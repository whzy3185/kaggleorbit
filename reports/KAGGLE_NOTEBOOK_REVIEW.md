# Orbit Wars Kaggle Notebook Review

Date: 2026-06-16

This audit collects public Kaggle Code entries for Orbit Wars and statically
scans high-value notebooks. It does not submit anything and does not treat
notebook title score claims as official leaderboard evidence.

## Collection Methods

Kaggle CLI:

```bash
kaggle kernels list --competition orbit-wars --sort-by scoreDescending --page-size 200 -v
kaggle kernels list --competition orbit-wars --sort-by voteCount --page-size 200 -v
kaggle kernels list --competition orbit-wars --sort-by hotness --page-size 200 -v
kaggle kernels list --competition orbit-wars --sort-by dateRun --page-size 200 -v
kaggle kernels list --competition orbit-wars --sort-by dateCreated --page-size 200 -v
kaggle kernels list --competition orbit-wars --sort-by viewCount --page-size 200 -v
kaggle kernels list --competition orbit-wars --sort-by commentCount --page-size 200 -v
```

Keyword searches:

```text
LB, gold, strategy, baseline, agent, starter, rush, defense, comet, sun,
tournament, producer, reinforce, PPO, RL, heuristic, orbit wars
```

Web searches:

```text
site:kaggle.com/code orbit-wars agent
site:kaggle.com/code orbit-wars LB
site:kaggle.com/code orbit-wars strategy
site:kaggle.com/code orbit-wars baseline
site:kaggle.com/code orbit-wars comet
site:kaggle.com/code orbit-wars sun
site:kaggle.com/code orbit-wars tournament
```

Pulled notebook sources were stored under ignored
`external/kaggle_notebooks/`.

## Coverage

- CLI-unique Kaggle Code entries registered: 297
- Additional web-only / pull-failed lead: 1
- Total registered entries: 298
- High-value notebooks pulled and statically scanned: 27
- Registry output: `configs/kaggle_notebook_registry.yaml`
- Metadata limitation: Kaggle `kernel-metadata.json` did not include license
  fields in this session, so license is recorded as
  `unknown_from_kaggle_metadata`.

## Required Known Public Agents

| Kernel | Visible | Pulled | Static result |
|---|---:|---:|---|
| `romantamrazov/orbit-star-wars-lb-max-1224` | yes | yes | `agent(obs)` present; layered world-model style; writes `submission.py`. |
| `ykhnkf/distance-prioritized-agent-lb-max-score-1100` | yes | yes | `agent(obs)` present; distance-prioritized layered strategy; writes `submission.py`. |
| `pilkwang/orbit-wars-structured-baseline` | yes | yes | `agent(obs)` present; world model, reinforcement, recapture, swarm, crash-exploit concepts; writes `submission.py`. |
| `sigmaborov/lb-958-1-orbit-wars-2026-reinforce` | yes | yes | `agent(obs)` present; defense/reinforcement-focused layered baseline; writes `submission.py`. |
| `sigmaborov/orbit-wars-2026-starter` | yes | yes | `agent(obs)` present; simpler sun/comet/ETA-aware starter; writes `submission.py`. |
| `yuriygreben/orbit-wars-physics-aware-architect` | yes | yes | `agent(obs)` present; physics/world-model architecture; writes `submission.py`. |
| `kashiwaba/orbit-wars-reinforcement-learning-tutorial` | yes | yes | tutorial/training package; no direct `agent(obs)` submission in pulled notebook. |

## Additional High-Value Pulls

| Kernel | Family | Why it matters | Repro status |
|---|---|---|---|
| `slawekbiel/the-producer-agent` | production-greedy | Public Producer ROI/frontline planner from discussion. | `main.py` + `agent(obs)` present. |
| `slawekbiel/the-producer-v2` | production-greedy | Updated Producer with additional reinforcement/opponent-flow handling. | `main.py` + `agent(obs)` present. |
| `kuni05/lb-1240-5-orbit-wars-producer-agent-submission` | production-greedy | Multi-file Producer-style submission; useful for wrapper/path lessons. | `main.py` + multi-file package present. |
| `romantamrazov/orbit-wars-i-m-smarter` | production-greedy | Later Producer-hybrid style notebook. | `main.py` + `agent(obs)` present. |
| `anthonytherrien/floor-matched-fleets-target-veto-evacuation` | production-greedy/defense | Producer hybrid with floor-matched fleets, veto, evacuation. | `main.py` + `agent(obs)` present. |
| `vickimar/orbit-wars-heuristic-lb-1110` | hybrid-layered | Public heuristic lineage cited by community tournaments. | `agent(obs)` present; writes `/kaggle/working/submission.py`. |
| `konbu17/orbit-wars-rule-base-ml-shot-validator-hybrid` | hybrid-layered | Rule-based agent plus numpy shot validator. | `agent(obs)` present; writes `submission.py`. |
| `aidensong123/lb-highest-1000-search-learned-value-function` | search/value | Simulated outcomes ranked by learned value model. | `main.py` + `agent(obs)` present; dataset dependency. |
| `yashm917/orbit-wars-sim-value-search-agent` | search/value | Sim + value search with defense/attack phases. | `main.py` + `agent(obs)` present. |
| `rahulchauhan016/orbit-wars-parallel-mcts-video-analytics` | MCTS/tooling | MCTS and analytics code, not a direct submission. | pulled as analysis notebook; no `agent(obs)`. |
| `debugendless/orbit-wars-sun-dodging-baseline` | sun-dodge/physics | Public sun-dodging physics baseline. | `agent(obs)` present; writes `submission.py`. |
| `zacharymaronek/orbit-wars-heuristic-agent-scored-1000` | heuristic | Standalone Python script public heuristic. | `agent(obs)` present. |
| `slawekbiel/benchmark-for-aiming-implementation` | benchmark | Aiming benchmark from real top-10% shots plus negatives. | pulled as benchmark; no `agent(obs)`. |
| `souldrive/why-cloning-the-1-bot-loses-to-greedy` | replay analysis | BC failure analysis; useful evidence against blind imitation. | pulled as analysis notebook; no `agent(obs)`. |
| `sangrampatil5150/api-download-replay-orbit-wars` | replay tooling | Demonstrates replay API workflow. | pulled as tooling notebook; no `agent(obs)`. |

`konbu17/orbit-wars-tamrazov-ykhnkf-hybrid` appeared in web search, but
`kaggle kernels pull` returned 404 in this session. It is registered as a
web-only pull-failed lead.

## Static Strategy Family Counts

These counts are registry tags from title/metadata plus static scans for the
27 pulled notebooks. Low-signal entries are intentionally conservative.

| Family | Count |
|---|---:|
| unknown_or_low_signal | 181 |
| hybrid_layered_agent | 75 |
| production_greedy_expander | 13 |
| sun_dodge_physics_agent | 8 |
| RL_policy_agent | 6 |
| world_model_forecaster | 6 |
| defense_reinforcement_agent | 4 |
| distance_prioritized_rusher | 2 |
| aiming_benchmark_not_agent | 1 |
| replay_analysis_not_agent | 1 |
| replay_tooling_not_agent | 1 |

## Observed Notebook Patterns

1. Public strong heuristic code is mostly layered, not starter-simple.
   The major public lineages contain ETA/predictive aiming, sun checks, future
   ownership timelines, defense/reinforcement, recapture, multi-source swarm,
   and phase-specific scoring.

2. Producer-style notebooks are a distinct and important family.
   They are less like Pilkwang/Tamrazov world-model mission planners and more
   like ROI/flow-diff production planners with frontline movement and
   reinforcement constraints.

3. Notebook title scores are noisy leads only.
   Many titles include `LB`, `1200+`, `1300+`, or similar strings. The registry
   stores these as `title/community claim only`; no title claim is written as
   an official leaderboard fact.

4. `submission.py` vs `main.py` matters for loading.
   Many notebooks write `submission.py`, while the competition expects
   submission root `main.py`. These require wrapper/rename handling in Stage 5.
   Producer-style notebooks often already write `main.py`.

5. Some notebooks are not agents but are high value.
   RL tutorials, aiming benchmarks, replay download helpers, MCTS/video
   analytics, and BC failure analysis are not direct opponents but are important
   evidence for evaluation, replay analysis, and optimization direction.

## Reproducibility Risks

- License is unknown from pulled Kaggle metadata; do not vendor code blindly.
- Dataset/model dependencies must be checked before local runs
  (`aidensong123/orbit-wars-value`, `kashiwaba/orbitwars-ppo-sample-weight`,
  and some multi-file Producer packages are examples).
- Static scan is not a load/smoke test. Stage 5 must import and run wrappers.
- Kaggle Code may include notebook outputs, hidden assumptions, or packaging
  paths that differ from repository layout.
- One web-discovered lead returned 404 through the API in this session.

## Stage 5 Loading Priority From Notebook Audit

P0:

- `pilkwang_structured`
- `tamrazov_starwars`
- `sigmaborov_reinforce`
- `ykhnkf_distance_prioritized`
- `producer_v2` / `producer_agent`
- `vickimar_heuristic`
- `konbu17_rule_ml_validator`

P1:

- `yuriygreben_architect`
- `sigmaborov_starter`
- `debugendless_sun_dodging`
- `aidensong_search_value`
- `yashm917_sim_value`
- `kuni05_producer_submission`

P2:

- `kashiwaba_rl_tutorial`
- `souldrive_clone_analysis`
- `slawekbiel_aiming_benchmark`
- `rahul_mcts_analytics`
- replay download/tooling notebooks

