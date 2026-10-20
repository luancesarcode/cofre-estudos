# 7. Ziegler–Nichols, SO-OV e NO-OV

## 1. O que você precisa decidir antes da tabela

**Malha aberta:** aplica-se um degrau à planta e ajusta-se uma aproximação por curva de reação em S. É preciso uma resposta que se acomode, com tangente útil no ponto de inflexão.

**Malha fechada:** usa-se inicialmente **controle proporcional puro**, aumenta-se $K$ e procura-se um ganho crítico finito com oscilação sustentada. Routh fornece esse limite nos exercícios.

Uma planta com integrador não se acomoda a um degrau em malha aberta. Uma resposta fortemente oscilatória não é apropriada ao ajuste clássico em S. A simples existência de polos complexos, isoladamente, não substitui a análise da resposta.

Nas provas, a malha fechada é usada em 2023.1, 2023.2, 2024.1, 2024.2 e 2026.1. A Revisão 2EE também exige fazer a sintonia em malha aberta.

## 2. Malha fechada: algoritmo completo

1. Substitua temporariamente o controlador por $K$.
2. Calcule $\Delta=D+KN$.
3. Ache o limite de estabilidade $K_{cr}$ por Routh.
4. Use o polinômio auxiliar para achar $\omega_{cr}$.
5. Calcule $P_{cr}=2\pi/\omega_{cr}$.
6. Use a linha da tabela pedida.
7. Converta os tempos para ganhos: $K_i=K_p/T_i$ e $K_d=K_pT_d$.
8. Verifique a malha com o controlador final.

| Sintonia | $K_p$ | $T_i$ | $T_d$ |
|---|---|---|---|
| ZN P | $0,50K_{cr}$ | — | — |
| ZN PI | $0,45K_{cr}$ | $P_{cr}/1,2$ | — |
| ZN PID clássico | $0,60K_{cr}$ | $P_{cr}/2$ | $P_{cr}/8$ |
| SO-OV da revisão | $0,33K_{cr}$ | $P_{cr}/2$ | $0,33P_{cr}$ |
| NO-OV da prova | $0,20K_{cr}$ | $P_{cr}/2$ | $0,33P_{cr}$ |

Use a tabela entregue pelo professor. Os nomes das variantes não constituem garantias matemáticas de desempenho.

## 3. Exemplo completo: 2026.1

$$G=\frac{10}{(s+1)^2(s+5)}.$$

Com P:

$$\Delta=s^3+7s^2+11s+5+10K.$$

Routh: $77-(5+10K)=0\Rightarrow K_{cr}=7,2$.

Auxiliar: $7s^2+77=0\Rightarrow\omega_{cr}=\sqrt{11}$.

$$P_{cr}=1,89445,\quad K_p=1,44,\quad
T_i=0,94723,\quad T_d=0,62517.$$

$$\boxed{G_c(s)\approx1,44+\frac{1,52023}{s}+0,90024s.}$$

O ganho da forma fatorada é **$K_d\approx0,90024$**, não 1,44.

## 4. Malha aberta: leia L e R na tangente

Para degrau unitário, seja $t_i$ o instante de inflexão, $y_i=y(t_i)$ e $R=y'(t_i)$:

$$y_{\rm tang}(t)=y_i+R(t-t_i),\qquad L=t_i-\frac{y_i}{R}.$$

Se a tangente intercepta o valor final $y_\infty$ em $L+T$:

$$R=\frac{y_\infty}{T}.$$

| Controlador | $K_p$ | $T_i$ | $T_d$ |
|---|---|---|---|
| P | $1/(RL)$ | — | — |
| PI | $0,9/(RL)$ | $L/0,3$ | — |
| PID | $1,2/(RL)$ | $2L$ | $0,5L$ |

Se o degrau de ensaio não for unitário, normalize a inclinação pela amplitude da entrada antes de aplicar essa convenção.

Na Revisão 2EE pp. 12–13, a leitura gráfica usada foi $L\approx0,3$, $T\approx1,95$ e $R\approx0,5128$. Resulta:

$$K_p\approx7,8,\quad K_i\approx13,\quad K_d\approx1,17.$$

São **estimativas gráficas**. Não exigem coincidência com uma tangente obtida por cálculo exato.

## 5. Qual PID diminui mais o erro de rampa?

Com planta tipo 0, $G(0)=g_0$, e PID com integral não nula:

$$K_v=K_i g_0,\qquad e_{ss}=\frac{A}{K_i g_0}
=\frac{AT_i}{K_p g_0}.$$

Compare **$K_p/T_i$**, e não $K_p$ isoladamente. Na tabela ZN/SO-OV/NO-OV da revisão, $T_i$ é igual nas três opções; portanto ZN clássico produz o maior $K_i$ e o menor erro de rampa, desde que a malha final seja estável.

## 6. Atalho útil para conferir as contas

Se $G=A/(s^3+a s^2+b s+c)$, com coeficientes adequados e realimentação unitária:

$$K_{cr}=\frac{ab-c}{A},\quad\omega_{cr}=\sqrt b,\quad
P_{cr}=\frac{2\pi}{\sqrt b}.$$

Isso vem da tabela de Routh; não dispense a justificativa quando a prova pedir o desenvolvimento.

**Treino:** 2023.2 Q2 → 2024.1 Q2 → 2026.1 Q1a → Revisão pp. 12–15.
