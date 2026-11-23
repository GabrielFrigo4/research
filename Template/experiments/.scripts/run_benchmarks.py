#!/usr/bin/env python3

import argparse
import csv
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run benchmark suite.")
    parser.add_argument("--suite", choices=["ic", "book"], required=True)
    parser.add_argument("--bin", required=True)
    parser.add_argument("--instances-dir", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=16)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    instances = sorted(Path(args.instances_dir).glob("*.dat"))

    rows = []
    for inst in instances:
        for _ in range(args.repeats):
            proc = subprocess.run(
                [args.bin, str(inst)],
                capture_output=True,
                text=True,
                timeout=args.timeout,
                check=True,
            )
            parts = proc.stdout.strip().split(",")
            if len(parts) == 4:
                rows.append([args.suite, inst.stem, *parts])

    csv_path = out_dir / "results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["suite", "instance", "algorithm", "size", "time_ms", "result"])
        writer.writerows(rows)


if __name__ == "__main__":
    main()
