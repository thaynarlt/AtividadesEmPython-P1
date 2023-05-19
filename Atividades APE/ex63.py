#2. Uma matriz quadrada contendo valores inteiros é denominada quadrado
#mágico quando a soma dos elementos de cada linha, a soma dos elementos
#de cada coluna e a soma dos elementos das diagonais principal e secundária
#são todos iguais. Por exemplo, a matriz seguinte é um quadrado mágico.
#  |8 0 7|
#  |4 5 6|
#  |3 10 2|
#Escreva um programa que preencha uma matriz com valores fornecidos pelo
#usuário, determine e mostre se ela é um quadrado mágico.

ordem = int(input("Digite a ordem da matriz: "))

matriz = [[int(input("Digite um valor: "))for l in range(ordem)]for c in range(ordem)]

#Imprimindo matriz inicial
for l in range(ordem):
    for c in range(ordem):
        print(matriz[l][c], end = ' ')
    print()

#Matriz de quadrado mágico se:
soma_coluna = sum(matriz[c])
soma_linha = sum(matriz[l])

diagonal_1 = []
diagonal_2= []

#Diagonal princial da matriz
for l in range(ordem):
    for c in range(ordem):
        if l == c:
            diagonal_1.append(matriz[l][c])

#Diagonal secundária da matriz
for l in range(ordem):
    for c in range(ordem):
        if l + c == ordem - 1:
            diagonal_2.append(matriz[l][c])

soma_diag1 = sum(diagonal_1)
soma_diag2 = sum(diagonal_2)

#quadrado mag
quadrado_mag = soma_coluna == soma_linha == soma_diag1 == soma_diag2

#conferindo se é quadrado mágico:
for l in range(ordem):
    for c in range(ordem):
        if quadrado_mag == True:
            quadrado_mag == True    
        else:
            quadrado_mag == False

if quadrado_mag == True:
    print("É uma matriz de quadrado mágico")
else:
    print("Não é uma matriz de quadrado mágico")

