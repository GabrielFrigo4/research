#!/usr/bin/env python3

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate benchmark PDF charts.")
    parser.add_argument("--suite", choices=["ic", "book", "all"], default="all")
    args = parser.parse_args()

    try:
        import matplotlib.pyplot as plt  # noqa: F401
    except ImportError:
        return

    root = Path.cwd().resolve().parent
    targets = []
    if args.suite in ("ic", "all"):
        targets.append(root / "latex/figures")
    if args.suite in ("book", "all"):
        targets.append(root / "latex/book/figures")
    for target in targets:
        target.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
