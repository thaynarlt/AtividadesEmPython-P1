# 1. Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia
# da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de
# semana (sábado e domingo). Considere que o dia 1 é o domingo.

sem = int(input('\033[0;1;34m'+"""Digite um número qualquer de 1 a 7 correspondente
a um dia da semana (dia 1 é o domingo):"""+'\033[0m'))

if sem == 2:
    print('\033[0;1;31m'+"O dia da semana é a Segunda-feira e é um DIA ÚTIL"+'\033[0m')
elif sem == 3:
    print('\033[0;1;31m'+"O dia da semana é a Terça-feira e é um DIA ÚTIL"+'\033[0m')
elif sem == 4:
    print('\033[0;1;31m'+"O dia da semana é a Quarta-feira e é um DIA ÚTIL"+'\033[0m')
elif sem == 5:
    print('\033[0;1;31m'+"O dia da semana é a Quinta-feira e é um DIA ÚTIL"+'\033[0m')
elif sem == 6:
    print('\033[0;1;31m'+"O dia da semana é a Sexta-feira e é um DIA ÚTIL"+'\033[0m')
elif sem == 1:
    print('\033[0;1;32m'+"O dia da semana é o Domingo e é FINAL DE SEMANA"+'\033[0m')
elif sem == 7:
    print('\033[0;1;32m'+"O dia da semana é o Sábado e é FINAL DE SEMANA"+'\033[0m')