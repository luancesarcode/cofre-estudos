---
tipo: aula
data: 2026-09-02
cadeira: "[[Controle 2]]"
unidade: 1
tema: 4
tags: [aula, controle]
---

# Tema 4 — Desempenho de sistemas de ordens superiores

Resumo para estudo e transcrição no caderno, com fórmulas explicadas, exemplos e imagens dos slides.

**Fonte:** Fabrício Bradaschia, UFPE, *Tema 4 — Desempenho de Sistemas de Controle de Ordens Superiores*, slides 1 a 82. As imagens numeradas são reproduções do material original.

**Hipóteses:** modelos lineares e condições iniciais nulas para as transferências. Fórmulas de erro estacionário finito exigem estabilidade e validade do teorema do valor final. As regras de dominância e de redução de ordem são aproximações a verificar, não garantias universais.

## 1. O que muda em relação ao Tema 2?

O Tema 2 estudou principalmente modelos de primeira e segunda ordem sem zeros. Sistemas reais podem apresentar polos e zeros adicionais, alterando sobressinal, rapidez e erro.

O Tema 4 responde a quatro perguntas:

1. O que muda ao adicionar um polo ou um zero?
2. Quando é possível desprezar dinâmicas e usar um modelo de ordem menor?
3. Como o tipo do sistema determina o erro para degrau, rampa e parábola?
4. Como comparar respostas usando índices integrais de desempenho?

## 2. Distinção essencial: cascata e ramo direto

**Em cascata com uma transferência já definida:** multiplicamos a transferência total por um novo fator. Os polos que já existiam permanecem, salvo cancelamentos; um novo polo acrescenta um modo e um zero muda os resíduos.

**No ramo direto, dentro da realimentação:** o novo fator entra também na equação característica. Ao fechar a malha, os polos podem mudar de posição.

Para sensor unitário, se $F(s)$ é o ramo direto:

$$\boxed{T(s)=\frac{F(s)}{1+F(s)}}.$$

**Não podemos usar o mesmo raciocínio para as duas situações.** Um zero em cascata não muda os polos existentes; um zero no ramo direto pode deslocar os polos da malha fechada.

## 3. Polo adicional em cascata

Partimos de uma segunda ordem de ganho unitário:

$$T_2(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}.$$

Acrescentamos o polo $-\alpha_r$, preservando o ganho estático:

$$\boxed{T_3(s)=T_2(s)\frac{\alpha_r}{s+\alpha_r}}.$$

Para um degrau, a resposta assume a forma:

$$y(t)=A+e^{-\zeta\omega_nt}[B\cos(\omega_dt)+C\sin(\omega_dt)]+De^{-\alpha_rt}.$$

O último termo é o modo associado ao polo adicional.

![[03_Recursos/Controle 2/imagens/tema_4/slide_06.png]]

*Slide 6. Um polo adicional próximo dos polos originais produz um transitório relevante. Muito à esquerda, sua contribuição desaparece mais cedo.*

### Quando o polo pode ser desprezado?

Defina $\alpha=\zeta\omega_n$, a taxa de decaimento do par complexo. A regra prática do material compara:

$$\boxed{\frac{\alpha_r}{\alpha}\geq5\quad\text{ou, com maior separação,}\quad\frac{\alpha_r}{\alpha}\geq10}.$$

A lógica de cinco constantes de tempo é:

$$\frac5{\alpha_r}\leq\frac1\alpha\quad\Rightarrow\quad\frac{\alpha_r}{\alpha}\geq5.$$

**Exemplo:** se o par complexo tem parte real $-2$ e o terceiro polo é $-20$, a razão é $20/2=10$. O polo real é candidato a não dominante.

Além da velocidade, precisamos avaliar o resíduo. Neste modelo específico:

$$D=-\frac{\omega_n^2}{\alpha_r^2+\omega_n^2-2\alpha_r\zeta\omega_n}.$$

Mantendo $\zeta$ e $\omega_n$ fixos, quando $\alpha_r\to\infty$, $D\to0$. A distância dos polos, isoladamente, não substitui a comparação das respostas.

![[03_Recursos/Controle 2/imagens/tema_4/slide_11.png]]

*Slide 11. Quanto mais rápido o polo adicional, mais a resposta se aproxima da segunda ordem original. A interação dos modos pode produzir mínimos locais no tempo de acomodação.*

## 4. Polo adicional no ramo direto

O material usa o ramo direto:

$$F(s)=\frac{\omega_n^2}{s(s+2\zeta\omega_n)(1+T_ps)}.$$

Aqui, $T_p$ é a constante de tempo do polo adicional, não tempo de pico nem perturbação.

Fechando a malha:

$$T(s)=\frac{\omega_n^2}{s(s+2\zeta\omega_n)(1+T_ps)+\omega_n^2}.$$

Expandindo:

$$\boxed{T(s)=\frac{\omega_n^2}{T_ps^3+(1+2\zeta\omega_nT_p)s^2+2\zeta\omega_ns+\omega_n^2}}.$$

Agora todos os polos da malha fechada dependem de $T_p$.

![[03_Recursos/Controle 2/imagens/tema_4/slide_14.png]]

*Slide 14. No exemplo de $\zeta=1$ e $\omega_n=1$, aumentar $T_p$ pode introduzir oscilações e elevar o sobressinal. Não é o mesmo efeito de adicionar um polo à transferência já fechada.*

A inclusão de polos no ramo direto pode prejudicar a estabilidade. As tendências de tempo de subida e acomodação dependem dos parâmetros; não devem ser tratadas como regras sempre monotônicas.

## 5. Zero à esquerda em cascata

Adicionamos um zero em $s=-a$, com $a>0$, preservando o ganho estático:

$$\boxed{T_z(s)=T_2(s)\frac{s+a}{a}=T_2(s)\left(1+\frac sa\right)}.$$

Os polos permanecem, mas os resíduos das parcelas transitórias mudam. Isso pode alterar bastante o sobressinal e os tempos.

![[03_Recursos/Controle 2/imagens/tema_4/slide_20.png]]

*Slide 20. As curvas correspondem a diferentes razões $a/(\zeta\omega_n)$. Um zero próximo da origem pode aumentar muito o pico.*

### Interpretação pela derivada

Se $y_1(t)$ é a resposta sem o zero, com $y_1(0^-)=0$:

$$Y(s)=Y_1(s)+\frac{s}{a}Y_1(s).$$

$$\boxed{y(t)=y_1(t)+\frac1a\frac{dy_1(t)}{dt}}.$$

O zero acrescenta uma parcela proporcional à inclinação da resposta original.

- $a$ grande: $1/a$ pequeno; a alteração tende a ser pequena.
- $a$ pequeno: a derivada tem peso maior; o sobressinal pode aumentar muito.

![[03_Recursos/Controle 2/imagens/tema_4/slide_23.png]]

*Slide 23. Durante a subida, a derivada positiva acrescenta amplitude. Depois, a contribuição pode mudar de sinal.*

A razão $a/(\zeta\omega_n)$ de 5 ou 10 é uma referência prática do material para avaliar se o zero está distante. A aproximação precisa ser conferida na faixa de frequências e no transitório de interesse.

## 6. Zero à direita: resposta inversa

Um zero em $s=+a$, com ganho estático preservado, corresponde ao fator:

$$\frac{a-s}{a}=1-\frac sa.$$

Portanto:

$$\boxed{y(t)=y_1(t)-\frac1a\frac{dy_1(t)}{dt}}.$$

A derivada é subtraída. No modelo-padrão de segunda ordem, a saída inicialmente se move na direção contrária à referência positiva.

![[03_Recursos/Controle 2/imagens/tema_4/slide_26.png]]

*Slide 26. A saída primeiro fica negativa e só depois sobe para o valor final positivo. Essa resposta inversa é característica importante de modelos com zero no semiplano direito.*

### Por que a saída começa descendo?

Para o modelo-base sem zero, com degrau unitário e ganho unitário:

$$y_1(0^+)=0,\quad\dot y_1(0^+)=0,\quad\ddot y_1(0^+)=\omega_n^2.$$

Então:

$$y(0^+)=0,\qquad\boxed{\dot y(0^+)=-\frac{\omega_n^2}{a}<0}.$$

Ou seja, o efeito é uma **inclinação inicial negativa**, não necessariamente um salto inicial negativo. Essa distinção esclarece a discussão do valor inicial no slide 24.

O zero à direita não torna, por si só, uma transferência com polos estáveis instável. Entretanto, limita o desempenho possível e não deve ser cancelado por inversão com um polo instável do controlador.

## 7. Zero no ramo direto

O material considera:

$$F(s)=\frac{\omega_n^2(1+T_zs)}{s(s+2\zeta\omega_n)}.$$

Ao fechar a malha:

$$\boxed{T(s)=\frac{\omega_n^2(1+T_zs)}{s^2+(2\zeta\omega_n+\omega_n^2T_z)s+\omega_n^2}}.$$

O zero aparece no numerador e também modifica o coeficiente de $s$ no denominador. Para $T_z>0$, o zero está à esquerda, em $-1/T_z$.

O amortecimento associado ao denominador passa a ser:

$$\zeta_{\mathrm{den}}=\zeta+\frac{\omega_nT_z}{2}.$$

**Não use diretamente a fórmula de sobressinal da segunda ordem sem zeros:** o numerador também foi alterado.

![[03_Recursos/Controle 2/imagens/tema_4/slide_30.png]]

*Slide 30. No exemplo do material, o zero no ramo direto reduz as oscilações em várias das configurações mostradas, diferentemente do zero em cascata com polos fixos.*

## 8. Polos dominantes e redução de ordem

Para polos simples, podemos escrever a resposta ao degrau como:

$$Y(s)=\frac A s+\sum_i\frac{r_i}{s-p_i},\qquad y(t)=A+\sum_i r_ie^{p_it}.$$

Os polos $p_i$ determinam as velocidades e os formatos dos modos; os resíduos $r_i$ determinam suas amplitudes. Tanto polos quanto zeros e ganho influenciam os resíduos.

**Polos dominantes** são os que contribuem de modo relevante na escala de tempo de interesse. Normalmente estão mais próximos do eixo imaginário e não têm resíduos desprezíveis.

![[03_Recursos/Controle 2/imagens/tema_4/slide_39.png]]

*Slide 39. A distância dos polos não dominantes ao eixo imaginário é frequentemente escolhida 5 a 10 vezes maior. O $L$ da figura representa uma distância geométrica, não o ganho de malha $L(s)$ dos outros temas.*

Um polo lento quase cancelado por um zero pode ter contribuição pequena. Um polo rápido com resíduo grande pode afetar muito o início da resposta. Portanto, não basta selecionar o polo mais próximo da origem.

### Como desprezar um fator sem alterar o ganho estático

Substitua $s$ por zero **somente no fator desprezado**.

Exemplo complementar:

$$T(s)=\frac{320}{(s+20)(s^2+4s+16)}.$$

O par complexo tem parte real $-2$ e o polo real é $-20$, dez vezes mais distante. Aproximando $(s+20)\approx20$:

$$\boxed{T_{\mathrm{aprox}}(s)=\frac{16}{s^2+4s+16}}.$$

Ambos os modelos têm ganho estático 1. Simplesmente apagar $(s+20)$ e manter 320 no numerador produziria ganho estático errado.

Para um zero distante, $(s+a)\approx a$. Para um par polo-zero próximo e estável, pode ser possível aproximar a razão por um ganho, verificando a resposta resultante.

## 9. Erro estacionário com realimentação unitária

Defina o ramo direto:

$$F(s)=G_c(s)G(s).$$

Sem perturbação nem ruído e com $H=1$:

$$T(s)=\frac F{1+F},\qquad\boxed{E(s)=R(s)-Y(s)=\frac{R(s)}{1+F(s)}}.$$

![[03_Recursos/Controle 2/imagens/tema_4/slide_44.png]]

*Slide 44. Nesta estrutura, o sinal de entrada do controlador coincide com o erro de rastreamento.*

O erro estacionário finito é calculado por:

$$\boxed{e_{\mathrm{ss}}=\lim_{s\to0}sE(s)}.$$

O limite só fornece um valor final finito quando as condições do teorema são satisfeitas; para funções racionais usuais, todos os polos de $sE(s)$ devem estar no semiplano esquerdo. Se a análise indicar erro crescente, não há um regime de erro constante: a tabela pode registrar isso como erro infinito.

## 10. Ordem e tipo não são a mesma coisa

**Ordem:** grau do denominador da função de transferência reduzida.

**Tipo, para a tabela de erro com realimentação unitária:** número de integradores efetivos, isto é, polos na origem do ramo direto $F(s)$.

| Ramo direto | Ordem | Tipo |
|---|---:|---:|
| $10/[(s+1)(s+2)]$ | 2 | 0 |
| $10/[s(s+2)]$ | 2 | 1 |
| $10/[s^2(s+2)]$ | 3 | 2 |

Esses exemplos ilustram a contagem; a estabilidade fechada deve ser verificada separadamente. Um tipo elevado não garante que a malha seja estável.

> O tema também chama degrau de entrada tipo 1, rampa de entrada tipo 2 e parábola de entrada tipo 3, devido aos polos de $R(s)$. Não confunda o tipo da **entrada** com o tipo do **sistema**.

## 11. Constantes de erro e entradas de teste

Usaremos $A$ para a amplitude ou coeficiente da entrada, evitando confundir a constante com $R(s)$.

### 11.1 Degrau

$$R(s)=\frac A s.$$

$$e_{\mathrm{ss}}=\lim_{s\to0}\frac A{1+F(s)}.$$

Definimos a constante de erro do degrau:

$$\boxed{K_1=\lim_{s\to0}F(s)},\qquad\boxed{e_{\mathrm{ss}}=\frac A{1+K_1}}.$$

![[03_Recursos/Controle 2/imagens/tema_4/slide_49.png]]

*Slide 49. Um sistema tipo 0 pode deixar um deslocamento final; um integrador efetivo permite zerar esse erro em uma malha estável.*

### 11.2 Rampa

$$r(t)=At,\qquad R(s)=\frac A{s^2}.$$

$$e_{\mathrm{ss}}=\lim_{s\to0}\frac A{s+sF(s)}.$$

$$\boxed{K_2=\lim_{s\to0}sF(s)},\qquad\boxed{e_{\mathrm{ss}}=\frac A{K_2}}.$$

Se $K_2=0$ nos casos usuais, o erro cresce sem limite; se $K_2$ é finito não nulo, o erro tende a uma constante; se $K_2\to\infty$, o erro tende a zero, desde que a dinâmica fechada permita a conclusão.

![[03_Recursos/Controle 2/imagens/tema_4/slide_52.png]]

*Slide 52. A saída e a referência continuam aumentando, mas a distância vertical entre elas pode se tornar constante.*

### 11.3 Parábola

Neste tema, a convenção é:

$$r(t)=\frac{At^2}{2},\qquad R(s)=\frac A{s^3}.$$

$$\boxed{K_3=\lim_{s\to0}s^2F(s)},\qquad\boxed{e_{\mathrm{ss}}=\frac A{K_3}}.$$

![[03_Recursos/Controle 2/imagens/tema_4/slide_55.png]]

*Slide 55. Correção de notação: para a parábola, a constante no denominador é $K_3$, embora a figura original esteja rotulada com $K_2$.*

### Tabela essencial

Para sistemas fechados estáveis, nas condições usuais da análise:

| Tipo do sistema | Degrau $A$ | Rampa $At$ | Parábola $At^2/2$ |
|---|---|---|---|
| 0 | $A/(1+K_1)$ | Erro ilimitado | Erro ilimitado |
| 1 | 0 | $A/K_2$ | Erro ilimitado |
| 2 | 0 | 0 | $A/K_3$ |
| 3 ou superior | 0 | 0 | 0 |

Outros livros usam $K_p,K_v,K_a$ para essas constantes. Neste resumo mantemos $K_1,K_2,K_3$, como nos slides, evitando confundir $K_p$ com o ganho proporcional do controlador.

### Regra geral e sua exceção

Para $R(s)=A/s^j$:

$$K_j=\lim_{s\to0}s^{j-1}F(s).$$

Para $j\geq2$, a regra usual é $e_{\mathrm{ss}}=A/K_j$. **Para $j=1$, deve-se manter $e_{\mathrm{ss}}=A/(1+K_1)$.** A generalização do slide 56 não pode eliminar o termo 1 no caso do degrau.

## 12. Exemplo resolvido: controlador PI

O exemplo do tema utiliza:

$$G(s)=\frac K{\tau s+1},\qquad G_c(s)=K_p+\frac{K_i}{s}=\frac{K_ps+K_i}{s}.$$

$$F(s)=\frac{K(K_ps+K_i)}{s(\tau s+1)}.$$

### Sem ação integral: $K_i=0$

Após simplificar o fator $s$, o ramo direto é tipo 0:

$$F(s)=\frac{KK_p}{\tau s+1}.$$

$$K_1=KK_p,\qquad K_2=0.$$

Para entradas unitárias:

$$\boxed{e_{\mathrm{degrau}}=\frac1{1+KK_p}},\qquad\boxed{e_{\mathrm{rampa}}\text{ cresce sem limite}}.$$

### Com ação integral: $K_i\neq0$

Para ganhos positivos e malha estável, o ramo direto é tipo 1:

$$K_1\to\infty,\qquad K_2=\lim_{s\to0}\frac{K(K_ps+K_i)}{\tau s+1}=KK_i.$$

$$\boxed{e_{\mathrm{degrau}}=0},\qquad\boxed{e_{\mathrm{rampa}}=\frac1{KK_i}}.$$

No slide 62, o último denominador deve ser lido como $K_iK$; isso decorre do valor de $K_2$ obtido no slide 61.

**Exemplo complementar:** $K=2$, $\tau=1$, $K_p=3$ e $K_i=4$ produzem denominador fechado $s^2+7s+8$, estável. Logo, o erro ao degrau é zero e o erro à rampa unitária é $1/(2\cdot4)=0{,}125$.

![[03_Recursos/Controle 2/imagens/tema_4/slide_63.png]]

*Slide 63. A referência triangular é composta de trechos de rampa. Mudanças de inclinação geram novos transitórios; trechos suficientemente longos se aproximam do comportamento de erro constante.*

Adicionar integradores pode melhorar o rastreamento, mas também dificulta o projeto de estabilidade. Não basta aumentar o tipo sem verificar o denominador fechado.

## 13. Realimentação não unitária

Quando $H\neq1$, diferencie:

$$E_a=R-HY\quad\text{(sinal no somador)},\qquad E=R-Y\quad\text{(erro real de rastreamento)}.$$

Essa comparação de $R$ com $Y$ pressupõe que ambos estejam expressos em grandezas compatíveis. Conversões de unidade e escalas devem ser explicitadas no diagrama.

### 13.1 Sensor constante e referência escalonada

Se o somador recebe $k_sR-k_sY$, podemos fatorar $k_s(R-Y)$ e representar o sistema com realimentação unitária e ramo direto $k_sG_cG$.

![[03_Recursos/Controle 2/imagens/tema_4/slide_65.png]]

*Slide 65. A transformação exige ganhos iguais nos dois caminhos. Não basta o sensor ser constante para simplesmente apagá-lo.*

### 13.2 Sensor dinâmico: dedução de $Z(s)$

Defina $F=G_cG$. A transferência fechada é:

$$T=\frac F{1+FH}.$$

O erro real é:

$$E=(1-T)R=\frac{1+F(H-1)}{1+FH}R.$$

Queremos escrever $T=Z/(1+Z)$. Como $Z=T/(1-T)$:

$$\boxed{Z(s)=\frac{F(s)}{1+F(s)[H(s)-1]}}.$$

Então:

$$\boxed{E(s)=\frac{R(s)}{1+Z(s)}}.$$

![[03_Recursos/Controle 2/imagens/tema_4/slide_68.png]]

*Slide 68. O bloco equivalente $Z$ permite analisar o erro real com as expressões unitárias. Isso é uma equivalência algébrica; a estabilidade do sistema físico original ainda precisa ser verificada.*

As constantes passam a ser:

$$K_1=\lim Z(s),\qquad K_2=\lim sZ(s),\qquad K_3=\lim s^2Z(s),\qquad s\to0.$$

Não substitua apenas $F$ por $FH$ na tabela se o objetivo for calcular $R-Y$: isso analisaria o erro do somador em vez do erro real.

## 14. Exemplo: PI com sensor de primeira ordem

O material usa $H(s)=1/(T_ss+1)$. Para não confundir a constante do sensor com tempo de acomodação, vamos chamá-la de $\tau_h$:

$$G_c(s)=\frac{K_ps+K_i}{s},\quad G(s)=\frac K{\tau s+1},\quad H(s)=\frac1{\tau_hs+1}.$$

Como:

$$H-1=-\frac{\tau_hs}{\tau_hs+1},$$

substituímos em $Z=F/[1+F(H-1)]$:

$$\boxed{Z(s)=\frac{K(K_ps+K_i)(\tau_hs+1)}{s[(\tau s+1)(\tau_hs+1)-K\tau_h(K_ps+K_i)]}}.$$

Para ação integral não nula e malha estável, o erro ao degrau unitário é zero. Para a rampa unitária:

$$K_2=\frac{KK_i}{1-KK_i\tau_h}.$$

$$\boxed{e_{\mathrm{rampa}}=\frac{1-KK_i\tau_h}{KK_i}=\frac1{KK_i}-\tau_h}.$$

**Interpretação:** a dinâmica do sensor altera o erro real de rastreamento. Um erro negativo significa que a saída real está adiantada em relação à referência em regime de rampa. Não significa automaticamente instabilidade. Se $1-KK_i\tau_h=0$, use o limite: o erro de rampa é zero, desde que a malha original seja estável.

A equação característica física deste exemplo é:

$$s(\tau s+1)(\tau_hs+1)+K(K_ps+K_i)=0.$$

É ela que deve fundamentar a avaliação da estabilidade, e não somente o tipo de $Z$.

## 15. Índices integrais de desempenho

Os tempos e o sobressinal descrevem pontos específicos da resposta. Os índices integrais avaliam o erro ao longo de um intervalo.

Usaremos $T_f$ para o horizonte de integração, evitando confusão com uma função de transferência $T(s)$.

| Índice | Fórmula | O que valoriza |
|---|---|---|
| ISE | $\displaystyle\int_0^{T_f}e^2(t)\,dt$ | Penaliza fortemente erros de grande amplitude |
| IAE | $\displaystyle\int_0^{T_f}\vert e(t)\vert \,dt$ | Acumula a magnitude do erro |
| ITAE | $\displaystyle\int_0^{T_f}t\vert e(t)\vert \,dt$ | Dá mais peso aos erros que persistem tarde |
| ITSE | $\displaystyle\int_0^{T_f}te^2(t)\,dt$ | Penaliza erros grandes, principalmente tardios |

Todos são não negativos. Dentro da mesma definição, entrada, unidade e horizonte, valores menores indicam melhor resultado segundo aquele critério.

**Por que usar quadrado ou módulo?** Para evitar que erro positivo e negativo se cancelem na integral.

![[03_Recursos/Controle 2/imagens/tema_4/slide_74.png]]

*Slide 74. A partir de referência e saída, calcula-se $e$, depois $e^2$ e sua integral acumulada.*

### Exemplo complementar simples

Se $e(t)=e^{-t}$ e integramos até infinito:

$$ISE=\int_0^\infty e^{-2t}dt=\frac12,\qquad IAE=\int_0^\infty e^{-t}dt=1.$$

$$ITAE=\int_0^\infty te^{-t}dt=1,\qquad ITSE=\int_0^\infty te^{-2t}dt=\frac14.$$

Não conclua que ITSE é melhor porque seu número é menor: são critérios e unidades diferentes. Compare controladores usando o mesmo índice.

Para comparação justa, use uma entrada e um horizonte comuns, suficientemente longos. Se houver erro constante não nulo e o horizonte for infinito, esses índices podem divergir. A soma de índices diferentes exige escalas e pesos coerentes.

## 16. Escolha ótima e coeficientes tabelados

Um sistema é ótimo **em relação a um índice e a um conjunto de restrições**. Não existe um único controlador melhor em todos os critérios.

![[03_Recursos/Controle 2/imagens/tema_4/slide_77.png]]

*Slide 77. Índices diferentes atingem seus mínimos em valores diferentes de $\zeta$. O gráfico mostra, por exemplo, mínimos de IAE perto de 0,66 e de ITAE perto de 0,75 para o ensaio apresentado. Esses valores não são universais para outras plantas e entradas.*

### Modelo ótimo para degrau

O material apresenta famílias na forma:

$$\boxed{M(s)=\frac{\omega_n^n}{s^n+b_{n-1}\omega_ns^{n-1}+\cdots+b_1\omega_n^{n-1}s+\omega_n^n}}.$$

O numerador igual ao termo constante do denominador garante $M(0)=1$.

![[03_Recursos/Controle 2/imagens/tema_4/slide_78.png]]

*Slide 78. Os coeficientes $b_i$ definem a forma normalizada. O parâmetro $\omega_n$ escala o tempo.*

Exemplo da tabela, para segunda ordem:

$$M(s)=\frac{\omega_n^2}{s^2+1{,}4\omega_ns+\omega_n^2}.$$

Comparando com a forma-padrão, $2\zeta=1{,}4$, portanto $\zeta=0{,}7$. É um modelo tabelado de projeto, não uma garantia de ótimo exato para qualquer implementação, horizonte ou restrição.

### Modelo para rampa

O numerador inclui também o termo linear:

$$\boxed{M(s)=\frac{b_1\omega_n^{n-1}s+\omega_n^n}{s^n+b_{n-1}\omega_ns^{n-1}+\cdots+b_1\omega_n^{n-1}s+\omega_n^n}}.$$

![[03_Recursos/Controle 2/imagens/tema_4/slide_82.png]]

*Slide 82. O numerador e os dois termos de menor grau do denominador coincidem, favorecendo erro nulo à rampa em um modelo estável.*

Isso pode ser visto porque $1-M(s)$ tem um fator $s^2$ no numerador. Para rampa unitária, $E=(1-M)/s^2$; com estabilidade, $\lim_{s\to0}sE(s)=0$.

## 17. Roteiro para exercícios

1. Identifique se o polo ou zero foi inserido em cascata ou dentro da malha.
2. Escreva a nova função de transferência antes de prever o efeito.
3. Identifique polos, zeros, resíduos relevantes e ganho estático.
4. Para reduzir a ordem, compare escalas de tempo e preserve o ganho estático.
5. Para erro estacionário, verifique estabilidade e o tipo de realimentação.
6. Com $H=1$, calcule constantes a partir de $F=G_cG$; com $H\neq1$, analise o erro real diretamente ou use $Z$.
7. Escolha a constante correspondente à entrada: degrau, rampa ou parábola.
8. Para comparar respostas completas, escolha um índice e um horizonte comuns.

**Fórmulas para guardar:**

$$E=\frac R{1+F}\quad(H=1),\qquad Z=\frac F{1+F(H-1)}\quad(H\neq1).$$

$$K_1=\lim F,\quad K_2=\lim sF,\quad K_3=\lim s^2F\quad(s\to0).$$

$$e_{\mathrm{degrau}}=\frac A{1+K_1},\quad e_{\mathrm{rampa}}=\frac A{K_2},\quad e_{\mathrm{parábola}}=\frac A{K_3}.$$
