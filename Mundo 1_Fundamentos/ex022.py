#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.

nome = str(input('Digite um nome completo')).strip()
print('O nome em Maiúsculo fica:')
print(nome.upper())
print('O nome em Minúsculo fica:')
print(nome.lower())
print('A quantidade de letras ao todo:')
print(len(nome)-nome.count(' '))
d = nome.split()
print('Quantas letras tem o primeiro nome:')
print(len(d[0]))
