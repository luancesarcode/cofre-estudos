# Inventário e organização das fontes

[Voltar ao início](README.md)

Foram analisados os 18 PDFs presentes inicialmente na pasta, totalizando 92 páginas. As sete provas somam 16 questões principais. Os nomes originais foram mantidos; só a localização mudou.

| Arquivo original | Páginas | Local atual |
|---|---:|---|
| EL466 Prova da 2ª Unidade, 2023.1 questoes.pdf | 3 | [Abrir](<2023.1/EL466 Prova da 2ª Unidade, 2023.1 questoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2023.1 resolucoes.pdf | 6 | [Abrir](<2023.1/EL466 Prova da 2ª Unidade, 2023.1 resolucoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2023.2 questoes.pdf | 3 | [Abrir](<2023.2/EL466 Prova da 2ª Unidade, 2023.2 questoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2023.2 resolucoes.pdf | 5 | [Abrir](<2023.2/EL466 Prova da 2ª Unidade, 2023.2 resolucoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2024.1 questoes.pdf | 3 | [Abrir](<2024.1/EL466 Prova da 2ª Unidade, 2024.1 questoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2024.1 resolucoes.pdf | 5 | [Abrir](<2024.1/EL466 Prova da 2ª Unidade, 2024.1 resolucoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2024.2 questoes.pdf | 2 | [Abrir](<2024.2/EL466 Prova da 2ª Unidade, 2024.2 questoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2024.2 resolucoes.pdf | 4 | [Abrir](<2024.2/EL466 Prova da 2ª Unidade, 2024.2 resolucoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2025.1 questoes.pdf | 2 | [Abrir](<2025.1/EL466 Prova da 2ª Unidade, 2025.1 questoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2025.1 resolucoes.pdf | 5 | [Abrir](<2025.1/EL466 Prova da 2ª Unidade, 2025.1 resolucoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2025.2 questoes.pdf | 2 | [Abrir](<2025.2/EL466 Prova da 2ª Unidade, 2025.2 questoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2025.2 resolucoes.pdf | 4 | [Abrir](<2025.2/EL466 Prova da 2ª Unidade, 2025.2 resolucoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2026.1 questoes.pdf | 2 | [Abrir](<2026.1/EL466 Prova da 2ª Unidade, 2026.1 questoes.pdf>) |
| EL466 Prova da 2ª Unidade, 2026.1 resolucoes.pdf | 7 | [Abrir](<2026.1/EL466 Prova da 2ª Unidade, 2026.1 resolucoes.pdf>) |
| Gabarito 2EE.pdf | 9 | [Abrir](<2026.1/Gabarito 2EE.pdf>) |
| Monitoria 03.pdf | 7 | [Abrir](<Monitoria/Monitoria 03.pdf>) |
| Monitoria 05.pdf | 7 | [Abrir](<Monitoria/Monitoria 05.pdf>) |
| Revisão 2EE.pdf | 16 | [Abrir](<Monitoria/Revisão 2EE.pdf>) |

## Critério de organização

- Cada par de enunciado e resolução foi agrupado pelo período acadêmico do título, mesmo quando a aplicação ocorreu no ano seguinte.
- Gabarito 2EE foi identificado pelas duas questões como manuscrito de 2026.1 e movido para essa pasta.
- Monitoria 03, Monitoria 05 e Revisão 2EE ficam em Monitoria. Os recortes sem período identificado não receberam ano por inferência.
- Todos os PDFs tiveram o conteúdo preservado; os hashes SHA-256 anteriores à mudança foram conferidos depois.

## Como o conteúdo foi conferido

- Leitura textual das provas e resoluções digitadas, com inspeção das páginas, tabelas e diagramas renderizados.
- Leitura visual das 39 páginas dos quatro PDFs manuscritos, que não tinham camada de texto.
- Desenvolvimento das equações características, limites de Routh, condições de erro e projetos de controladores.
- Conferência numérica das raízes e de respostas completas em casos com aproximações ou divergências relevantes.

## Reproduzir as conferências

[Script de cálculos e figuras](verificacao/calculos_e_figuras.py) — depende de NumPy, SciPy e Matplotlib. Execute a partir desta pasta com um Python que tenha essas bibliotecas.

[Resultados numéricos](verificacao/resultados_numericos.json) · [Manifesto com hashes](verificacao/fontes.json)

O script resolve as raízes de D(s)+K N(s) para os gráficos de LGR. As trajetórias são amostradas numericamente; as resoluções escritas mostram as regras necessárias para desenhá-las à mão. As respostas numéricas são de modelos ideais, sem incerteza de parâmetros.

As notas novas não são gabaritos oficiais. Quando há diferença do material fornecido, a justificativa está na resolução e no arquivo de correções.
