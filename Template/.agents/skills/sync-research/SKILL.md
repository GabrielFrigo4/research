---
name: sync-research
description: Runbook cognitivo para compilação, testes algorítmicos, sincronização de apêndices LaTeX e rigor terminológico no projeto @@RESEARCH-TITLE@@.
---

# 🔄 Sync Research Skill — @@RESEARCH-TITLE@@

Este runbook orienta o agente na validação de implementações C++, execução de testes, sincronização de código com apêndices LaTeX e manutenção do rigor terminológico da pesquisa **@@RESEARCH-TITLE@@**.

---

## ⚙️ Fluxo Canônico de Build e Sincronização

Execute os alvos do `Makefile` na raiz do repositório na ordem operacional abaixo:

```sh
make impl
make test
make sync-code
make book
make clean
```

- **`make impl`:** Valida a sintaxe C++23 de todos os headers em `implementations/`.
- **`make test`:** Executa as suítes de testes de algoritmos e aplicações.
- **`make sync-code`:** Sincroniza implementações C++ com as listagens LaTeX (`.scripts/sync_listings.py`) e reconstrói o monólito (`.scripts/build_monolith.py`).
- **`make book`:** Compila exclusivamente a monografia (`book.pdf`).
- **`make clean`:** Remove artefatos temporários de compilação em todos os submódulos.

---

## ✍️ Diretrizes Editoriais & Rigor Terminológico

Para regras gerais de redação científica (No-Fluff, Math-First, Teste do Leitor Não-Nativo, build isolado e sincronização de listagens), siga a skill global `latex-typesetting`. No projeto **@@RESEARCH-TITLE@@**, aplique as distinções estruturais abaixo:

### 1. Escopo por Documento LaTeX

- **IC / Relatórios Institucionais (`latex/sections/`, `latex/ic.tex`, `latex/report.tex`, `latex/monolith.tex`, `latex/proposal.tex`, `latex/poster.tex`):** Escopo institucional da Iniciação Científica (UFABC), sujeito a limites rígidos de páginas/layout; uma vez entregue, permanece **congelado**, recebendo apenas sincronização automática de correções de código nos motores originais via `make sync-code`.
- **Livro / Monografia (`latex/book/chapters/`, `latex/book.tex`, `latex/book/`) e Famílias Vivas (`cards/`, `minibooks/`, `notebooks/`, `slides/`):** Evolução contínua sem limite de páginas; permite demonstrações completas, intuições bem fundamentadas e exemplos passo a passo mantendo sobriedade acadêmica.

### 2. Precisão Terminológica Matemática

Termos com definição formal rigorosa NUNCA devem ser usados como sinônimos casuais ou adornos estilísticos (_isomórfico_, _topologia_, _canônico_, _geométrico_, _convergência_).

## Numeração dos Apêndices de Código

Em `latex/appendices/`, a dezena do prefixo segue as Partes do Livro: `00` arquitetura, `1x` Parte I, `2x` Parte II, `3x` Parte III, `4x` Parte IV, `5x` Parte V e `99` repositório. Registre cada novo apêndice em `.scripts/sync_listings.py` e inclua-o em `book.tex` em ordem crescente.
