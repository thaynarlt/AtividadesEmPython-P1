#Faça um programa para ler as 8 dezenas apostadas por 20 apostadores e
#verificar se a aposta é válida (cada dezena está entre [1, 80] e não pode haver
#repetição). O programa deverá calcular e exibir a quantidade de números
#acertados em cada aposta.
#Atenção! As dezenas sorteadas são: 06, 07, 13, 14 e 26.

na = 3  #Número de apostadores (testando para apenas 3 apostadores ao invés de 20)

nda = 8  #Número de dezenas apostadas por cada apostador
vda = [None]*nda  #Vetor que irá conter as dezenas apostadas por um apostador

vds = [6,7,13,14,26]  #Vetor que contém as dezenas sorteadas
nds = len(vds) #Número de dezenas sorteadas

for i in range(na):

    #lendo as dezenas de um apostador
    print(f'\nDezenas do Apostador {i+1}:')
    for j in range(nda):
        vda[j] = int(input())

    #verificando se a aposta é válida
    valida = True
    for dezena in vda:
        if dezena < 1 or dezena > 80 or vda.count(dezena) > 1:
            valida = False
            break

    #contando a quantidade de acertos se a aposta for válida 
    if valida:
        cont = 0
        for dezena in vda:
            if dezena in vds:
                cont += 1
        print(f'Número de acertos: {cont}')
    else:
        print('Aposta inválida')