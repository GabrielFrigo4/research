# 🗺️ Roadmap & Backlog do Research Hub

> Planejamento estratégico, status operacional e visão de futuro para pesquisas em Otimização Combinatória de Gabriel Frigo.

---

## 📊 Status dos Módulos & Pesquisas

| Módulo           | Foco da Pesquisa                                      | Maturidade | Tecnologias Centrais             |
| :--------------- | :---------------------------------------------------- | :--------: | :------------------------------- |
| **Network Flow** | Fluxo Máximo e Fluxo de Custo Mínimo (UFABC/PIBIC)    |  🟢 Ativo  | C++23, DIMACS, LaTeX, bmake      |
| **Hub**          | Orquestrador de pesquisa, LaTeX e automação de testes | 🟢 Estável | POSIX Makefile, Shell, GitHub CI |

---

## 🎯 Grandes Épicos do Hub

### 1. 🔬 Algoritmos de Fluxo em Redes (C++23)

- [ ] **Push-Relabel com Heurísticas Globais:** Implementação de ponta com _gap relabeling_ e _highest-label first_.
- [ ] **Cancelamento de Ciclos de Custo Médio Mínimo:** Implementação e benchmarking de Goldberg-Tarjan para Min-Cost Flow.
- [ ] **Validação com Instâncias DIMACS:** Testes automatizados contra grafos massivos padronizados internacionalmente.

### 2. 📖 Publicação Acadêmica & Livro

- [ ] **Estruturação dos Capítulos Teóricos:** Formalização matemática dos teoremas de corte mínimo e dualidade.
- [ ] **Pipeline LaTeX Silencioso:** Garantir compilação hermética sem geração de sujeira na árvore git.
