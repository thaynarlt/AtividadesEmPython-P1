v1 = int(input('Digite um primeiro número qualquer'))
v2 = int(input('Digite um segundo número qualquer'))
v3 = int(input('Digite um terceiro número qualquer'))

if v1>v2 and v1>v3:
    maior = v1

if v2>v1 and v2>v3:
    maior = v2

if v3>v2 and v3>v1:
    maior = v3

print('O maior número é {}{}{}.'.format('\033[1;31;40m' ,maior,'\033[m'))

if v1 < v2 and v1 < v3:
    menor = v1

if v2 < v1 and v2 < v3:
    menor = v2

if v3 < v2 and v3 < v1:
    menor = v3

print('O menor número é {}{}{}'.format('\033[1;31;40m',menor,'\033[m'))
