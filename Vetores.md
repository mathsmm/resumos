# Vetores
Resumo de Vetores baseado em sua [página do Wikipédia](https://pt.wikipedia.org/wiki/Vetor_(matem%C3%A1tica)) e no material do Prof.º Christian Wagner (UFSC). 

Notas sobre o resumo:
1) Desconsideram-se demonstrações;
2) Espera-se que o leitor já esteja familiarizado com planos e espaços cartesianos e operações matemáticas básicas (o que inclui cálculo de determinante de matrizes 2x2 e 3x3).

## Sumário
- [Definição](#Definição)
	- [Representações](#Representações)
	- [Nomenclaturas](#Nomenclaturas)
- [Base Canônica do $\Real^3$](#Base-Canônica-do-$\R^3$)
- [Operações com Vetores](#Operações-com-Vetores)
	- [Decomposição](#Decomposição)
	- [Adição](#Adição)
	- [Subtração](#Subtração)
	- [Multiplicação por Escalar](#Multiplicação-por-Escalar)
	- [Produto Escalar](#Produto-Escalar)
	- [Ângulo entre Vetores](Ângulo-entre-Vetores)
	- [Ortogonalidade entre Vetores](#Ortogonalidade-entre-Vetores)
 - $mathbb{R}$

## Definição

Um **vetor** determinado por um segmento orientado AB (i.e. uma seta que sai do ponto $A$ e que vai até o ponto $B$) é o conjunto de todos os segmentos orientados [equipolentes](https://www.infopedia.pt/dicionarios/lingua-portuguesa/equipolente) a AB. Representa grandezas que possuem magnitude (comprimento), direção e sentido.

### Representações

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vector_from_A_to_B.svg/1920px-Vector_from_A_to_B.svg.png)

**Vetor:** $\vec{v}\in\R^n$ tal que $\vec{v}=(x_1, x_2, ..., x_n)$

**Módulo (comprimento) do vetor:** $|\vec{v}|=\|\vec{v}\|=\sqrt{x_1^2+x_2^2+...+x_n^2}$

Exemplos:
* $\vec{a}=(1,2)$. Neste caso, $\vec{a}$ está no plano cartesiano $\R^2$
* $\vec{b}=(5,10,15)$. Aqui, $\vec{b}$ está no espaço cartesiano $\R^3$

Seja o ponto $A=(1,0)$ e o ponto $B=(2,3)$. Para se obter o vetor $\overrightarrow{AB}$, deve-se calcular $B-A$:

$B-A$
$=(2,3)-(1,0)$
$=(2-1,3-0)$
$=(1,3)$
$=\overrightarrow{AB}$

O **módulo** do vetor $\overrightarrow{AB}$ é a distância entre os pontos $A$ e $B$. Para se obter esta distância, calcula-se:

$|\overrightarrow{AB}|$
$=\sqrt{1^2+3^2}$
$=\sqrt{10}$
$\approx3,16227$

### Nomenclaturas

- **Vetores iguais:** Dois vetores $\overrightarrow{AB}$ e $\overrightarrow{CD}$ são iguais se, e somente se são equipolentes;

- **Vetor nulo/zero:** Vetor cuja extremidade coincide com sua origem, ou seja, possui comprimento nulo e é indicado por $\vec{0}$;

- **Vetores opostos:** Dado um vetor $\vec{v}=\overrightarrow{AB}$, o vetor $\overrightarrow{BA}$ é oposto de $\overrightarrow{AB}$ e se indica por $-\overrightarrow{AB}$ ou  $-\vec{v}$ . O vetor oposto possui mesmo módulo e direção, mas sentido inverso;

- **Vetor unitário:** Um vetor $\vec{v}$ é unitário se seu comprimento é igual a 1, ou seja, $|\vec{v}|=1$;

- **Versor:** O versor de um vetor não nulo $\vec{v}$ é o vetor unitário de mesma direção o e sentido de $\vec{v}$;

- **Vetores colineares:** Dois vetores $\vec{u}$ e $\vec{v}$ são colineares se tiverem a mesma direção, ou seja, se tiverem representantes $AB$ e $CD$ pertencentes a uma mesma reta ou se as retas forem paralelas. Eles não necessitam ter mesmo módulo e mesmo sentido para serem colineares;

- **Vetores coplanares:** Se os vetores não nulos $\vec{u}$ , $\vec{v}$ e $\vec{w}$ possuem representantes $AB$, $CD$ e $EF$ pertencentes a um mesmo plano *ou a planos paralelos*, diz-se que eles são coplanares.

## Base Canônica do $\R^3$

A [base canônica](#https://pt.wikipedia.org/wiki/Base_can%C3%B4nica) no espaço vetorial $\R^3$ é formada pelos **versores** $\hat{i}=(1,0,0)$, $\hat{j}=(0,1,0)$ e $\hat{k}=(0,0,1)$.

![](https://calcworkshop.com/wp-content/uploads/standard-basis-vectors.png)

## Operações com Vetores

### Decomposição

Um vetor $\vec{a}=(x, y, z)$ em $\R^3$ pode ser decomposto em três componentes que são formadas pelos vetores $\vec{a_x}=(x,0,0)$, $\vec{a_y}=(0,y,0)$ e $\vec{a_z}=(0,0,z)$.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/3D_Vector.svg/800px-3D_Vector.svg.png)

### Adição
Sejam os vetores $\vec{u}=(a_1, a_2,..., a_n)$ e $\vec{v}=(b_1, b_2, ..., b_n)$. A soma dos vetores $\vec{u}$ e $\vec{v}$ é o vetor $\vec{w}$ definido pela sequência de expressões:

$\vec{w}$
$=\vec{u}+\vec{v}$
$=(a_1,a_2,...,a_n)+(b_1,b_2,...,b_n)$
$=(a_1+b_1, a_2+b_2, ..., a_n + b_n)$

![](https://mathinsight.org/media/image/image/vector_2d_add.png)

#### Propriedades da Adição

- Comutativa: $\vec{u}+\vec{v}=\vec{v}+\vec{u}$

- Associativa: $(\vec{u}+\vec{v})+\vec{w}=\vec{u}+(\vec{v}+\vec{w})$

- Elemento neutro: Existe um só vetor $\vec{0}$ nulo tal que para todo o vetor $\vec{v}$ tem-se $\vec{v}+\vec{0}=\vec{0}+\vec{v}=\vec{v}$

- Elemento inverso: Qualquer que seja o vetor $\vec{v}$, existe um só vetor $-\vec{v}$ (vetor oposto a $\vec{v}$) tal que $\vec{v}+(-\vec{v})=-\vec{v}+\vec{v}=\vec{0}$

### Subtração

Sejam os vetores $\vec{u}=(a_1, a_2,..., a_n)$ e $\vec{v}=(b_1, b_2, ..., b_n)$. A subtração (ou diferença) dos vetores $\vec{u}$ e $\vec{v}$ é o vetor $\vec{w}$ definido pela sequência de expressões (utiliza multiplicação por escalar com o valor $-1$):

$\vec{w}$
$=\vec{u}+(-\vec{v})$
$=(a_1,a_2,...,a_n)+(-(b_1,b_2,...,b_n))$
$=(a_1,a_2,...,a_n)+(-b_1,-b_2,...,-b_n)$
$=(a_1-b_1, a_2-b_2, ..., a_n-b_n)$

### Multiplicação por Escalar

Seja $\vec{u}=(x_1, x_2, ..., x_n)$ um vetor e $k$ um número real, o produto do real $k$ pelo vetor $\vec{u}$ é o vetor $\vec{w}$ definido pela sequência de expressões:

$\vec{w}$
$=k\vec{u}$
$=k(x_1, x_2, ..., x_n )$
$=(kx_1, kx_2, ..., kx_n)$

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
onde $\theta$ é o [ângulo formado entre os dois vetores](#Ângulo-entre-Vetores).

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

Dois vetores $\vec{u}$ e $\vec{v}$ são ortogonais se, e somente se $\vec{u}\bullet\vec{v}=0$. Em outras palavras, para determinar se dois vetores são ortogonais, basta verificar se o produto escalar entre eles é igual a zero. A ortogonalidade de dois vetores é representada pelo símbolo "$\perp$". Neste caso, $\vec{u}\perp\vec{v}$.

### Projeção de Vetores

Dado dois vetores não nulos $\vec{u}$ e $\vec{v}$, a projeção de $\vec{v}$ sobre $\vec{u}$, denominada $Proj_{\vec{u}}\vec{v}$, é o vetor $\vec{p}$ determinado por
$$\vec{p}=\left(\frac{\vec{u}\bullet\vec{v}}{|\vec{u}|^2}\right)\vec{u}$$

#### Observações

- Se os vetores forem **ortogonais**, i.e. $\vec{u}\perp\vec{v}$, então $Proj_{\vec{u}}\vec{v} = Proj_{\vec{v}}\vec{u}=\vec{0}$ (vetor nulo);

- Se os vetores forem **colineares**, $Proj_{\vec{u}}\vec{v}=\vec{v}$ e $Proj_{\vec{v}}\vec{u}=\vec{u}$;

- Se o vetor $\vec{u}$ for **unitário** (módulo igual a 1), então
	- $Proj_{\vec{u}}\vec{v}=(\vec{u}\bullet\vec{v})\vec{u}$
	- $|Proj_{\vec{u}}\vec{v}|=|\vec{u}\bullet\vec{v}|$

### Produto Vetorial

![](https://www.brunodorta.com.br/cg/images/06_vectors16.svg)
