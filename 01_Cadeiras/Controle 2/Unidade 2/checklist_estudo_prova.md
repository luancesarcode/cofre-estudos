# Checklist Passo a Passo de Estudo — Tema 5: Estabilidade e Critério de Routh-Hurwitz

Este checklist foi organizado em uma sequência lógica e progressiva para você dominar todo o conteúdo dos slides (**Tema 5 — Prof. Fabrício Bradaschia**) e resolver com segurança todas as questões da **Lista 4** e da **Prova de Engenharia de Controle 2 (EL466)**.

> **Como usar:** Vá marcando cada caixa `[x]` conforme avança na leitura do [Guia Didático Completo](file:///home/luan/Projetos/UFPE/Controle2/2/guia_didatico_estabilidade_routh_hurwitz.md), nos slides e nos exercícios.

---

## Etapa 1: Conceitos Fundamentais de Estabilidade (Slides 1 a 17)
*Objetivo: Saber classificar qualquer sistema batendo o olho nos polos e responder questões conceituais.*

- [ ] **1.1. Entender a diferença entre Planta Instável vs. Controle em Malha Fechada**
  - [ ] Compreender por que plantas naturalmente instáveis (ex.: caça moderno, pêndulo invertido) **não** podem ser estabilizadas em malha aberta e exigem realimentação.
- [ ] **1.2. Diferenciar Estabilidade Absoluta de Estabilidade Relativa**
  - [ ] **Absoluta:** resposta sim/não (o sistema é estável ou instável?).
  - [ ] **Relativa:** *quão* estável o sistema é? (distância dos polos ao eixo $j\omega$, amortecimento, compromisso entre estabilidade e manobrabilidade).
- [ ] **1.3. Dominar as duas definições matemáticas de estabilidade (Sistemas LIT)**
  - [ ] **Estabilidade BIBO (*Bounded-Input, Bounded-Output*):** entrada limitada $|r(t)| \le M < \infty \implies$ saída limitada $|y(t)| \le N < \infty$. Condição na resposta ao impulso: $\int_0^\infty |g(\tau)|\,d\tau < \infty$.
  - [ ] **Estabilidade Assintótica (entrada nula, condições iniciais não nulas):** a resposta é limitada e volta ao equilíbrio quando $t \to \infty$ ($\lim_{t \to \infty} |y(t)| = 0$).
  - [ ] Visualizar a analogia física da **bola na cuba** (cuba p/ cima com atrito = assintoticamente estável; plano sem atrito = marginalmente estável; cuba p/ baixo = instável).
- [ ] **1.4. Memorizar a Regra de Ouro da Posição dos Polos no Plano $s$**
  - [ ] **Absolutamente Estável:** TODOS os polos de malha fechada estão no **Semiplano Esquerdo (SPE)** ($\text{Re}(s) < 0$).
  - [ ] **Marginalmente Estável:** Existem polos **simples (não repetidos)** sobre o eixo imaginário $j\omega$ ($\text{Re}(s) = 0$) e todos os outros estão no SPE ($\text{Re}(s) < 0$).
  - [ ] **Absolutamente Instável:** Existe pelo menos **1 polo no Semiplano Direito (SPD)** ($\text{Re}(s) > 0$) **OU** existem **polos múltiplos (repetidos) sobre o eixo $j\omega$** (que geram termos crescentes $t^n \cos(\omega t + \phi)$).
- [ ] **1.5. Prática Rápida (Slide 13):**
  - [ ] Refazer o **Exercício 1 dos Slides** sem olhar a resposta e confirmar que **zeros** no semiplano direito (ex.: $s - 1$ no numerador) **não** afetam a estabilidade (apenas os **polos** importam!).

---

## Etapa 2: Condição Necessária e Tabela de Routh Padrão (Slides 18 a 37)
*Objetivo: Montar a Tabela de Routh rapidamente e sem errar sinais nos determinantes.*

- [ ] **2.1. Aplicar o "Filtro Rápido" (Condição Necessária, mas NÃO Suficiente — Slide 25)**
  - [ ] Antes de fazer qualquer conta em um polinômio $\Delta(s) = a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0 = 0$, checar:
    1. **Todos os coeficientes existem (nenhum é zero)?**
    2. **Todos os coeficientes têm o mesmo sinal?**
  - [ ] Saber que: se falhar em (1) ou (2), o sistema **já NÃO é estável** (é instável ou, no máximo, marginalmente estável). Se passar em (1) e (2), é **obrigatório** montar a Tabela de Routh (para $n \ge 3$).
- [ ] **2.2. Montar a Tabela de Routh no Caso Padrão (4 Passos — Slides 26 a 30)**
  - [ ] **Passo 1:** Organizar os coeficientes nas duas primeiras linhas ($s^n$ e $s^{n-1}$) em zigue-zague (cima-baixo, cima-baixo).
  - [ ] **Passo 2 e 3:** Calcular os elementos $b_i, c_i, \dots$ até a linha $s^0$ usando o pivô da linha anterior:
    $$b_1 = -\frac{\begin{vmatrix} a_n & a_{n-2} \\ a_{n-1} & a_{n-3} \end{vmatrix}}{a_{n-1}} = \frac{a_{n-1}a_{n-2} - a_n a_{n-3}}{a_{n-1}}$$
  - [ ] **Passo 4:** Contar o número de **trocas de sinal na 1ª coluna** = número exato de polos no **Semiplano Direito (SPD)**.
- [ ] **2.3. Decorar os Atalhos de 2ª e 3ª Ordem (Exercício 2 dos Slides — Slides 31 a 33)**
  - [ ] **2ª Ordem ($a_2 s^2 + a_1 s + a_0 = 0$):** Estável $\iff$ todos os coeficientes têm o mesmo sinal.
  - [ ] **3ª Ordem ($a_3 s^3 + a_2 s^2 + a_1 s + a_0 = 0$, com $a_i > 0$):**
    - Estável $\iff a_2 a_1 > a_3 a_0$ (**produto dos meios $>$ produto dos extremos**).
    - Marginalmente estável (polos em $\pm j\omega$) $\iff a_2 a_1 = a_3 a_0$.
- [ ] **2.4. Prática do Caso Padrão:**
  - [ ] Refazer o **Exercício 3 dos Slides** (Slide 35: $2s^4 + s^3 + 3s^2 + 5s + 10$).
  - [ ] Resolver a **Questão 1 da Lista 4** (itens a, b, c).

---

## Etapa 3: Os 4 Casos Especiais de Routh-Hurwitz (Slides 38 a 59)
*Objetivo: Não travar na prova quando aparecer um zero na tabela!*

- [ ] **3.1. Caso Especial 1: Zero isolado na 1ª coluna (demais elementos da linha $\neq 0$) — Slides 38 a 44**
  - [ ] **Método do $\epsilon$:** Substituir o $0$ por $\epsilon > 0$ ($\epsilon \to 0^+$), continuar os cálculos até o fim e analisar os sinais quando $\epsilon \to 0^+$.
  - [ ] **Método dos Polos Recíprocos:** Inverter a ordem dos coeficientes do polinômio ($a_n \leftrightarrow a_0$, $a_{n-1} \leftrightarrow a_1$, etc.) e montar uma nova tabela de Routh para confirmar o número de trocas de sinal.
  - [ ] Praticar: **Exercício 4 dos Slides** (Slides 40-44) e **Questão 3 da Lista 4**.
- [ ] **3.2. Caso Especial 2: Linha inteira igual a zero (Polos Simétricos) — Slides 45 a 54**
  - [ ] Entender o significado físico/matemático: existem **polos simétricos em relação à origem** ($\pm \sigma$, $\pm j\omega$, ou $\pm \sigma \pm j\omega$).
  - [ ] Dominar o procedimento do **Polinômio Auxiliar $P(s)$**:
    1. Pegar os coeficientes da linha **imediatamente acima** da linha nula para formar $P(s)$ (sempre só com potências pares!).
    2. Derivar em relação a $s$: $\frac{dP(s)}{ds}$.
    3. Substituir a linha nula pelos coeficientes da derivada e continuar a tabela até $s^0$.
  - [ ] Saber separar a contagem de polos:
    - Trocas de sinal **acima de $P(s)$** (de $s^n$ até $P(s)$) = polos **não-simétricos** no SPD.
    - Trocas de sinal **abaixo de $P(s)$** (de $P(s)$ até $s^0$) = polos **simétricos** no SPD.
    - Se não houver troca de sinal de $P(s)$ até $s^0$, todos os polos de $P(s)$ estão sobre o **eixo imaginário $j\omega$**!
  - [ ] Saber achar a **frequência de oscilação sustentada ($\omega$):** igualar $P(s) = 0$ no ganho crítico $K_{\text{marginal}}$, achar $s = \pm j\omega$.
  - [ ] Praticar: **Exercícios 5 e 6 dos Slides** (Slides 48-54) e **Questões 4 e 5(a) da Lista 4**.
- [ ] **3.3. Caso Especial 3: Duas linhas inteiras iguais a zero — Slides 55 a 57**
  - [ ] Reconhecer que ocorre em linhas $s^j$ ímpares quando há **polos simétricos duplos (repetidos)**.
  - [ ] Saber que o sistema é **SEMPRE INSTÁVEL** (mesmo que os polos duplos estejam no eixo $j\omega$, pois são repetidos!).
  - [ ] Praticar: **Exercício 7 dos Slides** (Slides 56-57).
- [ ] **3.4. Caso Especial 4: Parada prematura da tabela (Polos na Origem) — Slide 58**
  - [ ] Reconhecer que falta o termo independente ($a_0 = 0$, etc.), indicando $j$ polos na origem ($s = 0$).
  - [ ] Colocar $s^j$ em evidência: $\Delta(s) = s^j \Delta'(s)$, aplicar Routh em $\Delta'(s)$ e lembrar que se $j=1$ o sistema é no máximo **marginalmente estável**, e se $j > 1$ é **instável**.

---

## Etapa 4: Estabilidade Relativa e Deslocamento de Eixo (Slides 61 a 67)
*Objetivo: Descobrir em que região estão os polos mais lentos (dominantes) usando Routh.*

- [ ] **4.1. Entender a mudança de variável $s = s' - \sigma_1$**
  - [ ] Deslocar o eixo imaginário para a esquerda em $\sigma_1 > 0$ unidades significa substituir todo $s$ por $(s' - \sigma_1)$ em $\Delta(s)$.
  - [ ] Aplicar Routh ao novo polinômio em $s'$: o número de trocas de sinal na 1ª coluna indica quantos polos têm parte real **maior que $-\sigma_1$** (isto é, estão à direita da reta $\text{Re}(s) = -\sigma_1$).
  - [ ] Se a última linha zerar (ou surgir linha nula sem trocas antes), há polos **exatamente sobre a reta $\text{Re}(s) = -\sigma_1$**.
- [ ] **4.2. Prática de Estabilidade Relativa:**
  - [ ] Refazer o **Exercício 8 dos Slides** (Slides 64-67: $\Delta(s) = s^3 + 4s^2 + 6s + 4$ com $\sigma_1 = 1/2$ e $\sigma_1 = 2$).
  - [ ] Resolver a **Questão 8 da Lista 4** (itens a, b, c).

---

## Etapa 5: Análise Paramétrica e Sintonia de Controladores (Slides 68 a 78)
*Objetivo: Determinar faixas de ganhos ($K$, $K_p$, $K_i$, $K_d$, $a$, $T$) para garantir estabilidade e desempenho.*

- [ ] **5.1. Dominar o roteiro de questões com 1 parâmetro ($K$)**
  - [ ] Obter a equação característica de malha fechada: $1 + G_c(s)G(s)H(s) = 0$.
  - [ ] Montar a Tabela de Routh em função de $K$.
  - [ ] Impor que **todos os termos da 1ª coluna sejam $> 0$** e achar a interseção das inequações.
  - [ ] Praticar: **Exercício 9 dos Slides** (Slides 69-70) e **Questões 2, 4, 5 e 10 da Lista 4**.
- [ ] **5.2. Dominar o roteiro de questões com 2 parâmetros (Controladores PI, PD, avanço/atraso)**
  - [ ] Montar a equação característica com os dois parâmetros (ex.: $K_p$ e $K_i$, ou $k_p$ e $k_d$, ou $K$ e $a$, ou $K$ e $T$).
  - [ ] Extrair as inequações da 1ª coluna da Tabela de Routh.
  - [ ] Se houver requisito de **erro estacionário** (ex.: entrada em rampa $e_{ss} = \lim_{s \to 0} s E(s) = \frac{1}{K_v} \le e_{\max}$), combinar a inequação do erro com as inequações de Routh.
  - [ ] Praticar: **Exercício 10 dos Slides** (Slides 74-78) e **Questões 6, 7 e 9 da Lista 4**.

---

## Etapa 6: Checklist de Resolução da Lista 4 (Treino Final de Prova)
*Resolva cada questão no papel e confira no PDF de resoluções ([EL466 Lista 4 resolucoes.pdf](file:///home/luan/Projetos/UFPE/Controle2/2/EL466%20Lista%204%20Estabilidade%20e%20Criterio%20de%20Routh-Hurwitz%20resolucoes.pdf)):*

- [ ] **Questão 1 (Golnaraghi 5-3):** Tabela de Routh direta e contagem de raízes no SPD (atenção ao item *c* com termo $s^2$ ausente!).
- [ ] **Questão 2 (Dorf E6.1):** Faixa de $K$ levando a uma inequação de 2º grau na linha $s^1$ ($5K^2 - 2K - 15 > 0$).
- [ ] **Questão 3 (Autoral Monitor/Prof.):** Caso Especial 1 resolvido pelos dois métodos: **Método do $\epsilon$** e **Polinômio Recíproco**. *(Altíssima chance de cair na prova!)*
- [ ] **Questão 4 (Dorf P6.16):** Ganho máximo $K_{\max}$ e cálculo da frequência de oscilação $\omega$ via Polinômio Auxiliar $P(s)$ (Caso Especial 2).
- [ ] **Questão 5 (Golnaraghi 5-6):** Faixa de estabilidade, $K_{\text{marginal}}$, frequência $\omega$ (item *a*) e identificação imediata de instabilidade por termo ausente (item *b*).
- [ ] **Questão 6 (Autoral Monitor/Prof.):** Sintonia de **Controlador PI** ($K_p$ e $K_i$) via Routh-Hurwitz. *(Questão clássica de prova!)*
- [ ] **Questão 7 (Golnaraghi 5-7):** Região de estabilidade no plano $T \times K$ (análise em dois casos: $T \le 1/3$ e $T > 1/3$) e fronteira marginal.
- [ ] **Questão 8 (Dorf P6.5):** Estabilidade relativa por deslocamento de eixo ($s = s' - \sigma_1$).
- [ ] **Questão 9 (Golnaraghi 5-13):** Estabilização de **pêndulo invertido** (planta instável $G(s) = \frac{1}{s^2 - 4}$) com **Controlador PD + atuador**.
- [ ] **Questão 10 (Dorf DP6.2):** Veículo em Marte com realimentação não-unitária $H(s) = Ks + 1$, cálculo de $K$ para polo em $s = -1$, divisão polinomial e análise da resposta ao degrau pelo polo dominante.

---

## Etapa 7: Revisão Relâmpago (15 Minutos Antes da Prova)
- [ ] **Cuidado 1:** Nunca aplique Routh direto na função de transferência de malha aberta $G(s)H(s)$ se a questão pedir estabilidade em **malha fechada**! Primeiro feche a malha: $\Delta(s) = D_{MA}(s) + N_{MA}(s) = 0$ (ou $1 + G(s)H(s) = 0$).
- [ ] **Cuidado 2:** Se faltar uma potência de $s$ no polinômio (ex.: tem $s^4, s^3, s^1, s^0$, mas não tem $s^2$), coloque **$0$** no lugar daquele coeficiente na tabela de Routh! Não pule o termo!
- [ ] **Cuidado 3:** Na fórmula de Routh, o determinante $2 \times 2$ tem um **sinal de menos na frente**: $b_1 = \frac{\text{pivô} \cdot (\text{cima-direita}) - (\text{cima-esquerda}) \cdot (\text{baixo-direita})}{\text{pivô}}$.
- [ ] **Cuidado 4:** No Caso Especial 2 (linha nula), o polinômio auxiliar $P(s)$ é montado com a linha **ACIMA** da linha que zerou, e **só tem expoentes pares** ($s^4, s^2, s^0$ ou $s^2, s^0$).
- [ ] **Cuidado 5:** Polos simples no eixo $j\omega$ = **marginalmente estável**. Polos repetidos (duplos) no eixo $j\omega$ = **INSTÁVEL**!
