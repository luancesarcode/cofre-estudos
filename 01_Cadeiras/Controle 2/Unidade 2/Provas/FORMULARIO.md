# Formulário de revisão

[Voltar ao início](README.md) · Use depois de entender as notas, não como substituto da resolução.

## Malha

$$L=G_cGH,\qquad T=\frac{G_cG}{1+L}.$$

Se $H=1$ e $L=N/D$: $\Delta=D+N$.

## Erro, com estabilidade e realimentação unitária

$$K_{\rm pos}=\lim L,\quad K_v=\lim sL,\quad K_a=\lim s^2L.$$

$$e_{\rm degrau}=\frac1{1+K_{\rm pos}},\quad
e_{\rm rampa}=\frac1{K_v},\quad
e_{\rm parabola}=\frac1{K_a}.$$

Para $R=A/s^m$: $e_{ss}=\lim A/[s^{m-1}(1+L)]$.

## Routh

Cúbica $\Delta=s^3+a s^2+b s+c$:

$$\text{primeira coluna: }1,\ a,\ \frac{ab-c}{a},\ c.$$

Quártica $\Delta=s^4+a s^3+b s^2+c s+d$:

$$B=\frac{ab-c}{a},\quad C=\frac{Bc-ad}{B};
\quad\text{primeira coluna: }1,a,B,C,d.$$

Linha nula: auxiliar da linha acima, depois derivada do auxiliar para continuar.

$$\omega_{cr}=\sqrt{\frac{\text{constante do auxiliar quadrático}}
{\text{coeficiente de }s^2}},\qquad P_{cr}=2\pi/\omega_{cr}.$$

Parte real desejada $-\alpha$: $s=q-\alpha$.

## LGR positivo

$$\sigma_a=\frac{\sum p_i-\sum z_i}{n-m},\quad
\theta_\ell=\frac{(2\ell+1)180^\circ}{n-m}.$$

Trecho real: número ímpar de polos/zeros reais à direita.

$$\sum\arg(s_d-z_i)-\sum\arg(s_d-p_i)=(2\ell+1)180^\circ.$$

$$K=\frac{\prod|s_d-p_i|}{A\prod|s_d-z_i|}.$$

Ponto de saída: $d[-D(s)/N(s)]/ds=0$; verificar trecho e sinal do ganho.

LGR complementar, $K<0$: contagem par e ângulos $2\ell180^\circ/(n-m)$.

## Transitório

$$s_d=-\sigma\pm j\omega_d,\quad
\omega_n=\sqrt{\sigma^2+\omega_d^2},\quad\zeta=\sigma/\omega_n.$$

$$M_p=100e^{-\pi\zeta/\sqrt{1-\zeta^2}},\quad
\zeta=\frac{-\ln(M_p/100)}{\sqrt{\pi^2+\ln^2(M_p/100)}}.$$

Convenções aproximadas dos materiais:

$$T_s(2\%)\approx3,716/\sigma\quad
\text{na faixa subamortecida usada nos projetos};$$

$$T_s(1\%)\approx4,412/\sigma\quad
\text{na faixa de baixo amortecimento};$$

$$T_s(1\%)\approx(11,113\zeta-4,388)/\omega_n
\quad(\zeta>0,826,\ \text{formulário citado}).$$

Primeira ordem normalizada exata: $T_s(1\%)=\ln100/|p|$; material frequentemente usa $5/|p|$.

Crítico de segunda ordem sem zeros: $T_s(1\%)\approx6,63835/\omega_n$ exato, contra $6,725/\omega_n$ da aproximação.

## Controladores

$$G_c=K_p+\frac{K_i}s+K_ds
=K_p\left(1+\frac1{T_i s}+T_ds\right).$$

$$K_i=K_p/T_i,\quad K_d=K_pT_d.$$

$$G_{\rm PI}=K(s+z)/s:\quad K_p=K,\ K_i=Kz.$$

$$G_{\rm PID}=K(s+z_1)(s+z_2)/s:
\quad K_d=K,\ K_p=K(z_1+z_2),\ K_i=Kz_1z_2.$$

## Sintonia

| Método | $K_p$ | $T_i$ | $T_d$ |
|---|---|---|---|
| ZN fechado PI | $0,45K_{cr}$ | $P_{cr}/1,2$ | — |
| ZN fechado PID | $0,60K_{cr}$ | $P_{cr}/2$ | $P_{cr}/8$ |
| SO-OV da revisão | $0,33K_{cr}$ | $P_{cr}/2$ | $0,33P_{cr}$ |
| NO-OV | $0,20K_{cr}$ | $P_{cr}/2$ | $0,33P_{cr}$ |
| ZN aberto PI | $0,9/(RL)$ | $L/0,3$ | — |
| ZN aberto PID | $1,2/(RL)$ | $2L$ | $0,5L$ |

Em malha aberta: $R$ é a inclinação normalizada da tangente; $L$ é sua interceptação no eixo do tempo.

## Antes de entregar a questão

Verifique: sinal do ganho; multiplicidade; zero da planta; fator fixo do numerador; unidade de frequência; critério de 1%/2%; fronteira estável excluída; interseção com erro; hipótese de dominância.
