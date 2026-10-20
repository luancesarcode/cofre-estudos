# 8. Região de projeto: estabilidade ∩ erro

**Exercício recorrente:** desenhar um plano ganho × posição do zero, indicando onde as duas exigências são satisfeitas.

## 1. Modelo reutilizável das fresas

Escreva o denominador da planta como:

$$D=s^4+a s^3+b s^2+c s,\qquad G=A/D,\qquad G_c=K(s+z).$$

Então:

$$\Delta=s^4+a s^3+b s^2+(c+AK)s+AKz.$$

Defina $q=c+AK$. Routh dá:

$$ab>q,\qquad (ab-q)q>a^2AKz,\qquad AKz>0.$$

Com $A,K,z>0$:

$$K<\frac{ab-c}{A},\qquad
z<f(K)=\frac{(ab-c-AK)(c+AK)}{a^2AK}.$$

A restrição de rampa, porque $K_v=AKz/c$, é:

$$z\ge g(K)=\frac{c}{A e_{\max}K}.$$

A região existe apenas onde $g(K)<f(K)$.

## 2. Como desenhar para ganhar os pontos

1. Declare: “abscissa $K$, ordenada $z$”.
2. Trace $z=g(K)$ com linha contínua: igualdade de erro é permitida.
3. Trace $z=f(K)$ com linha tracejada: igualdade de estabilidade é excluída.
4. Encontre as interseções resolvendo $f(K)=g(K)$.
5. Hachure **acima de $g$ e abaixo de $f$**.
6. Escolha um ponto dentro da região e confira as duas condições.

Não basta escrever as inequações se a questão pede o desenho.

## 3. Tabela das quatro provas

| Prova | Fronteira de erro $g(K)$ | Fronteira estável $f(K)$ | Ganhos com alguma solução |
|---|---|---|---|
| 2024.1 | $2/K$ | $(-K^2+9K+10)/(6K)$ | $0,227998<K<8,772002$ |
| 2024.2 | $4/K$ | $(-9K^2+192K+420)/(96K)$ | $0<K<21,519214$ |
| 2025.1 | $10/K$ | $(-25K^2+885K+2880)/(405K)$ | $1,375479<K<34,024521$ |
| 2025.2 | $8/K$ | $(-K^2+33,8K+151,2)/(12,1K)$ | $0<K<35,339360$ |

Os intervalos da última coluna são abertos. Para cada ganho admissível, $z$ pertence a $[g(K),f(K))$.

![Exemplo de região](../figuras/2025_1_regiao.png)

## 4. Exemplo desenvolvido: 2025.1 Q2

$$\Delta=s^4+9s^3+23s^2+(15+5K)s+5Kz.$$

$$B=\frac{9\cdot23-(15+5K)}9=\frac{192-5K}9.$$

Então $K<38,4$ e:

$$C>0\iff(192-5K)(15+5K)-405Kz>0.$$

Expandindo:

$$-25K^2+885K+2880-405Kz>0.$$

Erro: $K_v=Kz/3$, então $e_{ss}=3/(Kz)\le0,3\Rightarrow Kz\ge10$.

As fronteiras se encontram quando:

$$25K^2-885K+1170=0.$$

O intervalo resultante é o da tabela. O ponto $K=10,z=1$ atende ao erro na igualdade e está estritamente abaixo da fronteira de estabilidade.

## 5. Por que esse assunto deve ser estudado em bloco

As quatro provas mudam os polos, o numerador e o erro permitido, mas o raciocínio é o mesmo. Resolva uma com consulta, uma sem consulta e só então use as outras como treino cronometrado. Memorize o procedimento, não quatro fórmulas independentes.
