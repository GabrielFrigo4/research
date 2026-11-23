# 🧩 Resolução de Problemas (`@@RESEARCH-TITLE@@`)

Este diretório concentra soluções de problemas clássicos e de juízes online utilizando a biblioteca polimórfica em C++23, além do utilitário [`bundle.py`](../bundle.py) para gerar códigos autocontidos em arquivo único.

- 🚀 **Template Inicial:** [`template/main.cpp`](./template/main.cpp)

## 🛠️ Workflow (`make clip`)

| Comando                      | Descrição                                                             |
| :--------------------------- | :-------------------------------------------------------------------- |
| **`make`** ou **`make run`** | Compila `main.cpp` com `-std=c++23 -O2` e executa sobre `input.txt`.  |
| **`make bundle`**            | Imprime o código C++23 unificado (com headers embutidos) no terminal. |
| **`make clip`**              | Empacota via `bundle.py` e copia o resultado para `wl-copy`.          |
| **`make clean`**             | Remove o binário compilado local.                                     |
