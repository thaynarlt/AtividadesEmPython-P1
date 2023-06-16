#1. Escreva uma função chamada vogal que receba uma letra e verifique se a letra é uma
#vogal, retornando o valor True nesse caso, ou o valor False caso contrário.
#Escreva também um programa que leia uma frase e, usando a função vogal criada,
#imprima a quantidade de vogais existentes na frase lida.

def vogal(letra): #criou a função chamada de vogal que está recebendo letra.
    vogais = ['a', 'e', 'i', 'o', 'u'] #lista das vogais
    if letra.lower() in vogais: #se letra está em contida em vogais então é verdadeiro
        return True
    else:
        return False #se não, é falso!

def contar_vogais(frase): #função criada para contar as vogais
    contador = 0 
    for letra in frase: #se a letra está na frase
        if vogal(letra): #se a letra for uma vogal então conta +1
            contador += 1
    return contador

frase = input("Digite uma frase: ") #usuário digita uma frase
qtd_vogais = contar_vogais(frase) #programa da função vai contar as vogais contidas na frase digitada
print("A quantidade de vogais na frase é:", qtd_vogais) #print a quantidade de vogais digitadas na frase
