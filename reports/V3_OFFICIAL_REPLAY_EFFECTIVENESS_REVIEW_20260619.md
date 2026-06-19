# V3 Official Replay Effectiveness Review - 2026-06-19

## Scope

This review refreshes the official Kaggle state for the submitted V3 package and
analyzes all currently visible V3 replays.

V3 submission:

```text
submission_id: 53842450
message: alyce_intervention_v3_soft_far_low_penalty_b1542f4
package: dist/alyce_intervention_v3_20260619.tar.gz
sha256: 166D8C827A2F91FA28DF943F7611A145082538747293D7DACBFC3B0C9E026B90
```

Local replay root:

```text
D:\orbitwars_replays\alyce_intervention_v3_latest
```

Generated analysis files, intentionally outside Git:

```text
D:\orbitwars_replays\alyce_intervention_v3_latest\analysis\v3_episode_summary.csv
D:\orbitwars_replays\alyce_intervention_v3_latest\analysis\v3_action_events.csv
D:\orbitwars_replays\alyce_intervention_v3_latest\analysis\v3_key_snapshots.csv
D:\orbitwars_replays\alyce_intervention_v3_latest\analysis\v3_phase_summary.csv
D:\orbitwars_replays\alyce_intervention_v3_latest\analysis\v3_analysis_summary.json
```

Important limitation:

```text
Replay JSON exposes observations and actions, not internal candidate scores.
Action target labels below are inferred from pre-launch source position, launch
angle, and nearest plausible planet. They are good aggregate signals but not
private runtime traces.
```

## Current Official State

Latest Kaggle CLI query in this review:

| Submission | Current public score | Status | Current interpretation |
|---:|---:|---|---|
| `53827977` V2 | `1087.7` | `SubmissionStatus.COMPLETE` | Current repo official best, though lower than the previous `1101.6` snapshot. |
| `53793561` Alyce repro | `1069.1` | `SubmissionStatus.COMPLETE` | Still above V3. |
| `53842450` V3 | `1018.9` | `SubmissionStatus.COMPLETE` | No longer just validation `600.0`, but still below V2 and Alyce repro. |

Conclusion:

```text
V3 is playable and has public ladder episodes, but the submitted V3 measure is
not effective enough to replace V2 or the Alyce reproduction.
```

## Replay Coverage

Downloaded replay files:

```text
total replay files: 34
public replays: 33
validation/self-play replays: 1
```

Public replay split:

| Mode | First-place wins | Non-first episodes | Total | First-place rate |
|---|---:|---:|---:|---:|
| 2P | 12 | 4 | 16 | 75.0% |
| 4P | 6 | 11 | 17 | 35.3% |

Do not interpret this simple first-place rate as official rating. Kaggle rating
updates depend on opponent ratings and match composition.

## V3 Versus V2 At The Same Metric Level

The samples are not paired against identical opponents, so this is a behavioral
comparison, not an A/B proof.

| Metric | V2 latest visible replay sample | V3 visible replay sample |
|---|---:|---:|
| Public score at latest CLI query | `1087.7` | `1018.9` |
| Public replay count | 54 | 33 |
| 2P first-place rate | 58.6% | 75.0% |
| 4P first-place rate | 36.0% | 35.3% |
| 4P loss step50 avg prod gap | -5.75 | -8.182 |
| 4P loss step100 avg prod gap | -24.5 | -28.5 |
| 4P loss step150 avg prod gap | -39.33 | -31.333 |

The most important row is official score. V3 is materially lower. The replay
sample also does not show a 4P recovery advantage: V3 4P losses still fall far
behind by step 50-100.

## Production Gap By Phase

Average production gap to the current production leader:

| Step | V3 2P wins | V3 2P losses | V3 4P wins | V3 4P losses |
|---:|---:|---:|---:|---:|
| 20 | -0.083 | 0.0 | -0.167 | -1.636 |
| 50 | 0.0 | -1.0 | -1.333 | -8.182 |
| 100 | 0.0 | -1.0 | 0.0 | -28.5 |
| 150 | 0.0 | -18.0 | 0.0 | -31.333 |

Interpretation:

- V3 2P is often fine through step 100; the 2P losses separate later.
- V3 4P losses are usually already unstable by step 20-50.
- By step 100, V3 4P losses average `-28.5` production behind the leader.
- That repeats the old Alyce/V2 failure pattern: the losing 4P game is decided
  by early production conversion, not by late tactical cleanup.

## Action Mix

V3 4P target mix:

| Phase | Outcome | Enemy rate | Neutral rate | Mine/regroup rate | Far-low enemy penalty-like | Far-low neutral |
|---|---|---:|---:|---:|---:|---:|
| 0-50 | win | 0.37 | 0.556 | 0.074 | 1 | 6 |
| 0-50 | loss | 0.436 | 0.45 | 0.114 | 11 | 11 |
| 50-150 | win | 0.472 | 0.123 | 0.404 | 32 | 14 |
| 50-150 | loss | 0.563 | 0.131 | 0.306 | 11 | 24 |
| 150-300 | win | 0.452 | 0.024 | 0.524 | 4 | 1 |
| 150-300 | loss | 0.632 | 0.211 | 0.158 | 0 | 1 |

Main signal:

```text
V3 losses remain more enemy-target heavy and less consolidation-heavy than wins.
The V3 far-low penalty does not create enough regroup/consolidation behavior.
```

Average commit rates in V3 are still close to full-drain:

| Phase | V3 4P win avg commit | V3 4P loss avg commit |
|---|---:|---:|
| 0-50 | 0.984 | 0.969 |
| 50-150 | 0.943 | 0.966 |
| 150-300 | 0.922 | 0.962 |

This is expected because V3 did not change send sizing or source reserve. It
only subtracts a score penalty from some candidate targets.

## Did The V3 Measures Work?

Short answer:

```text
No, not as a replacement candidate.
```

More precise assessment:

1. V3 did preserve runtime validity.
   - The package completed official evaluation.
   - The score rose from validation-only `600.0` to `1018.9` after public games.

2. V3 did not beat the relevant baselines.
   - V3: `1018.9`.
   - Alyce repro: `1069.1`.
   - V2 current official best: `1087.7`.

3. V3 did not solve the measured 4P collapse.
   - 4P public first-place rate is only `35.3%`.
   - 4P loss step100 production gap is `-28.5`.
   - Several 4P losses end with our final production at zero.

4. The exact far-low penalty is too narrow for the true failure.
   - Some losing games still contain far-low neutral or far-low non-leader enemy
     actions.
   - Other losing games do not have many V3-penalty-like moves; they lose from
     early leader pressure, local overcommit, or lack of holdability/regroup.

5. The leader exception is important.
   - The code exempts low-value enemy targets owned by the current leader.
   - In replay this means a low-production target can still be selected if it is
     leader-owned, even when it is not holdable or rank-improving.

6. The penalty is applied after FFA bonuses but before greedy selection.
   - It can be overridden by flow score, target production bonus, leader attack
     bonus, and dynamic ROI.
   - Without action-change trace, we cannot know how often it changed the final
     selected move.

## Code Cause

Relevant code paths:

```text
agents/variants/alyce_intervention_v3/main.py
```

The V3 change adds only these config fields:

```text
enable_ffa_v3_safety
v3_far_enemy_dist = 45.0
v3_far_enemy_prod_max = 2.0
v3_far_enemy_penalty = 3.5
v3_far_enemy_dist_penalty = 0.04
v3_low_value_neutral_dist = 55.0
v3_low_value_neutral_prod_max = 1.0
v3_low_value_neutral_penalty = 2.0
```

It is enabled only in `CONFIG_4P`.

The actual branch is `_apply_ffa_v3_safety_penalty(...)`:

```text
if not enable_ffa_v3_safety or player_count < 4:
    return score

penalize enemy target only if:
  enemy target
  not current leader-owned
  target production <= 2
  immediate distance >= 45

penalize neutral target only if:
  neutral target
  target production <= 1
  immediate distance >= 55
```

It does not:

- delete actions;
- change fleet size;
- raise source reserve;
- change regroup scoring;
- classify trap neutrals by enemy reaction;
- classify holdability after capture;
- change 2P behavior;
- emit trace counters.

Therefore the observed outcome is consistent with the code: V3 can reduce some
specific bad candidates, but it cannot change the broader attack-vs-regroup,
holdability, or source depletion mechanics that decide 4P losses.

## Key Loss Examples

### Episode 80649187 - 4P collapse not primarily far-low penalty

```text
teams: lengli | Chase Bonfiglio | Pawan Rama Mali | muelsyse111
turns: 119
result: loss
```

Snapshots:

| Step | Our production | Leader production | Gap | Rank | Our planets |
|---:|---:|---:|---:|---:|---:|
| 20 | 8 | 11 | -3 | 2 | 3 |
| 50 | 8 | 18 | -10 | 4 | 3 |
| 100 | 0 | 65 | -65 | 3 | 0 |

Notable replay-inferred actions:

- step 31: full send to enemy prod-4 and far neutral prod-5.
- step 35: full send to enemy prod-1, distance 48.6, but target was leader-owned,
  so the V3 non-leader far-low enemy penalty would not apply.
- By step 50 the agent is rank 4 by production; by step 100 it has no planets.

This is a leader-pressure / holdability failure, not just an unpenalized far-low
neutral failure.

### Episode 80641852 - V3 still spends on far prod-1 neutrals

```text
teams: KoshinM | SUN | Reinhard | muelsyse111
turns: 124
result: loss
```

Snapshots:

| Step | Our production | Leader production | Gap | Rank | Our planets |
|---:|---:|---:|---:|---:|---:|
| 20 | 10 | 10 | 0 | 1 | 3 |
| 50 | 7 | 20 | -13 | 4 | 2 |
| 100 | 6 | 43 | -37 | 3 | 2 |

Notable replay-inferred actions:

- step 32: full send to neutral prod-1, distance 86.3.
- step 42: full send to the same far prod-1 neutral class.
- step 46: full send to neutral prod-1, distance 73.5.
- step 54-59: more far prod-1 neutral actions after the production position is
  already weak.

This directly shows the exact V3 neutral penalty did not remove the pattern. It
was only a score subtraction, and the candidate can still clear the planner's
threshold.

### Episode 80643617 - Penalty-like far enemy still appears

```text
teams: Akira Yasuda | Thomas | junesdata | muelsyse111
turns: 141
result: loss
```

Snapshots:

| Step | Our production | Leader production | Gap | Rank | Our planets |
|---:|---:|---:|---:|---:|---:|
| 20 | 12 | 13 | -1 | 2 | 3 |
| 50 | 8 | 18 | -10 | 4 | 3 |
| 100 | 0 | 33 | -33 | 3 | 0 |

Notable replay-inferred actions:

- step 21: enemy prod-2, distance 45.3, non-leader, penalty-like.
- steps 27-30: repeated enemy prod-2 at around 80 distance, penalty-like.
- step 49: enemy prod-2, distance 56.3, penalty-like.

This suggests either the base score remains high enough after penalty, or the
nearest-angle inferred target is not always the exact internal candidate. In
both cases, the action-level behavior did not improve enough.

## Synthesis With Previous Reports


### `ALYCE_INTRUDER_FULL_CODE_DECISION_REPORT.md`

Previous finding:

```text
The active Alyce Light line is a deterministic world-model heuristic. Attack
selection and regroup selection are separate layers, and replay moves cannot be
explained by attack scoring alone.
```

V3 confirms the same limitation. The replay shows final actions only. Because
V3 has no chosen-candidate trace, we still cannot distinguish whether a move was
an attack candidate, a defensive candidate, or regroup from replay alone. Any
next change must expose local-only selected action labels.

### `ALYCE_ELO_AND_OPPONENT_STRATEGY_RECHECK.md`

Previous finding:

```text
Alyce's broader notebook line discusses separate 2P/4P strategy presets,
ahead/even/behind behavior, stronger-enemy handling, and FFA anti-snowball
ideas. Light Intruder did not include all of that broader strategy.
```

V3 only restores one narrow static 4P target penalty. It does not implement the
richer opponent/rank/mode logic described in the broader Alyce line. The current
result supports that distinction: static distance/production penalties are not
enough.

### `OFFICIAL_REPLAY_PHASE_REVIEW_20260618.md`

Previous high-rank replay review suggested phase/rank-dependent behavior:

```text
leading, trailing, and mid-pack positions should not use one static target
preference in 4P.
```

V3 lacks rank-phase routing. The new V3 loss data is consistent with that gap:
when production rank falls by step 50-100, the agent still spends heavily on
enemy actions rather than switching into a consolidation or survival mode.

### `ALYCE_52_REPLAY_REVIEW_20260618.md`

Previous finding:

```text
4P failures are active games, not passive games. The issue is poor conversion of
launches into stable production and front control.
```

V3 confirms this. V3 4P losses have plenty of actions, high full-drain commit
rates, and high enemy-target rates, but still collapse by step 50-100.

### `TXT_BASED_4P_IMPROVEMENT_DESIGN_20260618.md`

Previous thesis:

```text
In 4P, every move must ask who benefits after arrival and whether the capture is
holdable after third-party response.
```

V3 did not implement that layer. It penalized two target classes by static
production and distance. It did not build a reaction map, holdability score, or
kingmaking/third-party cleanup estimate. The failure mode therefore persists.

### `ALYCE_FIRST_VERSION_FAILURE_COMMONALITY_20260619.md`

Previous finding:

```text
Full safe-drain itself is not automatically bad. The problem is large send plus
weak aftermath plus no durable front consolidation.
```

V3 preserves full-drain tempo, which was correct in principle. But it did not
add the missing aftermath model. The high average commit rates show that V3 is
still relying on full sends, and the 4P losses show the target/aftermath layer is
not good enough.

### `ALYCE_INTERVENTION_V3_ATTEMPT_20260619.md`

Previous local screen:

```text
2P short screen positive, 4P short screen negative.
```

Official result agrees with that warning. V3 is not a total runtime failure, but
it is lower than V2 and Alyce repro. The local 4P weakness was a real signal.

### `V2_LATEST_REPLAY_AND_V3_SUBMISSION_SYNTHESIS_20260619.md`

That report was written before V3 public ladder replays were visible. It said
not to compare V2 and V3 by phase until public V3 episodes exist. This report
fills that gap.

The updated conclusion is:

```text
V3 public replays are now visible and confirm that V3 should not be promoted.
```

## What Is Obviously Missing

1. Candidate-change trace.
   - We need to know whether V3 actually changed the selected action.
   - Current replay analysis can only observe final moves.

2. Reaction/holdability model.
   - Many failed moves are not low-production static targets; they are captures
     or attacks that do not survive the next enemy/third-party response.

3. 4P rank/phase policy.
   - V3 uses static 4P thresholds.
   - It does not behave differently when rank 1 at step 50 versus rank 4 at step
     50.

4. Attack-vs-regroup arbitration.
   - Loss phases still over-index on enemy actions and under-index on useful
     regroup/consolidation.

5. Leader target nuance.
   - Leader-owned low-value targets are exempt from the far enemy penalty.
   - That is too coarse: some leader attacks are valuable, but some are
     low-impact kingmaking or suicide pressure.

6. Target aftermath labels.
   - Need `safe_neutral`, `trap_neutral`, `leader_asset_holdable`,
     `threat_neighbor`, `enemy_rear`, and `regroup_front_node` labels.

## Next Optimization Route

Do not continue V3 unchanged.

Recommended next line:

```text
Base: current V2 official best for submission safety, but use Alyce Intervention
as the analysis/code base for candidate tracing.
```

Minimum next implementation should be trace-first:

1. Add local-only candidate trace in Intervention/V3 code.
   - pre-penalty score;
   - post-penalty score;
   - selected target family;
   - whether V3 penalty changed top candidate;
   - source remaining ships;
   - phase/rank context.

2. Run local replay-inspired 4P screens before submitting.

3. If action-changing again, make it narrower than V3:
   - no broad hard veto;
   - reduce far enemy penalty;
   - no blanket leader exemption;
   - add holdability and nearby-frontier checks;
   - boost regroup/front consolidation when trailing by production around step
     50-150.

4. Do not submit another candidate until it answers:
   - Does it keep 2P non-regression?
   - Does 4P step50/100 production gap improve?
   - Does selected-action trace show real intervention?
   - Does it reduce remote low-value tempo without killing winning full-drain
     openings?

## Decision

```text
V3 official replay review complete.
V3 measures are not sufficient.
Do not promote V3.
Do not resubmit V3 unchanged.
Current best remains V2 submission 53827977 at the latest visible score 1087.7.
```
