# Alyce V4 Local V1/V2/V3 Simulation

Date: 2026-06-19

## Scope

This report records the local simulation requested for Alyce V4:

1. 1v1: V4 vs V1, V4 vs V2, V4 vs V3.
2. 4P: V1/V2/V3/V4 play together with V4 rotated across all four positions.

This is local evaluation only. It is not an official Kaggle score and should not be treated as leaderboard evidence.

## Agents

| Version | Path | Notes |
| --- | --- | --- |
| V1 | `agents/variants/alyce_4p_ffa_v1` | First Alyce FFA intervention variant. |
| V2 | `agents/variants/alyce_4p_ffa_v2` | Current official best family, latest visible score recorded as 1087.7 in prior reports. |
| V3 | `agents/variants/alyce_intervention_v3` | Intervention V3, official result below V2 in prior reports. |
| V4 | `agents/variants/alyce_intervention_v4` | New context scorer variant. |

## Commands

1v1 outputs were already present under:

```text
outputs/v4_vs_v123_pair_s1_3/
```

The 4P rotation was run with seeds 1-3 and four fixed seat orders:

```text
outputs/v4_vs_v123_4p_s1_3/rot0_v4_pos0
outputs/v4_vs_v123_4p_s1_3/rot1_v4_pos1
outputs/v4_vs_v123_4p_s1_3/rot2_v4_pos2
outputs/v4_vs_v123_4p_s1_3/rot3_v4_pos3
```

No Kaggle submission was made.

## 1v1 Results

Each matchup used seeds 1-3, bidirectional, for 6 games per opponent.

| Matchup | V4 wins | Opponent wins | Draws | V4 winrate | Errors | Read |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| V4 vs V1 | 2 | 4 | 0 | 33.3% | 0 | V4 is worse than V1 in this small 1v1 screen. |
| V4 vs V2 | 3 | 3 | 0 | 50.0% | 0 | V4 is roughly neutral against V2 locally. |
| V4 vs V3 | 3 | 2 | 1 | 50.0% by all games / 60.0% excluding draw | 0 | V4 is slightly better than V3 in this small screen, but not decisive. |

Aggregated V4 1v1 line across all 18 games:

| Agent | Games | Wins | Losses | Draws | Winrate | Avg rank | Avg final ships | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| V4 | 18 | 8 | 9 | 1 | 44.4% | 1.5000 | 1078.06 | 0 |

## 4P Results

Setup:

```text
V1 + V2 + V3 + V4
seeds: 1-3
V4 seat positions: 0, 1, 2, 3
total games: 12
```

| Agent | Games | Wins | Losses | Draws | Winrate | Avg rank | Avg final ships | Rank distribution | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| V1 | 12 | 3 | 8 | 1 | 25.0% | 1.6667 | 1278.58 | rank1=4, rank2=8 | 0 |
| V2 | 12 | 5 | 6 | 1 | 41.7% | 1.6667 | 1246.25 | rank1=6, rank2=4, rank3=2 | 0 |
| V3 | 12 | 2 | 9 | 1 | 16.7% | 2.0833 | 1488.83 | rank1=3, rank2=6, rank3=2, rank4=1 | 0 |
| V4 | 12 | 1 | 10 | 1 | 8.3% | 2.0833 | 811.00 | rank1=2, rank2=7, rank3=3 | 0 |

V4 by seat:

| V4 position | Games | Wins | Winrate |
| ---: | ---: | ---: | ---: |
| 0 | 3 | 0 | 0.0% |
| 1 | 3 | 0 | 0.0% |
| 2 | 3 | 1 | 33.3% |
| 3 | 3 | 0 | 0.0% |

## 4P Match Outcomes

| Rotation | Seed | Winner | Status | Turns |
| --- | ---: | --- | --- | ---: |
| V4 pos0 | 1 | V3 | ok | 500 |
| V4 pos0 | 2 | V2 | ok | 222 |
| V4 pos0 | 3 | draw | draw | 500 |
| V4 pos1 | 1 | V1 | ok | 243 |
| V4 pos1 | 2 | V3 | ok | 251 |
| V4 pos1 | 3 | V1 | ok | 106 |
| V4 pos2 | 1 | V1 | ok | 221 |
| V4 pos2 | 2 | V2 | ok | 500 |
| V4 pos2 | 3 | V4 | ok | 500 |
| V4 pos3 | 1 | V2 | ok | 143 |
| V4 pos3 | 2 | V2 | ok | 500 |
| V4 pos3 | 3 | V2 | ok | 180 |

## Interpretation

V4 is not a safe upgrade candidate from this local screen.

The original V4 intent was to replace the V3 static far-low penalty with a more contextual 4P scorer. That did reduce some blind static behavior, but the current local result says the scorer is still harming competitive 4P outcomes. The most important signal is not the 1v1 result. The important signal is that V4 loses the direct four-way family test badly:

```text
V2: 5 wins / 12
V1: 3 wins / 12
V3: 2 wins / 12
V4: 1 win / 12
```

Because V2 is also the strongest current official family in prior reports, V4 should not be submitted in its current form.

## Likely Failure Pattern

The small sample suggests V4 may be over-filtering or over-penalizing actions that Alyce's original evaluator still needed for tempo. In 4P, avoiding bad far-low or trap targets is useful only if the replacement action preserves expansion speed and source pressure. If the filter demotes too many attacks without a strong alternative, the agent becomes a passive second-place finisher or loses race tempo.

Observed symptoms:

1. V4 often ranks second or third rather than converting to wins.
2. V4 has lower average final ships than V2 and V3 in the 4P family test.
3. V4 only wins from position 2 in this sample, so it does not show robust seat stability.
4. The 1v1 result against V1 is weak, which means the intervention may damage basic tempo even outside 4P.

## Decision

Do not submit V4 as-is.

Keep V2 as the current practical baseline. If V4 is continued, the next attempt should be narrower:

1. Preserve V2's default ranking unless the target is clearly suicidal.
2. Make trap/far-low penalties conditional on having a viable alternative target.
3. Add a trace comparison against V2 for the exact turns where V4 changes the chosen target.
4. Re-run the same `V4 vs V1/V2/V3` and `V1/V2/V3/V4` screens before any packaging or Kaggle upload.

