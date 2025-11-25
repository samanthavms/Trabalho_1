#1. input()
#O que faz: Lê a linha inteira que você digitou como um texto único (string).
#Neste momento, o computador tem: "12 50" (tudo entre aspas, inclusive o espaço).

#2. .split()
#O que faz: Pega esse texto e "corta" onde tem espaços em branco.
#Neste momento, o computador tem uma lista: ['12', '50'].
#Nota: Ainda são textos (strings), por isso estão entre aspas. Se você tentar somar aqui, daria erro ou concatenaria.

#3. map(int, ...)
#O que faz: A função map funciona como uma máquina de transformação. Ela pega uma função (no caso, int) e aplica a cada item da lista que veio do split().
#Ela pega o '12' e transforma em 12 (número inteiro).
#Ela pega o '50' e transforma em 50 (número inteiro).
#Neste momento, o computador tem (basicamente): 12 e 50 prontos para uso matemático.

#4. h1, m1 = ...
#O que faz: Isso se chama Desempacotamento (Unpacking).
#Como o map gerou dois valores, o Python pega o primeiro e joga dentro da variável h1 e o segundo dentro da variável m1.
#Resultado final: h1 vale 12 e m1 vale 50.

h1 , m1 = map( int , input("Insira hora e minuto da chegada: ").split())
h2 , m2 = map( int , input("insira a hora e minuto da saída: ").split())

 #converter para minutos 
tempo_chegada = h1 * 60 + m1
tempo_saida = h2 * 60 + m2

#saída no dia seguinte
if tempo_saida < tempo_chegada:
    tempo_saida += 24 * 60

#tempo total em minutos 
minutos_totais= tempo_saida - tempo_chegada

#arredonda para horas por excesso
duração = (minutos_totais + 59) // 60
if duração <= 2 :
    total = duração * 1 
elif  duração <= 4 :
    total = 2 * 1  + (duração - 2) * 1.40
else:
    total = 2 * 1 + 2 * 1.40 + (duração - 4) * 2 
print(f"\n O valor do estacionamento ficou R${total:.2f}")