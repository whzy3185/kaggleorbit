# Next Codex Task Chain

Date: 2026-06-16

Goal: turn the audit into measurable local optimization without submitting to
Kaggle.

## Guardrails

- Do not call `kaggle competitions submit`.
- Do not commit `data/`, `external/`, `outputs/`, `replays/`, `dist/`, zip files,
  tarballs, credentials, cookies, or tokens.
- Treat local tournament and replay results as local-only evidence.
- Do not claim gold-team strategy until final medals and visible replay/team
  mapping exist.

## Task 1 - Profile Trace Harness

Implement optional profile trace logging for local matches.

Deliverables:

- `outputs/profile_traces/` JSONL traces, ignored by git.
- CLI flag on local match runner or a separate trace script.
- Report with first trigger turn per public P0 agent.

Suggested files:

- `scripts/run_match.py`
- `src/orbitwars_agent/adaptive_agent.py`
- `src/orbitwars_agent/opponent_profiler.py`

Acceptance:

- Existing tests pass.
- At least one trace exists for each P0 public agent.
- Trace includes scores, confidence, effective scores, selected modifiers, and
  supplemental action count.

## Task 2 - Fix observed_turns and Confidence

Correct profiler time accounting and rerun the same trace harness.

Deliverables:

- Unit tests for one-observation-per-enemy-per-step.
- Before/after trigger timing summary.

Suggested files:

- `src/orbitwars_agent/opponent_profiler.py`
- `tests/test_opponent_profiler.py`

Acceptance:

- `turtle` and `reinforce_heavy` are no longer driven by enemy planet count.
- Trigger timing changes are documented in a report.

## Task 3 - Public Family Benchmark Pool

Create repeatable local benchmark schedules by strategy family.

Deliverables:

- Family-balanced benchmark config.
- Script or documented command for smoke and full local runs.
- Local-only report template.

Suggested files:

- `configs/public_agent_pool.yaml`
- `configs/strategy_taxonomy.yaml`
- `scripts/run_public_pool.py`
- `reports/LOCAL_PUBLIC_FAMILY_BENCHMARK.md`

Acceptance:

- P0 public agents can be run from one command.
- Outputs stay under ignored `outputs/benchmarks/`.

## Task 4 - Recapture Feature

Add recently captured planet tracking and conservative recapture target bonus.

Deliverables:

- Ownership transition feature in world/profiler layer.
- Unit tests for recently captured enemy planets.
- Local benchmark against Producer/reinforce/hybrid families.

Suggested files:

- `src/orbitwars_agent/world_model.py`
- `src/orbitwars_agent/opponent_profiler.py`
- `src/orbitwars_agent/adaptive_agent.py`

Acceptance:

- Recapture bonus only applies to low-garrison recent captures.
- No regression in starter or nearest-expander smoke matches.

## Task 5 - Production/Center Control Branch

Activate currently unused `production_greedy` and carefully gate center control.

Deliverables:

- Counter branch for production-greedy agents.
- Optional center branch only when production/ETA is favorable.
- Tests proving `center_weight_mult` and production modifiers are consumed.

Suggested files:

- `src/orbitwars_agent/counter_policy.py`
- `src/orbitwars_agent/adaptive_agent.py`
- `tests/test_counter_policy.py`

Acceptance:

- `production_greedy` no longer dead-ends at the profiler.
- `risky_expansion_penalty` is either consumed or removed from the modifier
  surface.

## Task 6 - Comet Window Logic

Add comet timing/preposition only after trace and benchmark harnesses are stable.

Deliverables:

- Windowed comet profiler metrics.
- Lifetime-aware comet target scoring.
- Local replay/benchmark analysis.

Suggested files:

- `src/orbitwars_agent/physics.py`
- `src/orbitwars_agent/world_model.py`
- `src/orbitwars_agent/opponent_profiler.py`
- `src/orbitwars_agent/adaptive_agent.py`

Acceptance:

- No blind comet overcommit on low-lifetime planets.
- Improved local results against comet-aware public agents.

## First Command Set For Next Run

```powershell
git status -sb
pytest
python scripts/run_match.py local/agents/public/pilkwang_structured local/. --seed 1 --out outputs/profile_traces/pilkwang_seed1.json
python scripts/run_match.py local/agents/public/tamrazov_starwars local/. --seed 1 --out outputs/profile_traces/tamrazov_seed1.json
```

The exact trace flag or script will be added in Task 1.
