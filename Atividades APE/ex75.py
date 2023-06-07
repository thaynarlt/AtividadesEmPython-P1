#4. Faça um programa que leia uma string S e um valor inteiro N, e exiba na tela a string S com as
#suas vogais repetidas N vezes.Exemplo:
#Entrada: S: Hoje tem aula de Python  
#N: 3

#Saída: Hooojeee teeem aaauuulaaa deee Pythooon

s = input('Digite uma frase: ').lower()
n = int(input('Digite um valor inteiro: '))

for i in s:
    if i in 'aeiou':
        print(i * n, end='')
    else:
        print(i, end='')
