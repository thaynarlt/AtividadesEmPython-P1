#1. Escreva uma função chamada menor que receba 3 números e retorne o menor
#deles. Faça também um programa para testar a função.

def menor(v1,v2,v3):
    if v1<v2 and v1<v3:
        return v1
    elif v2<v1 and v2<v3:
        return v2
    else:
        return v3

#Programa principal:
a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

resultado = menor(a,b,c)
print(resultado)