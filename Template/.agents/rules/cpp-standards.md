---
description: Padrões de engenharia C++23 e Clean Code para Pesquisa @@RESEARCH-TITLE@@.
globs: "**/*.{hpp,cpp}"
always_on: true
---

# Diretrizes de Código C++23 — @@RESEARCH-TITLE@@

1. **Padrão & Compilador:** C++23 obrigatório (`-std=c++23`), compilador `CXX = c++`.
2. **Tipos Canônicos:**
    - `using Long = long long;`
    - `using Size = std::size_t;`
    - `constexpr Long INF = std::numeric_limits<Long>::max() >> 8;`
3. **Herança Algorítmica:**
    - Algoritmos concretos herdam de uma classe base abstrata polimórfica em `implementations/core/AlgorithmBase.hpp`, implementando `make` e `clone` junto ao método de resolução da família.
4. **Formatação:** `.clang-format` Microsoft modificado (4 espaços, 85 colunas). Executar `make format`.
5. **Clean Code:** Zero comentários narrativos dentro do código executável. Identificadores estritamente em inglês técnico.
