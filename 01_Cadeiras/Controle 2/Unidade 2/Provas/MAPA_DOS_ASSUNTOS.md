# O que exatamente estudar

[Voltar ao início](README.md)

Este mapa registra o que foi encontrado nos arquivos. “Prioridade” é uma decisão de estudo baseada em recorrência, dependências e provas recentes; não é previsão estatística da próxima prova.

## Núcleo obrigatório

| Assunto | Operação que você precisa saber executar | Evidências |
|---|---|---|
| Malha aberta/fechada e controladores | Montar $L,\Delta$; passar entre formas do PID | Todas as provas |
| Tipo e erro estacionário | Escolher integração; calcular $K_v$; impor erro máximo | Todas as sete provas |
| Routh | Faixa de ganho, região de parâmetros, ganho crítico | Todas as sete provas |
| Esboço do LGR | Polos/zeros, trechos, assíntotas, centroide, trajetórias | 2023.1, 2024.1, 2024.2, 2025.1, 2025.2, 2026.1 |
| Região estabilidade ∩ erro | Duas fronteiras e hachura correta | 2023.2 Q3; 2024.1 Q1; 2024.2 Q1; 2025.1 Q2; 2025.2 Q1 |
| Transitório e dominância | $\zeta,\omega_n,M_p,T_s$; limitações de segunda ordem | 2023.1 Q1; 2024.1/2 Q1; 2025.1 Q1/Q3; 2025.2 Q1/Q2; 2026.1 |
| Refinamento por ângulo/módulo | Projetar zero e ganho de PI | Exigido explicitamente em 2025.1 Q1 e 2025.2 Q2 |
| ZN de malha fechada e NO-OV | $K_{cr},P_{cr},K_p,K_i,K_d$ | 2023.1 Q2; 2023.2 Q2; 2024.1/2 Q2; 2026.1 Q1 |
| Zeros para modificar o transitório | Cancelamentos estáveis e possibilidades de P/PD/PI/PID | 2023.1 Q1/Q2; 2024.1 Q1d; 2025.1 Q3; 2025.2 Q1c; 2026.1 |

## Variações que não devem ser esquecidas

| Assunto | Onde aparece | Prioridade |
|---|---|---|
| Ganho negativo e LGR complementar | 2023.1 Q1 | Após dominar LGR positivo |
| Planta de fase não mínima | 2023.1 Q1 | Estudar junto do ganho negativo |
| Período dado e ganho dobrado | 2023.2 Q1; Monitoria 03 pp. 6–7 | Alta: aplicação simples de Routh |
| Estabilidade relativa / deslocar eixo | 2023.2 Q3c | Média |
| Casos especiais de Routh | Monitoria 03 pp. 1–2 | Saber a receita; linha nula é central |
| Entrada $1/s^4$ | Revisão pp. 1–2 | Complemento curto e importante |
| Planta com polos no eixo imaginário | Revisão pp. 3–4 | Complemento; há correção no exemplo |
| Reconstruir controlador a partir de LGRs | Revisão pp. 5–6 | Complemento de LGR |
| Comparar ZN, SO-OV e NO-OV pelo erro | Revisão pp. 7–10 | Complemento de sintonia |
| ZN em malha aberta, tangente e parâmetros $L,R$ | Revisão pp. 12–15 | Cobrir antes da prova |
| PID analógico e filtro derivativo | Revisão p. 16 | Menor recorrência; estudar após o núcleo |

## Mapa por questão

| Prova | Questão | Assuntos |
|---|---|---|
| 2023.1 | Q1, 4 pt | LGR positivo/negativo; zero não mínimo; crítico; PD |
| 2023.1 | Q2, 6 pt | Tipo; PI; ZN; Routh quártico; PID por zero adicional |
| 2023.2 | Q1, 2,5 pt | Tipo 1; Routh; frequência; ganho dobrado |
| 2023.2 | Q2, 2,5 pt | ZN fechado; PID |
| 2023.2 | Q3, 5 pt | PI; região; erro de rampa; deslocamento do eixo |
| 2024.1 | Q1, 7 pt | P/PD; Routh; erro; LGR; transitório |
| 2024.1 | Q2, 3 pt | Reconstruir planta por polos e ganho estático; ZN |
| 2024.2 | Q1, 7 pt | P/PD; Routh; erro; LGR; transitório |
| 2024.2 | Q2, 3 pt | Ganho estático; ZN |
| 2025.1 | Q1, 3 pt | Refinamento PI; dominância |
| 2025.1 | Q2, 3 pt | PD; região estabilidade ∩ erro |
| 2025.1 | Q3, 4 pt | Comparar P/PD/PI/PID; polos reais |
| 2025.2 | Q1, 7 pt | LGR; região; cancelamento PD; rapidez |
| 2025.2 | Q2, 3 pt | PI por ângulo e módulo; zero da planta |
| 2026.1 | Q1, 6 pt | NO-OV; fatoração; LGR; PID por cancelamento |
| 2026.1 | Q2, 4 pt | I/PI/PID; Routh; estabilidade e não oscilação |

As pontuações somam 10 em cada prova, mas não foram usadas para inventar porcentagens por assunto: várias questões cobram diversos métodos simultaneamente.

## O que não apareceu como exercício neste conjunto

Não foram encontrados exercícios de Bode, Nyquist, margens de ganho/fase, discretização, controlabilidade/observabilidade, LQR ou projeto em espaço de estados. A Monitoria 03 menciona autovalores apenas como motivação para estabilidade.

Avanço e atraso aparecem como alternativas de escolha em 2023.2, sem um projeto completo desses compensadores. Saiba reconhecê-los; não gaste o primeiro bloco aprendendo um método de projeto que não está nesses arquivos.
