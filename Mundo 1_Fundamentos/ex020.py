#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
g1 = str(input('Grupo A:'))
g2 = str(input('Grupo B:'))
g3 = str(input('Grupo C:'))
g4 = str(input('Grupo D:'))
lista = [g1, g2, g3, g4]
random.shuffle(lista)
print('A ordem dos grupos escolhida foi ')
print(lista)