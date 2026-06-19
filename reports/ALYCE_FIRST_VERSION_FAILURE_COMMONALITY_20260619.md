# Alyce First-Version Failure Commonality Review

Date: 2026-06-19

## Scope

This report re-checks the first submitted Alyce line after the failed V1/V2
modification attempts.

Primary replay source:

```text
D:\orbitwars_replays\alyce_intruder_latest
submission_id: 53793561
description: alyce_intruder_repro_20260618
official public score in latest CLI query: 1062.9
```

Local replay analysis files:

```text
D:\orbitwars_replays\alyce_intruder_latest\analysis\episode_summary.csv
D:\orbitwars_replays\alyce_intruder_latest\analysis\action_events.csv
D:\orbitwars_replays\alyce_intruder_latest\replays\*.json
```

Additional local derived files, not committed:

```text
outputs/alyce_first_replay_commonality/enriched_our_actions.csv
outputs/alyce_first_replay_commonality/episode_risk_features.csv
outputs/alyce_first_replay_commonality/phase_snapshots.csv
outputs/alyce_first_replay_commonality/episode_80405449_steps100_135_actions.csv
outputs/alyce_first_replay_commonality/summary.json
```

Important parsing correction:

```text
steps[N].action is already reflected in steps[N].observation.
For pre-launch source state, use steps[N-1].observation.
```

The existing `action_events.csv` `source_ships` column is therefore not used as
the pre-launch source garrison. I re-derived pre-launch source ships from raw
replay JSON.

## Why The V1/V2 Modifications Performed Poorly

The failed modifications tried to fix a real weakness, but at the wrong
integration level.

Observed results:

```text
V1 local 4P screen:
  alyce_4p_ffa_v1: 5/16 wins
  original Alyce repro: 10/16 wins

V1.1 local 4P quick screen:
  alyce_4p_ffa_v1: 3/8 wins
  original Alyce repro: 5/8 wins

V2 official:
  public score: 600.0
  current Alyce repro best: 1062.9
```

Root issue:

```text
The first Alyce Light version wins by fast full-safe-drain expansion plus
regroup amplification. V1/V2 added filters and reserves around that mechanism
without adding the missing higher-level planner features.
```

The replay data shows that full or near-full sends are not automatically bad.
They occur in both wins and losses:

| Segment | Fullish action rate | Near-empty-source rate |
|---|---:|---:|
| 4P rank-1 early 0-50 | 0.982 | 0.982 |
| 4P non-win early 0-50 | 0.960 | 0.949 |
| 4P rank-3/4 collapse early 0-50 | 0.947 | 0.930 |

So the simple rule "reserve more ships" suppresses a core winning pattern. The
real question is whether a full send converts into durable position.

V1/V2 did not answer that question well:

- V1 hard-rejected or heavily suppressed contested neutrals.
- V1/V2 reserved source budget without knowing whether the target was actually
  a winning tempo capture.
- V2 softened contested neutral rejection, but it still inherited the older
  Light structure, not the stronger Alyce Intervention/ProducerLite v15 structure.
- Neither V1 nor V2 added floor-sized/multi-tier fleet sizing, dynamic ROI,
  comet guard/evacuation, or strong FFA leader-pressure scoring from Alyce
  Intervention.

Conclusion:

```text
The modification failed because it reduced tempo before adding a better
candidate model. It treated symptoms as filters instead of improving scoring,
sizing, and aftermath evaluation.
```

## Common Failure Pattern In First-Version Alyce Replays

### 1. 4P Losses Are Decided Early By Production Conversion

4P rank-1 games have already pulled ahead by step 50:

| 4P segment | Step | Avg our production | Avg prod gap vs best opponent | Behind-best rate |
|---|---:|---:|---:|---:|
| rank-1 | 50 | 24.88 | +8.12 | 0.000 |
| non-win | 50 | 11.39 | -8.44 | 0.833 |
| rank-3/4 | 50 | 8.75 | -9.00 | 0.917 |
| rank-1 | 100 | 46.12 | +32.38 | 0.000 |
| non-win | 100 | 9.12 | -26.35 | 1.000 |
| rank-3/4 | 100 | 8.00 | -27.36 | 1.000 |

This is the strongest commonality:

```text
When Alyce is not ahead by production around step 50, the rest of the game is
usually recovery activity rather than a real comeback.
```

### 2. Collapse Games Spend Early Full Sends On Less Consolidating Targets

Early 4P rank-1 games:

```text
neutral_rate: 0.288
enemy_rate: 0.347
regroup_rate: 0.365
avg_target_dist: 38.73
avg_target_prod: 3.05
```

Early 4P collapse games:

```text
neutral_rate: 0.535
enemy_rate: 0.395
regroup_rate: 0.070
avg_target_dist: 51.90
avg_target_prod: 3.03
```

Interpretation:

```text
The losing/collapse opening is not idle. It is active, fullish, and neutral-heavy,
but less consolidating. It spends almost the same full-drain pattern on farther
targets and does much less early regroup/front consolidation.
```

This explains why the naive "reject contested neutral" patch was dangerous:
some early neutral expansion is necessary, but the target has to be classified
as safe, contested-but-worth-it, or trap. A broad filter removes good tempo too.

### 3. Midgame Non-Wins Become Fragmented Enemy Pressure

4P rank-1 midgame 101-200:

```text
actions: 139
avg_ships: 145.47
enemy_rate: 0.504
regroup_rate: 0.439
far_low_enemy_count: 10
```

4P non-win midgame 101-200:

```text
actions: 355
avg_ships: 35.95
enemy_rate: 0.696
regroup_rate: 0.282
far_low_enemy_count: 33
```

Commonality:

```text
After losing the production race, Alyce often keeps attacking, but the attacks
are smaller, more numerous, and more often aimed at low-value or distant enemy
targets. This is activity after strategic failure, not a winning pressure plan.
```

### 4. Regroup Is Amplifier, Not Rescue

The first version's regroup layer is strong when it amplifies a good front. It is
weak when the expansion state is already bad.

Evidence:

- 4P rank-1 early games show substantial regroup share: 0.365.
- 4P collapse early games show very low regroup share: 0.070.
- 2P losing games often have high regroup counts later, but still fail to recover
  production.

Conclusion:

```text
Regroup helps a good opening snowball. It does not reliably repair bad target
choice or source depletion after the production gap is already formed.
```

## Episode 80405449: Why Self-Play Was Not Symmetric

Episode `80405449` is useful because both players used the same Alyce first
version and the game stayed close through the opening.

Key facts:

```text
players: 2
player 0 final rank: 2
player 1 final rank: 1
step 100 snapshot:
  player 0: 8 planets, production 18, ships 84
  player 1: 8 planets, production 18, ships 83
step 200 snapshot:
  player 0: 5 planets, production 13, ships 103
  player 1: 11 planets, production 23, ships 171
```

The split starts around steps 100-129.

Examples extracted from raw replay with pre-launch source state:

```text
step 100 player 0:
  32/32 to neutral, dist 55.05, target prod 1
  12/12 to neutral, dist 100.97, target prod 1
  21/21 and 9/9 regroup

step 103 player 0:
  42/42 to neutral, dist 47.10, target prod 1
  31/31 to neutral, dist 47.10, target prod 1
  44/44 to enemy, dist 90.50, target prod 1
  12/12 to enemy, dist 105.27, target prod 4

step 103 player 1:
  44/44 to neutral, dist 47.10, target prod 1
  40/40 regroup, dist 74.44, target prod 4
  28/28 regroup, dist 10.79, target prod 1
  12/12 to enemy, dist 105.27, target prod 4

step 110-112 player 0:
  multiple 100 percent sends, including 97/97 to neutral and 96/96 into a
  nearby contest.

step 112-120 player 1:
  more large regroup/front consolidation moves, including 79/79, 112/112,
  79/79, 46/46, plus neutral captures.

step 129 player 1:
  75/105 to an enemy target while keeping 30 ships behind on the source,
  plus 90/90 to another enemy target.
```

Interpretation:

```text
The game did not diverge because one side had a different hard-coded opening.
It diverged because mirrored candidate slots were not semantically symmetric,
then full safe-drain and regroup amplified a small middle-game positional
difference.
```

Code causes:

- Candidate tie-break is by candidate ordering, not by geometric symmetry.
- Source/target slot IDs differ for mirrored planets.
- The agent considers one dominant send size: safe drain.
- Regroup and attack are selected through separate mechanisms.
- Once one side has better front-line ownership, regroup pushes more mass there,
  which creates larger future safe drains.

This is the same commonality seen in 4P, only cleaner:

```text
full-drain + nearest/ROI candidate + regroup amplification is high leverage.
If the target chain is good, it snowballs. If not, it empties sources and the
next decisions are forced recovery moves.
```

## Why The First Modification Direction Was Too Crude

The first-principles 4P diagnosis was mostly right:

```text
4P needs target labels, reaction maps, source protection, and aftermath scoring.
```

The implementation was too crude because it acted before measuring:

```text
bad: broad hard/soft filters on contested neutrals and source reserves
better: instrument decisions first, then change only candidates known to correlate
with collapse
```

The common failure is not "too many ships" or "too many neutral targets" in
isolation. The common failure is:

```text
large send + weak aftermath + no durable front consolidation
```

Therefore a good adjustment must preserve winning full-drain tempo when it is
safe and only intervene on low-conversion patterns.

## Evidence-Based Next Adjustment Route

Do not continue tuning `alyce_4p_ffa_v2`.

Reason:

```text
official score: 600.0
it remains weaker than the unmodified Alyce repro at 1062.9
it is based on the older Light structure rather than full Intervention
```

Next base:

```text
external/kaggle_outputs/alycemiki__intervention-command-w-ffa/submission_extracted
```

Why:

- It already includes floor-sized/multi-tier fleets.
- It already includes dynamic ROI.
- It already includes 4P FFA leader pressure.
- It already includes comet guard and evacuation.
- Local short screen beat V2 3-1 with no errors.

Next implementation must be trace-first:

```text
1. Add local-only decision trace counters to full Alyce Intervention.
2. Log candidate category, send_ratio, source_after_send, target_prod,
   target_distance, target_family, phase, player_count, and eventual local
   outcome when running local eval.
3. Do not add new hard filters until the trace shows which labels correlate
   with rank-3/4 collapse.
```

First action-changing candidates, only after trace:

```text
1. Narrow far-low-value enemy penalty:
   Only penalize enemy targets with low production, long ETA/distance, not
   leader-owned, and not adjacent to our high-value front.

2. Trap-neutral veto:
   Only reject neutral targets that are both far/low-value and likely to be
   cleaned up by another player before we can consolidate.

3. Source reserve only on high-value frontier:
   Do not reserve every source. Reserve only if the source is high production
   or adjacent to enemy pressure and the candidate is not a decisive capture.

4. Regroup-preserving target choice:
   Prefer captures that become useful regroup/front nodes over isolated low-prod
   captures.
```

Non-goals:

```text
Do not globally lower ROI.
Do not globally increase waves.
Do not re-submit V2.
Do not add opponent-name hardcoding.
Do not apply broad neutral suppression.
```

## Final Answer To The Current Question

Why was the modification worse than the pre-modification Alyce?

```text
Because it interfered with the same full-safe-drain tempo that makes Alyce win,
without adding a more accurate target/sizing/aftermath model. The original's
weakness is contextual conversion, not raw aggression.
```

Do key decision mistakes share a commonality?

```text
Yes. Losses repeatedly show early production lag caused by large sends that do
not become durable production/front control. In 4P this becomes fatal by step
50-100; in self-play it appears as a small midgame target/regroup divergence
that safe-drain then amplifies into a decisive snowball.
```

