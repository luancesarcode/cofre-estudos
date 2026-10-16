---
tipo: aula
data: 2026-08-19
cadeira: "[[Controle 2]]"
unidade: 1
tema: 2
tags: [aula, controle]
---

# Tema 2 — Desempenho de sistemas de 1ª e 2ª ordens

## Formulário de consulta rápida

Expressões do formulário enviado para a resolução da lista. As fórmulas de regime permanente pressupõem estabilidade e validade do teorema do valor final. As respostas de referência são ao degrau unitário, salvo indicação contrária.

### Sistemas de 1ª ordem

$$\boxed{G(s)=\frac{K}{Ts+1}=\frac{Ka}{s+a}}.$$

| Grandeza | Expressão |
|---|---|
| Ganho estático | $K=G(0)=c_{\mathrm{ss}}$ para degrau unitário |
| Constante de tempo | $T$: instante em que a saída atinge 63,2% do valor final |
| Frequência exponencial | $a=1/T$ |
| Tempo de subida, de 10% a 90% | $T_r\approx2{,}2T$ |
| Tempo de acomodação | $T_s(5\%)\approx3T$; $T_s(2\%)\approx4T$; $T_s(1\%)\approx5T$ |
| Erro estacionário ao degrau unitário | $e(\infty)=1-K$ |

### Sistemas de 2ª ordem

$$\boxed{G(s)=\frac{K\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}}.$$

Para o caso subamortecido:

$$p_{1,2}=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}=-\alpha\pm j\omega_d,$$

$$\alpha=\zeta\omega_n,\qquad\omega_d=\omega_n\sqrt{1-\zeta^2}.$$

| Grandeza | Expressão |
|---|---|
| Tempo de pico | $\displaystyle T_p=\frac{\pi}{\omega_n\sqrt{1-\zeta^2}}=\frac{\pi}{\omega_d}$ |
| Sobressinal máximo, para valor final unitário | $\displaystyle M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| Sobressinal percentual | $\displaystyle M_p\%=100e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| Tempo de atraso — ajuste de ordem 1 | $\displaystyle T_d\approx\frac{0{,}920\zeta+0{,}859}{\omega_n}$ |
| Tempo de atraso — ajuste de ordem 2 | $\displaystyle T_d\approx\frac{0{,}284\zeta^2+0{,}352\zeta+1{,}048}{\omega_n}$ |
| Tempo de subida — ajuste de ordem 1 | $\displaystyle T_{r1}\approx\frac{3{,}893\zeta-0{,}065}{\omega_n}$ |
| Tempo de subida — ajuste de ordem 2 | $\displaystyle T_{r1}\approx\frac{1{,}313\zeta^2+1{,}267\zeta+0{,}811}{\omega_n}$ |
| Tempo de subida — ajuste de ordem 3 | $\displaystyle T_{r1}\approx\frac{-0{,}965\zeta^3+4{,}209\zeta^2-1{,}050\zeta+1{,}196}{\omega_n}$ |
| Erro estacionário ao degrau unitário | $e(\infty)=1-K$ |

As fórmulas de pico e sobressinal aplicam-se ao modelo-padrão sem zeros com $0<\zeta<1$. Os ajustes de atraso e subida são apresentados para $0\leq\zeta\leq2$; são aproximações e podem ser ruins nas extremidades. Por exemplo, o ajuste linear de subida dá valor negativo perto de $\zeta=0$, sem significado físico. $T_{r1}$ corresponde à subida de 10% a 90%.

**Amortecimento a partir do sobressinal:** a expressão aparece quebrada na captura; sua forma completa é, com $m=M_p\%/100$ e $0<m<1$:

$$\boxed{\zeta=\frac{-\ln m}{\sqrt{\pi^2+(\ln m)^2}}}.$$

### Tempo de acomodação de 2ª ordem

A tabela enviada vale para $0{,}1\leq\zeta\leq2$. Use a coluna esquerda quando $\zeta<\zeta_{\mathrm{limite}}$ e a direita quando $\zeta\geq\zeta_{\mathrm{limite}}$.

| Faixa | $\zeta$ abaixo do limite | $\zeta$ no limite ou acima | $\zeta_{\mathrm{limite}}$ |
|---|---|---|---:|
| 5% | $\displaystyle T_s\approx\frac{2{,}798}{\zeta\omega_n}$ | $\displaystyle T_s\approx\frac{6{,}772\zeta-1{,}967}{\omega_n}$ | 0,691 |
| 2% | $\displaystyle T_s\approx\frac{3{,}716}{\zeta\omega_n}$ | $\displaystyle T_s\approx\frac{9{,}274\zeta-3{,}394}{\omega_n}$ | 0,780 |
| 1% | $\displaystyle T_s\approx\frac{4{,}412}{\zeta\omega_n}$ | $\displaystyle T_s\approx\frac{11{,}113\zeta-4{,}388}{\omega_n}$ | 0,826 |

**Orientação do formulário:** nesta disciplina, use os ajustes da tabela em vez de aproximações mais grosseiras de livros, como $T_s(2\%)\approx4/(\zeta\omega_n)$. Os resultados numéricos podem diferir dos gabaritos que usam outras aproximações.

**Compatibilidade com o resumo:** os slides arredondam o limite de 5% para 0,69 em algumas equações; este quadro mantém 0,691, como na imagem enviada. Os ajustes lineares e quadrático de subida foram incluídos porque aparecem no formulário; os slides riscados priorizam o ajuste quadrático de atraso e o cúbico de subida, usados no desenvolvimento abaixo.

### Classificação quanto ao amortecimento

| Condição | Classificação |
|---|---|
| $\zeta>1$ | Superamortecido |
| $\zeta=1$ | Criticamente amortecido |
| $0<\zeta<1$ | Subamortecido |
| $\zeta=0$ | Não amortecido |
| $\zeta<0$ | Amortecimento negativo: instável |

---

## Resumo explicado

Resumo para estudo e transcrição no caderno, com fórmulas, exemplos resolvidos e imagens dos slides.

**Fonte:** Fabrício Bradaschia, UFPE, *Tema 2 — Desempenho de Sistemas de Controle de 1ª e 2ª Ordens*, slides 1 a 72. As imagens numeradas são reproduções do material original; os gráficos complementares foram elaborados para este resumo.

**Hipóteses:** condições iniciais nulas e modelos lineares. Salvo indicação contrária, as fórmulas de desempenho consideram os modelos-padrão sem zeros e resposta ao degrau. A saída aparece como $C(s)$ ou $Y(s)$ nos slides; aqui usamos $Y(s)$.

## 1. O que é desempenho?

O tema relaciona a função de transferência com quatro propriedades:

- **Rapidez:** quanto tempo a saída demora para responder.
- **Oscilação:** se ultrapassa o valor final e oscila antes de se acomodar.
- **Precisão:** diferença que permanece entre referência e saída.
- **Estabilidade:** comportamento dos modos naturais ao longo do tempo.

$$\boxed{y(t)=y_{\mathrm{tr}}(t)+y_{\mathrm{ss}}(t)}.$$

A parcela transitória desaparece em sistemas assintoticamente estáveis. O regime permanente é o comportamento restante: pode ser constante para degrau ou senoidal para entrada senoidal, por exemplo.

## 2. Sinais de teste

Entradas padronizadas permitem comparar sistemas e escolher testes próximos das situações reais.

| Entrada para $t\geq0$ | Laplace | Interpretação |
|---|---|---|
| Degrau: $r(t)=A$ | $A/s$ | Mudança brusca de referência |
| Rampa: $r(t)=At$ | $A/s^2$ | Crescimento a velocidade constante |
| Parábola do slide: $r(t)=At^2$ | $2A/s^3$ | Crescimento com aceleração constante $2A$ |
| Impulso: $A\delta(t)$ | $A$ | Excitação idealizada muito curta |
| Senoide: $A\sin(\omega t)$ | $A\omega/(s^2+\omega^2)$ | Excitação periódica |

Outra convenção comum é escrever a parábola como $At^2/2$, cuja transformada é $A/s^3$ e cuja aceleração é $A$. As duas convenções são corretas; aqui a tabela acompanha a imagem do slide.

O material também cita ruído branco, útil em identificação e análises específicas.

![[03_Recursos/Controle 2/imagens/tema_2/slide_05.png]]

*Slide 5. Degrau, rampa e parábola representam perfis distintos de referência.*

## 3. Polos, zeros e dinâmica

Para a função reduzida $G(s)=N(s)/D(s)$:

- **Zeros:** raízes do numerador, representados por círculos no plano $s$.
- **Polos:** raízes do denominador, representados por cruzes.

$$s=\sigma+j\omega.$$

O eixo horizontal representa a parte real; o vertical, a parte imaginária.

| Polo ou par de polos | Comportamento temporal |
|---|---|
| $-a$, com $a>0$ | Exponencial decrescente $e^{-at}$ |
| $+a$, com $a>0$ | Exponencial crescente $e^{at}$: instabilidade |
| $-\alpha\pm j\omega_d$ | Oscilação multiplicada por $e^{-\alpha t}$ |
| $\pm j\omega_d$ | Oscilação persistente |

Um polo real em $-5$ gera um decaimento mais rápido que um polo em $-1$, pois $e^{-5t}$ desaparece antes de $e^{-t}$.

![[03_Recursos/Controle 2/imagens/tema_2/slide_10.png]]

*Slide 10. Para $G(s)=(s+2)/(s+5)$, o zero está em $-2$ e o polo em $-5$.*

Aplicando um degrau unitário:

$$Y(s)=\frac{s+2}{s(s+5)}=\frac{2/5}{s}+\frac{3/5}{s+5}.$$

$$y(t)=\frac25+\frac35e^{-5t},\qquad t\geq0.$$

![[03_Recursos/Controle 2/imagens/tema_2/slide_11.png]]

*Slide 11. O polo do degrau na origem gera o termo constante; o polo do sistema gera o termo exponencial. O zero influencia os coeficientes.*

**Cuidado:** o polo na origem introduzido por $R(s)=1/s$ pertence à entrada, não à função de transferência da planta. Os zeros alteram a forma da resposta, por isso as fórmulas dos modelos sem zeros não se aplicam automaticamente a qualquer sistema.

## 4. Primeira ordem: forma-padrão

$$\boxed{G(s)=\frac{K}{Ts+1}=\frac{Ka}{s+a}},\qquad a=\frac1T.$$

| Parâmetro | Significado |
|---|---|
| $K=G(0)$ | Ganho estático |
| $T>0$ | Constante de tempo, em segundos |
| $a=1/T$ | Frequência exponencial |
| $p=-1/T$ | Polo do sistema |

**$K$ determina o valor final; $T$ determina a rapidez.**

Para degrau de amplitude $A$:

$$Y(s)=\frac{AK}{s(Ts+1)}=AK\left(\frac1s-\frac1{s+1/T}\right).$$

$$\boxed{y(t)=AK(1-e^{-t/T})},\qquad \boxed{y_\infty=AK}.$$

### Constante de tempo

Em $t=T$:

$$y(T)=AK(1-e^{-1})\approx0{,}632AK.$$

Portanto, $T$ é o tempo para atingir **63,2% do valor final**.

| Instante | Percentual do valor final |
|---|---:|
| $T$ | 63,2% |
| $2T$ | 86,5% |
| $3T$ | 95,0% |
| $4T$ | 98,2% |
| $5T$ | 99,3% |

![[03_Recursos/Controle 2/imagens/tema_2/slide_15.png]]

*Slide 15. A tangente inicial também encontra a linha do valor final em $t=T$. Para degrau unitário, a inclinação inicial é $K/T$.*

![[03_Recursos/Controle 2/imagens/tema_2/tema2_primeira_ordem.png]]

*Mesmo ganho estático, constantes de tempo diferentes: menor $T$ significa resposta mais rápida.*

### Como obter os parâmetros experimentalmente

Para um degrau de amplitude $A$, partindo de condições nulas, $K=y_\infty/A$. O instante em que a saída chega a 63,2% do valor final fornece $T$. Em ensaios ao redor de um ponto de operação, use as variações de entrada e saída: $K=\Delta y_\infty/\Delta r$.

## 5. Primeira ordem: tempos e erro

### Tempo de subida, de 10% a 90%

Para atingir uma fração $q$ do valor final:

$$q=1-e^{-t/T}\quad\Rightarrow\quad t=-T\ln(1-q).$$

$$t_{10\%}\approx0{,}105T,\qquad t_{90\%}\approx2{,}303T.$$

$$\boxed{T_r=t_{90\%}-t_{10\%}\approx2{,}2T}.$$

### Tempo de acomodação

É o tempo para entrar e permanecer na faixa de tolerância em torno do valor final. Para tolerância relativa $\delta$:

$$\boxed{T_s=-T\ln\delta}.$$

| Faixa | Valor calculado | Arredondamento do tema |
|---|---:|---:|
| 5% | $2{,}996T$ | $3T$ |
| 2% | $3{,}912T$ | $4T$ |
| 1% | $4{,}605T$ | $5T$ |

### Erro estacionário

$$\boxed{e_{\mathrm{ss}}=A-AK=A(1-K)}.$$

Para degrau unitário, $e_{\mathrm{ss}}=1-K$. Acomodar-se rapidamente não garante acertar a referência: a saída pode estabilizar em um valor incorreto.

### Exemplo

$$G(s)=\frac2{3s+1}.$$

Identificamos $K=2$ e $T=3$ s. Para degrau unitário:

$$y_\infty=2,\quad T_r\approx6{,}6\text{ s},\quad T_s(2\%)\approx12\text{ s},\quad e_{\mathrm{ss}}=-1.$$

O erro negativo indica saída acima da referência.

## 6. Segunda ordem: forma-padrão e identificação

$$\boxed{G(s)=\frac{K\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}}.$$

| Parâmetro | Significado |
|---|---|
| $K$ | Ganho estático |
| $\omega_n$ | Frequência natural não amortecida, em rad/s |
| $\zeta$ | Coeficiente de amortecimento, sem unidade |
| $\alpha=\zeta\omega_n$ | Taxa de decaimento da envoltória no caso subamortecido |
| $\omega_d=\omega_n\sqrt{1-\zeta^2}$ | Frequência amortecida no caso subamortecido |

Se a função for:

$$G(s)=\frac{b_0}{s^2+a_1s+a_0},$$

compare coeficientes:

$$\boxed{\omega_n=\sqrt{a_0}},\qquad \boxed{\zeta=\frac{a_1}{2\sqrt{a_0}}},\qquad \boxed{K=\frac{b_0}{a_0}}.$$

Se o coeficiente de $s^2$ não for 1, divida numerador e denominador por ele antes de comparar.

**Exemplo:**

$$G(s)=\frac{16}{s^2+4s+16}.$$

$$\omega_n=\sqrt{16}=4\text{ rad/s},\qquad \zeta=\frac4{2(4)}=0{,}5,\qquad K=1.$$

## 7. Classificação pelo amortecimento

Para $\omega_n>0$:

| Coeficiente | Classificação | Polos e resposta ao degrau do modelo-padrão |
|---|---|---|
| $\zeta>1$ | Superamortecido | Dois polos reais negativos distintos; sem oscilação |
| $\zeta=1$ | Criticamente amortecido | Polo duplo em $-\omega_n$; resposta mais rápida sem sobressinal para $\omega_n$ fixo |
| $0<\zeta<1$ | Subamortecido | Polos complexos à esquerda; oscilações decrescentes |
| $\zeta=0$ | Não amortecido | Polos imaginários puros; oscilações persistentes |
| $\zeta<0$ | Amortecimento negativo | Polos no semiplano direito; instabilidade |

No caso negativo, $-1<\zeta<0$ gera polos complexos à direita; $\zeta=-1$ gera polo real positivo duplo; $\zeta<-1$ gera dois polos reais positivos.

![[03_Recursos/Controle 2/imagens/tema_2/slide_29.png]]

*Slide 29. A comparação de rapidez sem sobressinal pressupõe a mesma frequência natural e o modelo-padrão sem zeros.*

Para o caso subamortecido:

$$\boxed{p_{1,2}=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}=-\alpha\pm j\omega_d}.$$

Para $\zeta>1$:

$$p_{1,2}=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}.$$

**Parte real:** determina o decaimento. **Parte imaginária:** determina a frequência de oscilação.

O sistema não amortecido não converge ao valor final. Sua resposta livre pode ser limitada, mas ele não é estável no sentido BIBO: uma entrada limitada na frequência de ressonância pode gerar saída crescente.

## 8. Geometria dos polos e significado de cada parâmetro

Para polos subamortecidos:

$$\alpha=\zeta\omega_n,\quad \omega_d=\omega_n\sqrt{1-\zeta^2},\quad \omega_n=\sqrt{\alpha^2+\omega_d^2}.$$

$$\zeta=\frac\alpha{\omega_n}=\cos\theta.$$

O ângulo $\theta$ é medido em relação ao eixo real negativo. A distância do polo até a origem é $\omega_n$.

![[03_Recursos/Controle 2/imagens/tema_2/slide_31.png]]

*Slide 31. O triângulo relaciona $\alpha$, $\omega_d$, $\omega_n$ e $\zeta$. A leitura geométrica com polos complexos aplica-se ao caso subamortecido.*

Mantendo $\zeta$ fixo e aumentando $\omega_n$, comprimimos a resposta no tempo sem alterar seu sobressinal percentual. Se $\omega_n$ dobrar, os tempos característicos caem pela metade.

![[03_Recursos/Controle 2/imagens/tema_2/slide_36.png]]

*Slide 36. Menor $\zeta$ aumenta o sobressinal e as oscilações; para $\zeta\geq1$, o modelo-padrão não ultrapassa o valor final.*

## 9. Resposta temporal de segunda ordem

Para degrau unitário, $K=1$ e $0<\zeta<1$:

$$\boxed{y(t)=1-\frac{e^{-\zeta\omega_nt}}{\sqrt{1-\zeta^2}}\sin(\omega_dt+\arccos\zeta)}.$$

- $1$ é o valor final.
- $e^{-\zeta\omega_nt}$ faz a oscilação desaparecer.
- $\omega_d$ determina sua frequência.
- $\arccos\zeta$ determina a fase.

Para ganho $K$ e degrau de amplitude $A$, multiplique a expressão inteira por $AK$.

Com $K=A=1$, duas outras respostas úteis são:

$$\zeta=1:\quad y(t)=1-(1+\omega_nt)e^{-\omega_nt}.$$

$$\zeta=0:\quad y(t)=1-\cos(\omega_nt).$$

No superamortecido, a resposta tem a forma $y(t)=c_1+c_2e^{p_1t}+c_3e^{p_2t}$, com polos reais negativos distintos.

## 10. Especificações na curva

![[03_Recursos/Controle 2/imagens/tema_2/slide_45.png]]

*Slide 45. Localize valor final, pico, tempo de pico, tempo de subida, tempo de atraso, faixa de acomodação e erro estacionário. A figura é genérica; no modelo-padrão estável com $K=1$, o erro ao degrau unitário é nulo.*

| Indicador | Definição |
|---|---|
| $T_d$ | Primeiro instante em que a saída chega a 50% do valor final |
| $T_{r1}$ | Intervalo entre as primeiras passagens por 10% e 90% do valor final |
| $T_p$ | Instante do primeiro pico no caso subamortecido |
| $M_p$ | Diferença entre pico e valor final |
| $M_p\%$ | Sobressinal dividido pelo valor final, em percentual |
| $T_s$ | Tempo para entrar e permanecer na faixa escolhida |
| $e_{\mathrm{ss}}$ | Erro em regime permanente |

**Notação:** $T_p$ agora é tempo de pico; não é a perturbação $T_p(s)$ do Tema 1. O tempo de atraso $T_d$ não é tempo morto: a resposta já pode estar variando antes dele.

## 11. Tempo de pico e sobressinal

Estas fórmulas valem para o modelo-padrão subamortecido, $0<\zeta<1$.

### Tempo de pico

A derivada da resposta contém $\sin(\omega_dt)$. O primeiro máximo após o início ocorre em $\omega_dT_p=\pi$:

$$\boxed{T_p=\frac\pi{\omega_d}=\frac\pi{\omega_n\sqrt{1-\zeta^2}}}.$$

### Sobressinal

$$\boxed{M_p=y(T_p)-y_\infty}.$$

Para $y_\infty=1$:

$$\boxed{M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}}.$$

Para valor final positivo, o sobressinal percentual é:

$$\boxed{M_p\%=100\frac{y(T_p)-y_\infty}{y_\infty}=100e^{-\pi\zeta/\sqrt{1-\zeta^2}}}.$$

Exemplo: valor final 10 e pico 12 dão sobressinal absoluto 2 e percentual 20%.

| $\zeta$ | Sobressinal aproximado |
|---:|---:|
| 0,2 | 52,7% |
| 0,5 | 16,3% |
| 0,7 | 4,6% |
| 0,8 | 1,5% |

O sobressinal percentual depende apenas de $\zeta$ nesse modelo.

![[03_Recursos/Controle 2/imagens/tema_2/slide_49.png]]

*Slide 49. A curva mostra a redução do sobressinal com o aumento de $\zeta$.*

Para encontrar $\zeta$ a partir do sobressinal desejado, defina $m=M_p\%/100$, com $0<m<1$:

$$\boxed{\zeta=\frac{-\ln m}{\sqrt{\pi^2+(\ln m)^2}}}.$$

Para 5%, use $m=0{,}05$, obtendo $\zeta\approx0{,}690$.

## 12. Tempo de atraso e tempo de subida

O material mantém as seguintes aproximações, válidas para $0\leq\zeta\leq2$.

**Tempo de atraso, ajuste quadrático:**

$$\boxed{T_d\approx\frac{0{,}284\zeta^2+0{,}352\zeta+1{,}048}{\omega_n}}.$$

**Tempo de subida de 10% a 90%, ajuste cúbico:**

$$\boxed{T_{r1}\approx\frac{-0{,}965\zeta^3+4{,}209\zeta^2-1{,}050\zeta+1{,}196}{\omega_n}}.$$

São ajustes aproximados, não expressões exatas. As aproximações de menor ordem estão riscadas nos slides 50 e 52; por isso, não são usadas aqui.

## 13. Tempo de acomodação: fórmulas do Tema 2

O tempo de acomodação é o tempo para entrar e **permanecer** numa faixa em torno do valor final. Para $y_\infty=1$ e faixa de 2%:

$$0{,}98\leq y(t)\leq1{,}02.$$

Entrar e sair depois não significa estar acomodado. O tempo exato depende de qual é a última ultrapassagem da faixa, podendo mudar bruscamente quando um pico passa a caber dentro dela.

### Faixa de 5%

$$T_s\approx\begin{cases}\dfrac{2{,}798}{\zeta\omega_n},&0{,}1\leq\zeta<0{,}69,\\[6pt]\dfrac{6{,}772\zeta-1{,}967}{\omega_n},&0{,}69\leq\zeta\leq2.\end{cases}$$

### Faixa de 2%

$$T_s\approx\begin{cases}\dfrac{3{,}716}{\zeta\omega_n},&0{,}1\leq\zeta<0{,}78,\\[6pt]\dfrac{9{,}274\zeta-3{,}394}{\omega_n},&0{,}78\leq\zeta\leq2.\end{cases}$$

### Faixa de 1%

$$T_s\approx\begin{cases}\dfrac{4{,}412}{\zeta\omega_n},&0{,}1\leq\zeta<0{,}826,\\[6pt]\dfrac{11{,}113\zeta-4{,}388}{\omega_n},&0{,}826\leq\zeta\leq2.\end{cases}$$

![[03_Recursos/Controle 2/imagens/tema_2/slide_60.png]]

*Slide 60. A curva exata tem descontinuidades e detalhes que não são reproduzidos pelos ajustes suaves. Use as fórmulas como estimativas dentro dos intervalos indicados.*

**Interpretação:** com pouco amortecimento, a demora vem das oscilações. Com amortecimento elevado, a demora vem de uma resposta lenta. Portanto, aumentar $\zeta$ não reduz $T_s$ indefinidamente.

O tema destaca valores próximos de $\zeta=0{,}691$ para 5%, $0{,}78$ para 2% e $0{,}827$ para 1%, associados a respostas rápidas dentro dessas tolerâncias. O material recomenda escolher um valor ligeiramente superior para evitar que pequenas variações façam um pico ultrapassar a faixa. Valores arredondados não devem ser tratados como limiares exatos.

## 14. Erro estacionário

Para o modelo-padrão estável:

$$G(0)=\frac{K\omega_n^2}{\omega_n^2}=K.$$

Para degrau de amplitude $A$:

$$y_\infty=AK,\qquad \boxed{e_{\mathrm{ss}}=A(1-K)}.$$

Para degrau unitário:

$$\boxed{e_{\mathrm{ss}}=1-K}.$$

Assim, $K=1$ zera o erro ao degrau nesse modelo estável. Isso não garante erro nulo à rampa ou a outras entradas.

O teorema do valor final exige verificar suas condições. Não se deve usá-lo para atribuir valor final à resposta oscilatória persistente de $\zeta=0$.

## 15. Exemplo completo de segunda ordem

$$G(s)=\frac{16}{s^2+4s+16}.$$

### Passo 1 — Parâmetros e classificação

$$K=1,\quad\omega_n=4\text{ rad/s},\quad\zeta=0{,}5.$$

Como $0<\zeta<1$, a resposta é subamortecida.

### Passo 2 — Polos e frequência amortecida

$$\alpha=\zeta\omega_n=2,\qquad\omega_d=4\sqrt{0{,}75}\approx3{,}464\text{ rad/s}.$$

$$p_{1,2}=-2\pm j3{,}464.$$

### Passo 3 — Pico

$$T_p=\frac\pi{3{,}464}\approx0{,}907\text{ s}.$$

$$M_p\%=100e^{-\pi(0{,}5)/\sqrt{0{,}75}}\approx16{,}3\%.$$

Como $y_\infty=1$, o pico vale aproximadamente $1{,}163$.

### Passo 4 — Tempos aproximados

$$T_d\approx\frac{0{,}284(0{,}5)^2+0{,}352(0{,}5)+1{,}048}{4}=0{,}324\text{ s}.$$

$$T_{r1}\approx\frac{-0{,}965(0{,}5)^3+4{,}209(0{,}5)^2-1{,}050(0{,}5)+1{,}196}{4}\approx0{,}401\text{ s}.$$

Para acomodação de 2%, usamos a expressão do intervalo $0{,}1\leq\zeta<0{,}78$:

$$T_s\approx\frac{3{,}716}{0{,}5(4)}=1{,}858\text{ s}.$$

Esse tempo de acomodação é uma estimativa pelo ajuste do material.

### Passo 5 — Erro

$$e_{\mathrm{ss}}=1-K=0.$$

![[03_Recursos/Controle 2/imagens/tema_2/tema2_segunda_ordem.png]]

*À direita, o exemplo resolvido: a saída chega a aproximadamente 1,163 antes de se acomodar em torno de 1. A faixa verde representa a tolerância de 2%.*

## 16. Movimento dos polos e desempenho

### Movimento horizontal: mesma parte imaginária

Se $\omega_d$ permanece constante, o tempo de pico permanece constante:

$$T_p=\pi/\omega_d.$$

![[03_Recursos/Controle 2/imagens/tema_2/slide_66.png]]

*Slide 66. Os polos mantêm a frequência de oscilação, mas a taxa de decaimento muda.*

### Movimento radial: mesmo ângulo

Manter o ângulo com o eixo real negativo mantém $\zeta$ constante e, portanto, o mesmo sobressinal percentual. Aumentar a distância à origem aumenta $\omega_n$ e acelera a resposta.

![[03_Recursos/Controle 2/imagens/tema_2/slide_67.png]]

*Slide 67. A forma normalizada e o sobressinal permanecem, enquanto a escala de tempo muda.*

### Movimento vertical: mesma parte real

Manter $\alpha$ constante mantém aproximadamente o tempo de acomodação no intervalo em que vale:

$$T_s(2\%)\approx\frac{3{,}716}{\alpha}.$$

![[03_Recursos/Controle 2/imagens/tema_2/slide_68.png]]

*Slide 68. A envoltória exponencial tem a mesma taxa de decaimento; o tempo exato de acomodação ainda pode variar com as oscilações. A invariância é aproximada.*

### Polo dominante no superamortecido

Com polos muito separados, o mais próximo da origem costuma dominar a parcela lenta. Se $p_1=-20$ e $p_2=-1$, o termo $e^{-20t}$ desaparece rapidamente, restando principalmente o modo $e^{-t}$.

Depois do transitório rápido, pode ser útil aproximar o sistema por primeira ordem com:

$$T\approx-\frac1{p_2}=1\text{ s}.$$

## 17. Roteiro para resolver exercícios

1. Coloque a função de transferência na forma-padrão.
2. Identifique $K,T$ ou $K,\zeta,\omega_n$.
3. Calcule os polos e classifique a resposta.
4. Confira a entrada e a faixa de acomodação pedidas.
5. Escolha as fórmulas válidas para o modelo e o intervalo de amortecimento.
6. Calcule tempos, sobressinal e erro; diferencie resultados exatos de aproximações.

**Para memorizar:** na primeira ordem, $K$ ajusta o destino e $T$ a rapidez. Na segunda ordem, $K$ ajusta o valor final, $\zeta$ a forma e o sobressinal, e $\omega_n$ a escala de tempo quando $\zeta$ é mantido fixo.
