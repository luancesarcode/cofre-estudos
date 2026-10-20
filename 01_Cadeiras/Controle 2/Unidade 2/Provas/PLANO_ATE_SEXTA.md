# Plano de estudo até sexta-feira

[Voltar ao início](README.md)

**Referência:** segunda-feira, 19/10/2026; sexta-feira, 23/10/2026. Como você não informou horários disponíveis, este plano usa cerca de **13 horas líquidas**, distribuídas em blocos. Pausas ficam fora dessa conta. Se começar depois, use a versão de 8 horas no fim.

## A estratégia

Você tem 16 questões principais, mas várias repetem o mesmo procedimento. O melhor uso do tempo é aprender os procedimentos e depois misturá-los:

1. Transformar o diagrama em $L$ e $\Delta$.
2. Cruzar erro estacionário e estabilidade.
3. Construir o LGR e justificar o transitório.
4. Posicionar o zero e calcular o ganho por ângulo/módulo.
5. Encontrar $K_{cr},P_{cr}$ e aplicar a tabela pedida.

**Regra para cada bloco de 50 minutos:** 10 min de conceito, 30 min resolvendo no papel e 10 min corrigindo. Faça uma pausa de 10 min entre blocos. Quando já souber o conceito, use os 40 primeiros minutos sem consulta.

## Segunda, 19/10 — diagnóstico e base, 60 minutos

- **10 min:** diagnóstico de [Treino ativo](TREINO_ATIVO.md).
- **20 min:** [Base](Assuntos/01_Base_e_controladores.md) e [Erro](Assuntos/02_Erro_estacionario.md).
- **30 min:** faça 2026.1 Q2b apenas como introdução a Routh, seguindo a tabela se precisar. Anote os erros.

**Entrega do dia:** conseguir escrever $\Delta$ e explicar a diferença entre tipo 0 e tipo 1. Se já estiver tarde, encerre aqui; o bloco seguinte exige atenção.

## Terça, 20/10 — estabilidade, erro e LGR, 4 × 50 min

### Bloco 1 — Routh de terceira ordem

Leia [Routh](Assuntos/03_Routh_Hurwitz.md). Resolva 2023.2 Q1: o ganho dobra e o período é dado. Refaça a conversão entre período e frequência sem olhar.

**Meta:** chegar a $K=10000$ e justificar por que exatamente um dos parâmetros $a,b$ é zero.

### Bloco 2 — região de projeto

Leia [Regiões](Assuntos/08_Regioes_de_projeto.md). Faça 2024.1 Q1a e Q1c com consulta apenas quando travar.

**Meta:** explicar por que o P não funciona e desenhar a faixa entre as curvas do PD.

### Bloco 3 — repetir sem consulta

Faça 2024.2 Q1a e Q1c. Compare com 2024.1: o que mudou nos coeficientes e na interseção? Se sobrar tempo, faça 2025.1 Q2.

**Meta:** tabela correta e desigualdades com fronteiras abertas/fechadas.

### Bloco 4 — esboço e interpretação

Leia [LGR](Assuntos/04_LGR_esboco.md) e [Transitório](Assuntos/05_Transitorio_e_dominancia.md). Faça 2025.1 Q3 desenhando P, PD, PI e PID.

**Meta:** explicar cada curva; não basta copiar o desenho.

## Quarta, 21/10 — projeto e sintonia, 4 × 50 min

### Bloco 1 — PI por refinamento

Leia [Refinamento](Assuntos/06_Refinamento_e_projeto_PI.md). Faça 2025.1 Q1. Marque os vetores de fase e confira a soma angular.

**Meta:** obter aproximadamente $z=5,K=8,10$ e explicar por que $T_s$ completo difere da meta.

### Bloco 2 — Ziegler–Nichols e NO-OV

Leia [Sintonia](Assuntos/07_Ziegler_Nichols_e_NO_OV.md). Faça 2023.2 Q2 e 2024.1 Q2. Depois compare as linhas ZN e NO-OV, sem abrir a resolução de 2026.1 Q1.

**Meta:** obter $K_{cr},P_{cr}$ e converter corretamente $T_i,T_d$ em $K_i,K_d$.

### Bloco 3 — duas variações importantes

Faça 2023.1 Q1, sobre ganho negativo e fase não mínima, e 2023.2 Q3c, sobre deslocamento do eixo.

**Meta:** reconhecer quando o LGR é complementar e usar $s=q-2$ sem trocar o sinal.

### Bloco 4 — complementos da revisão

Faça os Extras A e E de [Extras resolvidos](Monitoria/EXTRAS_RESOLVIDOS.md): entrada $1/s^4$ e ZN em malha aberta. Leia as conclusões dos Extras B, C e D. Reserve os últimos 10 min para a lógica dos circuitos do [Assunto 09](Assuntos/09_PID_com_amplificadores.md).

**Meta:** cobrir os assuntos que só aparecem na revisão. Se souber que circuitos serão cobrados, acrescente 40–50 min para refazer a dedução dos estágios.

## Quinta, 22/10 — dois simulados e correção, 270 minutos

### Simulado 1 — 2025.2, 90 minutos

Abra só o enunciado. Tempo sugerido: Q1 em 60 min, Q2 em 25 min, revisão em 5 min. São tempos de treino, não duração oficial informada da prova.

Use apenas o formulário que seria permitido na avaliação. Se não souber o que será permitido, faça com uma folha de fórmulas e registre toda consulta.

### Simulado 2 — 2026.1, 90 minutos

Faça uma pausa antes. Tempo sugerido: Q1 em 50 min, Q2 em 35 min, revisão em 5 min.

Você já viu Q2b na segunda: agora precisa executá-la sem olhar. Concentre-se em encadear a justificativa completa.

### Correção — 60 minutos

Use as resoluções didáticas. Dê crédito ao procedimento correto mesmo se houve erro aritmético, mas registre separadamente:

- erro de conceito;
- erro de montagem;
- erro de álgebra;
- falta de justificativa/desenho;
- excesso de tempo.

Preencha o [Caderno de erros](CADERNO_DE_ERROS.md).

### Recuperação — 30 minutos

Refaça de folha limpa os dois itens de maior dificuldade. Só reler a resposta não conta como recuperação.

**Meta da quinta:** completar os métodos centrais sem ajuda. Se um erro se repetir, ele passa a ser a prioridade da sexta.

## Sexta, 23/10 — revisão leve, 30–45 minutos

Faça em um horário anterior à prova, sem presumir que ela será pela manhã.

1. Reescreva de memória: tabela cúbica de Routh, $K_v$, assíntotas, condição de ângulo, $K_i=K_p/T_i$ e $K_d=K_pT_d$.
2. Leia apenas os erros que você registrou.
3. Faça uma soma angular com vetor no segundo quadrante.
4. Revise a lista de fechamento abaixo.

Não use esse bloco para aprender um assunto inteiro novo.

## Se você só tiver 8 horas líquidas

| Tempo | Atividade |
|---|---|
| 30 min | Base e erro estacionário |
| 90 min | Routh + 2024.1 Q1a/c + 2025.1 Q2 |
| 60 min | LGR e escolha de controlador: 2025.1 Q3 |
| 60 min | PI por refinamento: 2025.1 Q1 e 2025.2 Q2 |
| 60 min | ZN/NO-OV: 2023.2 Q2 e 2026.1 Q1a |
| 90 min | Simulado completo 2026.1 |
| 60 min | Corrigir, refazer erros e revisar os Extras A/E |
| 30 min | Ganho negativo, deslocamento do eixo e leitura dos circuitos |

Esta versão prioriza cobertura dos métodos. Ela não substitui o treino de todas as provas.

## Como saber se está pronto

- [ ] Escrevo $\Delta=D+N$ sem confundir MA e MF.
- [ ] Resolvo uma cúbica e uma quártica por Routh.
- [ ] Acho frequência pelo polinômio auxiliar.
- [ ] Traduzo erro em desigualdade e faço a interseção.
- [ ] Desenho LGR com polos, zeros, trechos, centroide, assíntotas e sentido.
- [ ] Explico estabilidade e transitório sem afirmar que ganho alto sempre ajuda.
- [ ] Calculo $z$ pelo ângulo e $K$ pelo módulo.
- [ ] Uso a fórmula de $T_s$ no critério de 1% ou 2% correto.
- [ ] Converto e fatoro um PID corretamente.
- [ ] Distingo aproximação do gabarito de resultado exato.

Se faltar uma caixa, escolha uma questão curta correspondente no mapa de assuntos e refaça sem consulta.
