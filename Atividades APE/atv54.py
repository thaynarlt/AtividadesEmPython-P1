#Escreva um programa para ler 6 números. Após a leitura dos números, verifique,
#para cada um deles, se é distinto, ou seja, não possui repetição.

N=6
nums = []
for i in range(N):
    n = int(input("Digite um número: "))
    nums.append(n)

for n in nums:
    if nums.count(n) == 1: #Retorna a quantidade de determinado elemento na lista.
        print(n, "é distinto")
    else:
        print(n, "não é distinto")
    