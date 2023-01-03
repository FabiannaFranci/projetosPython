import math
n = int(input('Escreva um número: '))
n2 = n%2
if n2 == 0:
    print('{}É par!{}'.format('\033[1;32m', '\033[m'))
else:
    print('{}Não é par!{}'.format('\033[1;31m', '\033[m'))
