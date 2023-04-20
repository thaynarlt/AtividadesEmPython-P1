#Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
#Obs: não use o comando for, use while.

soma = 0
contador = 0

while contador < 30:
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    contador += 1

print("A soma dos números é:", soma)