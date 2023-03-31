#4.Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem "Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", 
# de acordo com o sexo da pessoa. Obs: Fulano e Fulana são nomes exemplos.

nomef = str(input("Digite o seu nome: "))
nomel = str(input("Digite o seu sexo, se Feminino = F e Masculino = M: "))

if nomel == "F":
    print("Olá Sra. {}".format(nomef))
elif nomel == "M":
    print("Olá Sr. {}".format(nomef))