import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from orbitwars_agent.adaptive_agent import agent


def main() -> None:
    obs = {
        "player": 0,
        "step": 5,
        "angular_velocity": 0.03,
        "comet_planet_ids": [],
        "initial_planets": [
            [0, 0, 10.0, 10.0, 2.0, 30, 2],
            [1, -1, 24.0, 12.0, 2.1, 8, 3],
            [2, 1, 90.0, 90.0, 2.0, 25, 2],
        ],
        "planets": [
            [0, 0, 10.0, 10.0, 2.0, 30, 2],
            [1, -1, 24.0, 12.0, 2.1, 8, 3],
            [2, 1, 90.0, 90.0, 2.0, 25, 2],
        ],
        "fleets": [],
    }
    moves = agent(obs)
    if not isinstance(moves, list):
        raise SystemExit("agent did not return a list")
    print(moves)


if __name__ == "__main__":
    main()

