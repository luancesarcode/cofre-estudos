---
tipo: aula
data: 2026-08-28
cadeira: "[[Controle 2]]"
unidade: 1
tema: 3
tags: [aula, controle]
---

# Tema 3 — Projeto de sistemas de controle por alocação de polos

## Formulário e orientações de estudo

As questões partem do método de projeto por alocação de polos apresentado no Tema 3: iguala-se a **FTMF desejada** à **FTMF real** do sistema de controle e isola-se $G_c(s)$.

### Modelos desejados

| Modelo | FTMF desejada com ganho estático unitário |
|---|---|
| 1ª ordem | $\displaystyle M(s)=\frac{1}{\tau_ds+1}$ |
| 2ª ordem padrão | $\displaystyle M(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}$ |

O posicionamento dos polos é escolhido a partir do sobressinal e do tempo de acomodação desejados.

**Para obter $\zeta$ e $\omega_n$ a partir de $M_p$ e $T_s$:** use as expressões e a tabela de acomodação por faixa de $\zeta$ do formulário do Tema 2. Conforme as orientações enviadas, não substitua esses ajustes pela aproximação mais grosseira $T_s(2\%)\approx4/(\zeta\omega_n)$.

### Equações do projeto

$$\mathrm{FTMF}_{\mathrm{real}}(s)=\frac{G_c(s)G(s)}{1+G_c(s)G(s)H(s)}=M(s).$$

$$\boxed{G_c(s)=\frac{M(s)}{G(s)[1-H(s)M(s)]}}.$$

Com realimentação unitária:

$$\boxed{G_c(s)=\frac{1}{G(s)}\frac{M(s)}{1-M(s)}}.$$

| Objetivo ou verificação | Condição |
|---|---|
| Erro estacionário nulo ao degrau | $M(0)=1$, para modelo desejado estável |
| Controlador racional próprio | $\deg(\text{numerador})\leq\deg(\text{denominador})$ |
| Resultado final do projeto | Encontrar $G_c(s)$ com coeficientes numéricos |

**Orientação de estudo:** confira a propriedade do controlador antes de concluir o projeto. O critério de graus da imagem verifica se ele é próprio, condição usual de realizabilidade causal racional; também é necessário conferir estabilidade interna, cancelamentos e limites do sinal de controle, como explicado no resumo.

---

## Resumo explicado

Resumo para estudo e transcrição no caderno, com equações explicadas, exemplo resolvido e imagens importantes dos slides.

**Fonte:** Fabrício Bradaschia, UFPE, *Tema 3 — Projeto de Sistemas de Controle por Alocação de Polos*, slides 1 a 24. As imagens numeradas são reproduções do PDF original.

**Hipóteses:** modelos lineares no domínio de Laplace, realimentação negativa e condições iniciais nulas para as funções de transferência. As igualdades de desempenho são nominais: dependem da fidelidade do modelo e da viabilidade do controlador.

## 1. Qual é a ideia do método?

No Tema 2, partimos da função de transferência e descobrimos o comportamento da resposta. Neste tema, fazemos o caminho de projeto:

$$\text{requisitos de desempenho}\ \longrightarrow\ \text{modelo desejado}\ \longrightarrow\ \text{controlador}.$$

**Alocar polos** significa escolher onde os polos da malha fechada devem ficar para produzir uma dinâmica desejada.

Exemplos de requisitos:

- Erro estacionário nulo ao degrau.
- Sobressinal de aproximadamente 2%.
- Tempo de acomodação de 2% não superior a 0,5 s.

O tema realiza isso por **igualação da função de transferência desejada**, frequentemente envolvendo inversão e cancelamento da dinâmica da planta. É essa forma específica do método que estudaremos.

> Posicionar polos não determina sozinho toda a resposta: o numerador, os zeros e o ganho também importam. Por isso, o material escolhe uma função de transferência completa, e não somente um conjunto de polos.

## 2. Notação e função de transferência da malha fechada

| Símbolo | Significado |
|---|---|
| $R(s)$ | Referência |
| $Y(s)$ | Saída da planta |
| $U(s)$ | Sinal de controle aplicado à planta |
| $G(s)$ | Planta conhecida |
| $H(s)$ | Sensor conhecido |
| $G_c(s)$ | Controlador a determinar |
| $M(s)$ | Função de transferência desejada |
| $\mathrm{FTMF}(s)$ | Função de transferência em malha fechada |
| $\mathrm{FTRD}(s)$ | Função de transferência do ramo direto: $G_cG$ |

Para a realimentação negativa considerada:

$$\boxed{\mathrm{FTMF}(s)=\frac{Y(s)}{R(s)}=\frac{G_c(s)G(s)}{1+G_c(s)G(s)H(s)}}.$$

O projeto procura um controlador que faça essa expressão coincidir com $M(s)$.

## 3. Escolhendo o modelo desejado

### 3.1 Erro estacionário ao degrau

Para um degrau de amplitude $A$, em um modelo desejado estável:

$$y_\infty=AM(0),\qquad e_{\mathrm{ss}}=A[1-M(0)].$$

Portanto:

$$\boxed{M(0)=1\ \Rightarrow\ e_{\mathrm{ss}}=0\text{ ao degrau}}.$$

Isso garante o rastreamento nominal do degrau; não é uma garantia automática de rejeição a toda perturbação nem de erro nulo à rampa.

### 3.2 Modelo desejado de segunda ordem

Usando a forma-padrão do Tema 2:

$$M(s)=\frac{K\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}.$$

Para erro nulo ao degrau, escolhemos $K=1$:

$$\boxed{M(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}}.$$

Para $0<\zeta<1$, os polos desejados são:

$$\boxed{p_{1,2}=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}}.$$

O parâmetro $\zeta$ determina o sobressinal percentual. Mantendo $\zeta$ constante, $\omega_n$ determina a escala de tempo.

### 3.3 Requisitos numéricos do material

O exemplo usa aproximadamente 2% de sobressinal e acomodação de 2% em 0,5 s.

Para converter sobressinal em amortecimento, com $m=M_p\%/100$:

$$\zeta=\frac{-\ln m}{\sqrt{\pi^2+(\ln m)^2}}.$$

Com $m=0{,}02$:

$$\zeta\approx0{,}780.$$

O material escolhe $\omega_n=7{,}68$ rad/s, com base nos critérios aproximados do Tema 2. Logo:

$$\omega_n^2\approx58{,}97,\qquad2\zeta\omega_n\approx11{,}98.$$

$$\boxed{M(s)=\frac{58{,}97}{s^2+11{,}98s+58{,}97}}.$$

Os polos ficam próximos de:

$$\boxed{p_{1,2}=-5{,}99\pm j4{,}81}.$$

**Cuidado com a precisão:** os parâmetros e os critérios temporais do exemplo são arredondados. A própria simulação do slide 13 indica acomodação próxima de **0,468 s**, e não exatamente 0,500 s. O resultado atende ao limite de 0,5 s, mas não deve ser apresentado como igualdade exata. Próximo de um pico de 2%, pequenos arredondamentos podem alterar o instante da última saída da faixa.

## 4. Como encontrar o controlador: dedução passo a passo

Igualamos o modelo desejado à transferência da malha física:

$$M=\frac{G_cG}{1+G_cGH}.$$

Multiplicando pelo denominador:

$$M(1+G_cGH)=G_cG.$$

Distribuindo:

$$M+MG_cGH=G_cG.$$

Passando o termo com o controlador para o outro lado:

$$M=G_cG-MG_cGH.$$

Colocando $G_cG$ em evidência:

$$M=G_cG(1-MH).$$

Finalmente:

$$\boxed{G_c(s)=\frac{M(s)}{G(s)[1-M(s)H(s)]}}.$$

Uma forma equivalente, que destaca a inversão da planta, é:

$$\boxed{G_c(s)=\frac1{G(s)}\frac{M(s)}{1-H(s)M(s)}}.$$

**Leitura da fórmula:** $1/G$ inverte nominalmente a planta; o outro fator impõe o comportamento desejado. Isso é uma solução algébrica candidata: ainda precisamos verificar estabilidade interna, implementação e esforço de controle.

## 5. Simplificação para sensor unitário

Com $H=1$:

$$G_cG=\frac{M}{1-M}.$$

Para a segunda ordem desejada de ganho unitário:

$$1-M=\frac{s^2+2\zeta\omega_ns}{s^2+2\zeta\omega_ns+\omega_n^2}.$$

Dividindo $M$ por $1-M$, os denominadores comuns se cancelam:

$$\boxed{\mathrm{FTRD}_{\mathrm{desejada}}(s)=\frac{\omega_n^2}{s(s+2\zeta\omega_n)}}.$$

Portanto:

$$\boxed{G_c(s)=\frac1{G(s)}\frac{\omega_n^2}{s(s+2\zeta\omega_n)}}.$$

![[03_Recursos/Controle 2/imagens/tema_3/slide_10.png]]

*Slide 10. Os dois diagramas devem produzir a mesma malha fechada. Por isso, podemos igualar os ramos diretos neste caso unitário.*

O ramo direto desejado contém um integrador $1/s$, coerente com o objetivo de eliminar o erro ao degrau em malha fechada estável.

## 6. Exemplo completo do Tema 3

### 6.1 Planta

O slide 12 apresenta uma planta com ganho estático 0,8 e constantes de tempo de 0,1 s e 0,2 s:

$$G(s)=\frac{0{,}8}{(0{,}1s+1)(0{,}2s+1)}.$$

Como $(0{,}1s+1)=0{,}1(s+10)$ e $(0{,}2s+1)=0{,}2(s+5)$:

$$\boxed{G(s)=\frac{40}{(s+10)(s+5)}}.$$

Os polos naturais da planta estão em $-10$ e $-5$.

### 6.2 Controlador

Usando o modelo desejado e $H=1$:

$$G_c(s)=\frac{(s+10)(s+5)}{40}\frac{58{,}97}{s(s+11{,}98)}.$$

$$\boxed{G_c(s)=1{,}47425\frac{(s+10)(s+5)}{s(s+11{,}98)}}.$$

| Elemento | Posições |
|---|---|
| Polos da planta | $-10$ e $-5$ |
| Zeros do controlador | $-10$ e $-5$ |
| Polos do controlador | $0$ e $-11{,}98$ |
| Polos da transferência reduzida da malha fechada | Aproximadamente $-5{,}99\pm j4{,}81$ |

![[03_Recursos/Controle 2/imagens/tema_3/slide_12.png]]

*Slide 12. Os zeros do controlador coincidem nominalmente com os polos da planta.*

### 6.3 Conferência algébrica

Multiplicando planta e controlador:

$$G_cG=1{,}47425\frac{(s+10)(s+5)}{s(s+11{,}98)}\frac{40}{(s+10)(s+5)}.$$

Os fatores comuns se cancelam, resultando em:

$$G_cG=\frac{58{,}97}{s(s+11{,}98)}.$$

Fechando a malha:

$$\frac{G_cG}{1+G_cG}=\frac{58{,}97}{s(s+11{,}98)+58{,}97}=\boxed{M(s)}.$$

### 6.4 Resposta ao degrau

![[03_Recursos/Controle 2/imagens/tema_3/slide_13.png]]

*Slide 13. A planta sem o controlador chega a 0,8; a malha projetada chega a 1, com aproximadamente 2% de sobressinal e acomodação em cerca de 0,468 s.*

O controlador altera tanto a dinâmica quanto o ganho estático da transferência referência-saída. O modelo projetado possui erro estacionário nulo ao degrau unitário.

## 7. Por que verificar o sinal de controle?

Uma saída rápida pode exigir uma entrada muito intensa na planta. Precisamos examinar $U(s)$, não somente $Y(s)$.

Como $Y=GU$:

$$\boxed{\frac{U}{R}=\frac{M}{G}}.$$

Também podemos escrever:

$$\frac UR=\frac{G_c}{1+G_cGH}.$$

No exemplo, para degrau unitário:

$$u_\infty=\frac{M(0)}{G(0)}=\frac1{0{,}8}=1{,}25.$$

O controlador é próprio, com graus iguais no numerador e denominador. Sua transmissão direta permite um salto inicial finito no comando. Pelo modelo:

$$u(0^+)=\lim_{s\to\infty}\frac{M(s)}{G(s)}=\frac{58{,}97}{40}=1{,}47425.$$

![[03_Recursos/Controle 2/imagens/tema_3/slide_14.png]]

*Slide 14. O comando chega a aproximadamente 1,66 antes de se acomodar em 1,25. Esse pico deve caber nos limites do atuador e da planta.*

Se o atuador saturar, a dinâmica deixa de seguir o modelo linear ideal. Uma solução é reduzir a rapidez desejada, por exemplo diminuindo $\omega_n$ e refazendo o projeto. Também é necessário verificar limites de velocidade de atuação e efeitos de ruído.

## 8. Cancelamento de polos e zeros: o que significa?

Matematicamente:

$$\frac{s+a}{s+a}=1.$$

Fisicamente, a planta não perde seus elementos internos. O cancelamento aparece na transferência reduzida para determinados sinais e condições iniciais.

Se o modelo estima um polo em $-a$, mas o polo real está em $-(a+\Delta)$:

$$\frac{s+a}{s+a+\Delta}\neq1.$$

O cancelamento deixa de ser exato. Seu efeito depende da posição dos modos restantes e de seus resíduos.

### 8.1 Resíduos e exemplo dos slides

Na expansão:

$$Y(s)=\frac{A}{s}+\frac{B}{s+4}+\cdots,$$

o termo $B/(s+4)$ gera $Be^{-4t}$. O número $B$ é o resíduo: ele determina a amplitude dessa contribuição.

O material considera:

$$Y_a(s)=\frac{26{,}25(s+a)}{s(s+4)(s+5)(s+6)}.$$

O resíduo do polo $-4$ pode ser calculado diretamente:

$$B=\lim_{s\to-4}(s+4)Y_a(s)=\frac{26{,}25(a-4)}{(-4)(1)(2)}=-3{,}28125(a-4).$$

| $a$ | Resíduo do termo $1/(s+4)$ |
|---:|---:|
| 3,5 | 1,640625 |
| 4,1 | -0,328125 |
| 4,01 | -0,0328125 |
| 4 | 0 |

Quanto mais próximo o zero está do polo, menor é a amplitude desse modo no exemplo.

![[03_Recursos/Controle 2/imagens/tema_3/slide_18.png]]

*Slide 18. O termo associado ao polo $-4$ fica pequeno quando o zero se aproxima dele.*

![[03_Recursos/Controle 2/imagens/tema_3/slide_19.png]]

*Slide 19. Os casos com zero em $-4{,}01$ e $-4$ têm respostas muito próximas. Os valores finais também variam um pouco, pois o numerador é alterado sem reajuste do ganho.*

Um pequeno resíduo de modo estável pode justificar uma aproximação na faixa e na precisão de interesse. Isso não significa que qualquer cancelamento aproximado seja seguro.

## 9. Restrições e cuidados do método

### 9.1 Cancelamentos no semiplano direito

Se a planta tiver um polo instável, cancelá-lo com um zero do controlador pode esconder um modo instável na transferência reduzida. Condições iniciais e outras entradas podem excitar esse modo, mesmo que $Y/R$ pareça estável.

Se a planta tiver zero no semiplano direito, sua inversão introduz um polo instável no controlador. Isso também compromete a estabilidade interna.

**Não usar a inversão com cancelamento de modos instáveis para justificar estabilidade.** O problema não é somente o descasamento paramétrico; o cancelamento exato já pode esconder instabilidade interna.

> A restrição dos slides 23–24 refere-se ao procedimento por inversão/cancelamento usado neste tema. Ela não proíbe todas as técnicas de alocação de polos em plantas instáveis: outras estruturas, como realimentação de estados sob condições adequadas, não dependem desse cancelamento.

### 9.2 Controlador próprio ou impróprio

Uma função racional é **própria** quando:

$$\deg(\text{numerador})\leq\deg(\text{denominador}).$$

Se a inversão resultar em mais zeros que polos, o controlador é impróprio e exige diferenciação ideal. Isso não pode ser implementado exatamente como um sistema físico causal de banda finita.

Derivadores reais usam filtragem e banda limitada; não conhecem valores futuros do erro. Acrescentar filtros torna o controlador implementável, mas altera o modelo fechado e exige nova verificação do desempenho.

O critério correto envolve o **grau relativo** da planta e do modelo desejado, não somente suas ordens totais. Para $H=1$ e $M$ estritamente própria, um modelo desejado com grau relativo menor que o da planta geralmente produz controlador impróprio.

### 9.3 Robustez e complexidade

| Vantagem | Limitação correspondente |
|---|---|
| Projeto algébrico direto | Depende do modelo da planta |
| Especificações traduzidas em um modelo desejado | Nem todo modelo desejado é fisicamente realizável |
| Cancelamento nominal simplifica $Y/R$ | Incertezas recuperam dinâmicas canceladas |
| Possibilidade de resposta rápida | Esforço de controle, saturação e ruído podem limitar a rapidez |
| Modelo nominal de baixa ordem | Controlador e dinâmica interna podem ter ordem maior |

## 10. Complemento: modelo desejado de primeira ordem

O mesmo raciocínio pode ser aplicado a:

$$M(s)=\frac1{\tau_ds+1},\qquad H=1.$$

Então:

$$\frac{M}{1-M}=\frac1{\tau_ds},\qquad \boxed{G_c=\frac1{G\tau_ds}}.$$

Se $G(s)=K_g/(\tau s+1)$:

$$G_c(s)=\frac{\tau s+1}{K_g\tau_ds}=\frac{\tau}{K_g\tau_d}+\frac1{K_g\tau_d}\frac1s.$$

Isso corresponde a um PI:

$$\boxed{K_p=\frac{\tau}{K_g\tau_d},\qquad K_i=\frac1{K_g\tau_d}}.$$

Esse exemplo complementar mostra como um PI pode impor uma primeira ordem nominal ao cancelar um polo estável da planta. Os mesmos cuidados de modelagem e saturação permanecem.

## 11. Roteiro para exercícios

1. Identifique $G(s)$, $H(s)$ e a estrutura da realimentação.
2. Traduza erro, sobressinal e rapidez em um modelo desejado $M(s)$.
3. Use $G_c=M/[G(1-HM)]$.
4. Simplifique e identifique polos, zeros e grau relativo do controlador.
5. Recalcule a malha fechada e confira se ela coincide com $M$.
6. Examine estabilidade interna e cancelamentos.
7. Verifique $Y/R$ e também $U/R$; compare o comando com os limites físicos.
8. Avalie o desempenho com erros de modelagem e ajuste os requisitos se necessário.

**Fórmulas para guardar:**

$$\boxed{G_c=\frac{M}{G(1-HM)}},\qquad \boxed{H=1\Rightarrow G_cG=\frac{M}{1-M}},\qquad\boxed{\frac UR=\frac MG}.$$
