#Escreva um programa que leia duas variáveis inteiras e troque o conteúdo entre elas, mostrando o resultado.
v1 = int(input("Digite um valor inteiro qualquer:"))
v2 = int(input("Digite novamente um valor inteiro qualquer:"))



temp = v1
v1 = v2
v2 = temp



print("O primeiro valor é: {} e o segundo valor foi: {}".format(v1,v2))