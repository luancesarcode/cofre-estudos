# 2. Erro estacionário e tipo do sistema

**Onde aparece:** nas sete provas e na revisão. É um dos assuntos de maior retorno.

## 1. Primeiro verifique a estabilidade

Para realimentação negativa unitária:

$$E(s)=\frac{R(s)}{1+L(s)},\qquad e_{ss}=\lim_{s\to0}sE(s).$$

O teorema do valor final exige as condições de estabilidade de $sE(s)$. Um limite algébrico finito não demonstra que um sistema instável terá erro estacionário.

## 2. Tipo = número de integradores não cancelados em L(s)

| Tipo de L | Degrau unitário $1/s$ | Rampa unitária $1/s^2$ | Parábola normalizada $1/s^3$ |
|---|---|---|---|
| 0 | $1/(1+K_{\mathrm{pos}})$ | Sem erro finito | Sem erro finito |
| 1 | 0 | $1/K_v$ | Sem erro finito |
| 2 | 0 | 0 | $1/K_a$ |
| 3 | 0 | 0 | 0 |

$$K_{\mathrm{pos}}=\lim L(s),\quad K_v=\lim sL(s),\quad K_a=\lim s^2L(s).$$

Uso $K_{\mathrm{pos}}$ para não confundir a constante de posição com o ganho proporcional $K_p$.

**Escolha do controlador:** se a planta já tem um polo na origem, um P ou PD pode manter erro nulo de degrau. Se a planta é tipo 0, acrescente ação integral. Entre P, PI e PID, o PI é o mais simples que acrescenta essa ação.

## 3. O padrão das fresas: transforme o erro em uma curva

$$G(s)=\frac{A}{s(s+a)(s+b)(s+c)},\quad G_c=K(s+z).$$

$$K_v=\lim_{s\to0}\frac{A K(s+z)}{(s+a)(s+b)(s+c)}
=\frac{AKz}{abc}.$$

Assim:

$$e_{ss,\mathrm{rampa}}=\frac{abc}{AKz}\le e_{\max}
\quad\Longleftrightarrow\quad
z\ge \frac{abc}{Ae_{\max}K},\qquad K,z>0.$$

| Prova | $K_v$ com PD | Exigência de erro |
|---|---|---|
| 2024.1 Q1 | $Kz$ | $Kz\ge2$ |
| 2024.2 Q1 | $Kz/2$ | $Kz\ge4$ |
| 2025.1 Q2 | $Kz/3$ | $Kz\ge10$ |
| 2025.2 Q1 | $Kz/4$ | $Kz\ge8$ |

Essa condição é apenas uma metade da resposta. A outra é a região de estabilidade por Routh. A resposta final é a **interseção**.

## 4. Rampas com amplitude e entradas de ordem maior

Se $r(t)=At$, então $R(s)=A/s^2$ e $e_{ss}=A/K_v$.

Para $R(s)=A/s^m$:

$$e_{ss}=\lim_{s\to0}\frac{A}{s^{m-1}[1+L(s)]}.$$

Se $L(s)\sim k/s^\nu$ próximo de zero:

- $\nu>m-1$: erro zero;
- $\nu=m-1$: erro constante $A/k$;
- $\nu<m-1$: não há erro estacionário finito.

**Cuidado com a linguagem da revisão:** “entrada tipo 4” significa ali $R(s)=1/s^4$. É uma entrada cúbica $r(t)=t^3/6$ e exige sistema **tipo 3** para erro constante. Não significa que o sistema deva ser tipo 4.

### Exemplo completo da revisão, páginas 1–2

$$G=\frac1{s^2(s+10)},\quad G_c=\frac{K_1s^2+2K_1s+K_2}{s}.$$

$$L=\frac{K_1s^2+2K_1s+K_2}{s^3(s+10)},\quad
\lim s^3L=\frac{K_2}{10}.$$

Para $R=1/s^4$: $e_{ss}=10/K_2$. Exigir $e_{ss}\le1$ dá $K_2\ge10$.

Routh acrescenta $K_1>0$ e $K_2<0,16K_1^2$. Portanto:

$$\boxed{K_1>\sqrt{62,5}\approx7,9057,\quad 10\le K_2<0,16K_1^2.}$$

## 5. Teste de domínio

Sem consultar, explique por que:

- PI em uma planta tipo 0 zera o erro de degrau, mas geralmente não o de rampa.
- PD em uma planta tipo 1 pode satisfazer uma restrição de rampa.
- Aumentar o ganho para diminuir o erro pode tornar a malha instável.
- Um cancelamento na origem pode retirar a vantagem da ação integral.

**Exercício guiado:** 2024.1 Q1a mostra que a interseção pode ser vazia. **Repetição:** 2024.2 Q1a mostra uma interseção estreita.
