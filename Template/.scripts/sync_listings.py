#!/usr/bin/env python3

import sys
from pathlib import Path

LISTING_DEFINITIONS = [
    {
        "source": "implementations/core/AlgorithmBase.hpp",
        "output": "latex/appendices/10_base.tex",
        "title": "Implementação da Interface Base ``AlgorithmBase''",
        "label_appendix": "ap:base",
        "caption": "Implementação em C++23 da interface base abstrata \\lstinline{AlgorithmBase}.",
        "label_listing": "lst:base",
    },
    {
        "source": "implementations/algorithms/SampleAlgorithm.hpp",
        "output": "latex/appendices/11_sample_algorithm.tex",
        "title": "Implementação da Classe ``SampleAlgorithm''",
        "label_appendix": "ap:sample_algorithm",
        "caption": "Implementação de referência \\lstinline{SampleAlgorithm} em C++23.",
        "label_listing": "lst:sample_algorithm",
    },
]


def generate_appendix_content(
    title: str, label_appendix: str, caption: str, label_listing: str, source_code: str
) -> str:
    separator = "% " + "=" * 73
    return (
        f"\\newpage\n\n"
        f"{separator}\n"
        f"% {title.upper()}\n"
        f"{separator}\n"
        f"\\apendice{{{title}}}\n"
        f"\\label{{{label_appendix}}}\n\n"
        f"\\begin{{lstlisting}}[caption={{{caption}}}, label={{{label_listing}}}]\n"
        f"{source_code.strip()}\n"
        f"\\end{{lstlisting}}\n"
    )


def find_repo_root() -> Path:
    current = Path.cwd().resolve()
    for directory in [current, *current.parents]:
        if (directory / ".git").exists() or (directory / "implementations").exists():
            return directory
    return current


def sync_listings(check_only: bool = False) -> bool:
    repo_root = find_repo_root()
    is_in_sync = True

    for definition in LISTING_DEFINITIONS:
        source_path = repo_root / definition["source"]
        output_path = repo_root / definition["output"]

        if not source_path.exists():
            sys.stderr.write(f"Source file not found: {source_path}\n")
            return False

        source_code = source_path.read_text(encoding="utf-8")
        expected_content = generate_appendix_content(
            definition["title"],
            definition["label_appendix"],
            definition["caption"],
            definition["label_listing"],
            source_code,
        )

        if check_only:
            if not output_path.exists():
                sys.stderr.write(f"Missing appendix file: {output_path}\n")
                is_in_sync = False
            else:
                current_content = output_path.read_text(encoding="utf-8")
                if current_content != expected_content:
                    sys.stderr.write(
                        f"Listing out of sync: {output_path} with {source_path}\n"
                    )
                    is_in_sync = False
        else:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(expected_content, encoding="utf-8")

    return is_in_sync


def main() -> None:
    check_mode = "--check" in sys.argv
    if not sync_listings(check_only=check_mode):
        sys.exit(1)


if __name__ == "__main__":
    main()
