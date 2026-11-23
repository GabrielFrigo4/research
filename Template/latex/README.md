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

## 🛠️ Comandos

```sh
make book
make reports
make all
make editorial
make sync-code
make clean
```
