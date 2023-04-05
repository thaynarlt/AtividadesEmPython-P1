#7.Escreva um programa que leia o peso (kg) e a altura (m) de uma pessoa, determine e mostre o seu grau de obesidade, de acordo com a tabela seguinte. 
# O grau de obesidade é determinado pelo índice de massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa pelo quadrado da sua altura.
# IMC

peso = float(input("Digite o valor de seu peso em kg: "))
altura = float(input("Digite o seu tamanho em metros: "))

imc = peso/ (altura * altura)

if imc >= 30:
    print("O valor do seu IMC é: {:.1f}, e você está com Obesidade".format(imc))
elif imc >= 25 and imc <30:
    print("O valor do seu IMC é: {:.1f}, e você está com Sobrepeso".format(imc))
elif imc >= 18.5 and imc <30:
    print("O valor do seu IMC é: {:.1f}, e você está com Peso Normal".format(imc))
elif imc <18.5:
    print("O valor do seu IMC é: {:.1f}, e você está com Baixo Peso!".format(imc))