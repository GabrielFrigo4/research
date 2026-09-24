# 🔬 Research — AI Agent Briefing

> Este é o **repositório hub** de **Research** de Gabriel Frigo. Ele orquestra os projetos de pesquisa científica, publicações acadêmicas em LaTeX e implementações de ponta em Otimização Combinatória e Teoria dos Grafos.

---

## 🧭 1. Identidade e Papel

O **Research** é o ponto de entrada para a produção científica (UFABC / PIBIC):

| Componente                            | Papel                                                                                                                                                                 | Repositório Remoto               |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| **[`Network Flow`](Network%20Flow/)** | Iniciação Científica em Problemas de Fluxos em Redes (Fluxo Máximo e Fluxo de Custo Mínimo), implementações C++23, benchmarks DIMACS e monografia/relatórios em LaTeX | `GabrielFrigo4/IC_Networks_Flow` |

---

## ⚠️ 2. Regras Críticas para Agentes de IA

1. **A Regra de Ouro:** Ao modificar artefatos de pesquisa em `Network Flow`, consulte `AGENTS.md` e `PRINCIPLES.md` daquele diretório.
2. **Rigor Científico:** Códigos de benchmark e modelos teóricos devem preservar reprodutibilidade estrita.
3. **Hermetismo de Produção (`rm -rf .agents`):** A compilação dos documentos LaTeX (`book.pdf`, `ic.pdf`) e códigos C++23 deve ser 100% independente de arquivos de IA.
4. **Makefile como Orquestrador:** Use a raiz para gerenciar status e sincronização do hub.
5. **Zero-Tweaks Invariant:** O repositório deve compilar seus artefatos imediatamente após `git clone --recursive`.

---

## 🌲 3. Estrutura do Repositório

```
Research/
├── .agents/                   # Governança e runbooks locais de IA
├── .githooks/                 # Quality gates de pre-commit e commit-msg
├── .github/                   # Workflows de CI
├── Network Flow/              # Iniciação Científica (C++23, DIMACS, LaTeX)
├── AGENTS.md                  # Este briefing de engenharia
├── LICENSE                    # Licença MIT
├── Makefile                   # Orquestrador POSIX silencioso
├── PRINCIPLES.md              # 18 Princípios de Engenharia aplicados
└── README.md                  # Apresentação executiva do Research Hub
```

---

## ⚡ 4. Comandos de Verificação Rápida

| Comando       | Finalidade                                         |
| :------------ | :------------------------------------------------- |
| `make help`   | Exibe o catálogo completo de tarefas operacionais  |
| `make status` | Inspeciona o estado Git dos submódulos de pesquisa |
| `make pull`   | Sincroniza submódulos de pesquisa com o remoto     |
| `make test`   | Valida integridade geral e conformidade            |
