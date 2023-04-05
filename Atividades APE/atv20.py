#5.A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o total de vendas daquele vendedor,
#  mas essa comissão nunca deve ser inferior ao salário-mínimo. 
# Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu salário.

ndevendas = float(input("Digite o valor total de vendas: "))
SALARIO_MINIMO = 1320
comissao = ndevendas * 0.05

if ndevendas < SALARIO_MINIMO:
    salariotot = SALARIO_MINIMO
else:
    salariotot = comissao + SALARIO_MINIMO

print("O seu salário total é {}".format(salariotot))