# Alyce Intervention V3 Wrapper

Entry point:

```python
def agent(obs):
    ...
```

Submission shape:

- Multi-file candidate.
- `main.py` imports local package directory `orbit_lite/`.
- Intended package format is a directory or tar.gz preserving `main.py` and `orbit_lite/` at submission root.

Current verification:

- `python -m py_compile agents/variants/alyce_intervention_v3/main.py`
- `python scripts/smoke_candidate.py agents/variants/alyce_intervention_v3`

Risk:

- The V3 penalties are evidence-based but not yet proven by large tournament.
- A soft penalty may still disturb Alyce Intervention's tuned ranking of targets.
- Do not submit before smoke and a short V3 vs base/local 4P screen.
