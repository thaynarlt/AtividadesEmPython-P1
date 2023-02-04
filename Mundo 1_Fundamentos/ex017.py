#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
import math

c1 = float(input('Digite o valor do cateto oposto'))
c2 = float(input('Digite o valor do cateto adjacente'))
hip = c1**2 + c2**2
print('O valor da hipotenusa é {:.1f}'.format(math.sqrt(hip)))
