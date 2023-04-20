#Faça um programa que leia vários números, determine e mostre o maior e o menor deles.
#Obs: a leitura do número 0 (zero) encerra o programa.

num = int(input("Digite o limite de números e ZERO para parar: "))
maior = menor = num
while num != 0:
    if num > maior:
        maior = num
    elif num< menor:
        menor = num
    num = int(input("Digite um  número: "))
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")