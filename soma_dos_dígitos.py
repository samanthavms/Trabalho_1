N = 9999
lista_digitos_igual_numero = []
for i in range(1000, 10000):

    alta_ordem = i // 100 #Alta ordem os números que representam milhar e centena 
    # A parte inteiro da divisão por 100 retorna as centenas e milhares 
    baixa_ordem = i % 100 #Baixa ordem os números representa a dezena e unidade 

    soma= alta_ordem + baixa_ordem
    numero= soma **2

    if numero == i: 
        lista_digitos_igual_numero.append(i) #Adiciona o elemento na lista vazia 
        
if lista_digitos_igual_numero:
    print(f"LISTA:{lista_digitos_igual_numero}")
else:
    print("Não foi encontado nenhum valor")