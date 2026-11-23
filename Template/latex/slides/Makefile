.POSIX:
.SILENT:

MAKEFLAGS += --no-print-directory -s

# ----------------------------------------------------------------
# Makefile: @@RESEARCH-TITLE@@ — Apresentações Beamer
# ----------------------------------------------------------------

LATEXMK  = latexmk
PDFLATEX = pdflatex
BIBTEX   = bibtex

SOURCES != find . -maxdepth 1 -name "*.tex" -exec basename {} \; 2> "/dev/null" | sort || true

.PHONY: default help all clean clear distclean

default: help

### ================================
### HELP & DOCUMENTATION
### ================================
help:
	_e=$$'\e'; \
	cmd() { printf "    $${_e}[36mmake %-14s$${_e}[0m %s\n" "$$1" "$$2"; }; \
	printf "\n  $${_e}[1;37m@@RESEARCH-TITLE@@ — Apresentações Beamer$${_e}[0m\n"; \
	printf "  ============================================================\n"; \
	cmd "all"       "Compila todos os documentos .tex deste diretório"; \
	cmd "clean"     "Remove pasta build/ e arquivos temporários (.aux, .log)"; \
	cmd "distclean" "Remove temporários e PDFs gerados neste diretório"; \
	echo ""

### ================================
### COMPILATION
### ================================
all:
	if [ -z "$(SOURCES)" ]; then \
		printf "%s\n" "-> [slides] Nenhum arquivo .tex encontrado (aguardando criação de artefatos)."; \
		exit 0; \
	fi; \
	mkdir -p build; \
	for src in $(SOURCES); do \
		base="$${src%.tex}"; \
		pdf="$${base}.pdf"; \
		printf "%s" "-> Compilando slides/$${pdf}... "; \
		if command -v $(LATEXMK) > "/dev/null" 2>&1; then \
			TEXINPUTS="..:" BIBINPUTS="..:" $(LATEXMK) -pdf -silent -interaction=nonstopmode -outdir=build "$${src}" > "/dev/null" 2>&1 || true; \
		else \
			TEXINPUTS="..:" BIBINPUTS="..:" $(PDFLATEX) -interaction=batchmode -output-directory=build "$${src}" > "/dev/null" 2>&1 || true; \
			TEXINPUTS="..:" BIBINPUTS="..:" $(BIBTEX) "build/$${base}.aux" > "/dev/null" 2>&1 || true; \
			TEXINPUTS="..:" BIBINPUTS="..:" $(PDFLATEX) -interaction=batchmode -output-directory=build "$${src}" > "/dev/null" 2>&1 || true; \
			TEXINPUTS="..:" BIBINPUTS="..:" $(PDFLATEX) -interaction=batchmode -output-directory=build "$${src}" > "/dev/null" 2>&1 || true; \
		fi; \
		if [ ! -f "build/$${pdf}" ]; then \
			printf "%s\n" "[FAIL]"; \
			grep -A 4 -B 1 '^!' "build/$${base}.log" >&2 || tail -n 25 "build/$${base}.log" >&2 || true; \
			exit 1; \
		fi; \
		cp "build/$${pdf}" "$${pdf}"; \
		printf "%s\n" "[OK]"; \
	done

### ================================
### CLEANUP
### ================================
clean:
	rm -rf build
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.nav *.snm *.vrb *.synctex.gz *.fls *.fdb_latexmk

clear: clean

distclean: clean
	rm -f *.pdf
	if command -v $(LATEXMK) > "/dev/null" 2>&1; then $(LATEXMK) -C > "/dev/null" 2>&1 || true; fi
