#5. Faça um programa que leia uma frase e a exiba na tela conforme o exemplo abaixo. Exemplo:
#Entrada: ABCDE
#Saída: A
#BB
#CCC
#DDDD
#EEEEEE
#DDDD
#CCC
#BB
#A

frase = input('Digite uma frase: ')
tam = len(frase)

for i in range(tam):
    print(f'{frase[i]*(i+1)}')

for i in range(tam-2,-1,-1):
    print(f'{frase[i]*(i+1)}')