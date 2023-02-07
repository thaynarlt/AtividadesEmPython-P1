idade = int(input('\033[7;34;40mDigite sua idade:\033[m'))
if idade <= 60:
    print('Você tem {}{}anos{}, ainda não está velho.'.format('\033[1;34;40m', idade, '\033[m'))
else:
    print('Parece que você está ficando um pouco velho...')
    
