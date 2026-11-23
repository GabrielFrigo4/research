#!/usr/bin/env python3

import argparse
import random
from pathlib import Path


def generate_instance(path: Path, n: int, rng: random.Random) -> None:
    values = [str(rng.randint(1, 1000)) for _ in range(n)]
    path.write_text(f"{n}\n" + " ".join(values) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate synthetic benchmark instances."
    )
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--count", type=int, default=5)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for idx in range(1, args.count + 1):
        n = idx * 1000
        generate_instance(out_dir / f"sample_{idx:02d}.dat", n, rng)


if __name__ == "__main__":
    main()
