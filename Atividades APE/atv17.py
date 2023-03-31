#2.Escreva um programa que leia dois números e exiba-os em ordem crescente.
num1 = float(input("Digite um número qualquer:"))
num2 = float(input("Digite novamente um número qualquer:"))

if num1 > num2:
    maior = num1
    print("A ordem crescente dos números digitados é: {:.1f}, {:.1f}".format(num2, num1))
else:
    maior = num2
    print("A ordem crescente dos números digitados é: {:.1f}, {:.1f}".format(num1, num2))
