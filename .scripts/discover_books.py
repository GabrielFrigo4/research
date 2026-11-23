#!/usr/bin/env python3

import argparse
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

EXCLUDED_DIRS = {"Template", "OSS", "build", "dist", "node_modules", ".venv"}


def to_slug(name: str) -> str:
    ascii_name = (
        unicodedata.normalize("NFKD", name)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_name.lower()).strip("-")
    return slug or "research"


def parse_gitmodules_paths(repo_root: Path) -> list[str]:
    gitmodules = repo_root / ".gitmodules"
    if not gitmodules.is_file():
        return []

    paths = []
    for raw_line in gitmodules.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = re.match(r"^\s*path\s*=\s*(.+?)\s*$", raw_line)
        if match:
            paths.append(match.group(1))
    return paths


def discover_research_books(repo_root: Path) -> list[tuple[Path, str, str]]:
    candidates: list[str] = []
    seen: set[str] = set()

    for rel in parse_gitmodules_paths(repo_root):
        if rel not in seen:
            seen.add(rel)
            candidates.append(rel)

    for entry in sorted(repo_root.iterdir(), key=lambda p: p.name.lower()):
        if not entry.is_dir():
            continue
        name = entry.name
        if name.startswith(".") or name in EXCLUDED_DIRS:
            continue
        if name not in seen:
            seen.add(name)
            candidates.append(name)

    books: list[tuple[Path, str, str]] = []
    for rel in candidates:
        if rel in EXCLUDED_DIRS or rel.startswith("."):
            continue
        project_dir = repo_root / rel
        if not (project_dir / "Makefile").is_file():
            continue
        if not (project_dir / "latex" / "book.tex").is_file():
            continue
        slug = to_slug(project_dir.name)
        books.append((project_dir, rel, f"{slug}-book.pdf"))

    books.sort(key=lambda item: item[1].lower())
    return books


def cmd_map(books: list[tuple[Path, str, str]]) -> None:
    for _, rel, pdf_name in books:
        print(f"{rel}/latex/book.tex\t{pdf_name}")


def cmd_list(books: list[tuple[Path, str, str]]) -> None:
    if not books:
        print("Nenhum livro de pesquisa descoberto.")
        return
    for _, rel, pdf_name in books:
        print(f"- {rel}: {rel}/latex/book.tex -> dist/{pdf_name}")


def cmd_build(repo_root: Path, books: list[tuple[Path, str, str]]) -> int:
    if not books:
        print("Erro: nenhum livro encontrado para compilar.", file=sys.stderr)
        return 1

    dist_dir = repo_root / "dist"
    dist_dir.mkdir(parents=True, exist_ok=True)

    for project_dir, rel, pdf_name in books:
        print(f"==> Compilando livro de '{rel}' ({pdf_name})...")
        subprocess.run(["make", "book"], cwd=project_dir, check=True)
        built_pdf = project_dir / "latex" / "book.pdf"
        if not built_pdf.is_file():
            print(
                f"Erro: artefato esperado não encontrado: {built_pdf}",
                file=sys.stderr,
            )
            return 1
        shutil.copy2(built_pdf, dist_dir / pdf_name)
        print(f"    -> Publicado em dist/{pdf_name}")

    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Discover and compile research monographs in the Research hub."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--map", action="store_true", help="Emit release-map lines.")
    group.add_argument("--build", action="store_true", help="Build all books into dist/.")
    group.add_argument("--list", action="store_true", help="List discovered books.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    books = discover_research_books(repo_root)

    if args.map:
        cmd_map(books)
    elif args.list:
        cmd_list(books)
    elif args.build:
        sys.exit(cmd_build(repo_root, books))


if __name__ == "__main__":
    main()
