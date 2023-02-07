nasc = int(input('\033[7;30;47mDigite o ano em que nasceu:\033[m'))
fut = int(input('\033[7;30;47mDigite o ano em que estamos:\033[m'))
idade = fut - nasc
print('De acordo com os dados que nos forneceu você possui, ou irá fazer, {}{}anos{}'.format('\033[1;34;40m', idade,'\033[m'))
