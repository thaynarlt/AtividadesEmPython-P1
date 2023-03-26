#Escreva um programa que, dado um número inteiro representando uma quantidade de segundos, calcule quantas horas,
# minutos e segundos estão contidos nesta quantidade.
#Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.

n1 = int(input("Digite um número inteiro em segundos"))

horas = n1 / 3600
resto = n1 % 3600
min = resto / 60
seg = resto % 60

print("{:.0f} horas, {:.0f} minutos e {:.0f} segundos".format(horas, min, seg))