# V7 Pause And MD Coverage Recheck - 2026-06-20

## Scope

User requested that V7 testing be paused and that the repo be rechecked for:

1. whether V7 was actually built on V6 and its replay-derived weak points;
2. whether the V6 replay review report exists;
3. whether V7 covered the prior report requirements sufficiently;
4. whether any relevant markdown files were missed.

No further V7 local tournament testing was run after this pause request.

## Immediate Status

```text
python test processes running: none observed
V7 submitted to Kaggle: no
V7 promoted: no
V7 committed: no
```

Current pending worktree items:

```text
modified: reports/SCORECARD.md
modified: reports/ALYCE_V6_SUBMISSION_RESULT_20260619.md
untracked: reports/ALYCE_V6_OFFICIAL_REPLAY_REVIEW_20260620.md
untracked: agents/variants/alyce_v7_continuous_recovery/
```

## V6 Replay Report Status

V6 replay review exists at:

```text
reports/ALYCE_V6_OFFICIAL_REPLAY_REVIEW_20260620.md
```

It is generated but not yet committed.

The report records:

```text
submission_id: 53852919
status: COMPLETE
public score snapshot: 1177.8
downloaded replay files: 73
public episodes analyzed: 72
2P public episodes: 38
4P public episodes: 34
```

Core V6 replay finding:

```text
V6 is the current official best observed in this repo, but 4P non-first games
still fall behind by step 50-100 and continue spending too many actions into
enemy or remote low-value targets after production position has deteriorated.
```

## Was V7 Built On V6?

Yes.

The V7 variant is a direct copy of:

```text
agents/variants/alyce_v6_prod_gap_mode
```

into:

```text
agents/variants/alyce_v7_continuous_recovery
```

The code diff confirms V7 changes only the selected-action filter path in
`main.py` plus trace environment naming. Bundled `orbit_lite/` helper code is
unchanged from V6.

V7 keeps V6/V2 behavior:

```text
severe trap neutral hard veto
soft contested neutral penalty
safe neutral bonus
source reserve and source depletion penalty
leader asset bonus
low-value rear enemy penalty
V6 production-gap selected-action branch
```

V7 adds:

```text
real production leader comparison instead of strength-leader production gap
4P turn 35-190 continuous recovery gate
continuous risk score from prod gap/rank/source depletion/target prod/distance/reaction gap
low-impact leader target risk
ORBIT_V7_TRACE_PATH support
```

## V7 Coverage Against V6 Replay Weak Points

| V6 replay weak point | V7 coverage | Status |
|---|---|---|
| Production gap should use actual production leader | Uses `prod_by_owner.argmax()` for `prod_leader` | covered |
| Hard V6 trigger was too rare | Adds softer `prod_gap <= -3` or `prod_rank >= 2` recovery gate | partially covered |
| Source depletion from important sources | Adds depletion and high-source production risk terms | partially covered |
| Low-value target while trailing | Adds target production and distance risk terms | partially covered |
| Bad enemy reaction / low holdability | Adds reaction gap risk and safer alternative preference | partially covered |
| Frontier/regroup alternative should be favored | Adds near/frontier and mine/regroup alternative bonus | partially covered |
| Low-impact leader target can be kingmaking | Adds `low_impact_leader_target` risk | partially covered |
| Full holdability / third-party aftermath model | Not implemented | not covered |
| Replay-inspired targeted local trace cases | Not implemented yet | not covered |

Conclusion: V7 is directionally based on the V6 replay weak points, but it is a
partial selected-action filter, not the full solution described across the
earlier design reports.

## Coverage Against Earlier MD Requirements

Important prior reports reviewed:

```text
reports/ALYCE_52_REPLAY_REVIEW_20260618.md
reports/TXT_BASED_4P_IMPROVEMENT_DESIGN_20260618.md
reports/OFFICIAL_REPLAY_PHASE_REVIEW_20260618.md
reports/V2_LATEST_REPLAY_AND_V3_SUBMISSION_SYNTHESIS_20260619.md
reports/V3_OFFICIAL_REPLAY_EFFECTIVENESS_REVIEW_20260619.md
reports/ALYCE_V4_SIM_CAUSE_ANALYSIS_20260619.md
reports/ALYCE_V5_IMPROVEMENT_TASK_CHAIN_20260619.md
reports/ALYCE_V6_PROD_GAP_TASK_CHAIN_20260619.md
reports/ALYCE_V6_LOCAL_EVAL_20260619.md
reports/ALYCE_V6_OFFICIAL_REPLAY_REVIEW_20260620.md
```

Covered or partially covered by V7:

```text
start from V2/V6 branch, not rejected V3/V4 branch
selected-action filter instead of supplemental action injection
local trace hook
production rank/gap signal
source depletion signal
reaction-gap signal
low-value enemy/leader target signal
frontier/regroup alternative preference
avoid broad static far-low penalty
```

Not covered by V7:

```text
full FFA mission layer
candidate-label trace for every candidate, not only final selected action
local match CSV step 50/100 production rank/gap integration
explicit third-party cleanup simulation
true holdability model after launch arrival
phase/rank reserve floor that changes send size directly
multi-size drain / tiered send sizes
contested neutral swarm / multi-source timing
rank-improvement counterfactual before leader pressure or elimination
official replay-inspired local scenario harness for the listed V6 non-first episodes
```

Therefore V7 does not fully cover all prior MD requirements. It only covers the
lowest-risk subset that can be expressed as a selected-action replacement
filter on top of V6.

## Current V7 Local Evidence Before Pause

These tests had already completed before the pause request.

1v1 small screens:

```text
V7 vs V6, seeds 1-3 bidirectional: V7 4-1-1, errors 0
V7 vs V2, seeds 1-3 bidirectional: V7 4-2, errors 0
```

4P rotated small screen against V1/V2/V6:

```text
V7 position 0: 1/3 first
V7 position 1: 0/3 first
V7 position 2: 1/3 first
V7 position 3: 0/3 first
total: 2/12 first
errors: 0
```

Interpretation:

```text
The 1v1 signal is promising but too small.
The 4P rotated signal is weak and seat-sensitive.
V7 should not be submitted or promoted from this evidence.
```

## Markdown Completeness Check

Tracked `reports/*.md` count:

```text
85 tracked markdown reports
```

Additional untracked generated report:

```text
reports/ALYCE_V6_OFFICIAL_REPLAY_REVIEW_20260620.md
```

A markdown filename reference scan across `reports/*.md` found no missing
referenced markdown filenames. In other words, there are no obvious broken
`*.md` report references from the current tracked report set.

However, the V7 implementation notes currently cite only a narrow subset of the
relevant prior reports. The strategy coverage review above shows that broader
prior design content exists and has not been fully implemented.

## Decision

Pause V7 as a research branch.

Do not submit V7.

Before any next code attempt, the missing items should be addressed in this
order:

1. Add candidate-label trace coverage and step 50/100 production rank/gap to
   local evaluation outputs.
2. Build replay-inspired local scenario checks from the V6 non-first episode
   list.
3. Decide whether to stay with selected-action replacement or move to a real
   FFA mission layer.
4. If staying with a filter, reduce V7's 4P seat sensitivity before any Kaggle
   submission.
5. If moving to mission layer, implement only trace-first FFA context and
   reaction map before changing launch sizes.
