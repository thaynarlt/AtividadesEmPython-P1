#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
a1 = str(input('Aluno 1:'))
a2 = str(input('Aluno 2:'))
a3 = str(input('Aluno 3:'))
a4 = str(input('Aluno 4:'))
lista =[a1, a2, a3, a4]
print('O aluno escolhido para apagar o quadro foi: {}'.format(random.choice(lista)))
