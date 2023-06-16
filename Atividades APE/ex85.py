#4. Faça um programa que leia duas matrizes de inteiros e gere uma terceira matriz que
#corresponderá a soma das duas matrizes lidas. A ordem das matrizes também será lida.
#O programa deverá conter as seguintes funções:
#• Uma função para gerar e ler uma matriz, sendo passados como parâmetros a ordem da matriz.
#• Uma função para exibir uma matriz em sua representação clássica (linhas e colunas).
#• Uma função para somar duas matrizes.



#FUNÇÃO PARA GERAR MATRIZ
def gerar_ler_matriz(ordem):
    matriz = [[int(input('Digite um número para adicionar a matriz: '))for c in range(ordem)]for l in range(ordem)]
    return matriz
#PROGRAMA PRINCIPAL PARA GERAR A MATRIZ A E B
ord = int(input('Digite a ordem da matriz: '))
print('Escreva os números da primeira matriz:')
matriz_preenchidaA= gerar_ler_matriz(ord)

print('Escreva os números da segunda matriz:')
matriz_preenchidaB= gerar_ler_matriz(ord)


#FUNÇÃO PARA IMPRIMIR A MATRIZ EM FORMATO DE MATRIZ
def exibir_matriz(matriz,ordem):
    for l in range(ordem):
        for c in range(ordem):
            print(matriz[l][c], end=' ')
        print()

#PROGRAMA PRINCIPAL PARA EXIBIR A MATRIZ EM FORMATO DE MATRIZ        
print('Gerando Matriz A:')
exibir_matriz(matriz_preenchidaA,ord)

print('Gerando Matriz B:')
exibir_matriz(matriz_preenchidaB,ord)


#FUNÇÃO PARA SOMAR AS MATRIZES A E B
def somar_matrizes(matrizA,matrizB,ordem):
    print(f'A soma das matrizes é:')
    matrizC= [[None for c in range(ordem)]for l in range(ordem)]
    for l in range(ordem):
        for c in range(ordem):
            matrizC[l][c] = matrizA[l][c] + matrizB[l][c]
    return matrizC

#PROGRAMA PRINCIPAL PARA EXIBIR A MATRIZC DA SOMA             
matrizC= somar_matrizes(matriz_preenchidaA, matriz_preenchidaB,ord)
exibir_matriz(matrizC,ord)