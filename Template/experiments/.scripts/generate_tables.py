#!/usr/bin/env python3

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def build_table(csv_path: Path, out_tex: Path, label: str, caption: str) -> None:
    if not csv_path.exists():
        return

    grouped = defaultdict(list)
    sizes = {}
    with csv_path.open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            grouped[(row["instance"], row["algorithm"])].append(float(row["time_ms"]))
            sizes[row["instance"]] = row["size"]

    lines = [
        "\\begin{table}[!ht]",
        "\\centering",
        "\\small",
        "\\begin{tabular}{lrrr}",
        "\\toprule",
        "\\textbf{Instância} & \\textbf{Tamanho} & \\textbf{Algoritmo} & \\textbf{Tempo Médio (ms)} \\\\",
        "\\midrule",
    ]
    for (inst, algo), vals in sorted(grouped.items()):
        avg = sum(vals) / len(vals)
        inst_tex = inst.replace("_", "\\_")
        lines.append(
            f"\\texttt{{{inst_tex}}} & {sizes.get(inst, '-')} & \\texttt{{{algo}}} & {avg:.3f} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            f"\\caption{{{caption}}}",
            f"\\label{{{label}}}",
            "\\end{table}",
            "",
        ]
    )
    out_tex.parent.mkdir(parents=True, exist_ok=True)
    out_tex.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate LaTeX benchmark tables.")
    parser.add_argument("--suite", choices=["ic", "book", "all"], default="all")
    args = parser.parse_args()

    root = Path.cwd().resolve().parent
    if args.suite in ("ic", "all"):
        build_table(
            Path("results/ic/results.csv"),
            root / "latex/tables/table_results.tex",
            "tab:results_ic",
            "Resultados experimentais da suíte da IC.",
        )
    if args.suite in ("book", "all"):
        build_table(
            Path("results/book/results.csv"),
            root / "latex/book/tables/table_results.tex",
            "tab:results_book",
            "Resultados experimentais da suíte do Livro.",
        )


if __name__ == "__main__":
    main()
