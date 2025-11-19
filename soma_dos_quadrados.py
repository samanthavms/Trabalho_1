N=100
soma_quad=0
for i in range (1,N +1 ):
    quad = i * i
    soma_quad = soma_quad + quad
print("---" * 40)
print(f" A soma dos quadrados dos 100 primeiros números naturais é {soma_quad}")

soma = 0
for i in range (1,N+1):# O for vai de 0 até 99, por isso devo adicionar os intervalos 
    soma= soma + i 
    valor = soma ** 2 
print("---" * 40)
print(f"O quadrado da soma dos 100 primeiros números é {valor}")
print("---" * 40)
print(f"A diferença entre o quadrado da soma dos 100 primeiros números e a soma dos quadrados é {valor - soma_quad} ")
print("---" * 40)
