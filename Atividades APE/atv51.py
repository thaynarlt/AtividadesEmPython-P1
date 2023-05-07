#Escreva um programa que leia um vetor de N números inteiros (N será lido),
#inverta a ordem dos elementos do vetor e exiba o vetor invertido.
#Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
#Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em
#ordem inversa!

n = int(input("Digite uma quantidade de números inteiros: "))

vetor = [None]*n
for index in range(n):
    vetor[index]= int(input("Digite um número:"))

print(f'A ordem inicial é: {vetor}')

aux = [None]*n
for i in range(n):
    aux[i] = vetor[i]
inicial = 0
for i in range(n -1, -1, -1):
    vetor[i] = aux[inicial]
    inicial +=1

print(f'A ordem final inversa da lista é: {vetor}')