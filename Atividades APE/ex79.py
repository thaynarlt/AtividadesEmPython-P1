#2. Escreva uma função chamada fatorial que receba um número inteiro e retorne
#seu fatorial. Faça também um programa para testar a função.

def fatorial(n):
    cont=1
    for i in range(2,n+1):
        cont *= i
    return(cont)

#Programa principal
numero = int(input('Digite um valor: '))
resultado_fatorial = fatorial(numero)
print(resultado_fatorial)