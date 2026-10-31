# 🔬 Research — AI Agent Briefing

> Este é o **repositório hub** de **Research** de Gabriel Frigo. Ele orquestra os projetos de pesquisa científica, publicações acadêmicas em LaTeX e implementações de ponta em Otimização Combinatória e Teoria dos Grafos.

---

## 🧭 Identidade e Papel

O **Research** é o ponto de entrada para a produção científica institucional (UFABC / PIBIC) e monográfica independente:

| Componente                            | Papel                                                                                                                                                                 | Repositório Remoto               |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| **[`Network Flow`](Network%20Flow/)** | Iniciação Científica em Problemas de Fluxos em Redes (Fluxo Máximo e Fluxo de Custo Mínimo), implementações C++23, benchmarks DIMACS e monografia/relatórios em LaTeX | `GabrielFrigo4/IC_Networks_Flow` |

---

## 📦 Os Repositórios Federados

```text
Research/
├── .agents/                   # Governança e runbooks locais de IA
├── .githooks/                 # Quality gates de pre-commit e commit-msg
├── .github/                   # Workflows de CI
├── Network Flow/              # Iniciação Científica (C++23, DIMACS, LaTeX)
├── AGENTS.md                  # Este briefing de engenharia
├── LICENSE                    # Licença MIT
├── Makefile                   # Orquestrador POSIX silencioso
├── PRINCIPLES.md              # 22 Princípios de Engenharia aplicados
├── README.md                  # Apresentação executiva do Research Hub
└── TODO.md                    # Matriz de status operacional e roadmap
```

---

## ⚠️ Regras Críticas para Agentes de IA

1. **A Regra de Ouro:** Ao modificar artefatos de pesquisa em `Network Flow`, consulte `AGENTS.md` e `PRINCIPLES.md` daquele diretório.
2. **Rigor Científico:** Códigos de benchmark e modelos teóricos devem preservar reprodutibilidade estrita.
3. **Hermetismo de Produção (`rm -rf .agents`):** A compilação dos documentos LaTeX (`book.pdf`, `ic.pdf`) e códigos C++23 deve ser 100% independente de arquivos de IA.
4. **Makefile como Orquestrador:** Use a raiz para gerenciar status e sincronização do hub.
5. **Zero-Tweaks Invariant:** O repositório deve compilar seus artefatos imediatamente após `git clone --recursive`.

---

## 🛡️ Regra da Proatividade e Correção Contínua (Boy Scout Rule)

O agente de IA atua de forma proativa na manutenção e aplicação dos padrões canônicos deste repositório.

Ao identificar linhas ou artefatos fora dos padrões estabelecidos:

1. **Notificar concisamente** o usuário sobre o ajuste realizado.
2. **Corrigir a inconformidade**, aplicando o padrão correspondente:
    - **Comentários Narrativos:** Eliminar comentários óbvios que apenas narram código executável.
    - **Banners Estruturais:** Ajustar réguas para exatamente 64 hífens no topo ou 32 caracteres com `### ` no corpo.
    - **Portabilidade POSIX:** Substituir bashismos (`[[ ]]`, `&>`, arrays, `source`) por sintaxe estrita POSIX `/bin/sh`.
    - **Shebang Universal:** Garantir sempre `#!/usr/bin/env sh` ou `#!/usr/bin/env python3`.
    - **Sequências ANSI & Escapes:** Não use octais (`\033`, `\001`) para caracteres ou escapes. Use `[ -t 1 ] && echo -n $\x27\e...\x27` ou notação hexadecimal (`\x01`, `\x1b`). Octal é exclusivo para permissões POSIX (`chmod 0755`, `chmod 0644`, `umask`).
    - **Redirecionamento Seguro:** Envolver destinos em aspas duplas (ex: `> "/dev/null" 2>&1`).
    - **Makefiles:** Assegurar cabeçalho `.POSIX: .SILENT:`, `MAKEFLAGS += --no-print-directory -s`, alinhamento estético de variáveis e zero `@` redundante.
    - **Permissões Canônicas:** Aplicar 4 dígitos octais (`chmod 0755`, `chmod 0644`, `chmod 0700`, `chmod 0600`).
    - **Invariante Out-of-the-Box:** Garantir modos octais corretos no Git Index e auto-cura em tempo de execução sem requerer intervenção manual pós-clone.
    - **Emissão Semântica de UI:** Substituir `echo` avulsos com emojis pelas rotinas canônicas `_ui_*`.
    - **Antifragilidade & Resiliência:** Resolução ativa de caminhos em cascata, auto-cura de permissões (0600 em chaves/segredos) e validação defensiva de pré-requisitos.
    - **Curadoria Cognitiva:** Capturar decisões estruturais e regras tácitas em skills locais compactas (`.agents/skills/`), mantendo-as atualizadas e expurgando ruído obsoleto.
    - **Refatoração Sem Legado:** Expurgar aliases obsoletos, variáveis mortas e shims de compatibilidade em renomeações.
    - **Elevação Antifrágil & Shift Seguro:** Usar o bloco explícito `if [ "$(id -u)" -ne 0 ]` para resolução de `ELEVATE` (evitando término fatal sob `set -e` como root) e proteger todo comando `shift` com validação prévia de parâmetros (`[ "$#" -ge N ] && shift N`).
    - **Simetria de Documentação:** Mover regras ou invariantes universais documentadas erroneamente em sub-membros específicos para o documento de arquitetura do grupo correspondente, eliminando falsas assimetrias.

---

## 🚀 Comandos de Verificação Rápida (Quality Gates)

| Comando            | Finalidade Operacional                                      |
| :----------------- | :---------------------------------------------------------- |
| `make help`        | Exibe o catálogo completo de tarefas operacionais           |
| `make status`      | Inspeciona o estado Git dos submódulos de pesquisa          |
| `make pull`        | Sincroniza submódulos de pesquisa com o remoto              |
| `make test`        | Valida integridade geral e conformidade nos submódulos      |
| `make audit`       | Executa rotinas de auditoria nos componentes                |
| `make format`      | Aplica formatação automática em arquivos suportados         |
| `make prettier`    | Formata arquivos Markdown e JSON com Prettier               |
| `make lint-format` | Valida conformidade de formatação sem modificar arquivos    |
| `make hooks`       | Configura permissões e ganchos Git em todos os repositórios |
| `make ci`          | Executa pipeline local completa de validação integrada      |

---

## 📖 Referências Obrigatórias

Antes de qualquer modificação neste ecossistema, consulte:

- [README.md](README.md) — Apresentação executiva do Research Hub
- [PRINCIPLES.md](PRINCIPLES.md) — 22 Princípios de Engenharia aplicados
- [TODO.md](TODO.md) — Matriz de status operacional e roadmap
- [LICENSE](LICENSE) — Licença MIT do projeto
