n = int(input('Escreva um ano qualquer e eu direi se ele é bissexto ou não: '))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('{}É bissexto!{}'.format('\033[1;32m', '\033[m'))
else:
    print('{}Não é bissexto{}'.format('\033[1;31m', '\033[m'))
