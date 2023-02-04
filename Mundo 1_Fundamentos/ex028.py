#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o
# número escolhido pelo computador.
# -O programa deverá escrever na tela se o usúario venceu ou perdeu.
import random
from time import sleep
r = random.randint(0, 5)
valor = (int(input('Digite um valor de 0 a 5')))
print('PROCESSANDO...')
sleep(2)
if r == valor:
    print('Acertou!')
else:
    print('Perdeu!')

    
