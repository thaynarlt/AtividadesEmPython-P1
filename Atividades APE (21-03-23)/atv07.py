#O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Faça um programa que leia o peso do prato montado pelo cliente (em quilos) e exiba o valor a pagar. Assuma que a balança já desconte o peso do prato.
#1kg de refeição = R$ 25,00

kgc = float(input("Digite o valor do peso de seu prato em Quilos:"))

prato = kgc * 25

print(" O total a pagar é: {:.2f}".format(prato))