#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
dist = float(input('Digite a distancia da viagem em Km:'))
duzentoskm = dist * 0.50
maisdedkm = dist * 0.45
if dist >= 200:
    print('Sua viagem percorre mais de 200km')
    print('O valor total da viagem é R${}'.format(maisdedkm))
else:
    print('Sua viagem percorre menos de 200km')
    print('O valor total da viagem é R${}'.format(duzentoskm))