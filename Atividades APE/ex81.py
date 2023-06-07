#4. Escreva uma função chamada soma que receba um vetor e retorne a soma dos seus elementos (obs: não use a função sum).
#Escreva também um programa que, dado o vetor V = [ 6,3,8,7,2,5 ] e usando a função soma criada, 
#informe a soma dos elementos do vetor V.


#ex1
def soma(vetor):
    soma=0
    for i in range(len(vetor)):
        soma+=vetor[i]    
    return soma

n = int(input('Digite o número máximo de valores contidos no vetor: '))
vetor=[None]*n
for i in range(n):
        vetor[i] = int(input('Digite um valor: '))

atrib = soma(vetor)
print(f'A soma do primeiro vetor: {atrib}')

#ex2
vetor2 = [6,3,8,7,2,5]
print(vetor2)
atrib2 = soma(vetor2)
print(f'A soma do segundo vetor: {atrib2}')
