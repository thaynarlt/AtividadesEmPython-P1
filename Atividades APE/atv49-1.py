TAM = 10

vetor = [None]*10
for index in range(TAM):
    vetor[index] = int(input("Digite um número:"))

print(f"Números que estão nos índices pares:")
for index in range(0, TAM, 2):
    print(vetor[index], end ='')

print(f"Números que estão nos índices ímpares:")
for index in range(1, TAM, 2):
    print(vetor[index], end ='')
