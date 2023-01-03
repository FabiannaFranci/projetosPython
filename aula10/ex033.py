import operator
n = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
r1 = max(n, n2, n3)
r2 = min(n, n2, n3)
print('O maior número é {}\nO menor número é {}'.format(r1, r2))

