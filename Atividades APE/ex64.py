#3. Escreva um programa que preencha uma matriz quadrada de ordem 3 com
#valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente), calcule e exiba:
#• A soma dos elementos de cada linha; OK
#• A soma dos elementos de cada coluna; OK 
#• A soma dos elementos da diagonal principal da matriz; OK
#• A soma dos elementos da diagonal secundária da matriz; OK
#• A soma de todos os elementos da matriz. OK

from random import randint
ORDEM = 3

matriz = [[randint(1,9)for l in range(ORDEM)]for c in range(ORDEM)]

#Imprimindo a matriz:
for l in range(ORDEM):
    for c in range(ORDEM):
        print(matriz[l][c], end = ' ')
    print()




#A soma dos elementos de cada linha e coluna;
somalinha = []
for l in range(ORDEM):
    soma_linha = sum(matriz[l])
    somalinha.append(soma_linha)
somacoluna = []
for c in range(ORDEM):
    soma_coluna = sum(matriz[l][c] for l in range(ORDEM))
    somacoluna.append(soma_coluna)

somacolunas = sum(somacoluna)
somalinhas = sum(somalinha)




#Diagonal princial da matriz
diagonal_1 = []
diagonal_2= []

for l in range(ORDEM):
    for c in range(ORDEM):
        if l == c:
            diagonal_1.append(matriz[l][c])

#Diagonal secundária da matriz
for l in range(ORDEM):
    for c in range(ORDEM):
        if l + c == ORDEM - 1:
            diagonal_2.append(matriz[l][c])

#A soma dos elementos das diagonais;
soma_diag1 = sum(diagonal_1)
soma_diag2 = sum(diagonal_2)



#Soma de todos os elemntos da matriz:
somatotLINHA = sum(somalinha)
print(f"A soma dos elementos de cada linha:\n 1º LINHA ={somalinha[0]},\n 2º LINHA = {somalinha[1]},\n 3º LINHA = {somalinha[2]} ")
print(f"A soma dos elementos de cada coluna:\n 1º COLUNA ={somacoluna[0]},\n 2º COLUNA = {somacoluna[1]},\n 3º COLUNA = {somacoluna[2]}")
print("A soma dos elementos da diagonal principal da matriz: ", soma_diag1)
print("A soma dos elementos da diagonal secundária da matriz: ", soma_diag2)
print(f"A soma de todos os elementos da matriz: {somatotLINHA}")