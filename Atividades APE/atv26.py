#3. Escreva um programa que solicite a digitação de um ano e imprima sua classificação como bissexto ou não bissexto.

ano = int(input('\033[1;7m'+"Digite um ano qualquer (exemplo-> 2012):"+'\033[0m'))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('\033[1;32m'+"O ano é BISSEXTO"+'\033[0m')
else:
    print('\033[1;31m'+"O ano NÃO é BISSEXTO"+'\033[0m')