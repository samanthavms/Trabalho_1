numero=int(input("Digite o número "))
if numero <= 0:
    print("NÚMERO INVÁLIDO")
    exit()
soma = 0
num_string = str(numero)
for algarismo_char in num_string:
    soma += int(algarismo_char)
print(f"O número é {numero} a soma do seus algoritmos é {soma}")