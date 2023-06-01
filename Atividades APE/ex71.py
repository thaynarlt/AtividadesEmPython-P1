#Faça um programa para ler uma palavra ou frase e informe se ela é um palindromo

frase = input('Digite uma frase:').replace(' ', '')

frase_invertida = frase[::-1]
if frase == frase_invertida:
    print('É uma frase/palavra palindroma')
else:
    print('Não é uma frase/palavra palindroma')