# Baseline Tournament

Date: 2026-06-16

These are local tournament results only. They are not official Kaggle scores.

Minimum acceptance checks:

| Check | Command/source | Result |
|---|---|---|
| Agent zoo lists | `python -m orbit_wars_app.tournament ... list` | 11 agents listed |
| Starter vs nearest | lab run `2026-06-16-001` | starter won, 5397 vs 600, status ok |
| Starter vs starter | lab run `2026-06-16-003` | player-0 starter won, 2426 vs 0, status ok |
| Public strong vs starter | lab run `2026-06-16-002` | Pilkwang won, 1655 vs 0, status ok |
| Wrapper match | `scripts/run_match.py` | starter won vs nearest, 1486 vs 0, status ok |
| Wrapper gauntlet | `scripts/run_tournament.py` | Pilkwang 2-0 vs starter/nearest, no errors |

Wrapper gauntlet summary:

```json
{
  "external/pilkwang-structured": {
    "wins": 2,
    "losses": 0,
    "draws": 0,
    "errors": 0,
    "games": 2
  },
  "baselines/starter": {
    "wins": 0,
    "losses": 1,
    "draws": 0,
    "errors": 0,
    "games": 1
  },
  "baselines/nearest-sniper": {
    "wins": 0,
    "losses": 1,
    "draws": 0,
    "errors": 0,
    "games": 1
  }
}
```

Interpretation:

- Local evaluation is operational.
- Pilkwang is clearly stronger than starter/nearest in the smoke runs.
- This is not enough for final base selection; next step is a multi-agent,
  multi-seed gauntlet over P0/P1 public candidates.

