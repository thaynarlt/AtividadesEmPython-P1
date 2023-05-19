#1. Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's
#ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento
#igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.
#  |1 0 0|
#  |0 1 0|
#  |0 0 1|
#Com base na definição apresentada, escreva um programa que preencha uma
#matriz quadrada com valores fornecidos pelo usuário, determine e mostre se
#ela é uma matriz de permutação.

ordem = int(input("Digite a ordem da matriz: "))

matriz = [[int(input("Digite um valor: "))for l in range(ordem)]for c in range(ordem)]

#gerando a matriz quadrada:
print("Matriz quadrada digitada pelo usuário: ")
for l in range(ordem):
    for c in range(ordem):
        print(matriz[l][c], end =' ')
    print()

#conferindo se é matriz de permutação
for l in range(ordem):
    for c in range(ordem):
        soma = sum(matriz[l])
        if soma == 1:
            soma = True    
        else:
            soma = False

if soma == True:
    print("É uma matriz de permutação")
else:
    print("Não é uma matriz de permutação")


#conferindo se é matriz identidade (elementos da diagonal principal == 1)
identidade = True
#Diagonal princial da matriz

for l in range(ordem):
    for c in range(ordem):
        if (l == c and matriz[l][c] != 1) or (l != c and matriz[l][c] != 0):
            identidade = False
            break

if identidade:
    print('É uma matriz identidade!')
else:
    print("Não é uma matriz identidade!")
            