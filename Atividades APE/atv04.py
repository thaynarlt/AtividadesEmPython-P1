#Escreva um programa para calcular a área de um triângulo, dados os valores de base e altura.
base = float(input("Digite o valor da base do triângulo:"))
altura = float(input("Digite o valor da altura do triângulo:"))

area = (base * altura)/2

print("O valor da área do triângulo é:{:.1f}".format(area))