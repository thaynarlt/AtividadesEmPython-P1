#1. Faça um programa que leia uma frase e determine a quantidade de brancos contidos na mesma.

frase = input("Digite uma frase: ")

quantidade_brancos = 0
for caractere in frase:
    if caractere == ' ':
        quantidade_brancos += 1

print("A frase possui", quantidade_brancos, "espaços em branco.")
