#Faça um programa que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

n1 = float(input("Digite a nota da primeira prova:"))
n2 = float(input("Digite a nota da segunda prova:"))
n3 = float(input("Digite a nota da terceira prova:"))

media = (n1 + n2 + n3)/3

print("A média aritmética das três notas desse aluno é: {:.1f}".format(media))
