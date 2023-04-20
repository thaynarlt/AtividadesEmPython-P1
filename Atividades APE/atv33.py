#Faça um programa que leia 20 números inteiros, determine e mostre o maior deles.
maior = 0
for i in range(1,21):
    num = int(input('\033[34m'+"Digite um número: "+'\033[0m'))

    if num >= maior:
        maior = num
    else:
        maior = maior
print('\033[1;32m'+f"O maior número é: {maior}"+'\033[0m')