#6. Escreva um programa que, a partir da digitação do infinitivo de um verbo regular, faça a
#conjugação dele no presente do indicativo para as pessoas do singular e plural. Veja o exemplo abaixo.
#Entrada:
#CANTAR
#Saída:
#Eu canto
#Tu cantas
#Ele canta
#Nós cantamos
#Vós cantais
#Eles cantam

verbo = input('Digite o verbo: ')

tam = len(verbo)

radical = tam -2

verbo1=[]
for i in range(tam-2):
    verbo1.append(verbo[i])

string_lista = ''.join(verbo1)
for i in range(1):
    print(f'Eu {string_lista}o')
    print(f'Tu {string_lista}as')
    print(f'Ele {string_lista}a')
    print(f'Nós {string_lista}amos')
    print(f'Vós {string_lista}ais')
    print(f'Eles {string_lista}am')
