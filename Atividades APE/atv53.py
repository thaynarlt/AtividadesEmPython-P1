#Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão
#lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a
#intercalação dos elementos de A e B.
#Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]

n= int(input("Digite o limite de números dos vetores: "))

vetorA= []
vetorB = []

for index in range(n):
    vetorA.append(int(input("Digite o elemento " + str(index) + " de A: ")))

for index in range(n):
    vetorB.append(int(input("Digite o elemento " + str(index) + " de B: ")))

vetorC = [0]*(n*2)

for index in range(n):
    vetorC[index * 2] = vetorA[index]
    vetorC[index * 2 + 1] = vetorB[index]

print(vetorA)
print(vetorB)
print(vetorC)