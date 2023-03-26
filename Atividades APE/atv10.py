#Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-se que nota1 possui peso 6 e nota2 possui peso 4.
NOTA1 = 6
NOTA2 = 4

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

mediap = (NOTA1 * n1 + NOTA2 * n2)/2

print("A média ponderada das duas notas digitadas é:{:.2f}".format(mediap))