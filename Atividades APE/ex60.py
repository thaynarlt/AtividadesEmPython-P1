# Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
# será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
# corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
# o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0 (zero).
# Veja o exemplo a seguir:
# índ:    0 1 2             0 1 2
#     0 | 1 2 3 |        0| 0 3 0  |
# A=  1 | 4 5 6 |     B= 1| 5 0 9  |
#     2 | 7 8 9 |        2| 0 11 0 |

# Ao final, imprima as duas matrizes (no formato de matriz).
from random import randint

N = int(input('Digite a ordem da matriz quadrada: '))
C = L = N

# cria uma matriz de ordem N com elementos vazios ainda.
matrizA = [[randint(1, 100)for l in range(L)] for c in range(C)]
matrizB = [[randint(1, 100)for l in range(L)] for c in range(C)]

# gerando a matriz A
for l in range(N):
    for c in range(N):
        matrizA[l][c]


# gerando a matriz B
for l in range(N):
    for c in range(N):
        if l == c or l + c == N - 1:
            matrizB[l][c] = 0
        else:
            matrizB[l][c] = matrizA[l][c] + l + c

# impressão da matriz A
print('\nMatriz A: ')
for l in range(N):
    for c in range(N):
        print(f'{matrizA[l][c]:3}', end='')
    print()

# impressão da matriz B
print('\nMatriz B: ')
for l in range(N):
    for c in range(N):
        print(f'{matrizB[l][c]:3}', end='')
    print()
