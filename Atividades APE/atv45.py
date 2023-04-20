#O cardápio de uma casa de lanches, especializada em sanduíches, é dado a seguir.

#CÓDIGO | NOME |PREÇO
#H -> Hamburger -> R$ 5,00
#C -> Cheese Burger -> R$ 6,00
#B -> Cheese Bacon -> R$ 7,00
#F -> Cheese Frango -> R$ 4,00

#Faça um programa que leia o código e a quantidade de cada item comprado
#por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao
#final, calcule e exiba o total a pagar.

#Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2 Cheese Bacon:

#Entrada:
#    Código: H
#    Quantidade: 3
#    Código: B
#    Quantidade: 2
#    Código: X
#Saída:
#    Total a pagar: R$ 29.00

total = 0
while True:
    codigo = input("Digite o código da refeição: ").upper()
    if codigo == 'X': 
        print("Fim das compras!")
        break
    quantidade = int(input("Digite a quantidade comprada: "))
    H=5
    C=6
    B=7
    F=4
        
    if codigo == 'H':
        total = quantidade * H

    elif codigo == 'C':
        total = quantidade * C

    elif codigo == 'B':
        total = quantidade * B

    elif codigo == 'F':
        total = quantidade * F
  
print(f"O total que deve ser pago é: R${total}.")