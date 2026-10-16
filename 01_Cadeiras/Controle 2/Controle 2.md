---
tipo: cadeira
nome: "Engenharia de Controle 2"
codigo: EL466
semestre: 2026.2
professor: Fabrício Bradaschia
status: ativa
creditos: 4
turma: CAEE
horario: "Quartas e sextas, 15h-17h (Sala 003 - DEE)"
carga_horaria: 60h
tags: [cadeira, controle]
---

# Engenharia de Controle 2 (EL466)

UFPE · DEE · Controle e Automação / Elétrica (CAEE) · 7º período
Professor: Fabrício Bradaschia (fabricio.bradaschia@ufpe.br, sala 113 DEE). Contato: Google Sala de Aula, G-Mail Chat ou e-mail. Notas no SIGAA.
Pré-requisito: EL465 (Engenharia de Controle 1): modelagem nos domínios do tempo e da frequência, malha aberta e fechada, sistemas de 1ª e 2ª ordem.

## Ementa / Objetivos
- **Ementa:** projeto de sistemas de controle analógicos de tempo contínuo por alocação de polos, métodos heurísticos, lugar geométrico das raízes e resposta em frequência, para atender requisitos transitórios e estacionários. Análise de estabilidade por Routh-Hurwitz, Nyquist e Bode. Aspectos práticos: controle em cascata, influência do atraso e da saturação.
- **Objetivos:** conduzir o projeto de um sistema de controle passo a passo; aplicar técnicas de análise e projeto de controladores analógicos de tempo contínuo e escolher a técnica mais adequada a cada sistema, respeitando os limites de estabilidade; projetar para requisitos transitórios e estacionários.
- **Metodologia:** presencial, aulas expositivas com quadro, projetor e simulações em MATLAB/Simulink feitas pelo docente. Apoio: MATLAB/Simulink (Control System Designer / SISO Tool), slides, monitoria (monitor a definir), Google Sala de Aula.
- **Bibliografia:**
  - Nise. *Engenharia de Sistemas de Controle*. LTC, 7ª ed., 2017 (básica)
  - Dorf e Bishop. *Sistemas de Controle Modernos*. LTC, 13ª ed., 2018 (básica)
  - Ogata. *Engenharia de Controle Moderno*. Pearson, 5ª ed., 2010
  - Golnaraghi e Kuo. *Sistemas de Controle Automático*. LTC, 9ª ed., 2012
  - Complementares: Franklin, Powell e Emami-Naeini. *Sistemas de Controle para Engenharia*. 6ª ed., 2013; Chen. *Analog and Digital Control System Design*. Oxford, 1995

## MOC — Mapa de Conteúdo

> Ao criar as notas de aula (em `01_Cadeiras/Controle 2/`) e de conceito, linke-as nas listas abaixo.

### Unidade 1 — Prova em 11/09
- [ ] **Tema 1:** Histórico, introdução e características dos sistemas de controle (12/08, 14/08)
- [ ] **Tema 2:** Desempenho de sistemas de 1ª e 2ª ordens (19/08, 21/08, 26/08)
- [ ] **Tema 3:** Projeto por alocação de polos (28/08)
- [ ] **Tema 4:** Desempenho de sistemas de ordens superiores (02/09, 04/09, 09/09)
- Aulas: [[Tema_1_Malha_Aberta_e_Fechada]] · [[Tema_2_Desempenho_1_e_2_Ordens]] · [[Tema_3_Projeto_por_Alocacao_de_Polos]] · [[Tema_4_Desempenho_de_Ordens_Superiores]]
- Conceitos: [[]]

### Unidade 2 — Prova em 23/10
- [ ] **Tema 5:** Estabilidade e critério de Routh-Hurwitz (16/09, 18/09, 23/09)
- [ ] **Tema 6:** Ações básicas de controle: P, I, D, avanço e atraso de fase (25/09)
- [ ] **Tema 7:** Métodos heurísticos de projeto de PID (30/09)
- [ ] **Tema 8:** Lugar geométrico das raízes: esboço e refinamento (02/10, 07/10, 09/10, 14/10)
- [ ] **Tema 9:** Propriedades do lugar geométrico das raízes (16/10, 21/10)
- Aulas: [[]]
- Conceitos: [[]]

### Unidade 3 — Prova em 04/12
- [ ] **Tema 10:** Resposta em frequência: Nyquist, Bode e projeto de controladores (30/10, 04/11, 06/11, 11/11, 13/11, 18/11, 25/11)
- [ ] **Tema 11:** Aspectos práticos de sistemas de controle: cascata, atraso, saturação (27/11, 02/12)
- Aulas: [[]]
- Conceitos: [[]]

## Provas e Trabalhos

| Avaliação | Data | Peso | Conteúdo | Nota |
|---|---|---|---|---|
| Prova da 1ª Unidade | 2026-09-11 | 1/3 | Temas 1-4 | |
| Prova da 2ª Unidade | 2026-10-23 | 1/3 | Temas 5-9 | |
| Prova da 3ª Unidade | 2026-12-04 | 1/3 | Temas 10-11 | |
| 2ª Chamada | 2026-12-09 | | Conteúdo completo | |
| Prova Final | 2026-12-11 ou 2026-12-16 | | Conteúdo completo | |

O plano de ensino não informa os pesos das provas. O 1/3 acima é uma suposição (média simples das três provas): confirme com o professor.

### Regras de aprovação
- **Média ≥ 7,0:** aprovado direto.
- **3,0 ≤ média < 7,0:** faz a Prova Final. Aprovado se a média final ≥ 5,0.
- **Média < 3,0 ou média final < 5,0:** reprovado por nota.
- **Frequência:** a presença conta nas aulas e nas provas (72 HA = 60 de aula + 12 de provas, 2 HA por prova). Limite de 25% de faltas (18 HA); acima disso, reprovação por falta.
- **2ª Chamada:** direito a 1 pedido (via secretaria da Coordenação) com justificativa válida, em até 3 dias úteis após a prova perdida. Sem pedido ou com pedido indeferido, conta como reprovação por falta (faltou a ≥ 33% das provas).
- **Feriados:** 28/10 (Servidor Público) e 20/11 (Consciência Negra) sem aula.

## Aulas
```dataview
TABLE data AS "Data"
FROM "01_Cadeiras"
WHERE tipo = "aula" AND cadeira = this.file.link
SORT data DESC
```
