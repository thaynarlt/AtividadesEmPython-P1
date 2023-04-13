#Faça um programa que calcule e mostre os números múltiplos de 5 do
#intervalo 50 a 300, juntamente com suas raízes e seus cubos.
import math

# Loop através do intervalo de 50 a 300
for i in range(50, 301):
    # Verifica se o número é um múltiplo de 5
    if i % 5 == 0:
        # Calcula a raiz quadrada e o cubo do número
        raiz = math.sqrt(i)
        cubo = i ** 3
        # Exibe o número, sua raiz e seu cubo
        print(f"{i} -> Raiz Quadrada: {raiz} -> Cubo: {cubo}")

