print("---"*20)
numero=int(input('Digite o número: '))
if numero < 0:
    print("Número Inválido")
else:
    import math
    base = 10
    resultado= math.log(numero, base)
print("---"*20)
print(f"O logaritmo do número {numero} é {resultado} ")