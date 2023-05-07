#2. Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.

TAMANHO = 30
vetor = [None]*TAMANHO

for index in range(TAMANHO):
    vetor[index]= int(input("Digite um número:"))

k = int(input("Digite o valor a ser pesquisado no vetor:"))

cont = 0
for index in range(TAMANHO):
    if vetor[index]==k:
        cont+=1

print(f"O valor {k} apareceu {cont} vez(es)!.")