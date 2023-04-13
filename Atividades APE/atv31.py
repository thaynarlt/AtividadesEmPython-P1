#Faça um programa que leia um número N, inteiro, e some todos os números
#de 1 até N, mostrando o resultado.

n = int(input('\033[1;34m'+"Digite um número inteiro: "+'\033[0m'))
print('\033[32m'+"A soma de 1 até o número digitado é: "+'\033[0m')
soma = 0

for i in range(1, n+1):
    soma += i 
    print(f"A soma dos números de 1 até {n} é: "+'\033[1;32m'+f'{soma}'+'\033[0m')