# Alyce Intruder 52 Replay Review

Date: 2026-06-18

Scope:

- Subject: official Alyce Intruder reproduction submission replays.
- Submission id: `53793561`
- Description: `alyce_intruder_repro_20260618`
- Local replay root: `D:\orbitwars_replays\alyce_intruder_latest`
- Raw replay JSON files: `D:\orbitwars_replays\alyce_intruder_latest\replays`
- Local analysis files:
  - `D:\orbitwars_replays\alyce_intruder_latest\analysis\aggregate.json`
  - `D:\orbitwars_replays\alyce_intruder_latest\analysis\episode_summary.csv`
  - `D:\orbitwars_replays\alyce_intruder_latest\analysis\action_events.csv`

This report is the missing Alyce-only replay review. It is separated from:

- `OFFICIAL_REPLAY_PHASE_REVIEW_20260618.md`, which mixes Alyce latest replay
  review with current high-rank replay slices.
- `TXT_BASED_4P_IMPROVEMENT_DESIGN_20260618.md`, which intentionally uses the
  user's txt first-principles notes and excludes high-rank replay evidence.

The raw replay files remain outside Git because `replays/`, `outputs/`, and large
downloaded datasets are not supposed to be committed.

## 1. Dataset Summary

Visible episodes downloaded:

```text
52
```

Mode split:

| Mode | Episodes | Rank distribution | Average rank |
|---|---:|---|---:|
| 2P | 26 | rank-1: 18, rank-2: 8 | 1.3077 |
| 4P | 26 | rank-1: 8, rank-2: 6, rank-3: 6, rank-4: 6 | 2.3846 |

Main finding:

```text
Alyce Intruder is much more reliable in 2P than in 4P.
The 4P failure mode is not simple passivity. It is unstable early/mid production
and survival after contested expansion or enemy pressure.
```

## 2. Aggregate Behavior

Mode-level averages from `episode_summary.csv`:

| Mode | Episodes | Avg actions | Avg enemy attacks | Avg regroup | Avg ships sent | Avg final production | Avg final planets |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2P | 26 | 129.2 | 34.6 | 61.9 | 6039.3 | 46.1 | 14.7 |
| 4P | 26 | 106.0 | 43.5 | 45.8 | 6045.6 | 22.0 | 6.7 |

Interpretation:

- 4P sends a similar total number of ships on average, but converts them into
  far less final production and fewer planets.
- 4P has more enemy-targeting pressure per episode than 2P, but that pressure
  does not reliably become stable ownership.
- The issue is not "Alyce never attacks"; it is that the chosen attacks and
  expansions do not consistently survive the 4P aftermath.

## 3. 2P Split

2P rank split:

| Result | Episodes | Avg actions | Avg enemy attacks | Avg regroup | Avg ships sent | Avg final production | Avg final planets | Avg steps |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| rank-1 | 18 | 111.2 | 33.1 | 50.5 | 6103.8 | 65.4 | 20.9 | 124.4 |
| rank-2 | 8 | 169.8 | 38.0 | 87.6 | 5894.0 | 2.5 | 0.6 | 258.5 |

2P observations:

- Losing 2P games have more total actions and more regroup actions than winning
  2P games.
- The loss pattern is therefore not lack of activity.
- Losses usually show early or midgame production failing to scale, followed by
  long defensive/regroup activity that cannot recover the production gap.
- This matches the code-level concern: once early target quality is wrong,
  later regroup can be busy but strategically late.

2P implication:

```text
Do not fix Alyce by simply lowering ROI or increasing wave count.
The 2P loss mode needs target-quality and source-budget safety, not just more launches.
```

## 4. 4P Split

4P rank split:

| Result | Episodes | Avg actions | Avg enemy attacks | Avg regroup | Avg ships sent | Avg final production | Avg final planets | Avg steps |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| rank-1 | 8 | 110.6 | 42.5 | 47.5 | 8900.0 | 64.8 | 19.5 | 157.0 |
| rank-2 | 6 | 220.7 | 90.8 | 107.5 | 11080.3 | 9.2 | 3.2 | 239.5 |
| rank-3 | 6 | 53.2 | 26.2 | 16.0 | 1989.0 | 0.0 | 0.0 | 160.0 |
| rank-4 | 6 | 37.8 | 14.7 | 11.7 | 1261.7 | 0.0 | 0.0 | 216.5 |

4P rank-1 pattern:

- High final production.
- Large ship expenditure can work when it converts into durable expansion.
- Enemy attacks are present but do not destroy the production base.

4P rank-2 pattern:

- The bot is extremely active: highest average actions, enemy attacks, regroup,
  and ships sent.
- Despite this activity, final production is only `9.2` and final planets `3.2`.
- This suggests many rank-2 games are not clean wins denied by small variance;
  they are survival/cleanup results after losing the production race.

4P rank-3 and rank-4 pattern:

- Final production and planets are zero on average.
- These are collapse games.
- Rank-4 sample episodes include:

| Episode | Actions | Enemy attacks | Neutral actions | Regroup | Ships sent | Final planets |
|---:|---:|---:|---:|---:|---:|---:|
| 80407605 | 8 | 3 | 5 | 0 | 252 | 0 |
| 80411852 | 46 | 17 | 16 | 13 | 1296 | 0 |
| 80414083 | 15 | 5 | 9 | 1 | 302 | 0 |
| 80414462 | 65 | 27 | 13 | 25 | 1723 | 0 |
| 80414821 | 28 | 5 | 9 | 14 | 1097 | 0 |
| 80418501 | 65 | 31 | 17 | 17 | 2900 | 0 |

Interpretation:

- Some rank-4 collapses are early and low-action.
- Some are high-action but still end at zero planets.
- The common failure is not one scalar like "too passive" or "too aggressive";
  it is poor conversion of launches into stable 4P position.

## 5. What The Replays Say About Current Alyce

### 5.1 Strengths

- Strong 2P conversion when early production scaling works.
- Good tactical movement volume.
- Uses regroup heavily, so it does not simply leave ships idle.
- Can win 4P when early/mid production survives.

### 5.2 Weaknesses

The 52 replays support these weakness categories:

1. 4P target-quality weakness.
   - Actions are made, but many do not produce stable final production.

2. Overcommit / source depletion risk.
   - Large sends can be correct, but the rank-2/rank-4 split shows that activity
     alone does not secure durable position.

3. Missing FFA aftermath model.
   - 4P needs to ask whether a capture can be held after nearby third-party
     reactions.

4. Missing neutral classification.
   - Neutral actions appear frequently even in collapse games.
   - The agent needs to distinguish safe neutral, contested neutral, and trap
     neutral.

5. Missing rank-aware enemy target classification.
   - Enemy-targeting action count can be high without preserving final position.
   - The bot needs to know whether an enemy target is a leader asset, immediate
     threat neighbor, low-value rear target, or elimination target.

6. Regroup is not enough after the position has already failed.
   - Losing 2P and rank-2 4P games often have high regroup counts.
   - Regroup should be paired with earlier source-budget protection and target
     holdability checks.

## 6. Connection To The Txt-Based Design

The 52 replay review strengthens, rather than replaces, the txt-based design.

The txt-based design said:

```text
4P needs a FFA mission layer:
safe/contested/trap neutral labels,
leader/threat/rear enemy labels,
reaction map,
third-party cleanup risk,
kingmaking penalty,
multi-size drain.
```

The 52 Alyce replays add concrete evidence:

```text
4P non-wins are not inactive games.
They have enough launches, enemy attacks, and regroup.
The missing piece is stable conversion and aftermath control.
```

Therefore the next code direction should still be:

```text
1. Do not lower ROI globally.
2. Do not simply add more waves.
3. Add trace-only FFA labels first.
4. Then gate unsafe neutrals and low-value enemy targets.
5. Then add source reserve and multi-size drain.
```

## 7. Recommended Next Implementation Order

### Step A: Replay-Derived Trace Targets

Before changing actions, add local-only trace labels:

```text
mission_type
neutral_label
enemy_label
reaction_gap
post_capture_hold_margin
source_depletion_ratio
self_rank_before
leader_before
```

Run this trace on the 52 downloaded Alyce episodes where possible, plus local 4P
games. The goal is to identify which labels correlate with collapse.

### Step B: 4P Trap Neutral Rejection

First action-changing rule:

```text
if 4P and neutral is trap:
    reject unless terminal all-in
```

This is low risk because it removes bad targets rather than adding new attacks.

### Step C: 4P Source Reserve Protection

Add a phase/rank-dependent reserve floor:

```text
opening: higher reserve on frontier/high-production sources
midgame: reserve based on incoming enemy pressure
endgame: lower reserve only if terminal all-in is justified
```

### Step D: Enemy Rear Penalty And Threat Neighbor Bonus

Only after neutral safety is stable:

```text
penalize distant low-value enemy rear targets
boost direct threat neighbors
boost leader assets only when holdable
```

### Step E: Multi-Size Drain

Evaluate:

```text
capture_floor
50 percent safe drain
75 percent safe drain
100 percent safe drain
```

This should reduce the "all safe ships into one uncertain target" pattern.

## 8. What Is Not Proven Yet

The 52 replay review does not prove:

- Which exact individual turn caused each collapse.
- That a specific formula will improve official rating.
- That high-rank leaderboard agents follow the same policy.
- That Alyce's official public score can be recovered by a small patch.

It does prove enough for the next engineering gate:

```text
Alyce's immediate improvement path is not more activity.
It is 4P target filtering, source protection, and mission-level aftermath scoring.
```

## 9. Relationship To Existing Reports

Use this report as the Alyce replay evidence report.

Use:

- `ALYCE_INTRUDER_FULL_CODE_DECISION_REPORT.md` for source-code decision structure.
- `ALYCE_ELO_AND_OPPONENT_STRATEGY_RECHECK.md` for Alyce's broader mode/ELO notes.
- `TXT_BASED_4P_IMPROVEMENT_DESIGN_20260618.md` for first-principles design.
- `OFFICIAL_REPLAY_PHASE_REVIEW_20260618.md` for combined Alyce plus current
  high-rank replay analysis.

Do not claim the txt-based design already contained this 52-replay review. It did
not. This report fills that gap.
