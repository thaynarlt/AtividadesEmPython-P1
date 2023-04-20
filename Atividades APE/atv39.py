#Faça um programa que leia vários números, calcule e exiba a média desses
#números. Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
#computado na média)

num = int(input("Digite o limite de números: "))
media = 0
cont = 0
soma = 0
if num == 999:
        print("Fim dos dados de entrada")
else:
    while cont < num:
        numero = int(input("Digite um número inteiro: "))
        soma += numero
        cont+= 1
        media = soma/num
    print("A média dos números é:", media)