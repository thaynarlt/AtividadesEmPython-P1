# Crie um programa que leia quanto dinheiro uma pessoa tem
#na carteira e mostre quantos dólares ela pode comprar
# considere US$ 1,00 = R$5,19
saldo = float(input('Digite o seu saldo'))
dolar = saldo/5.19
print('O seu saldo é equivalente a US${:.2f}'.format(dolar))