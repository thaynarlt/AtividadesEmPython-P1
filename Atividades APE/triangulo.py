a = float(input("Digite o valor do 1º lado (positivo e maior que zero): "))
b = float(input("Digite o valor do 2º lado (positivo e maior que zero): "))
c = float(input("Digite o valor do 3º lado (positivo e maior que zero): "))

#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

if a<b+c and b<c+a and c<a+b:                       #Para ser um triângulo é preciso que a soma de dois lados seja maior que o lado restante.
    if (a == b and b == c):                         #se os 3 lados são iguais então ele é equilátero
        print("É um triângulo EQUILÁTERO.")
    else:
        if (a == b or a==c or c==b):                #se pelo menos dois lados são iguais então ele é isósceles
            print("É um triângulo ISÓSCELES.")
        else:
            print("É um triâgulo ESCALENO.")        # e se ele não atende a nenhum fator dos acima, então seus 3 lados são diferentes, ou seja, é escaleno
else: 
    print("Os lados apresentados não formam um triãngulo!")