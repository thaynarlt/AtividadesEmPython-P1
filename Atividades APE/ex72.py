#1. Faça um programa que leia o email de uma pessoa e mostre, separadamente, qual o login e qual o domínio.
#Por exemplo, suponha que o email seja "fulano@provedor.com.br", então o login será "fulano"
#e o domínio será "provedor.com.br".

email = input('Digite o seu email:').lower()

if "@" in email:
    partes = email.split("@") #vai dividir a partir do @
    login = partes[0]
    dominio = partes[1]

print(f'Login: {login}')
print(f'Domínio: {dominio}')