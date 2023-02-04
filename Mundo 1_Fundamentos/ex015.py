#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar,sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado
kmc = float(input('Digite a quantidade de Km percorridos'))
dal = int(input('Digite a quantidade dias em que o carro foi alugado'))
d = dal * 60
km = kmc * 0.15
tot = d + km
print('O total que deve ser pago pelos dias alugados e os kms rodados é R${:.2f}'.format(tot))