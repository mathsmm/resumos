# Vetores
Resumo de Vetores baseado em sua [página do Wikipédia](https://pt.wikipedia.org/wiki/Vetor_(matem%C3%A1tica)) e no material do Prof.º Christian Wagner (UFSC). 

Notas sobre o resumo:
1) Desconsideram-se demonstrações;
2) Espera-se que o leitor já esteja familiarizado com planos e espaços cartesianos e operações matemáticas básicas (o que inclui cálculo de determinante de matrizes 2x2 e 3x3).

## Sumário
- [Definição](#definição)
  - [Representações](#representação)
  - [Nomenclaturas](#nomenclaturas)
- [Base Canônica](#base-canônica)
- [Operações com Vetores](#operações-com-vetores)
  - [Decomposição](#Decomposição)
  - [Adição](#adição)
  - [Subtração](#subtração)
  - [Multiplicação por Escalar](#multiplicação-por-escalar)
  - [Produto Escalar](#produto-escalar)
  - [Ângulo entre Vetores](#ângulo-entre-vetores)
  - [Ortogonalidade entre Vetores](#ortogonalidade-entre-vetores)
  - [Projeção de Vetores](#projeção-de-vetores)
  - [Produto Vetorial](#produto-vetorial)

## Definição

Um **vetor** determinado por um segmento orientado AB (i.e. uma seta que sai do ponto $A$ e que vai até o ponto $B$) é o conjunto de todos os segmentos orientados [equipolentes](https://www.infopedia.pt/dicionarios/lingua-portuguesa/equipolente) a AB. Representa grandezas que possuem magnitude (comprimento), direção e sentido.

### Representação

![](img/Vetores%20(matemática)/Vector_from_A_to_B.png)

**Vetor:** $\vec{v}\in\mathbb{R}^n$ tal que $\vec{v}=(x_1, x_2, ..., x_n)$

**Módulo (comprimento) do vetor:** $|\vec{v}|=||\vec{v}||=\sqrt{x_1^2+x_2^2+...+x_n^2}$

Exemplos:
* $\vec{a}=(1,2)$. Neste caso, $\vec{a}$ está no plano cartesiano $\mathbb{R}^2$
* $\vec{b}=(5,10,15)$. Aqui, $\vec{b}$ está no espaço cartesiano $\mathbb{R}^3$

Seja o ponto $A=(1,0)$ e o ponto $B=(2,3)$. Para se obter o vetor $\overrightarrow{AB}$, deve-se calcular $B-A$:

$B-A$<br>
$=(2,3)-(1,0)$<br>
$=(2-1,3-0)$<br>
$=(1,3)$<br>
$=\overrightarrow{AB}$<br>

O **módulo** do vetor $\overrightarrow{AB}$ é a distância entre os pontos $A$ e $B$. Para se obter esta distância, calcula-se:

$|\overrightarrow{AB}|$<br>
$=\sqrt{1^2+3^2}$<br>
$=\sqrt{10}$<br>
$\approx3,16227$<br>

### Nomenclaturas

- **Vetores iguais:** Dois vetores $\overrightarrow{AB}$ e $\overrightarrow{CD}$ são iguais se, e somente se são equipolentes;

- **Vetor nulo/zero:** Vetor cuja extremidade coincide com sua origem, ou seja, possui comprimento nulo e é indicado por $\vec{0}$;

- **Vetores opostos:** Dado um vetor $\vec{v}=\overrightarrow{AB}$, o vetor $\overrightarrow{BA}$ é oposto de $\overrightarrow{AB}$ e se indica por $-\overrightarrow{AB}$ ou  $-\vec{v}$ . O vetor oposto possui mesmo módulo e direção, mas sentido inverso;

- **Vetor unitário:** Um vetor $\vec{v}$ é unitário se seu comprimento é igual a 1, ou seja, $|\vec{v}|=1$;

- **Versor:** O versor $\vec{u}$ de um vetor não nulo $\vec{v}$ é o vetor unitário de mesma direção o e sentido de $\vec{v}$. Pode ser obtido com a equação $\vec{u}=\frac{\vec{v}}{|\vec{v}|}$;

- **Vetores colineares:** Dois vetores $\vec{u}$ e $\vec{v}$ são colineares se tiverem a mesma direção, ou seja, se tiverem representantes $AB$ e $CD$ pertencentes a uma mesma reta ou se as retas forem paralelas. Eles não necessitam ter mesmo módulo e mesmo sentido para serem colineares. Notação: $\vec{u}\parallel\vec{v}$ ou $\vec{u}//\vec{v}$;

- **Vetores coplanares:** Se os vetores não nulos $\vec{u}$ , $\vec{v}$ e $\vec{w}$ possuem representantes $AB$, $CD$ e $EF$ pertencentes a um mesmo plano *ou a planos paralelos*, diz-se que eles são coplanares.

## Base Canônica

A [base canônica](#https://pt.wikipedia.org/wiki/Base_can%C3%B4nica) no espaço vetorial $\mathbb{R}^3$ é formada pelos **versores** $\hat{i}=(1,0,0)$, $\hat{j}=(0,1,0)$ e $\hat{k}=(0,0,1)$.

![](img/Vetores%20(matemática)/standard-basis-vectors.png)

## Operações com Vetores

### Decomposição

Um vetor $\vec{a}=(x, y, z)$ em $\mathbb{R}^3$ pode ser decomposto em três componentes que são formadas pelos vetores $\vec{a_x}=(x,0,0)$, $\vec{a_y}=(0,y,0)$ e $\vec{a_z}=(0,0,z)$. 

Também é possível representar um vetor utilizando os versores $\hat{i}$, $\hat{j}$ e $\hat{k}$ desta forma: $\vec{a}=x\cdot\hat{i}+y\cdot\hat{j}+z\cdot\hat{k}$

![](img/Vetores%20(matemática)/3D_Vector.png)

### Adição
Sejam os vetores $\vec{u}=(a_1, a_2,..., a_n)$ e $\vec{v}=(b_1, b_2, ..., b_n)$. A soma dos vetores $\vec{u}$ e $\vec{v}$ é o vetor $\vec{w}$ definido pela sequência de expressões:

$\vec{w}$<br>
$=\vec{u}+\vec{v}$<br>
$=(a_1,a_2,...,a_n)+(b_1,b_2,...,b_n)$<br>
$=(a_1+b_1, a_2+b_2, ..., a_n + b_n)$<br>

![](img/Vetores%20(matemática)/vector_2d_add.png)

#### Propriedades da Adição

- Comutativa: $\vec{u}+\vec{v}=\vec{v}+\vec{u}$

- Associativa: $(\vec{u}+\vec{v})+\vec{w}=\vec{u}+(\vec{v}+\vec{w})$

- Elemento neutro: Existe um só vetor $\vec{0}$ nulo tal que para todo o vetor $\vec{v}$ tem-se $\vec{v}+\vec{0}=\vec{0}+\vec{v}=\vec{v}$

- Elemento inverso: Qualquer que seja o vetor $\vec{v}$, existe um só vetor $-\vec{v}$ (vetor oposto a $\vec{v}$) tal que $\vec{v}+(-\vec{v})=-\vec{v}+\vec{v}=\vec{0}$

### Subtração

Sejam os vetores $\vec{u}=(a_1, a_2,..., a_n)$ e $\vec{v}=(b_1, b_2, ..., b_n)$. A subtração (ou diferença) dos vetores $\vec{u}$ e $\vec{v}$ é o vetor $\vec{w}$ definido pela sequência de expressões (utiliza multiplicação por escalar com o valor $-1$):

$\vec{w}$<br>
$=\vec{u}+(-\vec{v})$<br>
$=(a_1,a_2,...,a_n)+(-(b_1,b_2,...,b_n))$<br>
$=(a_1,a_2,...,a_n)+(-b_1,-b_2,...,-b_n)$<br>
$=(a_1-b_1, a_2-b_2, ..., a_n-b_n)$<br>

### Multiplicação por Escalar

Seja $\vec{u}=(x_1, x_2, ..., x_n)$ um vetor e $k$ um número real, o produto do real $k$ pelo vetor $\vec{u}$ é o vetor $\vec{w}$ definido pela sequência de expressões:

$\vec{w}$<br>
$=k\vec{u}$<br>
$=k(x_1, x_2, ..., x_n )$<br>
$=(kx_1, kx_2, ..., kx_n)$<br>

tal que:

1) Módulo: $|\vec{w}|=|k\vec{u}|=|k|\cdot|\vec{u}|$
2) Direção: A mesma de $\vec{u}$
3) Sentido: A mesma de $\vec{u}$ se $k>0$ e o contrário se $k<0$

OBS.: Se $k=0$ ou $\vec{u}=\vec{0}$, então $\vec{w}=\vec{0}$, o vetor nulo.

#### Propriedades da Multiplicação por Escalar

- $a(b\vec{v})=(ab)\vec{v}$
- $(a+b)\vec{v}=a\vec{v}+b\vec{v}$
- $a(\vec{u}+\vec{v})=a\vec{u}+a\vec{v}$
- $1\vec{v}=\vec{v}$

### Produto Escalar

Também denominado por Produto Interno.

Seja $\vec{u}=(x_1, x_2, ..., x_n)$ e $\vec{v}=(y_1, y_2, ..., y_n)$, o produto escalar entre $\vec{u}$ e $\vec{v}$, representado por $\vec{u}\bullet\vec{v}$ ou por $<\vec{u},\vec{v}>$, é o **número real** definido por
$$\vec{u}\bullet\vec{v}=x_1y_1+x_2y_2+...+x_ny_n$$
ou por
$$\vec{u}\bullet\vec{v}=|\vec{u}|\cdot|\vec{v}|\cdot\cos\theta$$
onde $\theta$ é o [ângulo formado entre os dois vetores](#ângulo-entre-vetores).

#### Propriedades do Produto Escalar

- $\vec{u}\bullet\vec{v}=\vec{v}\bullet\vec{u}$
- $(a\vec{u})\bullet\vec{v}=a(\vec{u}\bullet\vec{v})=\vec{u}\bullet(a\vec{v})$
- $\vec{u}\bullet(\vec{v}+\vec{w})=\vec{u}\bullet\vec{v}+\vec{u}\bullet\vec{w}$
- $\vec{u}\bullet\vec{u}=|\vec{u}|^2$

### Ângulo entre Vetores

O ângulo entre dois vetores não nulos $\vec{u}$ e $\vec{v}$ é o ângulo $\theta$ formado pelas semiretas $AO$ e $OB$, onde $O$ é a origem de ambos os vetores, $A$ é a extremidade de $\vec{u}$ e $B$ é a extremidade de $\vec{v}$, tal que $0\leq\theta\leq\pi$.

Tem-se:
$$\cos\theta=\frac{\vec{u}\bullet\vec{v}}{|\vec{u}|\cdot|\vec{v}|}$$

#### Observações
- Se $\theta=\pi$, então os vetores $\vec{u}$ e $\vec{v}$ têm a mesma direção porém sentidos opostos

- Se $\theta=0º$, então os vetores $\vec{u}$ e $\vec{v}$ têm a mesma direção e mesmo sentido

- Se $\theta=\frac{\pi}{2}$, os vetores são ditos **ortogonais** ou **perpendiculares** e indica-se por $\vec{u}\perp\vec{v}$

- O vetor nulo $\vec{0}$ é considerado ortogonal a qualquer vetor

### Ortogonalidade entre Vetores

Dois vetores $\vec{u}$ e $\vec{v}$ são ortogonais ou perpendiculares se, e somente se $\vec{u}\bullet\vec{v}=0$.

Em outras palavras, para determinar se dois vetores são ortogonais, basta verificar se o produto escalar entre eles é igual a zero. A ortogonalidade de dois vetores é representada pelo símbolo $\perp$. Neste caso, $\vec{u}\perp\vec{v}$.

### Projeção de Vetores

Dado dois vetores não nulos $\vec{u}$ e $\vec{v}$, a projeção de $\vec{v}$ sobre $\vec{u}$, denominada $Proj_{\vec{u}}\vec{v}$, é o vetor $\vec{p}$ determinado por:
$$\vec{p}=\left(\frac{\vec{u}\bullet\vec{v}}{|\vec{u}|^2}\right)\vec{u}$$

#### Observações

- Se os vetores forem **ortogonais**, i.e. $\vec{u}\perp\vec{v}$, então $Proj_{\vec{u}}\vec{v} = Proj_{\vec{v}}\vec{u}=\vec{0}$ (vetor nulo);

- Se os vetores forem **colineares**, $Proj_{\vec{u}}\vec{v}=\vec{v}$ e $Proj_{\vec{v}}\vec{u}=\vec{u}$;

- Se o vetor $\vec{u}$ for **unitário** (módulo igual a 1), então
  - $Proj_{\vec{u}}\vec{v}=(\vec{u}\bullet\vec{v})\vec{u}$
  - $|Proj_{\vec{u}}\vec{v}|=|\vec{u}\bullet\vec{v}|$

### Produto Vetorial

Seja $\vec{u}=(x_1,y_1,z_1)$ e $\vec{v}=(x_2,y_2,z_2)$ vetores do $\mathbb{R}^3$, define-se o vetor que é o produto vetorial de $\vec{u}$ e $\vec{v}$, representado por $\vec{u}\times\vec{v}$, da seguinte forma:

$$\vec{u}\times\vec{v}=(y_1z_2-y_2z_1)\hat{i}-(x_1z_2-x_2z_1)\hat{j}+(x_1y_2-x_2y_1)\hat{k}$$

ou ainda, utilizando determinante de matriz 3x3:

$$\vec{u}\times\vec{v}=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
\end{vmatrix}
$$

#### Observações

Sejam $\vec{u}$ e $\vec{v}$ vetores não paralelos entre si, o produto vetorial é um terceiro vetor que apresenta as seguintes características:

1) A direção do vetor $\vec{u}\times\vec{v}$ é perpendicular aos vetores $\vec{u}$ e $\vec{v}$;
2) Seu módulo é $|\vec{u}\times\vec{v}|=|\vec{u}|\cdot|\vec{v}|\cdot\sin\theta$, onde $\theta$ é a medida do ângulo entre $\vec{u}$ e $\vec{v}$;
3) Os vetores $\vec{u}$, $\vec{v}$ e $\vec{u}\times\vec{v}$ nesta ordem formam um [triedro](https://pt.wikipedia.org/wiki/Triedro) positivo.

![](img/Vetores%20(matemática)/06_vectors16.svg)

#### Propridedades do Produto Vetorial

- $\vec{u}\times\vec{v}=-(\vec{v}\times\vec{u})$
- $\vec{u}\times(\vec{v}+\vec{w})=\vec{u}\times\vec{v}+\vec{u}\times\vec{w}$
- $(a\vec{u})\times\vec{v}=a(\vec{u}\times\vec{v})$
- $\vec{u}\times\vec{v}=\vec{0}\Leftrightarrow$ $\vec{u}$ ou $\vec{v}$ são nulos ou se $\vec{u}\parallel\vec{v}$ ($\vec{u}$ colinear a $\vec{v}$)
- $\vec{u}\times\vec{v}$ é simultaneamente ortogonal a $\vec{u}$ e $\vec{v}$
- $|\vec{u}\bullet\vec{v}|^2=|\vec{u}|^2 \cdot|\vec{v}|^2-(\vec{u}\bullet\vec{v})^2$ (Identidade de Lagrange)
- Se $\vec{u}\neq\vec{0}$ e $\vec{v}\neq\vec{0}$, e $\theta$ é o ângulo entre $\vec{u}$ e $\vec{v}$, então $$\sin\theta=\frac{|\vec{u}\times\vec{v}|}{|\vec{u}|\cdot|\vec{v}|}$$
- O produto vetorial não é associativo, isto é $$\vec{u}\times(\vec{v}\times\vec{w})\neq(\vec{u}\times\vec{v})\times\vec{w}$$

#### Interpretação Geométrica do Produto Vetorial

A área $A$ de um paralelogramo formado pelos vetores $\vec{u}$ e $\vec{v}$ pode ser determinada pelo módulo do produto vetorial de $\vec{u}$ e $\vec{v}$. 
$$A=|\vec{u}\times\vec{v}|$$
