# Alyce 4P FFA V1 Implementation

Date: 2026-06-18

## 1. Inputs

This implementation follows two local review reports:

- `reports/TXT_BASED_4P_IMPROVEMENT_DESIGN_20260618.md`
- `reports/ALYCE_52_REPLAY_REVIEW_20260618.md`

The txt-based design supplied the first-principles route:

```text
4P is a relative-rank FFA game.
Do not only maximize local capture score.
Filter targets by reaction gap, third-party aftermath, source depletion, and rank pressure.
```

The 52-replay Alyce review supplied the local evidence:

```text
Alyce 4P non-wins are not inactive games.
They have enough launches, enemy attacks, and regroup.
The missing part is stable conversion of actions into durable production and survival.
```

## 2. Implementation Boundary

I did not modify the public reproduction in place. The original Alyce reproduction
remains:

```text
agents/public/alyce_intruder_repro
```

The new research variant is:

```text
agents/variants/alyce_4p_ffa_v1
```

Only the variant changes behavior. The bundled `orbit_lite/` helper files are
copied from the Alyce reproduction. The strategy changes are isolated in:

```text
agents/variants/alyce_4p_ffa_v1/main.py
```

No Kaggle submission was made.

## 3. Strategy Route

This is V1A, not the full final targeted agent.

Implemented now:

1. Keep 2P/3P on the Alyce Light path.
2. Enable the new FFA layer only in `CONFIG_4P`.
3. Estimate live player strength and current leader.
4. Approximate reaction ETA from enemy planets to each target.
5. Reserve ships on high-value or pressured 4P sources.
6. Reject trap neutrals.
7. Gate contested neutrals by surplus/hold margin.
8. Reward safe neutrals.
9. Penalize source depletion on valuable or pressured sources.
10. Add hold-gated leader-asset pressure.
11. Penalize low-value distant enemy rear targets.
12. Add a small threat-neighbor bonus for enemy targets near our valuable planets.

Deferred:

- full mission trace output;
- multi-size drain tiers;
- crash exploit;
- synchronized swarm planning;
- learned controller / GRU;
- packaging and submit confirmation.

## 4. Code-Level Changes

### 4.1 4P config gates

New `ProducerLiteConfig` fields control the FFA layer:

```text
enable_ffa_mission_filter
ffa_safe_neutral_gap
ffa_contested_neutral_gap
ffa_trap_neutral_gap
ffa_contested_min_surplus
ffa_source_reserve_frac
ffa_enemy_rear_eta
ffa_leader_bonus_weight
ffa_threat_neighbor_dist
```

Only `CONFIG_4P` sets:

```text
enable_ffa_mission_filter=True
```

### 4.2 FFA strength and leader proxy

Added `_ffa_strength(...)`:

```text
strength = owned production + planet ships component + fleet ships component
leader = argmax(strength)
```

This is board-state recognition, not opponent-name recognition.

### 4.3 Reaction map approximation

Added `_best_eta_to_targets(...)`:

```text
for each target:
  estimate first integer turn any source can reach it
```

This supports:

```text
reaction_gap = enemy_best_eta - our_candidate_eta
```

### 4.4 Source reserve protection

Added `_apply_4p_source_reserve(...)` before candidate sizing.

The reserve applies only when a source is:

```text
high production
or under notable enemy pressure
```

This is meant to reduce the 52-replay failure pattern where many actions still
collapse into zero final production.

### 4.5 Candidate adjustment

Added `_apply_4p_candidate_adjustments(...)` before greedy selection.

Neutral handling:

```text
trap neutral:
  reaction_gap < -1
  -> reject

bad contested neutral:
  reaction_gap <= 3 and surplus below hold requirement
  -> reject

safe neutral:
  reaction_gap >= 4
  -> small score bonus
```

Enemy handling:

```text
leader asset:
  bonus only if holdable

low-value rear:
  non-leader, low production, long ETA
  -> penalty

threat neighbor:
  enemy target near our high-production owned planet
  -> small bonus
```

Source depletion:

```text
if candidate sends >80% from a high-value/pressured source:
  apply penalty
```

## 5. Validation Run

Commands run:

```text
python -m py_compile agents\public\alyce_intruder_repro\main.py
python -m py_compile agents\variants\alyce_4p_ffa_v1\main.py
python scripts\smoke_candidate.py agents\variants\alyce_4p_ffa_v1 --seed 11 --json
```

2P smoke result:

```text
passed: true
env_status: ok
rewards: [1, -1]
turns: 96
```

4P smoke:

```text
agents: alyce_4p_ffa_v1, random, random, random
statuses: DONE/DONE/DONE/DONE
rewards: [1, -1, -1, -1]
turns: 117
```

2P sanity versus original Alyce:

```text
seed 21, variant first:
  winner: original Alyce
  status: ok

seed 22, original first:
  winner: variant
  status: ok
```

4P mixed sanity:

```text
seed 31: variant, original, random, random -> all DONE, variant rank-1
seed 32: original, variant, random, random -> all DONE, variant rank-1
seed 33: random, variant, original, random -> all DONE, original rank-1
```

These are smoke/sanity checks only. They prove the branch runs without immediate
runtime failure. They do not prove rating improvement.

## 6. Current Assessment

This is a useful first code slice because it changes the decision point where the
52-replay review found weakness:

```text
before greedy selection,
before source budget is spent,
only in 4P.
```

The implementation avoids the earlier bad pattern of appending supplemental
actions after the base has already drained ships.

The variant is not submit-ready yet.

## 7. Next Validation Route

Before any package or submit card:

1. Run 20 to 50 2P games against original Alyce to ensure 2P non-regression.
2. Run 40+ 4P mixed games with position rotation:
   - original Alyce
   - `alyce_4p_ffa_v1`
   - Vkhydras Last
   - Producer/Stronger public outputs if available locally
3. Add mission trace counters:
   - trap neutral rejects
   - contested neutral rejects
   - safe neutral bonuses
   - leader asset bonuses
   - source depletion penalties
4. If 4P improves without 2P collapse, then implement multi-size drain.

## 8. Submission Status

```text
submitted: false
official score: none
package: not generated
submit confirmation card: not generated
```

This is a research variant and should not be uploaded until a larger local
validation report exists.
