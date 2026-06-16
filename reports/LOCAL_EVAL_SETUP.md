# Local Eval Setup

Date: 2026-06-16

Local evaluation is now available through two paths:

1. Direct `orbit-wars-lab` CLI with `PYTHONPATH=external/orbit-wars-lab`.
2. Project wrappers in `src/orbitwars_eval/` and `scripts/`.

Installed/verified pieces:

| Component | Status | Notes |
|---|---|---|
| `kaggle_environments` | installed | `make("orbit_wars")` works |
| `orbit-wars-lab` | cloned | ignored under `external/` |
| `trueskill` | installed | needed by lab tournament CLI |
| `scripts/run_match.py` | pass | wraps lab fast match runner |
| `scripts/run_tournament.py` | pass | supports small round-robin and gauntlet runs |

Installation note:

The first `pip install kaggle-environments>=1.28.0` failed on Windows due an
`orbax-checkpoint` long-path install error. The workaround was:

```powershell
python -m pip install kaggle-environments==1.30.1 --no-deps
python -m pip install trueskill
```

This is enough for local `orbit_wars` matches in the current environment.

Useful commands:

```powershell
python scripts\run_match.py baselines/starter baselines/nearest-sniper --seed 201 --out outputs\eval\smoke_match.json

python scripts\run_tournament.py gauntlet external/pilkwang-structured `
  --opponents baselines/starter baselines/nearest-sniper `
  --seeds 301 `
  --out outputs\eval\pilkwang_smoke
```

Outputs are written under ignored `outputs/`.

