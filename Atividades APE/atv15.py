#A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do valor da venda. 
# Escreva um programa que leia o nome, o número de carros vendidos e o valor total das vendas de um vendedor, e calcule e exiba o seu salário.


SALARIOC = 1000
COMISSAO = 200
PORCENT = 0.05

nome = str(input("Digite o seu nome:"))
carros_vendidos = int(input("Digite a quantidade de carros vendidos por mês:"))
valortotalvendas = float(input("Digite o valor total de suas vendas:"))

dinheiro = SALARIOC + (carros_vendidos * COMISSAO) + (PORCENT * valortotalvendas)

print("O empregado {} vendeu um total de {} carros, faturou para a empresa um total de {:.2f} e recebeu seu salário no valor de {:.2f}".format(nome, carros_vendidos, valortotalvendas, dinheiro))