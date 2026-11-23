# 🔬 @@RESEARCH-TITLE@@

> @@RESEARCH-DESC@@

[![C++23](https://img.shields.io/badge/Language-C%2B%2B23-00599C?logo=c%2B%2B&logoColor=white)](implementations/)
[![LaTeX](https://img.shields.io/badge/Typesetting-LaTeX-green?logo=latex&logoColor=white)](latex/)
[![UFABC](https://img.shields.io/badge/Instituição-UFABC-darkblue)](https://www.ufabc.edu.br/)

---

## 📚 Documentação e Relatórios da Pesquisa

[![Baixar Livro (Monografia)][baixar_pdf_livro_icon]][baixar_pdf_livro] [![Baixar Pôster IC][baixar_pdf_poster_icon]][baixar_pdf_poster]

[![Baixar PDF do Relatório][baixar_pdf_relatorio_icon]][baixar_pdf_relatorio] [![Baixar PDF do Monólito][baixar_pdf_monolito_icon]][baixar_pdf_monolito]

[![Baixar PDF da IC][baixar_pdf_ic_icon]][baixar_pdf_ic] [![Baixar PDF do Projeto][baixar_pdf_projeto_icon]][baixar_pdf_projeto]

A documentação oficial da pesquisa é gerada a partir dos códigos-fonte em LaTeX disponíveis na pasta [`latex/`](./latex/), separando os artefatos institucionais da **Iniciação Científica (UFABC)** da **Monografia / Livro Contínuo**:

| PDF Gerado                                        | Escopo             | Status             | Arquivo Fonte                                  | Descrição                                                                                          |
| :------------------------------------------------ | :----------------- | :----------------- | :--------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [📗&nbsp;**`book.pdf`**][baixar_pdf_livro]        | **Livro / Pós-IC** | 🟢 **Em Evolução** | [🖋️&nbsp;`book.tex`](./latex/book.tex)         | **Livro e Monografia Independente.** Obra estruturada em 5 Partes com teoria, código e benchmarks. |
| [🖼️&nbsp;**`poster.pdf`**][baixar_pdf_poster]     | **IC (UFABC)**     | 🟡 **Escopo IC**   | [🖋️&nbsp;`poster.tex`](./latex/poster.tex)     | **Pôster Científico do Simpósio de IC da UFABC (90×120 cm).** Congelado após a entrega formal.     |
| [📘&nbsp;**`proposal.pdf`**][baixar_pdf_projeto]  | **IC (UFABC)**     | 🟡 **Escopo IC**   | [🖋️&nbsp;`proposal.tex`](./latex/proposal.tex) | Proposta e plano de trabalho inicial submetido ao edital `@@EDITAL@@`.                             |
| [📙&nbsp;**`report.pdf`**][baixar_pdf_relatorio]  | **IC (UFABC)**     | 🟡 **Escopo IC**   | [🖋️&nbsp;`report.tex`](./latex/report.tex)     | Relatório formal com capa institucional e folha de assinaturas da UFABC (`tables/`, `figures/`).   |
| [📕&nbsp;**`ic.pdf`**][baixar_pdf_ic]             | **IC (UFABC)**     | 🟡 **Escopo IC**   | [🖋️&nbsp;`ic.tex`](./latex/ic.tex)             | Documento principal da IC com capa limpa de leitura e apêndices computacionais.                    |
| [📄&nbsp;**`monolith.pdf`**][baixar_pdf_monolito] | **IC (UFABC)**     | 🟡 **Escopo IC**   | [🖋️&nbsp;`monolith.tex`](./latex/monolith.tex) | Versão em arquivo único compilável para Overleaf gerada a partir do `report.tex`.                  |

> [!IMPORTANT]
> **Política de Ciclo de Vida:** Os artefatos institucionais da Iniciação Científica (`proposal.pdf`, `report.pdf`, `ic.pdf`, `monolith.pdf`, `poster.pdf`) devem ser marcados como 🔒 **Finalizado (IC)** após a entrega oficial, preservando texto, tabelas, figuras e pôster intactos (mantendo apenas `make sync-code` para correções nos códigos originais da IC). O **Livro (`book.pdf`)**, as **famílias editoriais vivas**, as **implementações** e os **benchmarks Pós-IC** evoluem continuamente.

### 🎨 Artefatos Editoriais Vivos (Pós-IC)

| Família Editorial                            | Status                    | Escopo e Formato                                                    |
| :------------------------------------------- | :------------------------ | :------------------------------------------------------------------ |
| [**`latex/cards/`**](./latex/cards/)         | 🟢 Estrutura / ⏳ Autoria | Cards de referência rápida (1 página por tema; _cheat sheets_).     |
| [**`latex/minibooks/`**](./latex/minibooks/) | 🟢 Estrutura / ⏳ Autoria | Mini-books monotemáticos curtos (15–30 páginas autocontidos).       |
| [**`latex/notebooks/`**](./latex/notebooks/) | 🟢 Estrutura / ⏳ Autoria | Cadernos compactos em duas colunas e templates C++23 de competição. |
| [**`latex/slides/`**](./latex/slides/)       | 🟢 Estrutura / ⏳ Autoria | Apresentações didáticas em Beamer reaproveitando diagramas TikZ.    |

---

## 🗂️ Estrutura do Repositório

```text
.
├── .agents/                    # Governança local e regras de agentes de IA
├── .githooks/                  # Ganchos Git com auto-cura (pre-commit, commit-msg)
├── .github/                    # Workflows GitHub Actions (CI, LaTeX, Releases)
├── .scripts/                   # Sincronização de listagens e geração de monólito
├── applications/               # Aplicações práticas usando os motores C++23
├── experiments/                # Drivers C++23, geradores sintéticos e benchmarks
├── implementations/            # Motores algorítmicos C++23, testes e problemas
├── latex/                      # Livro, relatórios IC, pôster e famílias editoriais
└── materials/                  # Referências bibliográficas e notas de estudo
```

---

## 🛠️ Arquitetura de Automação e Makefiles (`.POSIX`)

| Comando           | Ação                                                                                          |
| :---------------- | :-------------------------------------------------------------------------------------------- |
| `make setup`      | Configura hooks locais do Git em [`.githooks/`](./.githooks/) e permissões.                   |
| `make book`       | Compila exclusivamente o livro monográfico (`latex/book.pdf`).                                |
| `make latex`      | Compila os 6 documentos principais em `latex/`.                                               |
| `make editorial`  | Compila todas as famílias editoriais vivas (`cards`, `minibooks`, `notebooks`, `slides`).     |
| `make impl`       | Valida a sintaxe C++23 de todos os headers em [`implementations/`](./implementations/).       |
| `make test`       | Executa a suíte de testes de algoritmos, problemas e aplicações.                              |
| `make exp`        | Compila os drivers de benchmark em [`experiments/`](./experiments/).                          |
| `make bench-ic`   | Executa benchmarks da suíte IC e gera artefatos em `latex/tables/` e `latex/figures/`.        |
| `make bench-book` | Executa benchmarks do Livro e gera artefatos em `latex/book/tables/` e `latex/book/figures/`. |
| `make sync-code`  | Sincroniza implementações C++23 nos apêndices LaTeX e reconstrói `monolith.tex`.              |
| `make format`     | Formata códigos C++ (`clang-format`) e Markdown/YAML (`prettier`).                            |
| `make clean`      | Remove artefatos temporários e arquivos gerados em todos os módulos.                          |

---

## 👥 Equipe

- **@@AUTHOR@@** (Autor) — Pesquisador
- **@@ADVISOR@@** (Orientação Acadêmica)

[baixar_pdf_projeto]: https://github.com/@@GITHUB-USER@@/@@RESEARCH-SLUG@@/releases/latest/download/proposal.pdf
[baixar_pdf_projeto_icon]: https://img.shields.io/badge/Projeto-Baixar-0969da?style=for-the-badge&logo=latex&logoColor=white
[baixar_pdf_livro]: https://github.com/@@GITHUB-USER@@/@@RESEARCH-SLUG@@/releases/latest/download/book.pdf
[baixar_pdf_livro_icon]: https://img.shields.io/badge/Livro-Baixar-2ea44f?style=for-the-badge&logo=gitbook&logoColor=white
[baixar_pdf_poster]: https://github.com/@@GITHUB-USER@@/@@RESEARCH-SLUG@@/releases/latest/download/poster.pdf
[baixar_pdf_poster_icon]: https://img.shields.io/badge/Pôster_IC-Baixar-006633?style=for-the-badge&logo=latex&logoColor=white
[baixar_pdf_ic]: https://github.com/@@GITHUB-USER@@/@@RESEARCH-SLUG@@/releases/latest/download/ic.pdf
[baixar_pdf_ic_icon]: https://img.shields.io/badge/IC-Baixar-cf222e?style=for-the-badge&logo=googledocs&logoColor=white
[baixar_pdf_relatorio]: https://github.com/@@GITHUB-USER@@/@@RESEARCH-SLUG@@/releases/latest/download/report.pdf
[baixar_pdf_relatorio_icon]: https://img.shields.io/badge/Relatório-Baixar-d97706?style=for-the-badge&logo=googledocs&logoColor=white
[baixar_pdf_monolito]: https://github.com/@@GITHUB-USER@@/@@RESEARCH-SLUG@@/releases/latest/download/monolith.pdf
[baixar_pdf_monolito_icon]: https://img.shields.io/badge/Monólito-Baixar-8b5cf6?style=for-the-badge&logo=latex&logoColor=white
