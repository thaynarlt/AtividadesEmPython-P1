#Faça um programa que leia os seguintes dados de um conjunto de alunos:
#matrícula, nome e as duas notas que ele obteve em suas avaliações. A
#condição de parada será a digitação de uma matrícula igual 0 (zero). O
#programa deverá mostrar, para cada aluno, as seguintes informações:
#matrícula, nome, média e situação (aprovado, se a média for igual ou superior
#a 7 e, reprovado, se a média for inferior a 7).

while True: #"while True" é uma construção de loop infinito que repete continuamente um bloco de código enquanto a condição "True" (verdadeiro) é satisfeita.
    matr = int(input("Digite a matrícula do aluno (0 para sair): "))
    if matr == 0:
        print("Fim dos dados de entrada")
        break
    nome = str(input("Digite o seu nome: "))
    n1 = float(input("Digite a sua primeira nota: "))
    n2 = float(input("Digite a sua segunda nota: "))
    media = (n1 + n2)/2
    if media >=7:
        sit = 'Aprovado'
    elif media <=7:
        sit = 'Reprovado'
    print("O aluno {} da matrícula {}, foi {} com a média de {}.".format(nome, matr,sit,media))