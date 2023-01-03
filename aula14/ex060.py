from time import sleep
h = 1
a = 0
c = int(input('Escreva um número: '))
print('Calculando fatorail de {}!'.format(c))
sleep(1)
for b in range(c, 0, -1):
    h *= b
    print(b, end='')
    print(' x ' if b > 1 else ' = ', end='')
print(h)

''' FORMA COM O WHILE SÓ Q MEIO SEM NOÇÃO
print('{} '.format(h))
c = int(input('Escreva um número: '))
print('Calculando fatorial de {}!'.format(c))
b = c
h = 1
while b > 0:
    print('{}'.format(b), end='')
    print(' x ' if b > 1 else ' = ', end='')
    h *= b
    b -= 1
print('{} '.format(h))'''

