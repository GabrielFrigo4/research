# 📊 Experimentos e Validação Experimental (`@@RESEARCH-TITLE@@`)

Infraestrutura de benchmarking computacional e avaliação empírica separada em duas suítes independentes:

- **Suíte da IC (`make ic` / `make bench-ic`):** Saídas destinadas a `latex/tables/` e `latex/figures/`.
- **Suíte do Livro (`make book` / `make bench-book`):** Saídas destinadas a `latex/book/tables/` e `latex/book/figures/`.

---

## 📂 Estrutura

```text
experiments/
├── Makefile                  # Orquestração POSIX separada entre IC e Livro
├── drivers/                  # Harness em C++23 com std::chrono::steady_clock
├── generators/               # Geradores sintéticos em Python
├── instances/                # Instâncias de teste
├── results/                  # CSVs brutos separados por suíte
└── .scripts/                 # Execução, geração de tabelas LaTeX e gráficos PDF
```
