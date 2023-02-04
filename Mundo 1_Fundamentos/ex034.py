#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# -Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# -Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor de seu salário'))
maior = salario * 0.10
menor = salario * 0.15
total1 = salario + (salario * 0.10)
total2 = salario + (salario * 0.15)
if salario >= 1250:
    print('Seu salário é maior que R$1.250,00. Seu aumento é de R${}. Seu novo saldo é R${}'.format(maior, total1))
else:
    print('Seu salário é menor que R$1.250,00. Seu aumento é de R${}. Seu novo saldo é R${}'.format(menor, total2))