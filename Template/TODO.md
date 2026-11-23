# 📋 TO-DO Geral: @@RESEARCH-TITLE@@

Documento de acompanhamento da pesquisa **@@RESEARCH-TITLE@@**, integrando fundamentação teórica, implementação em C++23, validação experimental e editoração científica em LaTeX.

> [!IMPORTANT]
> **Ciclo de Vida do Repositório:**
>
> - 🟡 **Iniciação Científica UFABC (`proposal.tex`, `report.tex`, `ic.tex`, `monolith.tex`, `poster.tex`, `latex/sections/`, `latex/tables/`, `latex/figures/`):** Quando concluída e entregue, congelar no escopo original (mantendo apenas `make sync-code` para eventuais correções nos códigos originais da IC).
> - 🟢 **Livro Monográfico (`latex/book.tex`), Famílias Editoriais Vivas (`cards/`, `minibooks/`, `notebooks/`, `slides/`), Biblioteca C++23 e Benchmarks Pós-IC (`make bench-book`):** Evolução contínua.

---

## 🧭 Sumário de Navegação

- [📖 Bloco I: Roadmap Ativo do Livro (book.tex) & Expansões](#-bloco-i-roadmap-ativo-do-livro-booktex--expansões)
- [⚡ Bloco II: Motores Algorítmicos em C++23](#-bloco-ii-motores-algorítmicos-em-c23)
- [🎯 Bloco III: Modelagem, Reduções e Problemas](#-bloco-iii-modelagem-reduções-e-problemas)
- [📚 Bloco IV: Teoria e Rigor Matemático](#-bloco-iv-teoria-e-rigor-matemático)
- [📊 Bloco V: Validação Experimental e Histórico Institucional](#-bloco-v-validação-experimental-e-histórico-institucional)

---

# 📖 Bloco I: Roadmap Ativo do Livro (`book.tex`) & Expansões

## 📚 Arquitetura Editorial do Livro (`book.tex`)

| Parte / Eixo Editorial                                         | Capítulos                                 | Status |
| :------------------------------------------------------------- | :---------------------------------------- | :----: |
| **Parte I:** Fundamentos Matemáticos e Algoritmos Base         | `01_fundamentals.tex`                     |   ✅   |
| **Parte II:** Teoria Estrutural e Garantias Combinatórias      | `02_structural_theory.tex`                |   ✅   |
| **Parte III:** Métodos Avançados e Otimização                  | `03_advanced_methods.tex`                 |   ✅   |
| **Parte IV:** Modelagem, Reduções e Aplicações Práticas        | `04_modeling_applications.tex`            |   ✅   |
| **Parte V:** Validação Experimental e Engenharia de Desempenho | `05_benchmarks.tex` + Apêndices `00`–`99` |   ✅   |

## 🧭 Roadmap Editorial e Estrutural do Livro

- [x] Estrutura inicial em 5 Partes, capa editorial e apêndices sincronizados via `make sync-code`.
- [ ] Expandir os capítulos teóricos com definições formais, teoremas, demonstrações e diagramas TikZ.
- [ ] Adicionar formalização de modelagens genéricas e aplicações práticas na Parte IV.

## 🎨 Novos Artefatos Editoriais Vivos (Pós-IC)

| Família Editorial              | Pasta                                    | Estrutura & Makefile | Artefatos `.tex` | Escopo                                                           |
| :----------------------------- | :--------------------------------------- | :------------------: | :--------------: | :--------------------------------------------------------------- |
| **Cards de Referência Rápida** | [`latex/cards/`](./latex/cards/)         |          ✅          |   ⏳ Planejado   | Cheat sheets de 1 página com teoremas, complexidades e receitas. |
| **Mini-Books Monotemáticos**   | [`latex/minibooks/`](./latex/minibooks/) |          ✅          |   ⏳ Planejado   | Volumes curtos (15–30 páginas) dedicados a temas isolados.       |
| **Cadernos ICPC e Maratona**   | [`latex/notebooks/`](./latex/notebooks/) |          ✅          |   ⏳ Planejado   | Cadernos competitivos de 2 colunas com templates C++23 enxutos.  |
| **Apresentações Beamer**       | [`latex/slides/`](./latex/slides/)       |          ✅          |   ⏳ Planejado   | Decks de slides reaproveitando diagramas de `latex/diagrams/`.   |

---

# ⚡ Bloco II: Motores Algorítmicos em C++23

| Nome                                                                  | LaTeX | Implementação | Descrição                                                    |
| :-------------------------------------------------------------------- | :---: | :-----------: | :----------------------------------------------------------- |
| [`AlgorithmBase`](./implementations/core/AlgorithmBase.hpp)           |  ✅   |      ✅       | Interface abstrata polimórfica com `make` e `clone`.         |
| [`SampleAlgorithm`](./implementations/algorithms/SampleAlgorithm.hpp) |  ✅   |      ✅       | Implementação de referência inicial validada em `make test`. |

---

# 🎯 Bloco III: Modelagem, Reduções e Problemas

| Técnica / Problema                            | LaTeX (Livro) | Código Local | Status       |
| :-------------------------------------------- | :-----------: | :----------: | :----------- |
| Template de Resolução em Juízes (`template/`) |      ⏳       |      ✅      | ⏳ Em Aberto |

---

# 📚 Bloco IV: Teoria e Rigor Matemático

| Teorema / Definição      | LaTeX | Prova Formal | Observações                                |
| :----------------------- | :---: | :----------: | :----------------------------------------- |
| Definições Base (Cap. 1) |  ✅   |      ⏳      | Estrutura pronta em `01_fundamentals.tex`. |

---

# 📊 Bloco V: Validação Experimental e Histórico Institucional

| Ferramenta / Componente    | Código-Fonte                                                        | Status | Descrição                                                          |
| :------------------------- | :------------------------------------------------------------------ | :----: | :----------------------------------------------------------------- |
| Driver C++23 de Benchmark  | [`runner.cpp`](./experiments/drivers/runner.cpp)                    |   ✅   | Medição de tempo via `std::chrono::steady_clock`.                  |
| Gerador Sintético          | [`random_instance.py`](./experiments/generators/random_instance.py) |   ✅   | Gerador parametrizado de instâncias de teste.                      |
| Orquestrador de Benchmarks | [`run_benchmarks.py`](./experiments/.scripts/run_benchmarks.py)     |   ✅   | Coleta estatística separada em `--suite ic` e `--suite book`.      |
| Gerador de Tabelas LaTeX   | [`generate_tables.py`](./experiments/.scripts/generate_tables.py)   |   ✅   | Exportação `booktabs` para `latex/tables/` e `latex/book/tables/`. |
| Gerador de Gráficos PDF    | [`plot_charts.py`](./experiments/.scripts/plot_charts.py)           |   ✅   | Curvas de escalabilidade e barras em PDF.                          |

## 🏛️ Histórico Institucional: Iniciação Científica UFABC

| Entrega Institucional                         | Escopo / Arquivo                                                                                       | Status  |
| :-------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :-----: |
| **Proposta Inicial (`@@EDITAL@@`)**           | [`latex/proposal.tex`](./latex/proposal.tex)                                                           | 🟡 Base |
| **Relatório Final, Versão Limpa e Monólito**  | [`report.tex`](./latex/report.tex), [`ic.tex`](./latex/ic.tex), [`monolith.tex`](./latex/monolith.tex) | 🟡 Base |
| **Pôster Científico do Simpósio (90×120 cm)** | [`latex/poster.tex`](./latex/poster.tex)                                                               | 🟡 Base |
