n1 = float(input("Digite a nota da primeira prova:"))
n2 = float(input("Digite a nota da segunda prova:"))
n3 = float(input("Digite a nota da terceira prova:"))

media = (n1 + n2 + n3)/3

if media >=7:
    print("A média aritmética das três notas desse aluno é: {:.1f} e ele está APROVADO".format(media))
elif media >= 4:
    print("A média aritmética das três notas desse aluno é: {:.1f} e ele está NA FINAL".format(media))
else:
    print("A média aritmética das três notas desse aluno é: {:.1f} e ele está REPROVADO".format(media))

