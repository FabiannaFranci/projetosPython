n = 0
b = []
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        n += c
        b += [c]
print(' a soma de todos os {} valores solicitados é de {}'.format(len(b), n))
