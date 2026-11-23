# 🗺️ Roadmap & Backlog do Research Hub

> Planejamento estratégico, status operacional e visão de futuro para pesquisas em Ciência da Computação e Otimização Combinatória de Gabriel Frigo.

---

## 📊 Status dos Módulos & Pesquisas

| Módulo                      | Foco da Pesquisa                                                      | Maturidade | Tecnologias Centrais              |
| :-------------------------- | :-------------------------------------------------------------------- | :--------: | :-------------------------------- |
| **Network Flow**            | Fluxo Máximo e Fluxo de Custo Mínimo (UFABC / PIBIC + Livro Contínuo) |  🟢 Ativo  | C++23, DIMACS, LaTeX, POSIX Make  |
| **Template**                | Archetype canônico para criação de novas pesquisas científicas        | 🟢 Estável | C++23, LaTeX, POSIX Make, Shell   |
| **Hub & Release de Livros** | Orquestrador, CI/CD federado de livros (`*-book.pdf`) e Quality Gates | 🟢 Estável | POSIX Makefile, Python, GitHub CI |

---

## 🎯 Backlog & Tarefas

- [x] Estruturar [`Template/`](Template/) completo com interface C++23, suíte LaTeX completa (livro, relatórios IC, pôster e famílias editoriais vivas) e pipeline de benchmarks.
- [x] Implementar pipeline federado de publicação exclusiva de livros (`make build-latex`, `.scripts/discover_books.py`, `latex-pdf.yml` e `release-pdf.yml`).
- [ ] Instanciar futuras linhas de pesquisa a partir de [`Template/`](Template/) (ex.: _Algoritmos Probabilísticos_, _Programação Dinâmica Avançada_) e integrá-las automaticamente ao Release de Livros.
