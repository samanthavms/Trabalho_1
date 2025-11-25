print('\n')
distancia = float(input("Digite a distância percorrida em KM: "))
print("\n")
litros_consumidos = float(input("Digite a quantidade de gasolina em litros: "))
consumo = distancia / litros_consumidos

if consumo < 8 : 
    print('---'*20)
    print(f"O CONSUMO FOI DE {consumo:.2f} Km/l. VENDA O CARRO!!")
    print('---'*20)

elif consumo >= 8 or consumo < 12:
    print('---'*20)
    print(f"O CONSUMO FOI DE {consumo:.2f} km/l. O CARRO É ECONÔMICO!!")
    print('---'*20)

elif consumo > 12: 
    print('---'*20)
    print(f"O CONSUMO FOI DE {consumo:.2f} km/l. O CARRO É SUPER ECONÔMICO!!!")
    print('---'*20)


