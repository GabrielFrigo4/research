.POSIX:
.SILENT:

MAKEFLAGS += --no-print-directory -s

# ----------------------------------------------------------------
# Makefile: @@RESEARCH-TITLE@@ Applications
# ----------------------------------------------------------------

SUBDIRS != find . -mindepth 2 -maxdepth 2 -name "Makefile" -exec dirname {} \; 2> "/dev/null" | sort || true

.PHONY: default help all build apps verify test format format-cpp format-md clean clear

default: help
all: build

### ================================
### HELP & DOCUMENTATION
### ================================
help:
	_e=$$'\e'; \
	cmd() { printf "    $${_e}[36mmake %-20s$${_e}[0m %s\n" "$$1" "$$2"; }; \
	printf "\n  $${_e}[1;37m@@RESEARCH-TITLE@@ — Módulo de Aplicações Práticas$${_e}[0m\n"; \
	printf "  ============================================================\n"; \
	cmd "build"  "Compila todas as aplicações em applications/"; \
	cmd "test"   "Executa os testes das aplicações"; \
	cmd "verify" "Compila e testa todas as aplicações"; \
	cmd "clean"  "Limpa artefatos de build nas subpastas"; \
	echo ""

verify: build test

build:
	if [ -z "$(SUBDIRS)" ]; then \
		printf "%s\n" "-> [applications] Nenhuma aplicação registrada ainda."; \
		exit 0; \
	fi; \
	for dir in $(SUBDIRS); do \
		(cd "$$dir" && $(MAKE) all); \
	done

apps: build

format: format-cpp format-md

format-cpp:
	for dir in $(SUBDIRS); do \
		(cd "$$dir" && $(MAKE) format); \
	done

format-md:
	if command -v prettier > "/dev/null" 2>&1; then \
		prettier --write "**/*.md" > "/dev/null" 2>&1 || true; \
	fi

test:
	if [ -z "$(SUBDIRS)" ]; then \
		printf "%s\n" "-> [applications] Nenhum teste de aplicação registrado ainda."; \
		exit 0; \
	fi; \
	for dir in $(SUBDIRS); do \
		(cd "$$dir" && $(MAKE) test); \
	done

clean:
	for dir in $(SUBDIRS); do \
		(cd "$$dir" && $(MAKE) clean); \
	done

clear: clean
