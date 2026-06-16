from __future__ import annotations

from collections import defaultdict
from typing import Iterable


def summarize_matches(matches: Iterable[dict]) -> dict:
    stats = defaultdict(lambda: {"wins": 0, "losses": 0, "draws": 0, "errors": 0, "games": 0})
    for match in matches:
        agents = match.get("agent_ids", [])
        winner = match.get("winner")
        status = match.get("status")
        for agent in agents:
            stats[agent]["games"] += 1
            if status not in ("ok", "draw"):
                stats[agent]["errors"] += 1
            if winner is None:
                stats[agent]["draws"] += 1
            elif agent == winner:
                stats[agent]["wins"] += 1
            else:
                stats[agent]["losses"] += 1
    return dict(stats)

