# Opponent Profiler Design

Date: 2026-06-16

Implemented file:

- `src/orbitwars_agent/opponent_profiler.py`

The profiler tracks newly observed enemy fleets by ID, estimates likely target
from fleet angle/path, and accumulates per-enemy behavior counts.

Profile outputs:

- `neutral_rusher`
- `enemy_rusher`
- `turtle`
- `center_greedy`
- `production_greedy`
- `big_stack_attacker`
- `comet_greedy`
- `overcommitter`
- `weak_bot`
- `confidence`

API:

- `OpponentProfiler.update(state)`
- `OpponentProfiler.get_profile(enemy_id)`
- `OpponentProfiler.get_all_profiles()`

Safety rule:

The profiler does not name-match public agents. It only uses visible behavior:
new fleets, target type, target production, comet/center targeting, fleet size,
and estimated overcommit ratio.

Confidence:

Confidence grows with observed new fleets and observed turns. Early low-signal
states should not drive hard strategy changes.

Validation:

```powershell
$env:PYTHONPATH='E:\orbitwars_adaptive_agent\src'
python -m pytest tests\test_opponent_profiler.py -q
```

Result: pass.

