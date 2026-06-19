# Alyce Intervention V3 Attempt - 2026-06-19

## Summary

V3 is a narrow modification on top of the full public `alycemiki/intervention-command-w-ffa` output, not a continuation of the rejected `alyce_4p_ffa_v2` filter.

The goal was to test one evidence-backed change from the replay review:

- keep Alyce Intervention's original full-drain tempo;
- avoid broad source reserve or action deletion;
- softly demote far low-value targets in 4-player games.

This candidate is implemented at:

```text
agents/variants/alyce_intervention_v3/
```

## Evidence Used

The previous review found that failed local variants damaged Alyce's main strength by interfering with its tuned target tempo. The 52 replay review and first-version failure report showed common 4P loss patterns:

- non-winning games were often behind by step 50-100 production conversion;
- losing lines showed more early neutral-heavy/far target behavior;
- losing midgames showed more fragmented far/low-value enemy attacks;
- full safe-drain itself was not the problem, because both wins and losses used fullish sends.

Therefore V3 uses a soft score penalty instead of a hard launch veto.

## Code Change

Base package:

```text
external/kaggle_outputs/alycemiki__intervention-command-w-ffa/submission_extracted
```

V3 keeps the multi-file structure:

```text
main.py
orbit_lite/
```

New config fields in `ProducerLiteConfig`:

```text
enable_ffa_v3_safety
v3_far_enemy_dist
v3_far_enemy_prod_max
v3_far_enemy_penalty
v3_far_enemy_dist_penalty
v3_low_value_neutral_dist
v3_low_value_neutral_prod_max
v3_low_value_neutral_penalty
```

The feature is enabled only in `CONFIG_4P`.

The new `_apply_ffa_v3_safety_penalty(...)` is applied after permanent target bonuses and FFA bonuses, before the greedy selector. It does two things:

1. Penalizes far low-production enemy targets when that enemy is not the current strength leader.
2. Penalizes far low-production neutral targets.

It does not:

- delete actions;
- reserve ships globally;
- change launch format;
- inspect opponent names;
- modify 2P default config.

## Verification

Syntax:

```text
python -m py_compile agents/variants/alyce_intervention_v3/main.py
```

Result: pass.

Smoke:

```text
python scripts/smoke_candidate.py agents/variants/alyce_intervention_v3
```

Result:

```text
passed: true
env_status: ok
sample_actions_ok: true
turns: 96
seed: 1
```

## Short Local Evaluation

These are local tournament checks only, not official Kaggle scores.

### 2P: V3 vs Original Intervention

Command:

```text
python scripts/run_eval_tournament.py --series alyce_intervention_v3_pair_base_short --seeds 1-2 --out outputs/alyce_intervention_v3_pair_base_short --progress pair local/agents/variants/alyce_intervention_v3 local/external/kaggle_outputs/alycemiki__intervention-command-w-ffa/submission_extracted --bidirectional
```

Result:

```text
games: 4
V3 wins: 3
Original Intervention wins: 1
errors: 0
V3 avg_rank: 1.25
V3 avg_final_ships: 1409.0
```

Interpretation: positive smoke-level signal in 2P, but sample is too small.

### 4P: V3 Position 0, Original Intervention Position 1

Command:

```text
python scripts/run_eval_tournament.py --series alyce_intervention_v3_ffa_short --seeds 1-2 --out outputs/alyce_intervention_v3_ffa_short --progress free-for-all --agents local/agents/variants/alyce_intervention_v3 local/external/kaggle_outputs/alycemiki__intervention-command-w-ffa/submission_extracted local/agents/public/vkhydras_last_heuristic local/agents/public/pilkwang_structured
```

Result:

```text
games: 2
V3 wins: 0
Original Intervention wins: 2
errors: 0
V3 avg_rank: 2.0
Original avg_rank: 1.0
```

### 4P: Original Intervention Position 0, V3 Position 1

Command:

```text
python scripts/run_eval_tournament.py --series alyce_intervention_v3_ffa_swap_short --seeds 1-2 --out outputs/alyce_intervention_v3_ffa_swap_short --progress free-for-all --agents local/external/kaggle_outputs/alycemiki__intervention-command-w-ffa/submission_extracted local/agents/variants/alyce_intervention_v3 local/agents/public/vkhydras_last_heuristic local/agents/public/pilkwang_structured
```

Result:

```text
games: 2
V3 wins: 1
Original Intervention wins: 1
errors: 0
V3 avg_rank: 1.5
Original avg_rank: 1.5
```

### Combined 4P Short Screen

```text
games: 4
V3 wins: 1
Original Intervention wins: 3
errors: 0
```

Interpretation: the 4P result does not justify replacing or submitting over the original Intervention package.

## Decision

Do not submit V3 yet.

The modification is technically valid and does not crash, but the 4P short screen is weaker than the original Intervention baseline. The current official best in this repository remains the previously submitted Alyce reproduction, not V3.

## Next Adjustment

If continuing V3, make the penalty smaller or more conditional:

1. Reduce `v3_far_enemy_penalty` from `3.5` to `1.0-1.5`.
2. Restrict the far enemy penalty to steps `< 180`, because late-game low-value attacks may still be useful as finishing pressure.
3. Restrict the far neutral penalty to only targets with no nearby owned source or no production advantage, instead of using distance and production alone.
4. Add trace counters for how often V3 penalties change the selected action, then compare changed turns against replay outcomes.

No Kaggle submission was made for this V3 attempt.
