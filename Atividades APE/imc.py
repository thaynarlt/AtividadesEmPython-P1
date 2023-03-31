peso = float(input("Digite o valor de seu peso em kg: "))
altura = float(input("Digite o seu tamanho em metros: "))

imc = peso/ (altura * altura)

if imc >= 39.9 and imc >= 35:
    print("O valor do seu IMC é: {:.1f}, e você está com Obesidade de Grau II".format(imc))
elif imc >= 30 and imc <=34.9:
    print("O valor do seu IMC é: {:.1f}, e você está com Obesidade de Grau I".format(imc))
elif imc >= 25 and imc <=29.9:
    print("O valor do seu IMC é: {:.1f}, e você está com Sobrepeso".format(imc))
elif imc >= 18.5 and imc <=24.9:
    print("O valor do seu IMC é: {:.1f}, e você está com Peso Normal".format(imc))
elif imc <=18.5:
    print("O valor do seu IMC é: {:.1f}, e você está Abaixo do Peso!".format(imc))