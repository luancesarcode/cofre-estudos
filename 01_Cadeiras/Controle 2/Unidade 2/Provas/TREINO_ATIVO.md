# Treino ativo: testar antes de reler

[Voltar ao início](README.md)

Use papel e calculadora. Primeiro escreva uma tentativa; só depois consulte a resolução. Marque **0 = não consegui**, **1 = consegui com ajuda**, **2 = consegui sozinho**.

## Diagnóstico inicial — 10 a 15 minutos

1. Para $L=K(s+z)/[s(s+3)(s+5)]$, escreva $\Delta$.
2. Qual o tipo de $L$ para $K,z>0$? Qual o erro de degrau? E o de rampa?
3. Qual condição torna $s^3+4s^2+8s+K$ estável, para $K>0$?
4. Para polos de MA $0,-1,-2,-3$, sem zeros, dê trechos reais, centroide e ângulos das assíntotas.
5. Converta $K_p=2,T_i=0,5,T_d=0,1$ para $K_i,K_d$.
6. Uma tabela NO-OV garante sobressinal zero? Justifique em uma frase.

**Conferência do diagnóstico**

1. $\Delta=s^3+8s^2+(15+K)s+Kz$.
2. Tipo 1, erro de degrau zero; rampa $15/(Kz)$, desde que a malha seja estável.
3. $0<K<32$.
4. $(-3,-2)$ e $(-1,0)$; centroide $-1,5$; $45^\circ,135^\circ,225^\circ,315^\circ$.
5. $K_i=4,K_d=0,2$.
6. Não; é uma regra heurística e precisa ser verificada na malha final.

**Pontuação de 0 a 12:** até 6, siga todos os blocos de base; de 7 a 9, priorize os métodos em que errou; de 10 a 12, comece os exercícios sem consulta. Essa pontuação orienta a prática, não prevê sua nota.

## Exercícios curtos por método

### E1 — Routh e oscilação

Para $\Delta=s^3+7s^2+11s+5+10K$, encontre faixa estável positiva, ganho crítico, frequência e período.

**Conferência:** $0<K<7,2$; $K_{cr}=7,2$; $\omega=\sqrt{11}$; $P=2\pi/\sqrt{11}$.

### E2 — fronteiras incluídas ou excluídas

Você encontrou $K<4,375$ para estabilidade e $K\ge4$ para erro. Qual o intervalo? Por que as extremidades são diferentes?

**Conferência:** $[4;4,375)$; erro admite igualdade, estabilidade estrita não.

### E3 — região do PD

Para $\Delta=s^4+9s^3+23s^2+(15+5K)s+5Kz$ e $e_{\rm rampa}=3/(Kz)$, desenhe a região com erro $\le0,3$.

**Conferência:** $z\ge10/K$, $z<(-25K^2+885K+2880)/(405K)$; $1,375479<K<34,024521$.

### E4 — fatoração do PID

Expanda $0,625(s+1)^2/s$. Depois diga qual ganho deve virar variável para traçar o LGR conservando os zeros.

**Conferência:** $0,625s+1,25+0,625/s$; o ganho externo 0,625, correspondente a $K_d$.

### E5 — quadrantes

No ponto $s_d=-3,716+j3,6268$, o vetor que parte do polo $-2$ pertence a qual quadrante? E o que parte do zero $-4$?

**Conferência:** segundo e primeiro, respectivamente. Vetores: $-1,716+j3,6268$ e $0,284+j3,6268$.

### E6 — PI completo

Refaça 2025.2 Q2 pelo ângulo e módulo, sem olhar os números intermediários.

**Conferência:** $z\approx3,0231$, $K\approx6,2230$. Se acertar o ganho mas não justificar os quadrantes, refaça o desenho dos vetores.

### E7 — ganho negativo

Para $G=(s-2)/[s(s+2)]$ com P, encontre a faixa estável.

**Conferência:** $-2<K_p<0$. Use a quadrática para conferir o LGR complementar.

### E8 — ganho estático

Polos $-2,-1,5\pm j$, nenhum zero, $G(0)=2$. Encontre a planta.

**Conferência:** $G=13/[(s+2)(s^2+3s+3,25)]$.

### E9 — deslocamento do eixo

Para $\Delta=s^3+8s^2+(K_p+15)s+K_i$, substitua $s=q-2$ e imponha um par imaginário em $q$.

**Conferência:** $\Delta=q^3+2q^2+(K_p-5)q+K_i-2K_p-6$; $K_p=1+K_i/4$; para par complexo no plano original, $K_i>16$.

### E10 — entrada de ordem maior

Se $L(s)\sim(K_2/10)/s^3$ perto de zero e $R=1/s^4$, qual o erro? Que condição impõe erro $\le1$?

**Conferência:** $10/K_2$; $K_2\ge10$, com estabilidade verificada à parte.

### E11 — comparar sintonias

Dois PIDs na mesma planta estável tipo 0 têm $(K_p,T_i)=(6,2)$ e $(4,1)$. Qual produz menor erro de rampa, supondo ambas as malhas finais estáveis?

**Conferência:** o segundo, pois $K_i=4$ contra 3. Maior $K_p$ sozinho não decide.

### E12 — identificar uma justificativa inválida

“As assíntotas estão no semiplano esquerdo, logo todos os ganhos positivos são estáveis.” O que falta?

**Conferência:** analisar os ramos e seus cruzamentos. A revisão pp. 3–4 contém um contraexemplo: com zero do PD em $-1$, o centroide é $-0,5$, mas só $K_d>16,25$ estabiliza.

## Exercícios de prova em sequência sugerida

| Etapa | Questões | Tempo de treino |
|---|---|---|
| Aprender | 2024.1 Q1a/c | 40–50 min, com consulta |
| Repetir | 2024.2 Q1a/c | 35–45 min, sem consulta |
| Consolidar | 2025.1 Q2 | 25–30 min |
| Entender geometria | 2025.1 Q3 | 30–40 min |
| Projetar | 2025.1 Q1 | 35–45 min |
| Variar o refinamento | 2025.2 Q2 | 25–30 min |
| Sintonia | 2023.2 Q2 e 2024.1 Q2 | 20–25 min cada |
| Transferir o conhecimento | 2023.1 Q1 e 2023.2 Q3 | 45–60 min |
| Simular | 2025.2 inteira; 2026.1 inteira | 90 min cada |

## Como corrigir um simulado

Use os pesos dos itens no enunciado. Dentro de cada item, avalie estes componentes, sem inventar uma rubrica oficial:

- identificação do modelo e equação característica;
- método solicitado;
- contas e resultado;
- desenho e justificativa física, quando pedidos.

Uma conta correta por método diferente do explicitamente exigido pode não valer toda a pontuação. Nas questões de refinamento, mostre ângulo e módulo.

Registre a dúvida no [Caderno de erros](CADERNO_DE_ERROS.md) e refaça no dia seguinte.
