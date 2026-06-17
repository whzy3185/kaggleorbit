import os
import sys

ROOT = None
if "__file__" in globals():
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
else:
    cwd = os.getcwd()
    candidates = [
        cwd,
        os.path.abspath(os.path.join(cwd, "..")),
        os.path.abspath(os.path.join(cwd, "..", "..")),
    ]
    for candidate in candidates:
        if os.path.isdir(os.path.join(candidate, "src", "orbitwars_agent")):
            ROOT = candidate
            break

if ROOT is None:
    ROOT = os.getcwd()
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from orbitwars_agent.adaptive_agent import agent as _adaptive_agent

CONFIG = {
    "use_profiler": True,
    "use_counter_policy": True,
    "use_supplemental_moves": True,
    "enabled_policies": (
        "enemy_rusher",
        "big_stack",
        "weakest_targeter",
    ),
    "max_supplemental_ship_ratio": 0.08,
    "max_supplemental_actions": 3,
    "protect_threatened_sources": True,
    "supplemental_requires_threat": True,
    "allow_positive_commit_delta": False,
}


def agent(obs, config=None):
    return _adaptive_agent(obs, config=CONFIG)
