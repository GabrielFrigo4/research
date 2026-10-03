.POSIX:
.SILENT:

MAKEFLAGS += --no-print-directory -s

# ----------------------------------------------------------------
# Makefile: Research Hub Orchestrator
# ----------------------------------------------------------------

.PHONY: help clone pull status test audit format prettier hooks ci main

REPOS = "Network Flow"

### ================================
### HELP & DOCUMENTATION
### ================================
help:
	_e=$$'\e'; \
	cmd() { printf "    $${_e}[36mmake %-20s$${_e}[0m %s\n" "$$1" "$$2"; }; \
	sec() { printf "\n  $${_e}[1;33m%s$${_e}[0m\n" "$$1"; }; \
	printf "\n  $${_e}[1;37mResearch Hub — Orquestrador de Pesquisa Científica$${_e}[0m\n"; \
	printf "  =======================================================\n"; \
	sec "Sincronização & Submódulos:"; \
	cmd "clone"          "Inicializa e atualiza submódulos de pesquisa recursivamente"; \
	cmd "main"           "Alterna todos os submódulos clonados para a branch main"; \
	cmd "pull"           "Atualiza submódulos com seus remotos no GitHub"; \
	sec "Diagnóstico & Status:"; \
	cmd "status"         "Exibe status Git do ecossistema de pesquisa"; \
	cmd "hooks"          "Configura e aplica permissões canônicas em .githooks"; \
	sec "Qualidade & Testes:"; \
	cmd "test"           "Valida integridade e scripts locais"; \
	cmd "format"         "Formata documentações Markdown com Prettier"; \
	cmd "prettier"       "Formata documentações Markdown com Prettier"; \
	cmd "ci"             "Executa pipeline local de validação"; \
	echo ""

### ================================
### SUBMODULES ORCHESTRATION
### ================================
clone:
	echo "📦 Inicializando submódulos do Research..."
	git submodule update --init --recursive
	echo "✅ Submódulos inicializados com sucesso!\n"
	$(MAKE) main

main:
	echo "🌿 Alternando submódulos para a branch main..."
	for r in $(REPOS); do \
		if [ -e "$$r/.git" ]; then \
			echo "  🌿 $$r -> main"; \
			git -C "$$r" checkout main 2> "/dev/null" || git -C "$$r" switch main 2> "/dev/null" || echo "  ⚠️  $$r: falha ao alternar para main."; \
		else \
			echo "  ⏭️  $$r: não clonado, pulando."; \
		fi; \
	done
	echo "✅ Submódulos ativos configurados na branch main!\n"

pull: main
	echo "🔄 Sincronizando submódulos de pesquisa..."
	git submodule update --remote --merge
	echo "✅ Submódulos sincronizados!"

status:
	echo "📊 Status dos Submódulos do Research:"
	git submodule status

### ================================
### QUALITY GATES & AUDIT
### ================================
hooks:
	chmod 0755 .githooks/* 2> "/dev/null" || true
	git config core.hooksPath .githooks
	echo "✅ Hooks configurados com sucesso em .githooks!"

test:
	echo "🧪 Validando integridade e scripts de automação..."
	find . -name "*.sh" -not -path "*/.git/*" -exec sh -n {} +
	echo "✅ Validação concluída!"

format:
	if command -v prettier > "/dev/null" 2>&1; then \
		prettier --write "*.md"; \
		echo "✅ Documentação formatada com Prettier!"; \
	fi

prettier: format

ci: test status
	echo "✅ Pipeline local aprovada!"
