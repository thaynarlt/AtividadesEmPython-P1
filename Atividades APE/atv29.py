#Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
#tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
#segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
#nota maior ou igual a 8.0 para ser aprovado no concurso.
#Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
#se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
#foi aprovado ou não no concurso.

n1 = float(input('\033[1;36m'+"Digite a nota da primeira prova: "+'\033[0m'))
n2 = float(input('\033[1;36m'+"Digite a nota da segunda prova: "+'\033[0m'))

m1 = (n1 + n2)/ 2

if m1 >= 7:
    n3 = float(input('\033[1;35m'+"Digite a nota da segunda etapa: "+'\033[0m'))
    if n3 >= 8:
        print('\033[1;32m'+"Você está aprovado!"+'\033[0m')
    else:
        print('\033[1;31m'+"Você não conseguiu a nota necessária para a aprovação :("+'\033[0m')
else:
    print('\033[1;31m'+"Sua média não foi alta o suficiente para realizar a segunda etapa :("+'\033[0m')