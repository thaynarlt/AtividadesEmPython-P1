#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input('Digite o primeiro número:'))
b = float(input('Digite o segundo número:'))
c = float(input('Digite o terceiro número:'))
#Verificando o menor
menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c
#Verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))