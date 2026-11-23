# 📝 Códigos-Fonte em LaTeX (`@@RESEARCH-TITLE@@`)

Códigos-fonte da documentação científica da pesquisa em **LaTeX**.

## 📄 Documentos Principais

| Arquivo                                 | Escopo             | Status             | Descrição                                                                       |
| :-------------------------------------- | :----------------- | :----------------- | :------------------------------------------------------------------------------ |
| 📗 **[`book.tex`](./book.tex)**         | **Livro / Pós-IC** | 🟢 **Em Evolução** | Monografia completa em 5 Partes, com teoria, apêndices C++23 e benchmarks.      |
| 🖼️ **[`poster.tex`](./poster.tex)**     | **IC (UFABC)**     | 🟡 **Escopo IC**   | Pôster Científico do Simpósio de IC da UFABC (90×120 cm).                       |
| 📘 **[`proposal.tex`](./proposal.tex)** | **IC (UFABC)**     | 🟡 **Escopo IC**   | Proposta inicial submetida ao edital `@@EDITAL@@`.                              |
| 📙 **[`report.tex`](./report.tex)**     | **IC (UFABC)**     | 🟡 **Escopo IC**   | Relatório formal com capa institucional e folha de assinaturas da UFABC.        |
| 📕 **[`ic.tex`](./ic.tex)**             | **IC (UFABC)**     | 🟡 **Escopo IC**   | Versão da Iniciação Científica com capa limpa para leitura.                     |
| 📄 **[`monolith.tex`](./monolith.tex)** | **IC (UFABC)**     | 🟡 **Escopo IC**   | Monólito autocontido para Overleaf gerado automaticamente via `make sync-code`. |

### Pastas de Artefatos Editoriais Vivos (`cards/`, `minibooks/`, `notebooks/`, `slides/`)

- [`cards/`](./cards/) — Cards de referência rápida (1 página)
- [`minibooks/`](./minibooks/) — Mini-books monotemáticos (15–30 páginas)
- [`notebooks/`](./notebooks/) — Cadernos ICPC e Maratona em 2 colunas
- [`slides/`](./slides/) — Apresentações Beamer reaproveitando `diagrams/`

## 🧩 Arquitetura de Apêndices Compartilhados

- [`.scripts/sync_listings.py`](../.scripts/sync_listings.py) (`make sync-code`) gera arquivos `.tex` individuais em [`appendices/`](./appendices/) para cada header C++ registrado.
- [`sections/body.tex`](./sections/body.tex) (Relatório / IC) e [`book.tex`](./book.tex) (Livro) selecionam de forma independente quais `\input{appendices/...}` incluir — algoritmos Pós-IC podem ser adicionados apenas ao Livro mantendo eventuais correções de código sincronizadas na IC.
- [`appendices/99_github.tex`](./appendices/99_github.tex) utiliza o prefixo `99_` para nunca colidir com novos apêndices de algoritmos (`01_`, `02_`, ..., `98_`).

## 🛠️ Comandos

```sh
make book
make reports
make all
make editorial
make sync-code
make clean
```
