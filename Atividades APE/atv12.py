#Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,bem como o número de litros de combustível gastos.
#Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a capacidade do tanque e mostre:
#a) Quilometragem rodada. OK
#b) Quantos quilômetros por litro faz o veículo. OK
#c) Autonomia do veículo.
#d) Custo da viagem. OK

hodometro_antes = float(input("Digite o valor do hodômetro antes da viagem:"))
hodometro_dps = float(input("Digite o valor do hodômetro depois da viagem:"))
gasosa = float(input("Digite a quantidade de litros de combustível gastos na viagem:"))
preco_litro = float(input("Digite o preço do litro do combustível:"))
tanque = float(input("Digite a capacitade do tanque em litros:")) 





km_rodada = hodometro_dps - hodometro_antes
print("A quilometragem rodada foi: {:.1f}".format(km_rodada))

kml = km_rodada / (tanque - gasosa)
print("A quantidade de quilômetros por litro que o veículo faz é: {}".format(kml))

autonomia = km_rodada/tanque
print("A autonomia do carro é: {:.1f}".format(autonomia))

custo_viagem = preco_litro * gasosa
print("O custo da viagem foi: R${:.1f}".format(custo_viagem))
