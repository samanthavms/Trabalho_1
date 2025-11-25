n = int(input("Quantidade de multiplos dos números: "))
i = int(input("Digite o primeiro número: "))
j = int(input("Digite o segundo número: "))

resultado = []
num = 0 
#len(resultado) retorna o numero inteiro de contagem da
# lista
while len(resultado) < n:
    if num % i == 0 or num % j == 0:
        resultado.append(num)
    num += 1 
print(f"Os multiplos dos numeros {i} e {j} são :", end=" ")
#for in vai percorrendo a lista e pegando um número 
for x in resultado:

    print( x, end=" ")
