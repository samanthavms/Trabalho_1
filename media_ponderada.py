nota1= float(input("Insira a primeira nota "))
nota2= float(input("Insira a segunda nota "))
nota3= float (input("Insira a terceira nota "))

media= ((nota1*1)+(nota2*1)+(nota3*2)) / 4
if media >= 60 :
    print(f"O aluno foi aprovado com média de {media}")
else:
    print(f"O aluno foi reprovado com a média de {media}")