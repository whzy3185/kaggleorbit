# Base Reselection Review

Date: 2026-06-17

## Decision

Switch the local base candidate from `pilkwang_structured` to
`vkhydras_last_heuristic`.

This is a local engineering decision only. It is not an official Kaggle score
claim.

## Why Reconsider

The previous base choice was made from an early two-seed smoke round-robin that
did not include the later-loaded vkhydras heuristic agents. Subsequent work also
showed that the adaptive wrapper is not yet a proven source of strength:

- `adaptive_full` lost `3-97` to the selected base in a 50-seed bidirectional
  local tournament.
- The tar.gz adaptive package errored on Kaggle validation.
- The post-base supplemental-action model can miss the main budget problem
  because the base may have already spent the ships.

The user's concern is valid: before adding more targeted logic, the foundation
must already avoid low-quality launches such as under-sized fleets that cannot
hold a target or drips that arrive too slowly.

## Evidence

### Vkhydras Peak Initial Screen

Command:

```powershell
python scripts\run_eval_tournament.py --series base_candidate_screen_vkh_peak --seeds 1-3 --out outputs\tournament_raw\base_candidate_screen_vkh_peak --progress gauntlet local/agents/public/vkhydras_peak_heuristic --opponents local/agents/public/pilkwang_structured local/agents/public/vkhydras_last_heuristic local/agents/public/ykhnkf_distance_prioritized local/agents/public/tamrazov_starwars local/agents/public/sigmaborov_reinforce --bidirectional
```

Result summary:

| Candidate | Games | Wins | Losses | Errors | Avg rank |
|---|---:|---:|---:|---:|---:|
| `vkhydras_peak_heuristic` | 30 | 26 | 4 | 0 | 1.1333 |

This already showed that Pilkwang was not a strong enough default base.

### Peak vs Last Focused Screen

Command:

```powershell
python scripts\run_eval_tournament.py --series base_candidate_vkh_peak_vs_last_10 --seeds 1-10 --out outputs\tournament_raw\base_candidate_vkh_peak_vs_last_10 --progress pair local/agents/public/vkhydras_peak_heuristic local/agents/public/vkhydras_last_heuristic --bidirectional
```

Result summary:

| Candidate | Games | Wins | Losses | Errors | Avg rank |
|---|---:|---:|---:|---:|---:|
| `vkhydras_last_heuristic` | 20 | 15 | 5 | 0 | 1.25 |
| `vkhydras_peak_heuristic` | 20 | 5 | 15 | 0 | 1.75 |

Despite the repository's "peak" label, the current local screen favors
`vkhydras_last_heuristic`.

### Last vs P0 Public Pool

Command:

```powershell
python scripts\run_eval_tournament.py --series base_candidate_screen_vkh_last_p0_s1_2 --seeds 1-2 --out outputs\tournament_raw\base_candidate_screen_vkh_last_p0_s1_2 --progress gauntlet local/agents/public/vkhydras_last_heuristic --opponents local/agents/public/pilkwang_structured local/agents/public/ykhnkf_distance_prioritized local/agents/public/tamrazov_starwars local/agents/public/sigmaborov_reinforce --bidirectional
```

Result summary:

| Candidate | Games | Wins | Losses | Errors | Avg rank | Avg final ships |
|---|---:|---:|---:|---:|---:|---:|
| `vkhydras_last_heuristic` | 16 | 16 | 0 | 0 | 1.0 | 3824.94 |

Per-opponent result:

| Opponent | Games | `vkhydras_last_heuristic` wins |
|---|---:|---:|
| `pilkwang_structured` | 4 | 4 |
| `ykhnkf_distance_prioritized` | 4 | 4 |
| `tamrazov_starwars` | 4 | 4 |
| `sigmaborov_reinforce` | 4 | 4 |

### 4-Player Smoke

Command:

```powershell
python scripts\run_eval_tournament.py --series vkh_last_4p_smoke_s1_3 --seeds 1-3 --out outputs\tournament_raw\vkh_last_4p_smoke_s1_3 --progress free-for-all --agents local/agents/public/vkhydras_last_heuristic local/agents/public/pilkwang_structured local/agents/public/tamrazov_starwars local/agents/public/sigmaborov_reinforce
```

Result summary:

| Candidate | Games | Wins | Errors | Avg rank |
|---|---:|---:|---:|---:|
| `vkhydras_last_heuristic` | 3 | 2 | 0 | 1.3333 |

This is only a smoke check, but it did not show an immediate 4-player collapse.

## Strategy-Level Difference

`vkhydras_last_heuristic` is a better optimization foundation because it already
contains the basic logic that the current wrapper was trying to retrofit:

- minimum dispatch floors so tiny fleets are avoided;
- speed-aware dispatch so long-distance captures are not sent with slow,
  ineffective ship counts;
- capture-margin logic and small snipe buffers;
- anti-snipe and reactive-snipe projection around contested neutrals;
- defense source reservation in 4-player games;
- target ranking with production, distance, static-planet, fleet-intent and
  recapture signals;
- endgame ROI and launch blackout gates;
- 4-player forward-simulation capture filters.

This directly addresses the failure mode where an agent launches ships that are
not enough to occupy or hold the target.

## Current Repository Change

- `agents/base_agent.py` now calls `agents/public/vkhydras_last_heuristic/main.py`
  for `agent(obs)`.
- `build_world(obs)` remains available through the old Pilkwang world builder
  for legacy adaptive code that expects it.
- `configs/base_agent.yaml` now selects `vkhydras_last_heuristic`.
- `configs/final_agent.yaml` now treats the stronger single-file base as the
  current score-improvement candidate.

## Packaging Smoke

Generated ignored local candidate:

```text
dist/main.py
sha256: 5E35FE75AE5D32FDA08F839F5FC5BE245FDA0B26B050A0CB6CECD59CEF9938D8
```

Checks:

- `python -m py_compile dist\main.py`: pass
- banned-pattern scan for `kaggle.json`, token, cookie, password, secret,
  submit: no matches
- `smoke_dist_vkh_last` vs starter, seed 9, bidirectional: `2-0`, errors `0`
- `python -m py_compile agents\base_agent.py agents\base_agent_entry\main.py agents\public\vkhydras_last_heuristic\main.py`:
  pass
- `smoke_reselected_base_entry` vs starter, seed 7, bidirectional: `2-0`,
  errors `0`
- `reselected_base_entry_vs_old_base_seed7` vs Pilkwang, seed 7,
  bidirectional: `2-0`, errors `0`
- `$env:PYTHONPATH='src'; pytest -q tests`: `20 passed`

Full `pytest -q` was also tried, but it collects gitignored `external/`
repositories and fails before running the project suite because those imported
repos have missing optional dependencies such as `fastapi`, conflicting test
module names, and missing local packages. This is a test collection scope issue,
not a failure in the base wrapper smoke tests.

This package was not submitted to Kaggle in this stage.

## Risk

- The source repository has no discovered LICENSE file. The README says the
  files are shared as baselines, but reuse should keep attribution and treat
  licensing as a known risk.
- Local tournaments are not official Kaggle scores.
- The 4-player check is small and only tested one seating order.
- The current adaptive profiler/counter-policy stack is not proven on top of
  this new base.

## Next Optimization Direction

Do not continue by adding broad adaptive post-actions. The next work should be:

1. Package `vkhydras_last_heuristic` as the next single-file candidate and smoke
   test it.
2. If submitting is explicitly approved, submit the single-file candidate and
   update `reports/SCORECARD.md`.
3. Optimize only by porting or simplifying proven base-level mechanics:
   capture sufficiency, anti-snipe hold checks, defense reserve, and target
   scoring. These should happen inside candidate scoring or action selection,
   not as late supplemental moves after the ship budget is already spent.
