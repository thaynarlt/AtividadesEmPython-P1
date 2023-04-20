#Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10
#metros e cresce 3 centímetros por ano. Faça um programa que calcule e
#imprima quantos anos serão necessários para que Zé seja maior que Chico.

chico_alt = 1.50
ze_alt = 1.10
cresc_chico = 0.02
cresc_ze =0.03
anos = 0

while ze_alt <= chico_alt: #enquanto zé é menor que chico. |ele faz o while varias vezes ate zé ser mais alto que chico
    chico_alt += cresc_chico #1.50 = 1.50 + 0.02
    ze_alt += cresc_ze #1.10 = 1.10 + 0.03
    anos += 1 #anos =anos +1

print(f"Serão necessários {anos} anos para que Zé seja maior que Chico.")