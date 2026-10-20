# Como usar os materiais de monitoria

[Voltar ao início](../README.md)

As 39 páginas manuscritas foram examinadas visualmente, inclusive diagramas e cálculos. Elas complementam as sete provas; não são quatro provas adicionais.

## Monitoria 03 — 7 páginas

[Abrir PDF](<Monitoria 03.pdf>)

| Páginas | Conteúdo | Quando estudar |
|---|---|---|
| 1–2 | Routh, construção da tabela, sinais, casos especiais, deslocamento do eixo | Antes das regiões de estabilidade |
| 3 | Exemplo de projeto com integrador que termina instável | Para lembrar que erro não prova estabilidade |
| 4–5 | PD da mesa fresadora, erro de rampa 0,3 e região $K_d\times z$ | Junto de 2025.1 Q2 |
| 6–7 | Ganho que dobra e produz oscilação com período $\pi/10$ | Junto de 2023.2 Q1 |

**Exemplo da p. 3:** controlador $50/s$ e planta

$$G=\frac{11138,6469}{s^2+88,2400s+5569,3234}.$$

A característica é:

$$s^3+88,24s^2+5569,3234s+556932,345.$$

Routh exige $88,24\cdot5569,3234>556932,345$, o que não ocorre. A primeira coluna tem sinais $+,+,-,+$: **dois polos no semiplano direito**. O erro calculado pela regra de tipo não pode ser usado como garantia de regime permanente.

## Monitoria 05 — 7 páginas

[Abrir PDF](<Monitoria 05.pdf>)

| Páginas | Conteúdo | Correspondência |
|---|---|---|
| 1–2 | Equação característica, módulo/fase e regras básicas do LGR | Assuntos 04 e 06 |
| 3–5 | Comparação P/PD/PI/PID para $40/(s^2+8s+52)$ | 2025.1 Q3 |
| 6–7 | LGR com P da fresa $10/[s(s+2)(s+4)(s+5)]$ | 2025.2 Q1a |

As trajetórias coloridas representam cenários diferentes de posição dos zeros, não ramos extras simultâneos. Em um sistema de segunda ordem há dois ramos; trocar a posição do zero produz outro LGR.

**Atenção:** a tabela da p. 7 é ilustrativa. O tempo 6,725 s pressupõe $\omega_n=1$ no modelo crítico; não é um tempo universal para a fresa desenhada. Consulte a resolução de 2025.2 para o ponto de saída refinado.

## Revisão 2EE — 16 páginas

[Abrir PDF](<Revisão 2EE.pdf>)

| Páginas | Exercício/assunto | Material novo em Markdown |
|---|---|---|
| 1–2 | PID com $K_1,K_2$, entrada $1/s^4$, região viável | Extra A |
| 3–4 | Planta com polos imaginários, P instável, PD estabilizante | Extra B |
| 5–6 | Reconstruir PID a partir de dois LGRs | Extra C |
| 7–10 | Comparar ZN, SO-OV e NO-OV; calcular PID e esboçar LGR | Extra D |
| 11 | Refinar saída do eixo real da fresa de 2025.2 | Resolução 2025.2 Q1a |
| 12–15 | ZN em malha aberta e fechada; comparar erros | Extra E |
| 16 | Implementação analógica do controlador | Assunto 09 e Extra F |

Os exercícios recortados na revisão não trazem período acadêmico identificável. Foram mantidos em Monitoria, sem atribuir um ano por suposição.

## Gabarito 2EE — 9 páginas, identificado como 2026.1

[Abrir manuscrito](<../2026.1/Gabarito 2EE.pdf>) · [Ler resolução didática](../2026.1/RESOLUCAO_DIDATICA.md)

| Páginas | Conteúdo |
|---|---|
| 1–2 | Q1a: ganho crítico, período e PID NO-OV |
| 3 | Q1b: fatoração e LGR |
| 4–5 | Q1c: zeros em $-1$, cancelamento e ganho 0,625 |
| 6–7 | Q2a: I e PI com zero em $-1$ |
| 8 | Q2b: Routh e comparação de estabilidade |
| 9 | Q2c: PID com zeros em $-1$ e $-5$ |

**Correções de leitura:** na p. 8, $32+3K>0$ resulta em $K>-32/3$, não $K<-32/3$. A conclusão final para $K>0$ permanece correta. Na p. 5, o par do sistema reduzido está em $-2,5$; o polo cancelado em $-1$ não é o polo dominante da transferência reduzida.

## Como imitar o bom método do monitor

1. Escreva a FTMA antes de operar.
2. Traduza cada frase do enunciado em uma equação ou inequação.
3. Deixe visível o motivo de cada condição de Routh.
4. Desenhe cada fronteira antes de hachurar a interseção.
5. Destaque o resultado final e confira em uma linha.

Os arquivos didáticos usam essa sequência, mas corrigem erros de sinal e identificam os limites das aproximações.
