#3. Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo abaixo.
#Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
#Exemplo:
#Entrada: FLAVIO RIBEIRO COUTINHO
#Saída: COUTINHO, F. R.

nome = input('Digite o seu nome completo: ').upper()

partes_nome = nome.split()

ultimo_nome = partes_nome[-1]

iniciais = []
for parte in partes_nome[:-1]:
    primeira_letra = parte[0]
    iniciais.append(primeira_letra)

string_lista = ', '.join(iniciais)    
print(f'{ultimo_nome.upper()}, {string_lista}.')

