#O Brasil possui 26 estados e 1 distrito federal, totalizando 27 unidades
#federativas. Escreva um programa para armazene, em um vetor, a sigla de todas
#as unidades federativas. O programa deverá obter de vários usuários qual é a
#unidade federativa ele acha mais interessante, informando a respectiva sigla. O
#programa encerra quando for digitada uma sigla inexistente. Ao final, o
#programa deverá exibir qual foi a sigla mais votada (considere possibilidade de empate).

uf = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
n = len(uf)
cont = [0]*n

while True:
    voto = input('Digite a UF de sua preferência: ').upper()
    if voto not in uf:
        break
    ind = uf.index(voto)
    cont[ind] += 1

print('\nUF(s) mais votada(s):') 
maior = max(cont)
for i in range(n):
    if cont[i] == maior:
        print(f'{uf[i]} com {cont[i]} votos')