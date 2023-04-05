#8.Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve solicitar a digitação de dois operandos
#  e um operador (+ - x * / %) e deve imprimir ao resultado da operação aritmética. 
# Caso o usuário digite um operador inválido, o programa deve imprimir "Operador desconhecido".

a = float(input('\033[34m'+"Digite um valor qualquer : "))
b = float(input('\033[34m'+"Digite outro valor qualquer: "))
operador = str(input('\033[34m'+"Digite um operador (+, -, *, /, %) : "))

if operador == '+' or operador == '-' or operador == '*' or operador == '/' or operador == '%':
    if operador == '+':
        print('\033[42;1;33m'+"A soma é {}".format(a + b)+'\033[0;0m')
    elif operador == '-':
        print('\033[42;1;33m'+"A subtração é {}".format(a - b)+'\033[0;0m')
    elif operador == '*':
        print('\033[42;1;33m'+"A multiplicação é {}".format(a * b)+'\033[0;0m')
    elif operador == '/' and b == 0:
        print('\033[42;1;33m'+"Não é possível realizar a divisão por zero"+'\033[0;0m')
    elif operador == '/':
        print('\033[42;1;33m'+"A divisão é {}".format(a / b)+'\033[0;0m')
    elif operador == '%' and b == 0 :
        print('\033[42;1;33m'+"Não é possível realizar a divisão inteira por zero"+'\033[0;0m')
    elif operador == '%':
        print('\033[42;1;33m'+"O resto da divisão é de {}%{} é {}".format(a, b ,a % b)+'\033[0;0m')
else:
    print('\033[31m'+"Operador inválido.")
 