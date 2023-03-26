#As Ilhas Weblands formam um reino independente nos mares do Pacífico. Como é um reino recente, 
#a sociedade é muito influenciada pela informática. A moeda oficial é o Bit; existem notas de B$ 50, B$ 10, B$ 5 e B$ 1. 
#Você foi contratado(a) para ajudar na programação dos caixas automáticos de um grande banco das Ilhas Weblands.
#Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas disponíveis, mantendo um estoque para cada valor de cédula. 
#Os clientes do banco utilizam os caixas eletrônicos para efetuar retiradas de um certo número inteiro de Bits. Sua tarefa é escrever um programa que, 
#dado o valor de Bits desejado pelo cliente, determine o número de cada uma das notas necessário para totalizar esse valor, 
#de modo a minimizar a quantidade de cédulas entregues. Exemplo: Para B$ 72 seriam as seguintes notas:
#- 1 nota de B$ 50
#- 2 notas de B$ 10
#- 0 notas de B$ 5
#- 2 notas de B$ 1

valord = int(input("Digite a quantidade de Bits desejada: "))

resto1 = valord // 50 # =1
resto2 = valord % 50

nota1 = resto2 // 10 # = 2
resto3 = resto2 % 10  

nota3 = resto3 // 5 # = 0
resto4 = resto3 % 5

nota4 = resto4 // 1 # =2


print("O valor digitado corresponde a:\n {} cédulas de 50,\n {} cédulas de 10, \n {} cédulas de 5 e \n {} cédulas de 1".format(resto1, nota1, nota3, nota4))
