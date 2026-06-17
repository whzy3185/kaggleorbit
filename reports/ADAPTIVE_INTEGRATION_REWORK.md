# Adaptive Integration Rework

Date: 2026-06-17

Scope: local code rework only. No Kaggle submission was run.

## Why This Rework Was Needed

Stage 3 showed the old adaptive wrapper was not a viable candidate:

```text
base vs adaptive_full, seeds 1-50, bidirectional: base 97, adaptive_full 3
```

The most likely failure mode was not loading or timeout. It was integration: base actions were emitted first, then supplemental adaptive moves were appended without a hard budget or a safety filter.

## Changes

### 1. Supplemental Budget Cap

`src/orbitwars_agent/adaptive_agent.py` now supports:

```yaml
max_supplemental_ship_ratio: 0.12
max_supplemental_actions: 4
```

The reworked variant uses stricter values:

```yaml
max_supplemental_ship_ratio: 0.08
max_supplemental_actions: 3
```

This prevents adaptive post-actions from consuming an unbounded share of remaining ships.

### 2. Threatened Source Safety Filter

New setting:

```yaml
protect_threatened_sources: true
```

If a source planet has incoming enemy fleets that exceed its current ships, base actions from that source are reduced or removed to preserve a defensive reserve.

### 3. Threat-Required Supplemental Mode

New setting:

```yaml
supplemental_requires_threat: true
```

The reworked variant only allows supplemental moves when the current state has a concrete incoming threat. This avoids profile-only attacks from weak evidence.

### 4. No Positive Commit Delta By Default

New setting:

```yaml
allow_positive_commit_delta: false
```

Counter-policy modifiers may reduce commitment, but they do not increase supplemental commit ratio by default.

### 5. New Evaluation Variant

Added:

```text
agents/variants/adaptive_reworked/main.py
```

Registered in:

```text
configs/eval_variants.yaml
```

The default `agents/adaptive_agent/main.py` was also changed to use the constrained reworked configuration so the old full-policy behavior is not accidentally used as the default adaptive entrypoint.

## Smoke Validation

Tests:

```text
PYTHONPATH=E:\orbitwars_adaptive_agent\src python -m pytest tests -q
```

Result:

```text
20 passed
```

Starter smoke:

```text
python scripts/run_eval_tournament.py --series smoke_reworked_starter --seeds 1 --out outputs/tournament_raw/smoke_reworked_starter --progress pair local/agents/variants/adaptive_reworked baselines/starter --bidirectional
```

Result:

| matchup | games | adaptive_reworked wins | starter wins | errors |
| --- | ---: | ---: | ---: | ---: |
| adaptive_reworked vs starter, seed 1, bidirectional | 2 | 2 | 0 | 0 |

## Remaining Risk

This rework only proves the new entrypoint runs. It does not prove the candidate is stronger than base.

The next required gate is Stage 7:

```text
base vs adaptive_reworked
adaptive_reworked vs Pilkwang/Tamrazov/SigmaBorov
4-player mixed smoke or small sample
```

If adaptive_reworked still loses badly to base, the final candidate remains `base_safe_fallback`.
