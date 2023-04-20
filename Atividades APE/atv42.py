#Faça um programa que leia um número inteiro e determine se ele é par ou
#ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar
#(digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve
#repetir tudo de novo, caso contrário o programa deve ser encerrado.

while True:
    num = int(input("Digite um número inteiro: "))
    if num == 0:
        print("Fim dos dados de entrada")
        break
    if num%2 ==0:
        par = 'Par'
        print(f"O número é {par}")
    else:
        impar = 'Impar'
        print(f"O número é {impar}")
    print("Para continuar basta digitar outro número novamente, caso queira terminar o programa digite 0.")