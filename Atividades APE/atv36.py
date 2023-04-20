#Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
#próprio. Faça um programa que leia um número e determine se ele é ou não primo.

num = int(input("Digite um numero inteiro: "))

if num > 1:
    for i in range(2, num):
        if num %i == 0:
           print(f"O número {num} não é primo")
           break # o break para o laço
    else:
        print(f"O numero  {num} é primo")       
elif num == 0:
    print(num, 'é zero')
elif num == 1:
    print(num, 'é um')
else:
    print(num, 'é negativo')
