#Faça um programa que, para um grupo de N pessoas (obs: N será lido):
#• Leia o sexo (M ou F) de cada pessoa;
#• Calcule e escreva o percentual de homens;
#• Calcule e escreva o percentual de mulheres.

quant_pessoas = int(input('\033[34m'+"Digite a quantidade de pessoas: "+'\033[0m'))

masc= 0
fem = 0

for i in range(quant_pessoas):
    sexo = str(input("Digite o sexo: ")).upper()
    if sexo == 'M':
        masc =+ i
    elif sexo == 'F':
        fem =+ i

percentm = (masc/quant_pessoas) * 100
percentf = (fem/quant_pessoas) * 100

print("O percentual de homens é: "+ '\033[1;32m'+"{:.1f}%".format(percentm) +'\033[0m'+" e o percentual de mulheres é: " +'\033[1;32m'+"{:.1f}%".format(percentf)+'\033[0m')
