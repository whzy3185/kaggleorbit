from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ZOO = ROOT / "external" / "orbit-wars-lab" / "agents"


@dataclass(frozen=True)
class AgentRef:
    agent_id: str
    path: Path


def resolve_agent(agent_id: str, zoo_root: Path = DEFAULT_ZOO) -> AgentRef:
    if agent_id.startswith("local/"):
        rel = agent_id.removeprefix("local/")
        path = ROOT / rel
    else:
        path = zoo_root / Path(agent_id)
    if not (path / "main.py").is_file():
        raise FileNotFoundError(f"Agent {agent_id!r} has no main.py at {path}")
    return AgentRef(agent_id=agent_id, path=path)


def resolve_agents(agent_ids: Iterable[str], zoo_root: Path = DEFAULT_ZOO) -> list[AgentRef]:
    return [resolve_agent(agent_id, zoo_root=zoo_root) for agent_id in agent_ids]

