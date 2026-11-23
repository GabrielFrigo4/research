#!/usr/bin/env sh
# ----------------------------------------------------------------
# Scaffolding: Research Repository Archetype Initializer
# ----------------------------------------------------------------

set -eu

_dir="$(cd "$(dirname "$0")" && pwd)"
. "${_dir}/.scripts/ui.sh"

_rm=0
_name="${NAME:-}"
_subtitle="${SUBTITLE:-Teoria, Algoritmos e Implementações}"
_desc="${DESC:-}"
_slug="${SLUG:-}"
_author="${AUTHOR:-Gabriel Frigo}"
_advisor="${ADVISOR:-Profa. Dra. Orientadora}"
_year="${YEAR:-$(date +%Y 2> "/dev/null" || printf "2026")}"
_edital="${EDITAL:-01/2026 PIC/PIBIC/PIBITI/PIBIC-AF}"
_github_user="${GITHUB_USER:-GabrielFrigo4}"

_pos_idx=0
for _arg in "$@"; do
	if [ "${_arg}" = "--rm" ]; then
		_rm=1
	else
		_pos_idx=$((_pos_idx + 1))
		case "${_pos_idx}" in
			1) _name="${_arg}" ;;
			2) _desc="${_arg}" ;;
			3) _slug="${_arg}" ;;
			4) _advisor="${_arg}" ;;
		esac
	fi
done

if [ -z "${_name}" ]; then
	_ui_banner "Research Repository Archetype Initializer"
	printf "Título da Pesquisa (ex: Algoritmos Probabilísticos): "
	read -r _name
fi

if [ -z "${_desc}" ]; then
	printf "Descrição da Pesquisa (vazio para padrão): "
	read -r _desc || true
fi
[ -z "${_desc}" ] && _desc="Projeto de pesquisa científica em ${_name}, integrando teoria formal, implementações em C++23, validação experimental e monografia em LaTeX."

if [ -z "${_slug}" ]; then
	if command -v python3 > "/dev/null" 2>&1; then
		_slug="$(python3 -c '
import re, sys, unicodedata
s = unicodedata.normalize("NFKD", sys.argv[1]).encode("ascii", "ignore").decode("ascii")
s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
print(s or "research-project")
' "${_name}")"
	else
		_slug="$(printf "%s" "${_name}" | tr '[:upper:]' '[:lower:]' | tr ' _' '--')"
	fi
fi

_ui_step "Inicializando pesquisa '${_name}' (${_slug})..."

_ui_sub "Substituindo marcadores declarativos..."
if command -v python3 > "/dev/null" 2>&1; then
	python3 - "${_dir}" "${_name}" "${_subtitle}" "${_slug}" "${_desc}" "${_author}" "${_advisor}" "${_year}" "${_edital}" "${_github_user}" << 'PY'
import os
import sys

root, title, subtitle, slug, desc, author, advisor, year, edital, gh_user = sys.argv[1:11]
replacements = {
    "@@RESEARCH-TITLE@@": title,
    "@@RESEARCH-SUBTITLE@@": subtitle,
    "@@RESEARCH-SLUG@@": slug,
    "@@RESEARCH-DESC@@": desc,
    "@@AUTHOR@@": author,
    "@@ADVISOR@@": advisor,
    "@@YEAR@@": year,
    "@@EDITAL@@": edital,
    "@@GITHUB-USER@@": gh_user,
}

text_exts = {
    ".md", ".tex", ".bib", ".py", ".sh", ".cpp", ".hpp", ".h", ".c",
    ".yml", ".yaml", ".json", ".txt",
}
text_names = {"Makefile", ".gitignore", "LICENSE"}

for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in (".git", "build", "dist")]
    for fname in filenames:
        if fname == "init.sh":
            continue
        _, ext = os.path.splitext(fname)
        if ext.lower() not in text_exts and fname not in text_names:
            continue
        fpath = os.path.join(dirpath, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as fp:
                content = fp.read()
        except (OSError, UnicodeDecodeError):
            continue
        updated = content
        for key, val in replacements.items():
            updated = updated.replace(key, val)
        if updated != content:
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(updated)
PY
else
	find "${_dir}" -type f \( -name "*.md" -o -name "*.tex" -o -name "*.bib" -o -name "Makefile" -o -name ".gitignore" \) -not -path "*/.git/*" | while IFS= read -r _file; do
		sed -i \
			-e "s|@@RESEARCH-TITLE@@|${_name}|g" \
			-e "s|@@RESEARCH-SUBTITLE@@|${_subtitle}|g" \
			-e "s|@@RESEARCH-SLUG@@|${_slug}|g" \
			-e "s|@@RESEARCH-DESC@@|${_desc}|g" \
			-e "s|@@AUTHOR@@|${_author}|g" \
			-e "s|@@ADVISOR@@|${_advisor}|g" \
			-e "s|@@YEAR@@|${_year}|g" \
			-e "s|@@EDITAL@@|${_edital}|g" \
			-e "s|@@GITHUB-USER@@|${_github_user}|g" \
			"${_file}"
	done
fi

_ui_sub "Inicializando e configurando Git..."
if [ ! -e "${_dir}/.git" ]; then
	git init -b main "${_dir}" > "/dev/null" 2>&1 || git init "${_dir}" > "/dev/null" 2>&1
fi
git -C "${_dir}" config core.hooksPath .githooks > "/dev/null" 2>&1 || true

_ui_sub "Aplicando permissões canônicas..."
find "${_dir}" -type f \( -name "*.md" -o -name "*.tex" -o -name "*.bib" -o -name "*.hpp" -o -name "*.cpp" -o -name "Makefile" -o -name ".gitignore" -o -name "*.png" \) -not -path "*/.git/*" -exec chmod 0644 {} + > "/dev/null" 2>&1 || true
if [ -d "${_dir}/.githooks" ]; then
	find "${_dir}/.githooks" -type f -exec chmod 0755 {} + > "/dev/null" 2>&1 || true
fi
find "${_dir}" -type f \( -name "*.sh" -o -name "*.py" \) -not -path "*/.git/*" -exec chmod 0755 {} + > "/dev/null" 2>&1 || true

_ui_ok "Pesquisa '${_name}' inicializada com sucesso!"
_ui_info "Execute 'make help' para explorar o catálogo de comandos."

if [ "${_rm}" -eq 1 ]; then
	_ui_sub "Removendo script de inicialização (--rm)..."
	rm -f "$0"
fi
