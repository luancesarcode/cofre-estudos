---
tipo: aula
data: 2026-08-12
cadeira: "[[Controle 2]]"
unidade: 1
tema: 1
tags: [aula, controle]
---

# Tema 1 — Malha aberta versus malha fechada

## Formulário e orientações de estudo

As questões são agrupadas por bloco de conteúdo, na mesma ordem dos slides do Tema 1. Este quadro reproduz as orientações da imagem enviada.

**Ganho de malha:**

$$\boxed{L(s)=G_c(s)G(s)}.$$

**Erro estacionário ao degrau unitário**, sem perturbação nem ruído:

| Sistema | Expressão |
|---|---|
| Malha aberta | $\displaystyle e_{\mathrm{est}}^{\mathrm{ma}}=1-L(0)$ |
| Malha fechada, com $H(s)=1$ | $\displaystyle e_{\mathrm{est}}^{\mathrm{mf}}=\frac{1}{1+L(0)}$ |

**Sensibilidade a pequenas variações na planta**, mantendo o controlador fixo:

| Sistema | Expressão |
|---|---|
| Malha aberta | $\displaystyle S_G^T=1$ |
| Malha fechada, com $H(s)=1$ | $\displaystyle S_G^T=\frac{1}{1+L(s)}$ |

As expressões de erro estacionário pressupõem as condições de validade do teorema do valor final.

**Referência indicada nas orientações enviadas:** Capítulo 4 de Dorf & Bishop — características de sistemas de controle com retroação.

---

## Resumo explicado

Resumo para estudo e transcrição no caderno, com fórmulas explicadas e imagens dos slides.

**Fonte:** Fabrício Bradaschia, UFPE, *Tema 1 — Histórico, Introdução e Características dos Sistemas de Controle*, principalmente slides 22 a 56. As imagens identificadas por número de slide são reproduções do material original. Os gráficos complementares são exemplos elaborados para este resumo.

**Hipóteses das equações:** sistemas lineares, condições iniciais nulas, realimentação negativa e sensor unitário, salvo indicação contrária. A perturbação entra na entrada da planta, depois do controlador.

## 1. Ideia principal

**Malha aberta:** o controlador aplica um comando a partir da referência, sem utilizar a saída para corrigir sua ação. Seu desempenho depende do conhecimento e da calibração do sistema.

Exemplo: aquecedor ligado por um tempo programado, sem medir a temperatura atingida.

**Malha fechada:** a saída é medida, comparada com a referência e utilizada para ajustar a ação do controlador. O objetivo é reduzir o erro.

Exemplo: aquecedor com termostato, que ajusta o funcionamento conforme a temperatura medida.

| Característica | Malha aberta | Malha fechada |
|---|---|---|
| Realimentação | Não utiliza a saída no controle | Utiliza a saída medida |
| Ação de controle | Baseada na referência | Baseada no erro medido |
| Custo e complexidade | Geralmente menores | Geralmente maiores |
| Variações da planta | Podem comprometer a precisão | Podem ter seus efeitos reduzidos |
| Perturbações desconhecidas | Não são corrigidas por realimentação | Podem ser rejeitadas |
| Ruído de medição | Não entra por uma malha de realimentação | Pode afetar a ação de controle |
| Estabilidade | Depende da planta e do controlador | Também depende do projeto da realimentação |

> A afirmação do slide de que a malha aberta não apresenta problemas de estabilidade deve ser entendida como ausência de problemas **introduzidos pela realimentação**. Uma planta pode ser instável mesmo em malha aberta.

## 2. Símbolos e diagrama do Tema 1

| Símbolo | Significado |
|---|---|
| $R(s)$ | Referência: valor desejado |
| $Y(s)$ | Saída real da planta |
| $G_c(s)$ | Função de transferência do controlador |
| $G(s)$ | Função de transferência da planta |
| $H(s)$ | Função de transferência do sensor |
| $T_p(s)$ | Perturbação adicionada à entrada da planta |
| $N(s)$ | Ruído de medição |
| $E(s)$ | Erro real de rastreamento: $R(s)-Y(s)$ |
| $L(s)$ | Produto $G_c(s)G(s)$, conforme a definição do tema |

As letras maiúsculas representam sinais no domínio de Laplace; por exemplo, $R(s)$ é a transformada de $r(t)$.

![[03_Recursos/Controle 2/imagens/tema_1/slide_31.png]]

*Slide 31. Observe que a perturbação é somada depois do controlador e antes da planta. O ruído aparece no caminho de medição.*

**Perturbação e ruído são diferentes:** a perturbação atua no processo físico; o ruído altera a informação medida. Em um motor, carga adicional é perturbação; interferência elétrica no sensor é ruído.

O material considera sensor ideal de ganho unitário:

$$H(s)=1.$$

Para representar a malha aberta, adota $H(s)=0$ e $N(s)=0$.

### Erro real e erro medido

Com sensor unitário, o controlador recebe:

$$E_c(s)=R(s)-[Y(s)+N(s)].$$

O erro real de rastreamento é:

$$\boxed{E(s)=R(s)-Y(s)}.$$

Assim, $E_c=E-N$. Na presença de ruído, o erro percebido pelo controlador não é necessariamente igual ao erro real. O rótulo $E(s)$ no somador do slide 31 deve ser interpretado com esse cuidado: neste resumo, usamos $E_c$ para esse sinal.

## 3. Análise do erro em malha aberta

A entrada da planta é a soma do comando com a perturbação:

$$Y(s)=G(s)[G_c(s)R(s)+T_p(s)].$$

Definindo $L(s)=G_c(s)G(s)$:

$$\boxed{Y(s)=L(s)R(s)+G(s)T_p(s)}.$$

Como $E=R-Y$:

$$\boxed{E(s)=[1-L(s)]R(s)-G(s)T_p(s)}.$$

- $[1-L]R$ é a contribuição do rastreamento imperfeito da referência.
- $-GT_p$ é a contribuição da perturbação.

O controlador pode ajustar o rastreamento por meio de $L$. Entretanto, neste diagrama, a transferência da perturbação para a saída depende apenas da planta.

## 4. Análise do erro em malha fechada

Partimos da entrada efetiva da planta:

$$Y=G\{G_c[R-Y-N]+T_p\}.$$

Distribuindo os termos e usando $L=G_cG$:

$$Y=LR-LY-LN+GT_p.$$

Reunindo os termos em $Y$:

$$[1+L]Y=LR-LN+GT_p.$$

Portanto:

$$\boxed{Y(s)=\frac{L(s)}{1+L(s)}R(s)+\frac{G(s)}{1+L(s)}T_p(s)-\frac{L(s)}{1+L(s)}N(s)}.$$

Subtraindo a saída da referência:

$$\boxed{E(s)=\frac{1}{1+L(s)}R(s)-\frac{G(s)}{1+L(s)}T_p(s)+\frac{L(s)}{1+L(s)}N(s)}.$$

![[03_Recursos/Controle 2/imagens/tema_1/slide_33.png]]

*Slide 33. A equação do erro reúne as contribuições da referência, da perturbação e do ruído.*

Para memorizar, definimos as funções de sensibilidade e sensibilidade complementar:

$$S(s)=\frac1{1+L(s)},\qquad T(s)=\frac{L(s)}{1+L(s)}.$$

$$\boxed{E=SR-GS\,T_p+TN},\qquad \boxed{Y=TR+GS\,T_p-TN}.$$

Aqui, $T(s)$ é a transferência da referência para a saída da malha fechada; não confunda com a perturbação $T_p(s)$.

Se $H(s)\neq1$, o denominador passa a conter $1+G_cGH$. O caminho do ruído depende também do ponto em que ele é introduzido; as fórmulas acima usam exatamente a hipótese unitária do tema.

## 5. Sensibilidade: significado e cálculo passo a passo

A sensibilidade mede quanto uma pequena variação relativa na planta altera a transferência total do sistema. O controlador é mantido fixo.

Exemplos: mudança de resistência com a temperatura, desgaste, alteração de massa ou atrito.

Se $T=Y/R$, com as outras entradas nulas:

$$S_G^T=\frac{\partial T/T}{\partial G/G}.$$

Dividir por uma fração é multiplicar pelo seu inverso:

$$\boxed{S_G^T=\frac{\partial T}{\partial G}\frac{G}{T}}.$$

Portanto, devemos **derivar $T$ em relação a $G$ e multiplicar por $G/T$**. Nas próximas contas omitimos $(s)$ para facilitar a leitura.

### 5.1 Malha aberta

$$T=G_cG,\qquad \frac{\partial T}{\partial G}=G_c.$$

Logo:

$$S_G^T=G_c\frac{G}{G_cG}=\boxed1.$$

Uma variação de 5% no ganho da planta provoca uma variação de 5% no ganho total, com controlador fixo.

### 5.2 Malha fechada

$$T=\frac{G_cG}{1+G_cG}.$$

Pela regra do quociente, $(u/v)'=(u'v-uv')/v^2$:

$$\frac{\partial T}{\partial G}=\frac{G_c(1+G_cG)-(G_cG)G_c}{(1+G_cG)^2}.$$

No numerador, os termos quadráticos se cancelam:

$$G_c+G_c^2G-G_c^2G=G_c.$$

Assim:

$$\frac{\partial T}{\partial G}=\frac{G_c}{(1+G_cG)^2}.$$

O segundo fator é:

$$\frac GT=\frac{G}{G_cG/(1+G_cG)}=\frac{1+G_cG}{G_c}.$$

Multiplicando:

$$S_G^T=\frac{G_c}{(1+G_cG)^2}\frac{1+G_cG}{G_c}=\boxed{\frac1{1+L}}.$$

![[03_Recursos/Controle 2/imagens/tema_1/slide_36.png]]

*Slide 36. As contas acima desenvolvem as etapas condensadas neste slide.*

Para pequenas variações:

$$\frac{\Delta T}{T}\approx S_G^T\frac{\Delta G}{G}.$$

**Exemplo estático:** com $L(0)=9$, a sensibilidade da malha fechada é $1/10=0{,}1$. Uma pequena variação de 5% no ganho da planta provoca aproximadamente $0{,}1\times5\%=0{,}5\%$ no ganho total. A malha fechada é menos sensível à variação.

## 6. Perturbação: redução relativa e efeito restante

Para estudar somente a perturbação, fazemos $R=N=0$.

**Malha aberta:**

$$\boxed{\frac{Y}{T_p}=G}.$$

**Malha fechada:**

$$\boxed{\frac{Y}{T_p}=\frac{G}{1+L}}.$$

Comparando as transferências:

$$\frac{G/(1+L)}G=\frac{G}{1+L}\frac1G=\boxed{\frac1{1+L}}.$$

Esse fator indica quanto sobra do efeito em relação à malha aberta. Para comparar amplitudes senoidais, usamos seu módulo na frequência considerada.

### Exemplo para entender o que ainda sobra

Considere sistema estável, $G(0)=100$, $L(0)=9$ e perturbação constante de amplitude $D=1$.

$$\Delta y_{\mathrm{ma}}=100\cdot1=100.$$

$$\Delta y_{\mathrm{mf}}=\frac{100}{1+9}\cdot1=10.$$

A realimentação reduziu o desvio de 100 para 10: sobraram 10% do efeito inicial, uma redução de 90%. Mas, se o desvio permitido fosse 0,5, ainda não seria suficiente.

- $1/(1+L)$ informa a **redução relativa**.
- $G/(1+L)$ é o **ganho da perturbação até a saída**.
- O desvio efetivo também depende da amplitude da perturbação.

Quando $|L(j\omega)|\gg1$, há forte redução relativa naquela frequência. Para um efeito absoluto pequeno, também precisamos que $|G(j\omega)/(1+L(j\omega))|$ seja suficientemente pequeno para a aplicação.

## 7. Ruído de medição e compromisso de projeto

Fazendo $R=T_p=0$:

$$\boxed{\frac{Y(s)}{N(s)}=-\frac{L(s)}{1+L(s)}}.$$

O sinal negativo aparece porque o controlador reage à medição: uma saída artificialmente alta faz o controlador atuar para reduzi-la.

![[03_Recursos/Controle 2/imagens/tema_1/slide_41.png]]

*Slide 41. Para atenuar ruído, o material recomenda ganho de malha pequeno nas frequências em que ele predomina.*

| Condição | Transferência aproximada do ruído | Consequência |
|---|---|---|
| $\vert L(j\omega)\vert \gg1$ | $Y/N\approx-1$ | Ruído é transmitido com módulo próximo de 1 |
| $\vert L(j\omega)\vert \ll1$ | $Y/N\approx-L$ | Efeito do ruído na saída é atenuado |

O projeto usual busca:

| Faixa | Ganho desejado | Finalidade |
|---|---|---|
| Baixas frequências | $\vert L\vert \gg1$ | Rastrear referência, reduzir sensibilidade e rejeitar perturbações |
| Altas frequências | $\vert L\vert \ll1$ | Atenuar ruído de medição |

Referências e perturbações são frequentemente lentas; ruído costuma ter componentes rápidas. Isso não exclui erros lentos do sensor, como desvio de calibração.

$$\boxed{S(s)+T(s)=1}.$$

Não podemos tornar ambas as funções arbitrariamente pequenas na mesma frequência. A identidade vale para as funções complexas; seus módulos não necessariamente somam 1.

![[03_Recursos/Controle 2/imagens/tema_1/frequencia_malha_fechada.png]]

*Exemplo com $G(s)=1/(2s+1)$ e $G_c=9$. À esquerda, $S$ pequeno favorece precisão e baixa sensibilidade; à direita, $T$ pequeno reduz a transmissão do ruído.*

Aqui, $s=j\omega$ representa a análise de resposta senoidal, $\omega$ é a frequência angular e as barras indicam módulo. A estabilidade deve ser preservada: perto de $L(j\omega)=-1$, o denominador $1+L$ pode ficar pequeno e amplificar os efeitos.

## 8. Resposta transitória

Para uma entrada constante e um sistema estável:

$$y(t)=y_{\mathrm{est}}+y_{\mathrm{tr}}(t),\qquad y_{\mathrm{tr}}(t)\to0.$$

O transitório descreve o caminho até o regime permanente. O Tema 1 usa:

$$G(s)=\frac{K_g}{\tau s+1},\qquad G_c(s)=K_c.$$

### Malha aberta

Sem perturbação, para degrau de amplitude $A$:

$$\frac YR=\frac{K_cK_g}{\tau s+1},\qquad y(t)=AK_cK_g(1-e^{-t/\tau}).$$

Escolhendo $K_c=1/K_g$:

$$\boxed{y(t)=A(1-e^{-t/\tau})}.$$

O controlador proporcional ajusta a amplitude, mas **não altera a constante de tempo $\tau$ da malha aberta**. Outra estrutura de controlador pode alterar a dinâmica.

### Malha fechada

Sem perturbação nem ruído:

$$\frac YR=\frac{K_cK_g}{\tau s+1+K_cK_g}.$$

$$\boxed{\tau_{\mathrm{mf}}=\frac{\tau}{1+K_cK_g}}.$$

$$\boxed{y(t)=A\frac{K_cK_g}{1+K_cK_g}\left(1-e^{-t/\tau_{\mathrm{mf}}}\right)}.$$

Para ganhos positivos, aumentar $K_c$ reduz a constante de tempo desse modelo e aproxima o valor final da referência, exigindo maior esforço de controle.

![[03_Recursos/Controle 2/imagens/tema_1/slide_48.png]]

*Slide 48. O gráfico ilustra uma aceleração idealizada da dinâmica.*

> **Correção de leitura do slide:** uma resposta 100 vezes mais rápida corresponde a uma constante de tempo 100 vezes **menor**, não maior. A aceleração realizável depende do atuador, da potência disponível, de atrasos e da dinâmica real; não existe um limite universal de aceleração aplicável a todas as plantas.

Para primeira ordem, a saída atinge 63,2% de seu valor final em uma constante de tempo, e o tempo de acomodação de 2% é aproximadamente $4\tau_{\mathrm{ef}}$. Acomodação é medida em torno do valor final, que pode diferir da referência.

## 9. Resposta estacionária e erro permanente

$$\boxed{e_{\mathrm{est}}=\lim_{t\to\infty}e(t)=\lim_{s\to0}sE(s)}.$$

O teorema do valor final exige suas condições de validade; para o caso racional usual, os polos de $sE(s)$ devem estar no semiplano esquerdo.

### Referência em degrau, sem perturbação nem ruído

Para $R(s)=A/s$:

| Sistema | Erro estacionário |
|---|---|
| Malha aberta | $e_{\mathrm{est}}=A[1-L(0)]$ |
| Malha fechada | $e_{\mathrm{est}}=A/[1+L(0)]$ |

Na aberta, $L(0)=1$ zera o erro nominal, mas variações da planta podem desfazer o ajuste. Na fechada, ganho estático elevado reduz o erro com menor sensibilidade às variações.

**Ganho proporcional finito não zera o erro no exemplo de primeira ordem:** $L(0)=9$ deixa $0{,}1A$; $L(0)=99$ deixa $0{,}01A$. A igualdade com $A$ apresentada no slide 46 deve ser interpretada como aproximação para ganho elevado.

### Perturbação em degrau

Para $T_p(s)=D/s$, considerando somente sua contribuição:

$$\boxed{e_{\mathrm{est,pert}}^{\mathrm{ma}}=-DG(0)}.$$

$$\boxed{e_{\mathrm{est,pert}}^{\mathrm{mf}}=-\frac{DG(0)}{1+L(0)}}.$$

O sinal negativo significa que a perturbação positiva aumenta a saída, para ganho positivo, diminuindo $e=r-y$.

Com referência e perturbação constantes simultâneas, ganhos estáticos finitos e sem ruído:

$$e_{\mathrm{est}}^{\mathrm{mf}}=\frac{A-DG(0)}{1+L(0)}.$$

Uma ação integral pode tornar $|L(s)|\to\infty$ quando $s\to0$, zerando o erro ao degrau de referência se a malha permanecer estável. Para rejeitar a perturbação constante na entrada da planta, também precisamos de:

$$\lim_{s\to0}\frac{G(s)}{1+L(s)}=0.$$

## 10. Exemplo comparativo

Considere $G(s)=1/(2s+1)$, degrau de referência unitário, $K_c=1$ na malha aberta e $K_c=9$ na fechada.

| Resultado | Aberta | Fechada |
|---|---:|---:|
| Valor final para referência unitária | 1 | 0,9 |
| Erro estacionário | 0 nominal | 0,1 |
| Constante de tempo | 2 s | 0,2 s |
| Desvio final por perturbação de amplitude 0,2 | 0,2 | 0,02 |

![[03_Recursos/Controle 2/imagens/tema_1/comparacao_malhas.png]]

*À esquerda: a aberta calibrada chega à referência nominal; a fechada é mais rápida, mas o controlador escolhido deixa erro de 10%. À direita: somente a contribuição da perturbação aplicada em 2 s, cujo efeito final é dez vezes menor na fechada.*

## 11. Fórmulas essenciais para revisão

$$L=G_cG,\qquad E=R-Y.$$

$$E_{\mathrm{ma}}=(1-L)R-GT_p.$$

$$E_{\mathrm{mf}}=\frac R{1+L}-\frac{GT_p}{1+L}+\frac{LN}{1+L}.$$

$$S_G^{T_{\mathrm{ma}}}=1,\qquad S_G^{T_{\mathrm{mf}}}=\frac1{1+L}.$$

**Ideia para guardar:** malha aberta depende de calibração; malha fechada usa a medição para corrigir desvios. O projeto deve conciliar rastreamento, robustez, ruído, rapidez, esforço de controle e estabilidade.
