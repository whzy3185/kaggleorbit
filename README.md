# Orbit Wars Adaptive Agent

This project is the Orbit Wars workspace for a first official submission
baseline and then targeted agent development.

Current rule:

- Keep this project outside the Nemotron repository.
- Keep official data, downloaded zips, logs, replays, and packaged submissions out of git.
- First submit the official starter as a connectivity baseline.
- After official feedback exists, build targeted content around a stronger baseline:
  physics-aware world model, opponent tendency profiler, and confidence-gated
  counter-policy modifiers.

Competition:

- Slug: `orbit-wars`
- Environment: `orbit_wars`
- Entry file: `main.py`
- Required function: `agent(obs)`
- Action format: `[[from_planet_id, direction_angle, num_ships], ...]`

