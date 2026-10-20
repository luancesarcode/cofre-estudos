# 1. A base que destrava todas as questões

**Objetivo:** olhar o diagrama e escrever a equação certa antes de calcular qualquer ganho.

## 1. Malha aberta e malha fechada

Nestes exercícios, a realimentação é negativa e unitária, salvo indicação expressa.

$$
L(s)=G_c(s)G(s)H(s),\qquad
T(s)=\frac{G_c(s)G(s)}{1+G_c(s)G(s)H(s)}.
$$

Com $H=1$ e $L=N/D$:

$$T(s)=\frac{N(s)}{D(s)+N(s)},\qquad \Delta(s)=D(s)+N(s).$$

- Os polos e zeros de **L** são os pontos de partida e chegada do LGR.
- As raízes de **$\Delta$** são os polos de malha fechada para o ganho escolhido.
- A estabilidade se verifica em **$\Delta$**, não somente nos polos da planta.

**Exemplo:** $G=1/[(s+3)(s+5)]$ e $G_c=K(s+z)/s$.

$$L=\frac{K(s+z)}{s(s+3)(s+5)},\quad
\Delta=s^3+8s^2+(15+K)s+Kz.$$

O denominador da planta era de segunda ordem; o PI acrescentou um integrador e o sistema fechado passou a ter terceira ordem.

## 2. Reconheça o controlador pela função

| Controlador | Forma | O que acrescenta ao LGR |
|---|---|---|
| P | $K_p$ | Só varia o ganho |
| I | $K_i/s$ | Polo na origem |
| PD | $K_d(s+z)$ | Um zero |
| PI | $K_p(s+z)/s$ | Um polo na origem e um zero |
| PID | $K_d(s+z_1)(s+z_2)/s$ | Um polo na origem e dois zeros |
| Avanço | $K(s+z)/(s+p)$, $p>z>0$ | Zero e polo estáveis; polo mais à esquerda |
| Atraso | $K(s+z)/(s+p)$, $z>p>0$ | Zero e polo estáveis; polo mais próximo da origem |

Avanço e atraso aparecem como alternativas na questão 3 de 2023.2. Um polo próximo da origem **não equivale** a um integrador exato: os compensadores usuais com $p>0$ não aumentam o tipo do sistema.

## 3. Conversões que você precisa dominar

$$G_c=K_p\left(1+\frac1{T_i s}+T_d s\right)
=K_p+\frac{K_i}{s}+K_d s.$$

Logo:

$$K_i=\frac{K_p}{T_i},\qquad K_d=K_pT_d.$$

Na forma fatorada:

$$G_c=\frac{K_d s^2+K_p s+K_i}{s}
=K_d\frac{s^2+(K_p/K_d)s+K_i/K_d}{s}.$$

**A ordem é $K_d s^2+K_p s+K_i$.** Trocar $K_p$ e $K_i$ altera o controlador.

Se $G_c=K(s+z_1)(s+z_2)/s$:

$$K_d=K,\quad K_p=K(z_1+z_2),\quad K_i=Kz_1z_2.$$

Se $G_c=K(s+z)/s$: $K_p=K$ e $K_i=Kz$.

Zeros complexos conjugados são possíveis em um PID com coeficientes reais. Não force uma fatoração em dois zeros reais quando o discriminante for negativo.

## 4. Ganho estático não é o numerador

Uma planta sem zeros, polos $-2,-0,5\pm j$ e ganho estático 2 tem:

$$G(s)=\frac{A}{(s+2)(s^2+s+1,25)}.$$

Imponha $G(0)=A/2,5=2$. Portanto, **$A=5$**, não 2.

## 5. Roteiro de abertura de qualquer resolução

1. Copie $G$, $G_c$ e $H$.
2. Diga quais parâmetros são positivos e quais são incógnitas.
3. Monte $L$ e depois $\Delta$.
4. Conte integradores para discutir erro.
5. Use Routh para estabilidade e LGR para localização dos polos.
6. Só depois interprete o transitório.

**Treino:** 2023.2 Q3a e 2026.1 Q1a–b. Você domina este assunto quando converte um PID entre as três formas sem olhar uma tabela.
