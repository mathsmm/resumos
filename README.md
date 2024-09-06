# Resumos

- Matemática
  - [Matrizes](matematica/Matrizes.md)
  - [Vetores](matematica/Vetores.md)

# Como estão organizados?

**OBS.: Entende-se o diretório `resumos` como a "pasta raíz dos resumos" ou a "pasta de nível 0".**

- As pastas de nível 1 representam assuntos gerais;
- As pastas de nível 2 representam de fato os resumos. Elas podem ter;
  - Subpastas (nível 3), que por si só também podem ter subpastas (nível 4, 5, ..., n);
  - Cada subpasta gera um item para o sumário do resumo. O item pode estar linkado como também pode não estar. Para um item ser linkado, seu diretório correspondente deve possuir um arquivo *markdown* (`.md`) com o mesmo nome do diretório. O link então apontará para este *markdown*;
  - Se houver mais arquivos *markdown* dentro da subpasta, cada um gerará um item e um link para o sumário. O item será um subitem de sua subpasta;
- Imagens ficam guardadas no diretório `img` que fica dentro das pastas de nível 2.

As pastas e arquivos Markdown podem conter um *underline* (`_`) em seus nomes. O que aparecer antes do *underline* é um indicador:

**Tabela de indicadores:**
| Indicador | Representação | Aplicabilidade | Sintaxe |
| --------- | ------------- | -------------- | ------- |
| A | Artigo (não científico) | Subpastas de nível 2 | `A_Nome do Artigo` |
| SA | Artigo Científico | Subpastas de nível 2 | `SA_Nome do Artigo Científico` |
| B | Livro | Subpastas de nível 2 | `B_Nome do Livro` |
| <número> | Número do Cap., Seção, etc. | Subpastas de nível 3..n | `<indicador><número>` |
| P | Parte | Subpastas de nível 3..n | `P<número>_Nome da Parte` |
| C | Capítulo | Subpastas de nível 3..n | `C<número>_Nome do Capítulo` |
| S | Seção | Subpastas de nível 3..n | `S<número>_Nome da Seção` |
| SEQ | Sequência | Subpastas de nível 3..n | `SEQ<número>(.<número>)*_Nome qualquer` |

**Sobre o indicador de Sequência**
Ele pode ser utilizado caso o escritor do resumo não queira usar os indicadores de Parte, Capítulo, Seção, etc. Neste caso, utiliza-se números seguidos de pontos para agrupamento. Exemplo: 1, 1.1, 1.2, 1.1.1, 1.1.2, 2, 2.1, etc.

IMPORTANTE: Se pelo menos uma subpasta utiliza o indicador de sequência, todas devem utilizar.