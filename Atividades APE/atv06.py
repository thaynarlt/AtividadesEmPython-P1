#Faça um programa que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.
#1 Dolar = R$5,24 
saldo = float(input('Digite o seu saldo'))
dolar = saldo/5.19
print('O seu saldo é equivalente a US${:.2f}'.format(dolar))