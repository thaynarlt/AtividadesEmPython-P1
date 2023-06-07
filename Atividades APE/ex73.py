#2. Faça um programa que leia uma frase e a exiba criptografada. O método de criptografia será
#baseado na seguinte regra: trocar alguns caracteres por outros, conforme a tabela abaixo:

#CARACTER ORIGINAL | CARACTER CRIPTOGRAFADO
#       A          |        branco
#       E          |           U
#       I          |           O
#       O          |           I
#       U          |           E
#     branco       |           A
#Exemplo: "BOA NOITE" criptografado fica "BI ANIOTU"

frase=input('Digite uma frase para criptografarmos: ').upper()

print('Frase criptografada:')
for i in frase:
    if i == 'A':
        print(' ', end='')
    if i =='E':
        print('U', end='')
    if i =='I':
        print('O', end='')
    if i =='O':
        print('I', end='')
    if i =='U':
        print('E', end='')
    if i ==' ':
        print('A', end='')
    if i not in 'AEIOU ':
        print(i, end='')


    
