c = ''
a = b = 0
d = []
while c != 2:
    num = int(input('Digite um número: '))
    print('-----------------')
    c = int(input('''Quer continuar?
        [1] SIM
        [2] NÂO '''))
    a += num
    b += 1
    d += [num]
    if c != 1 and c != 2:
        print('Tente novamente')
print('Programa encerrado, a média dos números foi de {:.2f}, o maior {} e o menor {}'.format(a/b, max(d), min(d)))
