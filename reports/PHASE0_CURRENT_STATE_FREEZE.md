# Phase 0 Current State Freeze

Date: 2026-06-17

Scope: freeze repository state before validating `vkhydras_last_heuristic` as a
single-file Kaggle candidate. No Kaggle submit command was run in this phase.

## Latest Commit

```text
c9103ec3418a45e81a1cb82ad1d66e4a483957f7
analysis: reselect stronger orbit wars base agent
```

Current worktree note:

```text
?? agents/variants/base_plus_source_safety_filter/
```

That directory is an untracked Pilkwang safety-filter experiment from earlier
work. It is not part of the current Vkhydras Last validation path.

## Current Official Best

Current completed official best in `reports/SCORECARD.md`:

```yaml
agent: pilkwang_structured single-file fallback
submission_id: 53767789
status: SubmissionStatus.COMPLETE
public_score_current_repo_record: 653.7
```

The user task text cites `653.9`, which was an earlier observed Kaggle rating.
The rating can drift as Kaggle updates leaderboard games. This freeze treats the
Pilkwang single-file fallback as the official best agent and will compare the
new candidate against that official baseline, not against local scores.

## Current Selected Local Base

Current local selected base in `configs/base_agent.yaml`:

```yaml
source_id: vkhydras_last_heuristic
tracked_main: agents/public/vkhydras_last_heuristic/main.py
wrapper: agents/base_agent.py
sha256: 5E35FE75AE5D32FDA08F839F5FC5BE245FDA0B26B050A0CB6CECD59CEF9938D8
selection_status: selected_after_base_reselection_screen
```

`agents/base_agent.py` calls Vkhydras Last for `agent(obs)`. Its legacy
`build_world(obs)` compatibility path still uses Pilkwang's world builder,
because Vkhydras Last exposes only `agent(obs)`.

## Current Official Best Agent

Official best is still:

```text
pilkwang_structured single-file fallback
```

Vkhydras Last is not yet officially submitted and has no official score.

## Adaptive Rejected Status

Adaptive variants are not current candidates:

- `adaptive_full`: rejected after local `3-97` versus base in a 50-seed
  bidirectional tournament, errors `0`.
- `adaptive_defense_only`: not selected; seed-1 bidirectional smoke versus base
  lost `0-2`.
- `adaptive_no_profiler`: not selected; seed-1 bidirectional smoke versus base
  lost `0-2`.
- `adaptive_reworked`: local tar packaging path previously reached Kaggle
  `ERROR`; no official score.

The current validation path is single-file Vkhydras Last, not tar-based
adaptive packaging.

## Vkhydras Last Local Evidence

From `reports/BASE_RESELECTION_REVIEW.md`:

- `vkhydras_last_heuristic` beat `vkhydras_peak_heuristic` `15-5` in a local
  10-seed bidirectional screen.
- `vkhydras_last_heuristic` beat the P0 local public pool `16-0` across
  Pilkwang, ykhnkf, Tamrazov, and SigmaBorov, errors `0`.
- 4-player smoke with Vkhydras Last, Pilkwang, Tamrazov, and SigmaBorov:
  Vkhydras Last won `2/3`, avg rank `1.3333`, errors `0`.
- `dist/main.py` generated from Vkhydras Last previously passed py_compile,
  banned-pattern scan, and starter smoke; this task will regenerate and verify
  that candidate formally.

These are local validation results only. They are not official leaderboard
scores.

## Next Gate

Proceed to:

1. Audit whether `agents/public/vkhydras_last_heuristic/main.py` is a complete
   single-file agent.
2. Package it as `dist/main.py`.
3. Validate packaged behavior locally against source, Pilkwang official best
   source, the P0 public pool, and a 4-player smoke set.
4. Audit license/attribution risk.
5. Generate `reports/SUBMIT_CONFIRM_VKH_LAST.md`.
6. Stop before Kaggle submission until the user explicitly says to submit.
