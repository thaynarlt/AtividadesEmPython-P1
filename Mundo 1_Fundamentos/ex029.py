#Escreva um programa que leia a velocidade de um carro.
# -Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# -A multa vai custar R$7,00 por cada Km acima do limite.
velo = int(input('Digite a velocidade do carro'))
multa = velo * 7
max = 80
if velo >= max:
    print('Você ultrapassou 80km/h, MULTADO!')
    print('O valor da multa é {}'.format(multa))
else:
    print('Você não ultrappasou 80km, continue assim!')
    
