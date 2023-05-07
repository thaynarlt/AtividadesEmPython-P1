#1. Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
#respectivos elementos de a multiplicados por K. Ex: A = [1,2,3], K = 5, B = [5,10,15].

tamanho = int(input("Qual a quantidade de números: "))
a = [None]*tamanho

for index in range(tamanho):
    a[index]= int(input("Número:"))

k = int(input("Digite o multiplicador: "))

b = [None]*(tamanho)

for index in range(tamanho):
    b[index] = a[index] * k

print(b)