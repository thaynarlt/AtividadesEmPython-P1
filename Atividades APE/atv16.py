#1.Escreva um programa que leia um número inteiro e determine se ele é par ou ímpar.

num = int(input('Digite um número inteiro'))
resto = num % 2  # % é o resto da divisão 
if resto == 0:
    print('Esté número é par!')
else:
    print('Este número é ímpar!')