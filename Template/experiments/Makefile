.POSIX:
.SILENT:

MAKEFLAGS += --no-print-directory -s

# ----------------------------------------------------------------
# Makefile: @@RESEARCH-TITLE@@ Experiments
# ----------------------------------------------------------------

CXX         = c++
STACK_FLAG != case "$$(uname -s 2> "/dev/null")" in *Windows*|*MINGW*|*MSYS*|*CYGWIN*) echo "-Wl,--stack,268435456" ;; *) echo "-Wl,-z,stack-size=268435456" ;; esac
CXXFLAGS    = $(STACK_FLAG) -std=c++23 -O2 -Wall -Wextra -Wpedantic

PYTHON      = python3
REPEATS    ?= 2
TIMEOUT    ?= 16
WORKERS    ?= 1
RUN_OPTS    = --repeats "$(REPEATS)" --timeout "$(TIMEOUT)" --workers "$(WORKERS)"

EXE_EXT    != case "$$(uname -s 2> "/dev/null")" in *Windows*|*MINGW*|*MSYS*|*CYGWIN*) echo ".exe" ;; *) echo "" ;; esac
RUNNER_BIN  = ./runner$(EXE_EXT)
RUNNER_SRC  = drivers/runner.cpp

INST_DIR    = instances/generated
RES_DIR     = results

.PHONY: help all ic book build drivers instances generate run run-ic run-book tables plots sync-csv clean distclean clean-results bench-smoke

default: help
all: ic book

### ================================
### HELP & DOCUMENTATION
### ================================
help:
	_e=$$'\e'; \
	cmd() { printf "    $${_e}[36mmake %-18s$${_e}[0m %s\n" "$$1" "$$2"; }; \
	printf "\n  $${_e}[1;37m@@RESEARCH-TITLE@@ — Experimentos & Benchmarks$${_e}[0m\n"; \
	printf "  ============================================================\n"; \
	cmd "drivers"      "Compila os drivers C++23 de medição"; \
	cmd "generate"     "Gera instâncias sintéticas em instances/"; \
	cmd "ic"           "Executa suíte da IC e gera artefatos em latex/tables/"; \
	cmd "book"         "Executa suíte do Livro e gera artefatos em latex/book/tables/"; \
	cmd "bench-smoke"  "Executa teste rápido de fumaça no driver"; \
	cmd "clean"        "Remove binários, instâncias geradas e resultados"; \
	echo ""

ic: build instances run-ic tables plots

book: build instances run-book tables plots

bench-smoke: build
	$(RUNNER_BIN) 10000

drivers: build

build: $(RUNNER_BIN)

$(RUNNER_BIN): $(RUNNER_SRC)
	$(CXX) $(CXXFLAGS) "$(RUNNER_SRC)" -o "$(RUNNER_BIN)"

instances: generate

generate:
	mkdir -p "$(INST_DIR)"
	$(PYTHON) generators/random_instance.py --out-dir "$(INST_DIR)" --seed 42 --count 5

sync-csv:
	true

run: run-ic run-book

run-ic: build instances
	mkdir -p "$(RES_DIR)/ic"
	$(PYTHON) .scripts/run_benchmarks.py --suite ic --bin "$(RUNNER_BIN)" --instances-dir "$(INST_DIR)" --out-dir "$(RES_DIR)/ic" $(RUN_OPTS)

run-book: build instances
	mkdir -p "$(RES_DIR)/book"
	$(PYTHON) .scripts/run_benchmarks.py --suite book --bin "$(RUNNER_BIN)" --instances-dir "$(INST_DIR)" --out-dir "$(RES_DIR)/book" $(RUN_OPTS)

tables:
	$(PYTHON) .scripts/generate_tables.py --suite all

plots:
	$(PYTHON) .scripts/plot_charts.py --suite all

clean:
	rm -f "$(RUNNER_BIN)" "$(RUNNER_BIN).exe"
	rm -rf "$(INST_DIR)" "$(RES_DIR)" .venv
	find . -type d -name "__pycache__" -exec rm -rf {} + 2> "/dev/null" || true

distclean: clean

clean-results:
	rm -rf "$(RES_DIR)"
