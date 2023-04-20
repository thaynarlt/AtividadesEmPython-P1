#Faça um programa que leia um número inteiro N, calcule e mostre o maior
#quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o resultado é 36.
import math
num = int(input("Digite um número inteiro: "))

maior_qdo_pft = 1

for k in range(num,1, -1):
    raiz = math.sqrt(k)
    if int(raiz)==raiz and k>maior_qdo_pft:
        maior_qdo_pft = k
    break
print(f"O maior quadrado perfeito é: {maior_qdo_pft}")
