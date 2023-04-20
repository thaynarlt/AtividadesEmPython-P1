#Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os
#números múltiplos de N entre X e Y.

n = int(input("Digite o valor de N: "))
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

print("Os múltiplos de", n, "entre", x, "e", y, "são:")

for i in range(x, y+1):
    if i % n == 0:
        print(i)