#3. Escreva um programa que leia N números inteiros (máximo 20) e armazene em um
#vetor X. Calcule a média dos elementos do vetor e informe quantos elementos estão
#abaixo da média do conjunto.
#Crie as seguintes funções:

#• Uma função que faça a leitura dos elementos de um vetor de inteiros. Essa função
#deve receber como parâmetro o número de elementos do vetor e deve retornar o vetor preenchido.

def leitura_elementos(num_elements):
    vetor=[None] * num_elements 
    for i in range(num_elements):
        vetor[i]=int(input('Adicione um número ao seu vetor:'))
    print(vetor)
    return vetor


num=int(input('Digite a quantidade de números em seu vetor: '))
vetor_preenchido =leitura_elementos(num)  
#• Uma função que calcule a média dos elementos de um vetor. Essa função deve
#receber como parâmetro um vetor e retornar a média dos elementos dele.

def media_vetor(vetor):
    soma = sum(vetor)
    quantd = len(vetor)

    media = soma/quantd
    print(f'A média do vetor é: {media}')
    return media

media =media_vetor(vetor_preenchido)


#• Uma função que receba um vetor e um número, e retorne quantos elementos do
#vetor estão abaixo desse número.

def receber(vetor):
    cont=0
    num = int(input('Digite um número a ser conferido: '))
    for i in range(len(vetor)):
        if num < vetor[i]:
            cont+=1
    print(f'O número digitado foi {num} e {cont} elemento(s) está(ão) abaixo do número digitado.')

receber(vetor_preenchido)