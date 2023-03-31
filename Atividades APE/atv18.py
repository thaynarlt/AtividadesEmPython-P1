#3.Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.

n1 = int(input("Digite um número inteiro qualquer"))
n2 = int(input("Digite novamente um número inteiro qualquer"))
n3 = int(input("Digite novamente um número inteiro qualquer"))

if n1 > n2 and n1> n3:
    print("O maior é: ", n1)

elif n2>n1 and n2>n3:
    print("O maior é: ", n2)

elif n3> n1 and n3>n2:
    print("O maior é: ", n3)