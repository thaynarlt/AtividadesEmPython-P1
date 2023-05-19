# Escreva um programa que:
# • Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos inteiros (N será lido);
# • Exiba a matriz lida (no formato de matriz);
# • Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
from random import randint

n = int(input("Digite a ordem da matriz: "))


# vai gerar uma matriz de ordem 'n', com números aleatórios de 1 a 9 para suas linhas e colunas.
matriz = [[randint(1, 9) for linha in range(n)] for coluna in range(n)]

# vai gerar uma matriz de ordem 'n', com números digitados pelo usuário para suas linhas e colunas.
# matriz = [[int(input("Valor: ")) for j in range(n)] for i in range(n)]

# linha = coluna (matriz quadrada)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
    print()
# imprime a matriz em formato de matriz

# Para exibor os elementos da diagonal principal, os elementos vão se encontrar em i = j:
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            print(matriz[i][j], end=' ')
    print()
