# 9. PID com amplificadores operacionais

**Prioridade complementar:** aparece na última página da Revisão 2EE; não foi encontrado nos sete enunciados de prova por período. Estude depois do núcleo LGR–Routh–erro–sintonia.

## 1. O que saber

- Usar $Z_C=1/(sC)$.
- Para amplificador ideal não inversor: $V_o/V_i=1+Z_f/Z_g$.
- Para inversor: $V_o/V_i=-Z_f/Z_{\rm in}$.
- Multiplicar as transferências de estágios em cascata.
- Comparar coeficientes com $K_ds+K_p+K_i/s$.
- Distinguir derivador ideal de derivador filtrado.

## 2. Confira a forma algébrica antes de escolher componentes

Na revisão, a sintonia de malha fechada fornece aproximadamente:

$$K_p=7,68,\quad K_i=11,7239,\quad K_d=1,25774.$$

Consequentemente:

$$G_c=\frac{1,25774s^2+7,68s+11,7239}{s}.$$

Com os valores exatos da tabela ZN, os dois zeros coincidem:

$$G_c=K_d\frac{(s+z)^2}{s},\qquad
z=\frac{4}{P_{cr}}\approx3,05312.$$

**Correção localizada:** a p. 16 da revisão troca as posições de $K_p$ e $K_i$ no numerador e obtém outros zeros. Essa fatoração não corresponde aos ganhos calculados anteriormente. Preserve os ganhos e refaça a fatoração.

## 3. Uma implementação ideal com dois estágios não inversores

Esta é uma alternativa didática de circuito, sob hipótese de amplificadores ideais e derivação ideal. Não afirma um mínimo universal para todas as topologias.

**Estágio PI:** entrada em $+$; resistor $R_1$ da entrada $-$ ao terra; capacitor $C_1$ entre a saída e a entrada $-$.

$$G_1=1+\frac1{sR_1C_1}=\frac{s+z_1}{s},\qquad z_1=\frac1{R_1C_1}.$$

**Estágio PD:** entrada em $+$; resistor $R_f$ da saída à entrada $-$; entre a entrada $-$ e o terra, $R_g$ em paralelo com $C_2$.

$$G_2=1+R_f\left(\frac1{R_g}+sC_2\right)
=R_fC_2\left(s+\frac{1+R_f/R_g}{R_fC_2}\right).$$

Assim:

$$G_1G_2=K_d\frac{(s+z_1)(s+z_2)}s,$$

com:

$$R_fC_2=K_d,\qquad
1+\frac{R_f}{R_g}=K_dz_2,\qquad
R_1C_1=\frac1{z_1}.$$

Para resistores positivos nesta topologia, é necessário $K_dz_2>1$.

### Exemplo numérico da revisão, corrigido

Escolha $C_1=C_2=10\,\mu\mathrm{F}$ e $z_1=z_2\approx3,05312$:

$$R_1\approx32,7535\ \mathrm{k}\Omega,\quad
R_f\approx125,7736\ \mathrm{k}\Omega.$$

Como $K_dz_2=K_p/2=3,84$:

$$R_g=\frac{R_f}{2,84}\approx44,2865\ \mathrm{k}\Omega.$$

Expanda o produto para conferir os três ganhos antes de finalizar o circuito. Valores comerciais arredondados mudam ligeiramente os ganhos.

## 4. O estágio filtrado desenhado na revisão

Na p. 16, o segundo estágio possui resistor $R_2$ na realimentação e **$R$ em série com $C_2$** no caminho ao terra. Sua transferência correta é:

$$G_2=1+\frac{R_2}{R+1/(sC_2)}
=\frac{1+sC_2(R+R_2)}{1+sRC_2}.$$

Ou:

$$G_2=\frac{R+R_2}{R}\,
\frac{s+1/[C_2(R+R_2)]}{s+1/(RC_2)}.$$

Logo, o zero não é simplesmente $-R_2/R$; essa razão nem tem unidade de frequência. Há um polo de filtro adicional. É preciso incluí-lo ao comparar com o PID ideal.

Para reproduzir aproximadamente um zero em $-3,05312$ e um polo de filtro em $-100$, imponha:

$$RC_2=0,01,\qquad (R+R_2)C_2=\frac1{3,05312}.$$

Com $C_2=10\,\mu\mathrm{F}$, resulta $R=1\,\mathrm{k}\Omega$ e $R_2\approx31,7535\,\mathrm{k}\Omega$. Um estágio PI e ajuste do ganho completam o projeto; a função final passa a ter filtro, portanto não é exatamente o PID ideal.

## 5. Para a prova

Se pedirem o menor número de amplificadores, apresente a topologia, deduza cada estágio e explique onde incorporou o ganho. Não copie resistores sem verificar a função de transferência. Se exigirem o circuito industrial filtrado mostrado em aula, mantenha o polo de filtro explícito.
