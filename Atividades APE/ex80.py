#3. Escreva uma função chamada vertical que receba como parâmetro uma string e
#a exiba na vertical, ou seja, com uma letra em cada linha. Faça também um
#programa para testar a função.

def vertical(string):
    for i in string:
        print(f'{i}')
    return 

#Programa principal
frase=input('Digite uma frase: ')
atrib = vertical(frase)
print(atrib)