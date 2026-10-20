# 6. Refinamento do LGR e projeto de PI

**Prioridade alta:** 2025.1 Q1 e 2025.2 Q2 exigem explicitamente regras de refinamento.

## 1. A sequência que deve ficar automática

$$M_p,T_s\longrightarrow\zeta,\omega_n\longrightarrow s_d
\longrightarrow\text{ângulo do zero}\longrightarrow z
\longrightarrow K\longrightarrow\text{verificação}.$$

Não comece chutando o zero.

## 2. Condição de ângulo

Para $K>0$:

$$\sum_i\arg(s_d-z_i)-\sum_j\arg(s_d-p_j)=(2\ell+1)180^\circ.$$

Cada vetor vai **do polo ou zero até $s_d$**.

Se há um único zero desconhecido em $-z$ e $s_d=-\sigma+j\omega_d$:

$$\theta_z=\arg[(z-\sigma)+j\omega_d],\qquad
z=\sigma+\frac{\omega_d}{\tan\theta_z}.$$

Escolha o ângulo no quadrante correto. Use a função atan2 na conferência numérica. Um denominador negativo exige ângulo de segundo quadrante no semiplano superior.

## 3. Condição de módulo

Depois de encontrar $z$:

$$K=\frac{\prod_j|s_d-p_j|}{A\prod_i|s_d-z_i|},$$

onde $A$ inclui o ganho fixo da planta. Não esqueça fatores como 10, 40 ou 100.

Uma conferência excelente:

$$K=-\frac{D(s_d)}{N_0(s_d)}.$$

O resultado deve ser real positivo, salvo resíduo imaginário pequeno de arredondamento. Um ganho com parte imaginária relevante indica erro de fase ou de cálculo.

## 4. Exemplo: 2025.1

$$G=\frac{10}{(s+3)(s+8)(s+11)},\qquad G_c=K\frac{s+z}{s}.$$

Para $M_p=5\%$:

$$\zeta\approx0,6901,\qquad
\sigma=\frac{3,716}{2,4232}\approx1,5335,\quad
\omega_d\approx1,6085.$$

Os polos de malha aberta são $0,-3,-8,-11$. A soma de seus ângulos, usando os números arredondados do gabarito, é aproximadamente $204,8898^\circ$.

$$\theta_z=204,8898^\circ-180^\circ=24,8898^\circ.$$

$$z=1,5335+\frac{1,6086}{\tan24,8898^\circ}\approx5.$$

$$K=\frac{|s_d(s_d+3)(s_d+8)(s_d+11)|}{10|s_d+5|}
\approx8,10.$$

Portanto, $G_c\approx8,10(s+5)/s$.

## 5. Exemplo: 2025.2 — o quadrante muda

A planta tem um zero:

$$G=\frac{s+4}{(s+2)^2},\quad s_d=-3,716+j3,6268.$$

Conte duas vezes o ângulo do polo $-2$ e inclua o zero $-4$:

$$\theta_z=180^\circ+\theta_0+2\theta_{-2}-\theta_{-4}
\pmod{360^\circ}\approx100,8157^\circ.$$

O zero precisa ficar à direita da parte real do polo desejado:

$$z=3,716+\frac{3,6268}{\tan100,8157^\circ}\approx3,0231.$$

$$K=\frac{|s_d(s_d+2)^2|}{|(s_d+4)(s_d+3,0231)|}
\approx6,2230.$$

## 6. Refinamento para entrada/saída do eixo real

De $D+KN=0$, isole:

$$K(s)=-\frac{D(s)}{N(s)}.$$

Os candidatos a polos múltiplos satisfazem $dK/ds=0$. Retenha apenas os que:

- pertencem a um trecho real do LGR;
- produzem ganho com o sinal permitido;
- são compatíveis com o ponto de projeto.

Se $N$ é constante, basta resolver $D'(s)=0$.

Exemplo de 2025.2 com PD e cancelamento em $-2$:

$$K(s)=-\frac{s(s+4)(s+5)}{10},\quad
3s^2+18s+20=0.$$

As soluções são $-4,5275$ e $-1,4725$. Só a segunda pertence ao trecho real com ganho positivo dessa malha reduzida.

## 7. Ângulos de partida e chegada

Quando necessário, isole na equação de fase o vetor associado ao polo ou zero considerado. Para um polo complexo simples $p_k$, uma forma é:

$$\theta_{\rm partida}=180^\circ+\sum_i\arg(p_k-z_i)
-\sum_{j\ne k}\arg(p_k-p_j)\pmod{360^\circ}.$$

Não some o ângulo do próprio polo a ele mesmo. Esta regra complementa o esboço; nas duas questões de PI, a condição no ponto desejado é a ferramenta principal.

**Critério de domínio:** refazer 2025.2 Q2 em até 25 minutos, justificando o ângulo obtuso e incluindo o zero da planta.
