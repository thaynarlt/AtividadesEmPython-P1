#Escreva um programa que receba um vetor V de N números inteiros (N será lido),
#determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices.
#Obs: suponha a inexistência de valores repetidos.

n = int(input("Digite uma quantidade de números inteiros: "))
maior = 0
menor = 0
vetor = [None]*n
for index in range(n):
    vetor[index]= int(input("Digite um número:"))
    if vetor[index]> maior:
        maior = vetor[index]
    elif vetor[index]<menor:
        menor = vetor[index]
print(f"O maior valor é {maior} e o menor é o valor {menor}")