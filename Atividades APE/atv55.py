#Escreva um programa para ler 6 números distintos, ou seja, não podem repetir.
#Exiba os números lidos.

numeros = []

for i in range(6):
    while True:
        num = int(input(f"Digite o {i+1}º número: "))
        if num not in numeros:
            numeros.append(num)
            break
        else:
            print("Esse número já foi digitado. Tente novamente.")

print("\nNúmeros digitados:")
print(numeros)

