# Faça um algoritmo que leia o salário de um funcionário e
#mostre seu novo salário, com 15% de aumento
salário = float(input('Digite o valor do salário'))
aumento = 15/100 * salário
novo = salário + aumento
print('O novo salário com 15% de aumento é R${:.2f}'.format(novo))