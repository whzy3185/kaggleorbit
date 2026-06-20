# Alyce V6 Official Replay Review - 2026-06-20

## Scope

This review covers the latest completed Orbit Wars submission for this repository:

```text
submission_id: 53852919
message: alyce_v6_prod_gap_mode_1db7614
package: dist/alyce_v6_prod_gap_mode_20260619.tar.gz
latest public score snapshot: 1177.8
status: COMPLETE
```

Downloaded replay root:

```text
D:\orbitwars_replays\alyce_v6_latest
```

Generated analysis files:

```text
D:\orbitwars_replays\alyce_v6_latest\analysis\v6_episode_summary.csv
D:\orbitwars_replays\alyce_v6_latest\analysis\v6_action_events.csv
D:\orbitwars_replays\alyce_v6_latest\analysis\v6_key_snapshots.csv
D:\orbitwars_replays\alyce_v6_latest\analysis\v6_phase_summary.csv
D:\orbitwars_replays\alyce_v6_latest\analysis\v6_analysis_summary.json
```

Important limitation: replay JSON exposes observations and submitted actions, not internal candidate scores or V6 trace. Target labels are inferred from source planet, launch angle, and nearest angular planet at the action step.

## Current Official State

| Submission | Public score snapshot | Status | Interpretation |
|---:|---:|---|---|
| 53852919 V6 | 1177.8 | COMPLETE | Current best observed in this repo. |
| 53851968 V5 | 1100.1 | COMPLETE | Score drifted upward from the first observed 756.7, but remains below V6. |
| 53827977 V2 | 1073.1 | COMPLETE | Previous practical best. |
| 53793561 Alyce repro | 1069.1 | COMPLETE | Original reproduction baseline. |
| 53842450 V3 | 1021.6 | COMPLETE | Below V2/V5/V6. |

Interpretation: V6 is the first local modification in this line that has clearly beaten the previous V2/Alyce reproduction official snapshots. The local 4P gate was pessimistic, but the official queue rewarded V6.

## Replay Coverage

Downloaded replay files: `73`
Public episodes analyzed: `72`
Validation/self-play episodes: `1`

| Mode | Episodes | First-place | Non-first | First-place rate | Rank distribution | Avg rank | Avg final prod | Avg final ships |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| 2P | 38 | 21 | 17 | 0.5526 | {1: 21, 2: 17} | 1.4474 | 33.1842 | 1060.6053 |
| 4P | 34 | 11 | 23 | 0.3235 | {1: 11, 2: 23} | 1.6765 | 16.3529 | 1117.8824 |

## Phase Production Snapshots

| Mode | Outcome | Step | N | Avg prod | Avg prod gap | Avg prod rank | Avg planets | Avg ships |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2P | first | 20 | 21 | 9.9524 | 0 | 1 | 3.2381 | 83.619 |
| 2P | first | 50 | 21 | 25.1429 | -1.6667 | 1.2857 | 8.5238 | 455.2857 |
| 2P | first | 100 | 21 | 37.3333 | 0 | 1 | 12.619 | 862.619 |
| 2P | first | 150 | 21 | 46.2857 | 0 | 1 | 15.7143 | 1129.619 |
| 2P | first | 200 | 21 | 51.2857 | -0.1905 | 1.0476 | 17.381 | 1401.9524 |
| 2P | non-first | 20 | 17 | 7.7647 | -0.1765 | 1.1176 | 2.8824 | 74.5882 |
| 2P | non-first | 50 | 17 | 24.1176 | -2.2941 | 1.4118 | 8.0588 | 411.7059 |
| 2P | non-first | 100 | 17 | 23.0588 | -11.9412 | 1.8235 | 7.9412 | 555.0588 |
| 2P | non-first | 150 | 17 | 8.3529 | -43.4118 | 1.9412 | 2.8235 | 246.1176 |
| 2P | non-first | 200 | 17 | 4.5294 | -51.1765 | 1.9412 | 1.5882 | 134.7647 |
| 4P | first | 20 | 11 | 5.7273 | -1.1818 | 1.8182 | 2.1818 | 62 |
| 4P | first | 50 | 11 | 13.9091 | -0.2727 | 1.0909 | 4.8182 | 245.9091 |
| 4P | first | 100 | 11 | 26.4545 | 0 | 1 | 8.8182 | 578.4545 |
| 4P | first | 150 | 11 | 42.6364 | 0 | 1 | 15.0909 | 1367.5455 |
| 4P | first | 200 | 11 | 46.7273 | 0 | 1 | 16.3636 | 1788.6364 |
| 4P | non-first | 20 | 23 | 7.5652 | -1.3913 | 1.7826 | 2.6087 | 76.6087 |
| 4P | non-first | 50 | 23 | 9.3478 | -6.8696 | 2.7826 | 3 | 173.4348 |
| 4P | non-first | 100 | 23 | 7.2174 | -19.3913 | 2.8696 | 2.3043 | 144.8261 |
| 4P | non-first | 150 | 23 | 2.4783 | -41.087 | 2.6957 | 1 | 95.7826 |
| 4P | non-first | 200 | 23 | 1.2174 | -51.0435 | 2.087 | 0.4348 | 59.087 |

Main read: V6 4P first-place games usually reach step 50 without a severe production deficit, while 4P non-first games are already behind by step 50 and are often strategically lost by step 100. This matches the earlier V2/V3 diagnosis, but V6 improves enough cases to raise the official score.

## Action Mix

| Mode | Outcome | Phase | Actions | Enemy rate | Neutral rate | Mine/regroup rate | Far-low neutral | Far-low enemy | Avg commit | Avg distance |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2P | nonwin | opening_0_50 | 521 | 0.2111 | 0.5163 | 0.2726 | 65 | 30 | 7.552 | 48.07 |
| 2P | nonwin | mid_50_150 | 2819 | 0.2834 | 0.1809 | 0.5357 | 198 | 157 | 13.4995 | 38.34 |
| 2P | nonwin | late_mid_150_300 | 890 | 0.2022 | 0.1787 | 0.6191 | 56 | 32 | 13.115 | 32.52 |
| 2P | nonwin | end_300_500 | 258 | 0.2442 | 0.2093 | 0.5465 | 8 | 14 | 22.8193 | 40.12 |
| 2P | win | opening_0_50 | 592 | 0.2416 | 0.5118 | 0.2466 | 56 | 41 | 9.1382 | 47.68 |
| 2P | win | mid_50_150 | 3218 | 0.3316 | 0.1992 | 0.4692 | 189 | 196 | 17.1458 | 43.72 |
| 2P | win | late_mid_150_300 | 1749 | 0.3316 | 0.231 | 0.4374 | 116 | 123 | 22.1164 | 45.51 |
| 2P | win | end_300_500 | 424 | 0.3255 | 0.2594 | 0.4151 | 37 | 28 | 26.7459 | 47.39 |
| 4P | nonwin | opening_0_50 | 559 | 0.2952 | 0.4902 | 0.2147 | 21 | 50 | 5.947 | 42.18 |
| 4P | nonwin | mid_50_150 | 1197 | 0.4837 | 0.2331 | 0.2832 | 49 | 102 | 8.0908 | 40.28 |
| 4P | nonwin | late_mid_150_300 | 280 | 0.5393 | 0.075 | 0.3857 | 7 | 26 | 14.1296 | 39.98 |
| 4P | nonwin | end_300_500 | 20 | 0.0 | 0.0 | 1.0 | 0 | 0 | 10.0 | 15.07 |
| 4P | win | opening_0_50 | 234 | 0.2607 | 0.5983 | 0.141 | 23 | 9 | 5.7538 | 41.15 |
| 4P | win | mid_50_150 | 1121 | 0.3711 | 0.1989 | 0.43 | 69 | 58 | 14.8927 | 35.19 |
| 4P | win | late_mid_150_300 | 152 | 0.3092 | 0.1711 | 0.5197 | 9 | 8 | 42.0912 | 31.78 |
| 4P | win | end_300_500 | 117 | 0.0855 | 0.4188 | 0.4957 | 8 | 1 | 46.8255 | 32.64 |

Main read: V6 did not eliminate enemy pressure. In successful 4P games it still attacks enemies, but the difference is that wins preserve more production and later consolidation. Non-first 4P games still show too many enemy or remote low-value actions after the production position has deteriorated.

## Strong 4P Wins

| Episode | Mode | Result | Rank | Turns | Final prod | Final planets | Final ships | Actions | Enemy | Neutral | Mine | Far-low N | Far-low E | Step100 prod gap | Teams |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 80789196 | 4P | first | 1 | 500 | 41 | 18 | 10799 | 228 | 28 | 114 | 86 | 21 | 4 | 0 | 鹅鹅鹅虎虎虎 / Lixin73 / muelsyse111 / Dmitry Kozlov |
| 80737357 | 4P | first | 1 | 290 | 68 | 24 | 7103 | 347 | 99 | 33 | 215 | 10 | 8 | 0 | muelsyse111 / ghostiee11 / Criquet / TY0912 |
| 80688323 | 4P | first | 1 | 155 | 58 | 26 | 3048 | 116 | 49 | 34 | 33 | 5 | 15 | 0 | Jay_townsend19 / Thomas N. / muelsyse111 / Mark Coffey |
| 80709775 | 4P | first | 1 | 213 | 48 | 16 | 3006 | 112 | 48 | 13 | 51 | 6 | 5 | 0 | Amir Ghazi / mitsuki / muelsyse111 / Van-Phuc Huynh |
| 80690140 | 4P | first | 1 | 227 | 41 | 16 | 2474 | 71 | 30 | 19 | 22 | 2 | 4 | 0 | muelsyse111 / Julio Contreras / Muhammad Firdaus / Keven Li |

These games are the clearest positive signal for V6. They show that the production-gap selected-action mode did not destroy tempo; when the opening survives, V6 can still snowball into high final ship counts.

## Key 4P Non-First Episodes

| Episode | Mode | Result | Rank | Turns | Final prod | Final planets | Final ships | Actions | Enemy | Neutral | Mine | Far-low N | Far-low E | Step100 prod gap | Teams |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 80792868 | 4P | non-first | 2 | 113 | 0 | 0 | 0 | 57 | 22 | 17 | 18 | 2 | 3 | -61 | siman / lvisdd / PrtkPiyush / muelsyse111 |
| 80717823 | 4P | non-first | 2 | 123 | 0 | 0 | 0 | 54 | 30 | 17 | 7 | 5 | 9 | -56 | Yusaku Muroya / Kuni05 / Orbit Magnus / muelsyse111 |
| 80703035 | 4P | non-first | 2 | 169 | 0 | 0 | 0 | 66 | 32 | 9 | 25 | 0 | 5 | -38 | muelsyse111 / izzie1i000 / 史永刚 / ksew364 |
| 80693165 | 4P | non-first | 2 | 149 | 0 | 0 | 0 | 104 | 37 | 54 | 13 | 6 | 8 | -33 | HanaMoodYusi. / Dmitry Kozlov / muelsyse111 / Sky kun |
| 80696452 | 4P | non-first | 2 | 194 | 0 | 0 | 0 | 31 | 14 | 11 | 6 | 1 | 4 | -33 | muelsyse111 / linrock / SUN / shyjin |

The failure cases still look familiar: step100 production gaps are negative, and several games continue spending actions into enemy or low-value targets after the production race has already been lost.

## Key 2P Losses

| Episode | Mode | Result | Rank | Turns | Final prod | Final planets | Final ships | Actions | Enemy | Neutral | Mine | Far-low N | Far-low E | Step100 prod gap | Teams |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 80811179 | 2P | non-first | 2 | 98 | 0 | 0 | 0 | 96 | 26 | 26 | 44 | 2 | 6 | -64 | Gerar Del Toro / muelsyse111 |
| 80706036 | 2P | non-first | 2 | 131 | 0 | 0 | 0 | 171 | 23 | 21 | 127 | 8 | 2 | -32 | muelsyse111 / Criquet |
| 80774925 | 2P | non-first | 2 | 162 | 0 | 0 | 0 | 43 | 12 | 26 | 5 | 5 | 1 | -20 | muelsyse111 / Flamadesombra |
| 80798619 | 2P | non-first | 2 | 500 | 1 | 1 | 428 | 55 | 10 | 37 | 8 | 18 | 3 | -18 | muelsyse111 / MMMMok |
| 80745535 | 2P | non-first | 2 | 145 | 0 | 0 | 0 | 53 | 28 | 11 | 14 | 2 | 15 | -16 | muelsyse111 / pantheon of ducks 🦆 |

2P losses remain less structurally severe than 4P losses. The 2P problem is usually midgame conversion or overcommit after an initially playable opening, not immediate 4P-style production collapse.

## Did V6 Measures Work?

Yes, at the official-score level. V6 is materially above V2, V5, V3, and the Alyce reproduction in the latest CLI snapshot.

What likely helped:

1. V6 kept V2 as the base instead of continuing the weaker V3/V4 branch.
2. The selected-action filter stayed narrow and did not globally suppress full-drain tempo.
3. The production-gap mode gave some trailing/rank-weak states an alternative to low-value attacks.
4. V6 retained the V2 4P mission filter that had already helped official performance.

What did not fully work:

1. The same 4P production-collapse pattern is still visible in non-first games.
2. Replay-only analysis cannot prove exactly when V6 internal mode fired, because official replays do not include `ORBIT_V6_TRACE_PATH` logs.
3. Local rotated-seat testing was noisy and pessimistic; it failed to predict official improvement.
4. V6 still lacks a full holdability/third-party aftermath model.

## Concrete Next Optimization Route

V7 should start from V6, not V5/V3/V4.

Priority changes:

1. Preserve V6 package structure and V2/V6 base behavior.
2. Add official-replay-inspired local trace cases for the 4P non-first episodes listed above.
3. Expand production-gap mode from rare hard thresholds to a continuous risk score using:
   - production gap and production rank;
   - source production and depletion ratio;
   - target production and distance;
   - enemy reaction gap;
   - whether the alternative is a frontier/regroup node.
4. Avoid broad far-low penalties; V5/V3 showed that static target penalties can underperform or overfit.
5. Add a leader/kingmaker guard: do not spend trailing resources on low-impact leader-owned targets unless the target is holdable or directly rank-improving.

Validation gates for V7:

```text
smoke candidate
V7 vs V6, 20 seeds bidirectional
V7 vs V2, 20 seeds bidirectional
V1/V2/V6/V7 4P, at least 5 seeds per V7 seat
targeted replay-inspired cases from worst 4P non-first V6 episodes
```

Submission rule: V7 should not be submitted solely on a small local family screen. V6 proved official score can disagree with local screen, but the next change should at least preserve V6 in direct tests and target the concrete 4P non-first failure episodes above.
