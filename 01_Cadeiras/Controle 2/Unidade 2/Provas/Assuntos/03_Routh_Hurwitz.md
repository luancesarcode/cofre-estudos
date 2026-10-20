# 3. Routh-Hurwitz: estabilidade e ganho crítico

**Objetivo:** achar intervalos de ganho e regiões de parâmetros sem calcular todas as raízes.

## 1. Como montar

Escreva $\Delta(s)$ em potências decrescentes. Inclua coeficiente zero quando faltar um termo.

Para $\Delta=s^4+a s^3+b s^2+c s+d$:

| Linha | Primeira coluna | Segunda | Terceira |
|---|---|---|---|
| $s^4$ | 1 | $b$ | $d$ |
| $s^3$ | $a$ | $c$ | 0 |
| $s^2$ | $B=(ab-c)/a$ | $d$ | 0 |
| $s^1$ | $C=(Bc-ad)/B$ | 0 | 0 |
| $s^0$ | $d$ | 0 | 0 |

Para estabilidade estrita, com coeficiente líder positivo:

$$a>0,\quad B>0,\quad C>0,\quad d>0.$$

Quando $a>0$ e $ab-c>0$ já estão garantidos:

$$\boxed{ab>c,\quad abc>c^2+a^2d,\quad d>0.}$$

Não multiplique uma inequação por uma expressão de sinal desconhecido sem separar os casos. A monitoria simplifica linhas usando fatores positivos; essa simplificação é legítima apenas nas condições declaradas.

## 2. O caso de terceira ordem, que aparece o tempo inteiro

Para $\Delta=s^3+a s^2+b s+c$:

| Linha | Coluna 1 | Coluna 2 |
|---|---|---|
| $s^3$ | 1 | $b$ |
| $s^2$ | $a$ | $c$ |
| $s^1$ | $(ab-c)/a$ | 0 |
| $s^0$ | $c$ | 0 |

Estável se $a>0$, $c>0$ e $ab>c$; essas condições também implicam $b>0$.

**Exemplo de 2026.1:** $\Delta=s^3+7s^2+11s+5+10K$.

$$7\cdot11>5+10K\Rightarrow K<7,2.$$

Para $K>0$, a faixa estável é $0<K<7,2$.

## 3. Como obter frequência e período no limite

No exemplo, para $K=7,2$, a linha $s^1$ zera. Use a linha **acima**:

$$A(s)=7s^2+77=0\Rightarrow s=\pm j\sqrt{11}.$$

$$\omega_{cr}=\sqrt{11}\ \mathrm{rad/s},\qquad
P_{cr}=\frac{2\pi}{\omega_{cr}}\approx1,89445\ \mathrm{s}.$$

O outro polo é $-7$, pois $\Delta=(s+7)(s^2+11)$.

**Não confunda:** $\omega$ é em rad/s; $f=\omega/(2\pi)$ é em Hz; $P=1/f$ é em segundos.

## 4. Casos especiais presentes na Monitoria 03

### Primeiro elemento zero, restante da linha não nulo

Substitua esse elemento por $\varepsilon>0$, continue a tabela e analise os sinais quando $\varepsilon\to0^+$. Não divida por zero.

### Linha inteira nula

Forme $A(s)$ a partir da linha acima. Substitua a linha nula pelos coeficientes de $A'(s)$ e continue. Resolva também $A(s)=0$.

Linha nula indica raízes simétricas; **não garante sozinha estabilidade marginal**. As raízes podem incluir pares reais simétricos ou polos imaginários repetidos. Verifique o restante do polinômio.

### Termo constante zero

Há polo na origem. Fatore a potência de $s$, aplique Routh ao restante e mantenha a informação sobre os polos retirados. Não classifique esse caso como assintoticamente estável.

### Trocas de sinal

O número de trocas na primeira coluna, após tratar os casos especiais, dá o número de raízes no semiplano direito.

## 5. Estabilidade relativa: deslocar o eixo

Para investigar a linha $\operatorname{Re}(s)=-\alpha$, faça:

$$q=s+\alpha,\qquad s=q-\alpha.$$

Monte Routh em $\Delta(q-\alpha)$. Polos no eixo imaginário de $q$ correspondem a polos de parte real $-\alpha$ no plano original.

Em 2023.2 Q3, $\alpha=2$:

$$\Delta(q-2)=q^3+2q^2+(K_p-5)q+(K_i-2K_p-6).$$

Linha $q^1$ nula:

$$2(K_p-5)-(K_i-2K_p-6)=0
\Rightarrow K_p=1+\frac{K_i}{4}.$$

Depois confirme que o polinômio auxiliar tem raízes imaginárias, não reais.

## 6. Checklist de resposta

- [ ] Escrevi $\Delta$, e não o denominador de malha aberta?
- [ ] Incluí termos ausentes com zero?
- [ ] Mostrei a tabela ou as expressões intermediárias?
- [ ] Cruzei todas as inequações?
- [ ] Excluí a fronteira de estabilidade estrita?
- [ ] Se pedi $\omega$, usei a linha acima da linha nula?

**Ordem de treino:** 2026.1 Q2b → 2023.2 Q1 → 2024.2 Q1c → 2023.2 Q3c.
