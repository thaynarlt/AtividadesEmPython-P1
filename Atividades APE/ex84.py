#2. Escreva uma função chamada primo para determinar se um número é primo ou não. A
#função deve receber um número inteiro, retornar True se o número for primo, ou False caso contrário.
#Escreva também um programa que, usando a função primo criada, exiba os números primos entre 1 e 100.

def primo(numero):
    if numero > 1: #se o numero é maior que 1
        for i in range(2, numero):
            if numero % i == 0: #se o numero divido por i == 0 então
                print(f"O número {numero} não é primo") # o número não é primo
                break
        else:
            print(f"O número {numero} é primo") # o número é primo
            return True #vai 'receber' o True se for primo
    else:
        return False #vai 'receber' o False se não for primo

for num in range(2, 101): #vai percorrer os nmrs de 2 a 101
    primo(num)
