h1 , m1 = map(int, input("Insira hora e minuto da chegada: ").split())
h2 , m2 = map(int, input("Insira a hora e minuto da saída: ").split())

# converter para minutos 
tempo_chegada = h1 * 60 + m1
tempo_saida = h2 * 60 + m2

# saída no dia seguinte
if tempo_saida < tempo_chegada:
    tempo_saida += 24 * 60

# tempo total em minutos 
duracao_minutos = tempo_saida - tempo_chegada

# arredonda para horas por excesso
horas = (duracao_minutos + 59) // 60

# calcula o preço
if horas <= 2:
    total = horas * 1 
elif horas <= 4:
    total = 2 * 1 + (horas - 2) * 1.40
else:
    total = 2 * 1 + 2 * 1.40 + (horas - 4) * 2 

print(f"\nO valor do estacionamento ficou R$ {total:.2f}")
