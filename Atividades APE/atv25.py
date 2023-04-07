# 2. Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima
# sua classificação: vogal, consoante, número e caractere especial.

qq = str(input('\033[1;7m'+"Digite um caractere qualquer do seu teclado:"+'\033[0m')).lower()

if qq == 'a' or qq=='e' or qq=='i' or qq=='o' or qq=='u':
    print('\033[1;36m'+"O caractere digitado é uma VOGAL."+'\033[0m')

elif qq == 'b' or qq=='c' or qq=='d' or qq=='f' or qq=='g' or qq=='h' or qq=='j' or qq=='l':
    print('\033[1;35m'+"O caractere digitado é uma CONSOANTE."+'\033[0m')

elif qq=='m' or qq=='n' or qq=='p' or qq=='q' or qq=='r' or qq=='s' or qq=='t':
    print('\033[1;35m'+"O caractere digitado é uma CONSOANTE."+'\033[0m')

elif qq=='k' or qq=='v' or qq=='w' or qq=='x' or qq=='y' or qq=='z':
    print('\033[1;35m'+"O caractere digitado é uma CONSOANTE."+'\033[0m')

elif qq == '1' or qq=='2' or qq=='3' or qq=='4' or qq=='5' or qq=='6' or qq=='7' or qq=='8' or qq=='9' or qq=='0':
    print('\033[1;33m'+"O caractere digitado é um NÚMERO."+'\033[0m')
  
else:
    print('\033[1;34m'+"O caractere digitado é um CARACTERE ESPECIAL."+'\033[0m')