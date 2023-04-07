#Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os seus coeficientes. Fórmulas:
# x = (-b +- √Δ)/2a  Δ = b*b - 4ac
#Obs: se Δ for negativo, não existem as raízes da equação.
#Dica: use a função sqrt do módulo math.

import math

a = float(input('\033[1;36m'+"Digite o valor de a: "+'\033[0m'))
b = float(input('\033[1;36m'"Digite o valor de b: "+'\033[0m'))
c = float(input('\033[1;36m'"Digite o valor de c: "+'\033[0m'))

#a*(x*x) + b*x + c = 0

delta = (b*b)- 4 * (a) * (c)

if delta > 0:
    raiz = math.sqrt(delta)
    x1 = ((-b) + raiz)/ 2 *a
    x2 = ((-b) - raiz)/ 2 * a
    print('\033[1;32m'+"Os valores das raízes são: ({:.1f},{:.1f}.)".format(x1,x2)+'\033[0m')
else:
    print('\033[1;31m'+"Delta é negativo, não existe raizes!"+'\033[0m')