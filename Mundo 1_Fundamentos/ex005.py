# Faça um programa que leia um número inteiro e mostre
# na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número'))
a = n1 - 1
b = n1 + 1
#print('O número antecessor de', n1, 'é', a, 'e o número sucessor é', b)
print('O número antecessor de {} é {} e o número sucessor é {}'.format(n1, a, b))
