#6. Recomendam-se estudantes para bolsas de estudo em função de seu desempenho. A natureza das recomendações é baseada na seguinte tabela:
# CONCEITO / RECOMENDAÇÃO:
# A = Fortemente Recomendado
# B ou C = Recomendado
# D = Não recomendado
# Escreva um programa que leia o nome e o conceito de um estudante e exiba o nome do estudante e sua respectiva recomendação.
nome = str(input("Digite seu nome: "))
conceito = str(input("Digite o seu Conceito (A, B, C ou D):"))
a1 = "A"
b1 = "B"
c1 = "C"
d1 = "D"

if conceito == a1:
    print("O estudante {} apresenta o conceito A no estado de Fortemente Recomendado.".format(nome))
elif conceito == b1:
    print("O estudante {} apresenta o conceito B no estado de Recomendado.".format(nome))
elif conceito == c1:
    print("O estudante {} apresenta o conceito C no estado de Recomendado.".format(nome ))
elif conceito == d1:
    print("O estudante {} apresenta o conceito D no estado de Fortemente Não Recomendado.".format(nome))