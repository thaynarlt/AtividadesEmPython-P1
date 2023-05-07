#3. Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
#informe em que posição (índice). Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.


n = int(input("Digite uma quantidade de números inteiros: "))

vetor = [None]*n
for index in range(n):
    vetor[index]= int(input("Digite um número:"))

k = int(input("Digite o valor a ser procurado no vetor: "))

for index in range(n):
    if vetor[index]==k:
        print(f"O numero {k} está na posição {index}")
