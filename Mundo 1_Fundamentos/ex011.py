# Faça um programa que leia a largura e altura de uma
#parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que
#cada litro de tinta pinta uma área de 2m²
largura = float(input('Digite o valor da largura em metros'))
altura = float(input('Digite o valor da altura em metros'))
area = largura*altura
tinta = area/2
print('Sua parede tem uma área de {:.1f}m²'.format(area))
print('A tinta necessária para pintar essa área é {:.2f}l'.format(tinta))