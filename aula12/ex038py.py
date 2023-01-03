n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo {}'.format(n1, n2))
elif n1 < n2:
    print('O segundo valor {} é maior que o primeiro {}'.format(n2, n1))
else:
    print('Os valores são iguais'.format(n1, n2))