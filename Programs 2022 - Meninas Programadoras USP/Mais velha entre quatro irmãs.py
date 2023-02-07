idade1 = int(input('\033[0;31;42mDigite a idade da primeira filha:\033[m'))
idade2 = int(input('\033[7;31;42mDigite a idade da segunda filha:\033[m'))
idade3 = int(input('\033[0;31;42mDigite a idade da terceira filha:\033[m'))
idade4 = int(input('\033[7;31;42mDigite a idade da quarta filha:\033[m'))

if idade1 > idade2 and idade1>idade3 and idade1>idade4:
    maior = idade1

if idade2 > idade1 and idade2>idade3 and idade2>idade4:
    maior = idade2

if idade3 > idade1 and idade3>idade2 and idade3>idade4:
    maior = idade3

if idade4 > idade1 and idade4>idade2 and idade4>idade3:
    maior = idade4

print('A filha mais velha tem {}{}anos{}'.format('\033[1;37;40m', maior,'\033[m'))
