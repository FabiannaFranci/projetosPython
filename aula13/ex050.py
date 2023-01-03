s = 0
l = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        l += 1
print('A soma de todos os {} números pares foi {}'.format(l, s))
