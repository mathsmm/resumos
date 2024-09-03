Sumário:
- [Exemplos de diagrama mermaid](#exemplos-de-diagrama-mermaid)
- [Titulo](#titulo)
  - [subtitulo](#subtitulo)


# Exemplos de diagrama mermaid
```mermaid
flowchart LR
    direction LR
    q1(("$$*q_1$$")) --> |1| q1
    q1 --> |1| q2(("$$q_2$$"))
    q2 --> |0| q1
    q2 --> |1| q3((("$$q_3$$")))
    q3 --> |0, 1| q3
```

# Titulo

$\frac{A}{B}$

## subtitulo

teste