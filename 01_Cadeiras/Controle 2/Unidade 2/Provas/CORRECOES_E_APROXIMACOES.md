# Correções, aproximações e diferenças entre os materiais

[Voltar ao início](README.md)

Este arquivo evita que você perca tempo tentando conciliar resultados incompatíveis. Os PDFs foram preservados. As resoluções didáticas mostram a conta usada para conferir cada ponto.

As conferências numéricas usam os modelos nominais, realimentação negativa unitária, entrada degrau unitário e condições iniciais nulas. Os tempos de acomodação são medidos em relação ao valor final, com malha temporal de 0,001 s nos casos registrados. Código e resultados estão em [verificacao](verificacao/calculos_e_figuras.py).

## 1. Pontos médios de LGR são estimativas

| Fonte | Estimativa do material | Conferência |
|---|---|---|
| 2023.1 Q1b | Polo crítico em $-1$ | Exato: $-0,828427$ |
| 2024.1 Q1b | Encontro em $-0,5$ | Exato: $-0,381966$ |
| 2024.1 Q1d, PD $z=1$ | Encontro em aproximadamente $-0,9$ | Exato: $-0,784750$ |
| 2024.2 Q1b | Encontro em $-0,5$ | Exato: $-0,418861$ |
| 2025.2 Q1a | Encontro em aproximadamente $-0,7$ | Exato: $-0,746251$ |

Em 2023.1 o enunciado proíbe refinamento na letra b; preserve o caráter aproximado da resposta solicitada. Não substitua a habilidade de esboçar por cálculo de raízes quando o item pedir apenas esboço.

## 2. Tempos de acomodação

As expressões $3,716/\sigma$, $4,412/\sigma$ e $(11,113\zeta-4,388)/\omega_n$ são aproximações do material, não identidades gerais.

| Caso | Valor no PDF | Conferência nominal |
|---|---|---|
| 2023.1 PD $-5(s+2)/7$ | aproximadamente 1 s | 1,172 s na resposta completa com zero não mínimo |
| 2025.2 P, $K=1,68$ | aproximadamente 5,2 s | 5,494 s, banda de 1% |
| 2025.2 P, $K=8$ | aproximadamente 18,5 s | 22,323 s, banda de 1% |
| 2025.2 PD, $z=2,K=1,312845$ | “real” 4,16 s | aproximadamente 4,694 s |
| 2025.2 PD, $z=2,K=1,73$ | aproximadamente 2,6 s | 2,733 s |
| 2026.1 PID crítico | 2,66 s / fórmula 2,69 s | 2,655 s exato; 2,690 s pelo formulário |

No último caso, a diferença vem da aproximação do formulário, não apenas de arredondamento.

## 3. Interseção de requisitos

- **2024.1 Q1d:** o PD crítico com $z=1,K_d\approx0,352102$ melhora o transitório, mas não satisfaz $K_dz\ge2$ da letra c.
- **2025.2 Q1c:** o exemplo $z=2,K=1,73$ tem pequeno sobressinal, mas não satisfaz $Kz\ge8$ da letra b. O gabarito trata o item c como um novo projeto.

Não apresente esses exemplos como soluções simultâneas de todas as letras. As resoluções explicam a distinção.

## 4. Dominância e zeros

- **2025.1 Q1b:** o polo $-12,2274$ passa o teste prático de 5×; não é correto afirmar literalmente que todos os polos são dominantes. O polo $-6,7054$ e o zero $-5$ ainda prejudicam a aproximação.
- **2025.2 Q2:** o par pedido é alocado, mas a resposta completa tem aproximadamente 13,18% de sobressinal, não 4%. A meta de 4% é o parâmetro do modelo de segunda ordem usado para definir o par.
- **2026.1 Q1b:** o PID NO-OV efetivamente calculado tem polos complexos e cerca de 15,2% de sobressinal. O nome da sintonia não prova o resultado.
- Polos reais negativos não garantem monotonicidade se houver zeros.

## 5. Routh e sinal de ganho

- **2026.1 Q2:** para PI, $0<z\le4$ garante estabilidade para todo ganho positivo finito. O PDF considera $0<z<4$, que é uma escolha suficiente, mas omite a possibilidade da igualdade.
- **Gabarito 2EE p. 8:** $32+3K>0$ implica $K>-32/3$. Há um sinal invertido em uma linha intermediária do manuscrito.
- **2025.1 Q3:** “P não produz polos reais” pressupõe ganho positivo. Se negativos forem admitidos, existe faixa $-1,3<K_p<-0,9$ com polos reais estáveis.
- **2025.2 Q1:** o limite exato para P é aproximadamente 12,495868; “12” é uma leitura arredondada.

## 6. Correção importante na Revisão 2EE pp. 3–4

Para a planta

$$G=\frac{s+3}{s(s^2+2)(s+5)},$$

o PD com zero em $-1$ **não é estável para todo ganho positivo**, embora seu centroide esteja à esquerda. A faixa é $K_d>16,25$.

Uma escolha que satisfaz estabilidade para todo $K_d>0$ é zero em $-0,2$. Mais geralmente, $0<z\le4/17$ funciona. O [Extra B](Monitoria/EXTRAS_RESOLVIDOS.md) mostra o LGR, a condição de cruzamento e a conferência por Routh.

O ponto específico do manuscrito, $z=1,K_d=100/3$, é estável; o erro está na afirmação de estabilidade para **todos** os ganhos.

## 7. Fatoração e circuito na revisão

- **P. 10:** ZN clássico tem $T_i=4T_d$. Seus zeros são exatamente repetidos antes de arredondar. No exemplo, ambos ficam em aproximadamente $-2,11143$.
- **P. 15:** os ganhos de ZN aberto e fechado são próximos nesse exemplo, mas isso não prova equivalência geral dos métodos.
- **P. 16:** o numerador do PID deve ser $K_ds^2+K_ps+K_i$. O manuscrito troca $K_p$ e $K_i$ ao fatorar.
- **P. 16:** o estágio com $R_2$ na realimentação e $R+1/(sC_2)$ ao terra tem transferência $[1+sC_2(R+R_2)]/[1+sRC_2]$. A razão $R_2/R$ não pode ser usada diretamente como frequência de zero.

Veja a derivação corrigida e componentes de exemplo no [Assunto 09](Assuntos/09_PID_com_amplificadores.md).

## Como usar isto durante o estudo

Primeiro aprenda o método. Se seu resultado divergir do PDF, procure a linha correspondente aqui e compare as hipóteses. Na avaliação, explicite o critério e o nível de aproximação: “pelo esboço”, “pelo formulário” ou “pela função completa”.
