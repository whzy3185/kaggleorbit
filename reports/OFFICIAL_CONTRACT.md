# Official Contract

Date: 2026-06-16

Competition slug: `orbit-wars`

The Kaggle CLI can list the official competition files:

| File | Size |
|---|---:|
| `README.md` | 8241 |
| `agents.md` | 6486 |
| `main.py` | 2079 |

The submission must place `main.py` at the archive root or submit `main.py`
directly. The file must expose:

```python
def agent(obs):
    return []
```

Actions are returned as:

```python
[[from_planet_id, direction_angle, num_ships], ...]
```

Core game constants from the official README:

| Field | Value |
|---|---:|
| Board size | 100 x 100 |
| Sun center | 50, 50 |
| Sun radius | 10 |
| Max turns | 500 |
| Action timeout | 1 second |
| Max fleet speed | 6 |
| Comet spawn steps | 50, 150, 250, 350, 450 |

First baseline policy:

- Use the official starter `main.py`.
- Submit it once only to prove the account, file format, and feedback loop.
- Do not describe the starter as a custom improvement.

