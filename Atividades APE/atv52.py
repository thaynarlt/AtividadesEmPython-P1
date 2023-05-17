#Escreva um programa que leia um vetor contendo N elementos inteiros (N será lido), calcule e exiba:
#• A quantidade de elementos pares;
#• A quantidade de elementos ímpares;
#• A soma de todos os elementos;
#• A média dos elementos do vetor.

n = int(input("Digite o limite de números inteiros:"))
vetor = [None]*n

for index in range(n):
    vetor[index]= int(input("Digite um número:"))
    if vetor[index]%2 == 0:
        par = vetor[index]
        print(f'O número {par} é um número par')
    else:
        impar = vetor[index]
        print(f'O número {impar} é um número ímpar')


soma = sum(vetor)
print(f"A soma de todos os elementos é: {soma}")
lenght = len(vetor)
media = soma/lenght
print(f"A média é: {media}")