#Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
#• Os números que estão nos índices pares;
#• Os números que estão nos índices ímpares.

N = 10
impar = 0
par = 0
pares = []
impares = []
vetor = [None]*N
for index in range(N):
    vetor[index]= int(input("Digite um número:"))
    if vetor[index]%2 == 0:
        par = vetor[index]
        pares.append(par)
    else:
        impar = vetor[index]
        impares.append(impar)

print(f"Os numeros pares são: {pares} e os ímpares são: {impares}")