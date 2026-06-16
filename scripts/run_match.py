import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from orbitwars_eval.runner import run_match


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("agent_a")
    parser.add_argument("agent_b")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--mode", choices=["fast", "faithful"], default="fast")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    output = Path(args.out) if args.out else None
    result = run_match([args.agent_a, args.agent_b], seed=args.seed, mode=args.mode, output_json=output)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

