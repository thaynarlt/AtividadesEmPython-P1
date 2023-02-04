#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

a = float(input('Digite o comprimento da primeira reta:'))
b = float(input('Digite o comprimento da segunda reta:'))
c = float(input('Digite o comprimento da terceira reta:'))

if (a < b + c and b < a + c and c < b + c):
    if (a == b and b == c):
        print('Os lados formam um Triângulo Equilátero.')
    else:
        if (a == b or a == c or b == c):
            print('Os lados formam um Triângulo Isósceles.')
        else:
            print('Os lados formam um Triângulo Escaleno.')
else:
    print('Os lados não formam um triângulo!')