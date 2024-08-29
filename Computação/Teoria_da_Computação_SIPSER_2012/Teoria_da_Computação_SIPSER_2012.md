Resumo baseado no livro *SIPSER, M. Introduction to the theory of computation, 3rd ed. Boston: Cengage Learning, 2012.*

Notas:
- Utilizam-se diagramas Flowchart do [Mermaid](https://mermaid.js.org/) para representar os autômatos graficamente;
- Os diagramas de autômatos possuem um asterisco (`*`) para indicar o estado inicial.

Exemplo de autômato feito com Mermaid:
```mermaid
flowchart LR
    direction LR
    q1(("$$*q_1$$")) --> |1| q1
    q1 --> |1| q2(("$$q_2$$"))
    q2 --> |0| q1
    q2 --> |1| q3((("$$q_3$$")))
    q3 --> |0, 1| q3
```