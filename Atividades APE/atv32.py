#Faça um programa que calcule e mostre o fatorial de um número N, fornecido
#pelo usuário. A definição de fatorial é mostrada a seguir:
# N! = 1 * 2 * 3 * ... * N -1 * N
# 0! = 1

n = int(input("Fatorial de: ") )

resultado=1
for n in range(1,n+1):
    resultado *= n

print(resultado)