# Eval Blockers

Date: 2026-06-16

Resolved:

| Issue | Resolution |
|---|---|
| `kaggle_environments` missing | Installed package body with `--no-deps`; `make("orbit_wars")` works |
| `trueskill` missing | Installed `trueskill` |
| `dataclasses.asdict` crashed on replay structs | Project wrapper now extracts only primitive match fields |

Remaining noise/blockers:

| Issue | Impact | Workaround |
|---|---|---|
| `pip install kaggle-environments>=1.28.0` full dependency install fails on `orbax-checkpoint` long path | Full RL/JAX dependency set not cleanly installed | Current `orbit_wars` eval works with package body and installed core deps |
| Kaggle env import logs OpenSpiel unknown poker games | No impact on `orbit_wars` runs observed | Treat as startup noise |
| `werewolf` env load logs missing `litellm` | No impact on `orbit_wars` runs observed | Do not install unless needed |
| `outputs/` contains local replays/results | Should not enter Git | Covered by `.gitignore` |

Next validation:

Run a wider base-agent selection gauntlet:

```powershell
python scripts\run_tournament.py round-robin `
  --agents external/pilkwang-structured external/tamrazov-starwars external/ykhnkf-distance-prioritized external/sigmaborov-reinforce baselines/starter `
  --seeds 401,402,403 `
  --out outputs\eval\base_selection_rr
```

