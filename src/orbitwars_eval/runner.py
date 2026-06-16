from __future__ import annotations

import sys
import json
from pathlib import Path

from .loader import DEFAULT_ZOO, ROOT, resolve_agents

LAB_ROOT = ROOT / "external" / "orbit-wars-lab"
if str(LAB_ROOT) not in sys.path:
    sys.path.insert(0, str(LAB_ROOT))

from orbit_wars_app.match import run_match as lab_run_match  # noqa: E402


def run_match(
    agent_ids: list[str],
    *,
    seed: int = 42,
    mode: str = "fast",
    zoo_root: Path = DEFAULT_ZOO,
    output_json: Path | None = None,
) -> dict:
    refs = resolve_agents(agent_ids, zoo_root=zoo_root)
    outcome = lab_run_match(
        [ref.agent_id for ref in refs],
        [ref.path for ref in refs],
        seed=seed,
        mode=mode,  # type: ignore[arg-type]
    )
    data = {
        "agent_ids": list(outcome.agent_ids),
        "winner": outcome.winner,
        "scores": list(outcome.scores),
        "turns": outcome.turns,
        "duration_s": outcome.duration_s,
        "seed": outcome.seed,
        "status": outcome.status,
    }
    if output_json is not None:
        output_json.parent.mkdir(parents=True, exist_ok=True)
        output_json.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data
