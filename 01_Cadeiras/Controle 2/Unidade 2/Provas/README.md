# Controle 2 — preparação para a 2ª unidade

**Comece pelo [plano até sexta-feira](PLANO_ATE_SEXTA.md).** Depois estude por método e use as provas recentes como simulados.

Foram analisados **18 PDFs, 92 páginas e sete provas, de 2023.1 a 2026.1**. Os PDFs originais estão organizados nas pastas dos períodos, com conteúdo preservado. As resoluções em Markdown são explicações novas, baseadas nos enunciados e materiais fornecidos, com conferências algébricas e numéricas.

## Seu caminho de estudo

1. Faça o diagnóstico curto em [Treino ativo](TREINO_ATIVO.md).
2. Aprenda erro estacionário + Routh + região de projeto.
3. Aprenda a desenhar e interpretar o LGR.
4. Faça projeto de PI por ângulo e módulo.
5. Faça Ziegler–Nichols e NO-OV; compare com projeto pelo LGR.
6. Resolva 2025.2 e 2026.1 sem consultar; corrija usando as resoluções.

O núcleo aparece repetidamente nas provas. O material de revisão também traz entradas cúbicas, malha aberta de ZN e implementação analógica; esses complementos estão incluídos, com prioridade indicada no plano.

## Arquivos para orientar o estudo

| Arquivo | Para que serve |
|---|---|
| [Plano até sexta](PLANO_ATE_SEXTA.md) | Ordem, blocos de tempo e versão reduzida |
| [Mapa dos assuntos cobrados](MAPA_DOS_ASSUNTOS.md) | Cada assunto ligado às questões reais |
| [Formulário](FORMULARIO.md) | Consulta rápida depois de entender os métodos |
| [Treino ativo](TREINO_ATIVO.md) | Diagnóstico, exercícios e respostas de conferência |
| [Caderno de erros](CADERNO_DE_ERROS.md) | Registrar o que precisa ser refeito |
| [Correções e aproximações](CORRECOES_E_APROXIMACOES.md) | Divergências verificadas nos materiais |
| [Inventário das fontes](FONTES_E_ORGANIZACAO.md) | Os 18 PDFs e onde foram guardados |

## Assuntos em ordem de aprendizagem

| Ordem | Nota de estudo |
|---|---|
| 1 | [Base, malhas e controladores](Assuntos/01_Base_e_controladores.md) |
| 2 | [Erro estacionário e tipo](Assuntos/02_Erro_estacionario.md) |
| 3 | [Routh-Hurwitz](Assuntos/03_Routh_Hurwitz.md) |
| 4 | [Esboço do LGR](Assuntos/04_LGR_esboco.md) |
| 5 | [Transitório e dominância](Assuntos/05_Transitorio_e_dominancia.md) |
| 6 | [Refinamento e projeto de PI](Assuntos/06_Refinamento_e_projeto_PI.md) |
| 7 | [Ziegler–Nichols, SO-OV e NO-OV](Assuntos/07_Ziegler_Nichols_e_NO_OV.md) |
| 8 | [Regiões de projeto](Assuntos/08_Regioes_de_projeto.md) |
| 9 | [PID com amplificadores operacionais](Assuntos/09_PID_com_amplificadores.md) |

## Provas organizadas por período

Cada pasta contém o enunciado original, a resolução fornecida e uma resolução didática, item por item.

| Período | Questões | Melhor uso | Resolução |
|---|---:|---|---|
| 2023.1 | 2 | Ganho negativo, fase não mínima e PI de ZN | [Estudar](2023.1/RESOLUCAO_DIDATICA.md) |
| 2023.2 | 3 | Routh, ganho crítico e deslocamento do eixo | [Estudar](2023.2/RESOLUCAO_DIDATICA.md) |
| 2024.1 | 2 | Aprender região estável ∩ erro | [Estudar](2024.1/RESOLUCAO_DIDATICA.md) |
| 2024.2 | 2 | Repetir o método com outros coeficientes | [Estudar](2024.2/RESOLUCAO_DIDATICA.md) |
| 2025.1 | 3 | PI por refinamento e escolha de controlador | [Estudar](2025.1/RESOLUCAO_DIDATICA.md) |
| 2025.2 | 2 | Primeiro simulado | [Corrigir](2025.2/RESOLUCAO_DIDATICA.md) |
| 2026.1 | 2 | Último simulado, NO-OV e PID pelo LGR | [Corrigir](2026.1/RESOLUCAO_DIDATICA.md) |

O manuscrito Gabarito 2EE foi identificado pelos enunciados como a resolução de 2026.1 e está nessa pasta.

## Monitoria e revisão

- [Guia de páginas dos materiais](Monitoria/GUIA_DOS_MATERIAIS.md).
- [Exercícios exclusivos da revisão, resolvidos](Monitoria/EXTRAS_RESOLVIDOS.md).

## Como ler as resoluções

As fórmulas usam LaTeX em Markdown. Abra em um leitor com suporte matemático. Os gráficos são PNGs locais, disponíveis na pasta figuras, e aparecem dentro das notas.

Quando um resultado do PDF é apenas um esboço, o texto o identifica como estimativa. Quando a conferência encontra uma divergência, o valor corrigido e sua justificativa são apresentados. Não é necessário decorar a lista de divergências: use-a quando dois valores parecerem incompatíveis.

As prioridades descrevem o conjunto fornecido; não são garantia do conteúdo da próxima prova. Não foram acrescentados como núcleo assuntos sem ocorrência nesses materiais, como Bode, Nyquist, controle digital ou projeto em espaço de estados.
