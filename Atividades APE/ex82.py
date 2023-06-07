#5. Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua média e seu conceito.
#O programa deve conter as seguintes funções:
#• Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua média (aritmética).
#• Uma função que receba como parâmetro a média do aluno e retorne o seu conceito, de acordo com a tabela abaixo:

#   MÉDIA       |   CONCEITO
#  >= 8,0       |     A
#>= 5,0 e < 8,0 |     B
#   < 5,0       |     C

#média aritmética:
def media(n1,n2,n3):
    media=(n1+n2+n3)/3
    return media

def conceito(media):
    if media >=8:
        conceito = 'A'
    elif media >=5 and media <8:
        conceito = 'B'
    elif media <5:
        conceito= 'C'
    return conceito
nt1=float(input('Digite sua primeira nota: '))
nt2=float(input('Digite sua segunda nota: '))
nt3=float(input('Digite sua terceira nota: '))


atrib = media(nt1,nt2,nt3)
print(f'A média aritmética das notas é: {atrib}')

atrib2 = conceito(atrib)
print(f'A média aritmética das notas é: {atrib2}')

