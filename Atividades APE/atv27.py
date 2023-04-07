# 4. Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando
# apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
# O programa deve mostrar o resultado obtido.

h1 = int(input('\033[1;34m'+"Digite a hora (inteira) inicial do jogo:"+'\033[0m'))
h2 = int(input('\033[1;34m'+"Digite a hora (inteira) final do jogo:"+'\033[0m'))

TOT = 24


if h1 >= h2:
    duracao = (TOT - h1) + h2
    print('\033[1;32m'+f"A duração foi de: {duracao} horas"+'\033[0m')
else:
    duracao = h2 - h1
    print('\033[1;32m'+f"A duração foi de: {duracao} horas"+'\033[0m')
