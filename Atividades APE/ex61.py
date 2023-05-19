# Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma dada matriz.
# Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
# por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].
#    | -3 6 2 |        | -3 -1 |
# C= | -1 0 7 |     B= | 6   0 |
#                      | 2   7 |
# Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
# pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
# duas matrizes (no formato de matriz).
from random import randint

L = 3
C = 5

# matriz = [[int(input("Digite um valor: ")) for c in range(C)]for l in range(L)]
matriz = [[randint(1, 9) for c in range(C)]for l in range(L)]

# imprimindo a matriz normal
print('Matriz inicial: ')
for l in range(L):
    for c in range(C):
        print(matriz[l][c], end=' ')
    print()

# matriz transposta: 3x5 => 5x3
# cria variável para a matriz transposta
matriz_transp = [[0 for l in range(L)]for c in range(C)]
for l in range(L):
    for c in range(C):
        # troca as colunas pelas linhas e vice versa
        matriz_transp[c][l] = matriz[l][c]
    print()

print('Matriz transposta: ')
for l in range(C):  # troca Linha pela Coluna
    for c in range(L):  # troca Coluna pela Linha
        print(matriz_transp[l][c], end=' ')
    print()
