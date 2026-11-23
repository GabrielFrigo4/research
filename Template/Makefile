.POSIX:
.SILENT:

MAKEFLAGS += --no-print-directory -s

# ----------------------------------------------------------------
# Makefile: @@RESEARCH-TITLE@@ Research Suite
# ----------------------------------------------------------------

PYTHON   = python3

REPEATS ?= 2
TIMEOUT ?= 16
WORKERS ?= 1

.PHONY: help all \
        bench-all bench-pipeline bench-latex bench-publish bench-research sync-all check-all \
        latex build-latex release-map reports book report ic monolith proposal poster \
        editorial cards minibooks notebooks slides \
        apps impl exp generate \
        bench bench-ic bench-book bench-smoke bench-tables bench-plots bench-artifacts \
        format clang-format prettier format-cpp format-md test setup clean clear distclean clean-results sync-code

all: help

### ================================
### HELP & DOCUMENTATION
### ================================
help:
	_e=$$'\e'; \
	cmd() { printf "    $${_e}[36mmake %-22s$${_e}[0m %s\n" "$$1" "$$2"; }; \
	sec() { printf "\n  $${_e}[1;33m%s$${_e}[0m\n" "$$1"; }; \
	printf "\n  $${_e}[1;37m@@RESEARCH-TITLE@@ — Suíte de Pesquisa & Implementações$${_e}[0m\n"; \
	printf "  ============================================================\n"; \
	sec "Pipelines de Benchmark & Publicação:"; \
	cmd "bench-publish"    "Benchmark + gera artefatos + compila relatórios (PDFs)"; \
	cmd "bench-research"   "Pipeline completo: gera instâncias + benchmark + suíte LaTeX"; \
	cmd "bench-all"        "Benchmark completo + sincronização de tabelas/gráficos"; \
	cmd "sync-all"         "Sincroniza algoritmos C++, gera artefatos e reconstrói o monólito"; \
	cmd "check-all"        "Valida headers C++23, compilação de drivers, testes e sync"; \
	sec "Compilação de Relatórios & Livro:"; \
	cmd "reports"          "Compila os relatórios da IC (ic.pdf, report.pdf, monolith.pdf, poster.pdf)"; \
	cmd "latex"            "Compila os 6 documentos principais da suíte LaTeX"; \
	cmd "book"             "Compila exclusivamente a monografia do livro (book.pdf)"; \
	cmd "report"           "Compila o relatório formal institucional UFABC (report.pdf)"; \
	cmd "ic"               "Compila o texto da IC com leitura limpa (ic.pdf)"; \
	cmd "monolith"         "Gera e compila o monólito autocontido para Overleaf (monolith.pdf)"; \
	cmd "proposal"         "Compila a proposta do projeto de pesquisa (proposal.pdf)"; \
	cmd "poster"           "Compila o pôster do Simpósio de IC da UFABC (poster.pdf)"; \
	sec "Artefatos Editoriais Vivos:"; \
	cmd "editorial"        "Compila todas as famílias editoriais (cards, minibooks, notebooks, slides)"; \
	cmd "cards"            "Compila os cards de referência rápida (latex/cards)"; \
	cmd "minibooks"        "Compila os mini-books monotemáticos (latex/minibooks)"; \
	cmd "notebooks"        "Compila os cadernos ICPC e Maratona (latex/notebooks)"; \
	cmd "slides"           "Compila as apresentações Beamer (latex/slides)"; \
	sec "Módulos de Código & Experimentos:"; \
	cmd "impl"             "Valida a sintaxe C++23 de todos os headers de algoritmos"; \
	cmd "apps"             "Compila e executa as aplicações práticas em applications/"; \
	cmd "exp"              "Compila os drivers executáveis de benchmark"; \
	cmd "generate"         "Gera instâncias sintéticas de teste"; \
	cmd "bench"            "Executa todos os benchmarks (IC e Livro)"; \
	cmd "bench-ic"         "Executa e gera exclusivamente os benchmarks da IC (latex/tables)"; \
	cmd "bench-book"       "Executa e gera os benchmarks do Livro (latex/book/tables)"; \
	cmd "bench-smoke"      "Smoke-test rápido de benchmark"; \
	cmd "bench-artifacts"  "Gera tabelas finais e gráficos para LaTeX"; \
	sec "Qualidade, Formatação & Git:"; \
	cmd "test"             "Executa a suíte de testes de algoritmos e aplicações"; \
	cmd "format"           "Formata códigos C++ (clang-format) e documentação (prettier)"; \
	cmd "clang-format"     "Formata exclusivamente códigos C++ (.hpp/.cpp)"; \
	cmd "prettier"         "Formata exclusivamente arquivos Markdown (.md)"; \
	cmd "sync-code"        "Sincroniza implementações C++ com o LaTeX e monólito"; \
	cmd "setup"            "Configura os githooks locais e permissões canônicas"; \
	sec "Limpeza:"; \
	cmd "clean"            "Limpa artefatos de compilação em todos os submódulos"; \
	cmd "distclean"        "Expurga tudo incluindo instâncias geradas"; \
	cmd "clean-results"    "Remove resultados de medições, tabelas e gráficos gerados"; \
	echo ""

### ================================
### BATCH & WORKFLOW COMMANDS
### ================================
bench-all: generate exp bench-pipeline

bench-pipeline: generate exp
	(cd "experiments" && $(MAKE) WORKERS=$(WORKERS) REPEATS=$(REPEATS) TIMEOUT=$(TIMEOUT) run)
	(cd "experiments" && $(MAKE) tables)
	(cd "experiments" && $(MAKE) plots)
	$(PYTHON) .scripts/build_monolith.py

bench-publish: exp bench-all reports

bench-research: exp bench-all latex

bench-latex: exp bench-pipeline latex

sync-all: sync-code bench-artifacts
	$(PYTHON) .scripts/build_monolith.py

check-all: impl exp test
	$(PYTHON) .scripts/sync_listings.py --check
	$(PYTHON) .scripts/build_monolith.py --check

### ================================
### FORMATTING & PRETTIER
### ================================
format: format-cpp format-md

clang-format: format-cpp
prettier: format-md

format-cpp:
	find . -type f \( -name "*.hpp" -o -name "*.cpp" -o -name "*.h" -o -name "*.c" \) -not -path "*/.*/*" -exec clang-format -i {} +

format-md:
	if command -v prettier > "/dev/null" 2>&1; then \
		prettier --write "**/*.{md,json,jsonc,yml,yaml,html,css}" --ignore-path .gitignore > "/dev/null" 2>&1 || true; \
	elif command -v npx > "/dev/null" 2>&1; then \
		npx --yes prettier --write "**/*.{md,json,jsonc,yml,yaml,html,css}" --ignore-path .gitignore > "/dev/null" 2>&1 || true; \
	fi

### ================================
### REPO CONFIGURATION & HOOKS
### ================================
setup:
	git config core.hooksPath .githooks
	chmod 0755 .githooks/*

### ================================
### LATEX SUITE
### ================================
latex:
	(cd "latex" && $(MAKE) all)

build-latex: sync-code latex
	mkdir -p dist
	cp latex/*.pdf dist/

release-map:
	printf "latex/book.tex\tbook.pdf\n"
	printf "latex/ic.tex\tic.pdf\n"
	printf "latex/monolith.tex\tmonolith.pdf\n"
	printf "latex/poster.tex\tposter.pdf\n"
	printf "latex/proposal.tex\tproposal.pdf\n"
	printf "latex/report.tex\treport.pdf\n"

reports:
	(cd "latex" && $(MAKE) reports)

book:
	(cd "latex" && $(MAKE) book)

report:
	(cd "latex" && $(MAKE) report)

ic:
	(cd "latex" && $(MAKE) ic)

monolith:
	(cd "latex" && $(MAKE) monolith)

proposal:
	(cd "latex" && $(MAKE) proposal)

poster:
	(cd "latex" && $(MAKE) poster)

editorial:
	(cd "latex" && $(MAKE) editorial)

cards:
	(cd "latex" && $(MAKE) cards)

minibooks:
	(cd "latex" && $(MAKE) minibooks)

notebooks:
	(cd "latex" && $(MAKE) notebooks)

slides:
	(cd "latex" && $(MAKE) slides)

sync-code:
	$(PYTHON) .scripts/sync_listings.py
	$(PYTHON) .scripts/build_monolith.py

### ================================
### IMPLEMENTATIONS & BENCHMARKS
### ================================
apps:
	(cd "applications" && $(MAKE) build)

impl:
	(cd "implementations" && $(MAKE) check)

exp:
	(cd "experiments" && $(MAKE) drivers)

generate:
	(cd "experiments" && $(MAKE) generate)

bench: exp
	(cd "experiments" && $(MAKE) WORKERS=$(WORKERS) REPEATS=$(REPEATS) TIMEOUT=$(TIMEOUT) run)

bench-ic: exp
	(cd "experiments" && $(MAKE) WORKERS=$(WORKERS) REPEATS=$(REPEATS) TIMEOUT=$(TIMEOUT) ic)

bench-book: exp
	(cd "experiments" && $(MAKE) WORKERS=$(WORKERS) REPEATS=$(REPEATS) TIMEOUT=$(TIMEOUT) book)

bench-smoke: exp
	(cd "experiments" && $(MAKE) bench-smoke)

bench-tables:
	(cd "experiments" && $(MAKE) tables)

bench-plots:
	(cd "experiments" && $(MAKE) plots)

bench-artifacts: bench-tables bench-plots

test:
	(cd "implementations" && $(MAKE) test)
	(cd "applications" && $(MAKE) test)

### ================================
### CLEANING
### ================================
clean:
	(cd "latex" && $(MAKE) distclean)
	(cd "applications" && $(MAKE) clean)
	(cd "implementations" && $(MAKE) clean)
	(cd "experiments" && $(MAKE) clean)
	rm -rf .venv bin/ build/ dist/ .tmp/ *.log
	find . -type d -name "__pycache__" -exec rm -rf {} + 2> "/dev/null" || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2> "/dev/null" || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2> "/dev/null" || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2> "/dev/null" || true

clear: clean

distclean: clean
	(cd "experiments" && $(MAKE) distclean)

clean-results:
	(cd "experiments" && $(MAKE) clean-results)
