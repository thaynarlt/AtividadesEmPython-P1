# Faça um algoritmo que leia o preço de um produto e mostre
#seu novo preço, com 5% de desconto
preço = float(input('Digite o preço do produto'))
desconto = 5/100 * preço
novo = preço - desconto
print('O novo valor do produto com 5% de desconto é {:.2f}'.format(novo))
