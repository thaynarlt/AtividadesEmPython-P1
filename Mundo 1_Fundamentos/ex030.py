#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número inteiro'))
resto = num % 2
if resto == 0:
    print('Esté número é par!')
else:
    print('Este número é ímpar!')
    
