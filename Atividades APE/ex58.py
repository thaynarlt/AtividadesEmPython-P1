# 1. Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
# valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
# deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
# Ao final, exiba as 3 matrizes (no formato de matriz).

from random import randint

LINHA = 2
COLUNA = 3
matrizA = [[randint(1, 100) for c in range(COLUNA)]for l in range(LINHA)]
matrizB = [[randint(1, 100) for c in range(COLUNA)]for l in range(LINHA)]
matrizC = [[None for c in range(COLUNA)]for l in range(LINHA)]

# gerando a matriz A
print('Primeira Matriz:')
for l in range(LINHA):
    for c in range(COLUNA):
        print(matrizA[l][c], end=' ')
    print()

# gerando a matriz B
print('Segunda Matriz:')
for l in range(LINHA):
    for c in range(COLUNA):
        print(matrizB[l][c], end=' ')
    print()

# gerando a soma (matriz C)
for l in range(LINHA):
    for c in range(COLUNA):
        matrizC[l][c] = matrizA[l][c]+matrizB[l][c]
    print()


print("Soma das matrizes: ")
for l in range(LINHA):
    for c in range(COLUNA):
        print(f'{matrizC[l][c]:4}', end='')
    print()
