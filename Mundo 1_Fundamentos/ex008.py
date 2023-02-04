# Escreva um programa que leia um valor em metros e a exiba
#convertido em centimetros e milimetros
v= float(input('Digite um valor em metro a ser convertido:'))
vcm = v*100
vmm = v*1000
print('O valor em centímetros é {:.0f}cm'.format(vcm))
print('O valor em milímetros é {:.0f}mm'.format(vmm))
