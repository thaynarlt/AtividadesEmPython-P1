#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
num = float(input('Digite o valor de um ângulo qualquer'))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(math.radians(num)), math.cos(math.radians(num)), math.tan(math.radians(num))))
