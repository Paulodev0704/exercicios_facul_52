#Desenvolver um programa em Python que solicite a digiteção da idade e o sexo de 10 pessoas, calcule e imprima
#Idade media das mulheres
#Idade media dos homens
#Idade media do grupo
#A maior idade do grupo
import os 
listageral = []
listamulheres = []
listahomens = []
contF = 0
contM = 0
contG = 0
for i in range(0,11):
    sexo = input("Digite o sexo [M]asculino ou [F]eminino: ")
    sexo = sexo.upper()
    print(sexo)
    if sexo == "M":
        idade = int(input("Digite a idade: "))
        listahomens.append(idade)
        contG = contG + 1
        contM = contM + 1
        os.system("cls")
    elif sexo == "F":
        idade = int(input("Digite a idade: "))
        listamulheres.append(idade)
        contG = contG + 1
        contF = contF + 1
        os.system("cls")   
    else:
        ("Digite apenas numeros inteiros.")
somaidF = sum(listamulheres)
somaidM = sum(listahomens)
media_homens = int(somaidM / contM)
media_mulheres = int(somaidF / contF)
listageral = listamulheres + listahomens
mediageral = int(sum(listageral)/contG)
maior_idade = max(listageral)

os.system("cls")


print(f"A media geral foi, {mediageral} e a media de mulheres foi {media_mulheres} e de homens foi {media_homens} e a pessoa com mais idade tem {maior_idade} anos ")
