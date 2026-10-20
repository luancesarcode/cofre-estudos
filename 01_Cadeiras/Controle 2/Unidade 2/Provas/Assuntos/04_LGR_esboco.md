# 4. LGR: desenhar e explicar o que o desenho significa

**Fonte de apoio:** Monitoria 05, páginas 1–2. Esboços são cobrados explicitamente em seis das sete provas; 2023.2 concentra-se em Routh e projeto algébrico.

## 1. A ideia

Escreva $L=K L_0$. Os polos de malha fechada satisfazem:

$$1+K L_0(s)=0.$$

O LGR reúne esses polos enquanto $K$ varia. Os zeros de malha fechada não “andam” junto com os polos.

## 2. Receita de esboço para K positivo

1. Marque os polos de $L_0$ com × e os zeros com ○.
2. Conte multiplicidades. Um polo duplo conta duas vezes.
3. Há $n$ ramos, partindo dos $n$ polos. Eles chegam aos $m$ zeros finitos e aos $n-m$ zeros no infinito, para os sistemas próprios usuais.
4. Use simetria em relação ao eixo real.
5. Um trecho do eixo real pertence ao LGR se há um número **ímpar** de polos e zeros reais à sua direita.
6. Trace as assíntotas:

$$\sigma_a=\frac{\sum p_i-\sum z_i}{n-m},\qquad
\theta_\ell=\frac{(2\ell+1)180^\circ}{n-m},\quad \ell=0,\ldots,n-m-1.$$

7. Marque o sentido correspondente ao aumento de $K$.
8. Discuta onde os ramos estão à esquerda, sobre ou à direita do eixo imaginário.

Os símbolos $p_i,z_i$ nas somas são **coordenadas dos polos e zeros**. Um zero no fator $(s+3)$ contribui com $-3$, não $+3$.

## 3. Exemplo de quatro polos

Para $L=6K/[s(s+1)(s+2)(s+3)]$:

- Polos: $0,-1,-2,-3$; nenhum zero finito.
- Trechos reais: $(-1,0)$ e $(-3,-2)$.
- Centroide: $-6/4=-1,5$.
- Ângulos: $45^\circ,135^\circ,225^\circ,315^\circ$.
- Os polos próximos de 0 e $-1$ aproximam-se e deixam o eixo real.
- Dois ramos vão acabar no semiplano direito: ganho muito grande é instável.

![LGR de P e PD](../figuras/2024_1_lgr.png)

O gráfico numérico ajuda a conferir. Na prova, mostre as regras usadas para construí-lo.

## 4. O que um zero faz

Adicionar um zero altera os trechos reais, o centroide e o número de assíntotas. Ele pode ampliar a faixa estável, mas **“zero à esquerda” não é prova universal de estabilidade**.

A estratégia recorrente nestas provas é cancelar um polo **estável e lento**:

- 2024.1: zero em $-1$.
- 2025.2: zero em $-2$.
- 2026.1: dois zeros em $-1$.

No modelo nominal e no canal referência–saída, um cancelamento exato reduz a função de transferência. O modo cancelado não desaparece de toda realização interna; nos exemplos ele é estável. Se o cancelamento não for exato, a aproximação pode perder precisão.

## 5. LGR complementar: K negativo

Em 2023.1 Q1, escreva $K=-k$, com $k>0$:

$$1-kL_0=0\Rightarrow kL_0=+1.$$

Agora a condição de fase é $2\ell180^\circ$, os trechos reais têm contagem **par** à direita e:

$$\theta_\ell=\frac{2\ell180^\circ}{n-m}.$$

O sinal de $K$ importa. Não aplique automaticamente as regras do ganho positivo.

## 6. O que pode e o que não pode ser concluído pelo desenho

| Observação | Interpretação |
|---|---|
| Polo dominante próximo de zero | Resposta lenta |
| Par complexo perto do eixo imaginário | Baixo amortecimento e longa acomodação |
| Polos reais negativos | Modos exponenciais sem senoides |
| Par real repetido no modelo de segunda ordem | Amortecimento crítico |
| Ramo no semiplano direito | Instabilidade |
| Todos os polos reais | Não garante, sozinho, ausência de sobressinal se houver zeros |

**Não-oscilatório**, **monótono** e **sem sobressinal** não são sinônimos em funções com zeros. Use a convenção de polos do enunciado e, quando for avaliar $M_p$, considere a função completa.

**Treino:** redesenhe 2025.1 Q3 sem olhar os gráficos; explique em voz alta por que P, PI, PD e PID produzem possibilidades diferentes.
