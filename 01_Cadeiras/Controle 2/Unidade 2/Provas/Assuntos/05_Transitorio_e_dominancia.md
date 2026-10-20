# 5. Transitório: dos polos a Mp e Ts

## 1. Modelo padrão de segunda ordem

$$T_2(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}.$$

Se $p=-\sigma\pm j\omega_d$:

$$\omega_n=\sqrt{\sigma^2+\omega_d^2},\qquad
\zeta=\frac{\sigma}{\omega_n},\qquad \sigma=\zeta\omega_n.$$

| $\zeta$ | Classificação do modelo |
|---|---|
| $0<\zeta<1$ | Subamortecido |
| $\zeta=1$ | Criticamente amortecido |
| $\zeta>1$ | Sobreamortecido |

Para $0<\zeta<1$:

$$M_p(\%)=100e^{-\pi\zeta/\sqrt{1-\zeta^2}}.$$

Se $m=M_p/100$:

$$\zeta=\frac{-\ln m}{\sqrt{\pi^2+\ln^2m}}.$$

**Pegadinha:** para 5%, use $\ln(0,05)$, não $\ln(5)$.

## 2. As convenções de tempo usadas nos seus materiais

As resoluções usam aproximações específicas. Para reproduzir seus números:

| Situação | Expressão usada no material |
|---|---|
| Segunda ordem subamortecida, 2%, na faixa dos projetos de PI | $T_s\approx3,716/(\zeta\omega_n)$ |
| Segunda ordem subamortecida, 1%, na faixa de baixo amortecimento | $T_s\approx4,412/(\zeta\omega_n)$ |
| 1%, $\zeta>0,826$, conforme 2023.1 | $T_s\approx(11,113\zeta-4,388)/\omega_n$ |
| Primeira ordem | Material frequentemente usa $T_s(1\%)\approx5/|p|$ |

Na Revisão 2EE p. 6, a aproximação de 2% é indicada para $\zeta<0,78$. Não use essas expressões fora de contexto como identidades exatas.

Livros também usam $4/\sigma$ e $4,6/\sigma$. **Não misture convenções no meio do cálculo.** Nas provas de refinamento, mudar 3,716 para 4 muda o polo desejado e os valores finais de $K,z$.

## 3. Tempos exatos em dois modelos simples

Primeira ordem normalizada: $y=1-e^{-at}$.

$$T_s(1\%)=\frac{\ln100}{a}\approx\frac{4,60517}{a}.$$

Segunda ordem crítica sem zeros: $y=1-(1+\omega_n t)e^{-\omega_n t}$.

Para 1%, resolva $(1+x)e^{-x}=0,01$:

$$T_s(1\%)=\frac{6,63835}{\omega_n}.$$

O formulário dá $6,725/\omega_n$, que é uma aproximação. Por isso, em 2026.1 Q1c, $T_s$ é aproximadamente 2,655 s pelo modelo exato e 2,690 s pelo formulário. Não é apenas arredondamento.

## 4. Dominância

Um polo com parte real muito mais negativa decai mais rápido. A regra de “cinco vezes” é um critério prático: compare as taxas de decaimento $|\operatorname{Re}p|$.

**Mas verifique também zeros e resíduos.** Um zero próximo do par dominante pode alterar bastante o sobressinal.

Em 2025.1 Q1:

$$p\approx-1,5336\pm j1,6086,\;-6,7054,\;-12,2274,\qquad z=-5.$$

O polo $-12,2274$ passa o teste de 5× em relação a 1,5336; $-6,7054$ não. O zero $-5$ também não está suficientemente afastado para ignorar seu efeito com segurança. O par desejado não transforma a função inteira em segunda ordem.

## 5. Três conclusões que você deve saber escrever

1. “O polo foi alocado corretamente, mas o desempenho completo deve ser verificado porque há outros polos e zeros relevantes.”
2. “Aumentar $K$ não diminui sempre $T_s$; perto da fronteira de estabilidade, o amortecimento tende a zero.”
3. “A sintonia NO-OV é heurística. O nome do método não garante ausência de sobressinal para qualquer planta.”

![Comparação real dos dois projetos de 2026.1](../figuras/2026_1_degrau.png)

## 6. Mini-exercício

Para $p=-3,716+j3,6268$, obtenha $\omega_n\approx5,1924$ e $\zeta\approx0,7156$. No modelo padrão, $M_p\approx4\%$ e $T_s(2\%)\approx1$ pela convenção do material.

Agora compare com 2025.2 Q2: o sistema completo tem outro polo e dois zeros; seu sobressinal é diferente. Isso é parte da interpretação, não erro na regra do ângulo.
