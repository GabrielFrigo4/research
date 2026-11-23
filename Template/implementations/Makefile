.POSIX:
.SILENT:

MAKEFLAGS += --no-print-directory -s

# ----------------------------------------------------------------
# Makefile: @@RESEARCH-TITLE@@ Implementations
# ----------------------------------------------------------------

CXX            = c++
CXXFLAGS       = -std=c++23 -fsyntax-only -Wall -Wextra -Wpedantic
TEST_CXXFLAGS  = -std=c++23 -O2 -Wall -Wextra -Wpedantic
TEST_BIN       = tests/smoke_test.out

.PHONY: default help all check impl test smoke-test verify format format-cpp format-md clean clear

default: help
all: check

### ================================
### HELP & DOCUMENTATION
### ================================
help:
	_e=$$'\e'; \
	cmd() { printf "    $${_e}[36mmake %-20s$${_e}[0m %s\n" "$$1" "$$2"; }; \
	sec() { printf "\n  $${_e}[1;33m%s$${_e}[0m\n" "$$1"; }; \
	printf "\n  $${_e}[1;37m@@RESEARCH-TITLE@@ — Módulo de Implementações em C++23$${_e}[0m\n"; \
	printf "  ============================================================\n"; \
	sec "Fluxos Batch & Validação:"; \
	cmd "verify"              "Executa checagem de sintaxe dos headers e testes"; \
	cmd "check"               "Verifica a sintaxe C++23 de todos os headers"; \
	cmd "impl"                "Sinônimo para check"; \
	cmd "test"                "Executa testes de problemas e suíte smoke-test"; \
	cmd "smoke-test"          "Compila e executa tests/smoke_test.cpp"; \
	sec "Qualidade & Formatação:"; \
	cmd "format"              "Formata códigos C++ (clang-format) e documentação (prettier)"; \
	sec "Limpeza:"; \
	cmd "clean"               "Remove binários compilados"; \
	echo ""

verify: check test
	printf "\n$${_e}[1;32m==> Todas as implementações foram validadas com sucesso!$${_e}[0m\n\n"

format: format-cpp format-md

format-cpp:
	find . -type f \( -name "*.hpp" -o -name "*.cpp" \) -not -path "*/.*/*" -exec clang-format -i {} +

format-md:
	if command -v prettier > "/dev/null" 2>&1; then \
		prettier --write "**/*.md" > "/dev/null" 2>&1 || true; \
	fi

check:
	for f in core/*.hpp algorithms/*.hpp; do \
		[ -f "$$f" ] || continue; \
		$(CXX) $(CXXFLAGS) "$$f" || exit 1; \
	done
	printf "%s\n" "Todos os headers compilaram perfeitamente!"

impl: check

test:
	for dir in problems/*/; do \
		case "$$dir" in *template*|*Template*) continue ;; esac; \
		if [ -f "$${dir}Makefile" ]; then \
			printf "%s\n" "-> Testando $$dir"; \
			(cd "$$dir" && $(MAKE) all > "/dev/null") || exit 1; \
		fi; \
	done
	$(MAKE) smoke-test

smoke-test:
	if [ -f tests/smoke_test.cpp ]; then \
		$(CXX) $(TEST_CXXFLAGS) tests/smoke_test.cpp -o "$(TEST_BIN)"; \
		"./$(TEST_BIN)"; \
	fi

clean:
	rm -f "$(TEST_BIN)"
	for dir in problems/*/; do \
		if [ -f "$${dir}Makefile" ]; then \
			(cd "$$dir" && $(MAKE) clean); \
		fi; \
	done

clear: clean
