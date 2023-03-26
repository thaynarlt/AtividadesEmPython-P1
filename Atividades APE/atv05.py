#Escreva um programa para ler o nome e o sobrenome de uma pessoa e escrevê-los na seguinte forma: sobrenome seguido por uma vírgula e pelo nom
nome = str(input("Digite seu nome:"))
sobrenome = str(input("Digite seu sobrenome:"))

print("{},{}".format(sobrenome, nome))