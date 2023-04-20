#Faça um programa que leia a idade de várias pessoas visitantes de um show (a
#leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
#• A média de idade do público;
#• A porcentagem de pessoas com idade entre 18 e 21 anos;
#• Idade do visitante mais jovem.
idades = [] #criou a lista para armazenar as idades
idade = int(input("Digite a idade:"))
while idade != 0:
    idades.append(idade) #adicionou a idade digitada na lista
    idade = int(input("Digite a idade:")) #quando eu digito 0 ele pula para fazer as somas das idades armazenaadas
    
# Calcula a média de idade do público
soma_idades = sum(idades) #soma das idades
quantidade_pessoas = len(idades) #quantidade de pessoas 
media_idade = soma_idades / quantidade_pessoas

print("A média de idade do público é:", media_idade)

# Calcula a porcentagem de pessoas com idade entre 18 e 21 anos
idades_18_21 = [idade for idade in idades if 18 <= idade <= 21] #aqui ele vai olhar na lista, um por um, qual idade atende aos requisitos 18<= idade <=21
quantidade_18_21 = len(idades_18_21) #armazenou o valor da idade que atende aos requisitos
porcentagem_18_21 = (quantidade_18_21 / quantidade_pessoas) * 100 #calcula a porcentagem

print(f"{porcentagem_18_21:.2f}% das pessoas têm entre 18 e 21 anos")

# Calcula a idade do visitante mais jovem
idade_jovem = min(idades) #identifica a idade mais jovem

print("A idade do visitante mais jovem é:", idade_jovem)