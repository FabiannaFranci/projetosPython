pessoas = []
for c in range (1,4):
    a = float(input('Qual o peso da {}ª pessoa?'.format(c)))
    pessoas += [a]
print('a pessoa mais pesada tem {}kg e a mais leve tem {}kg'.format(max(pessoas), min(pessoas)))
print(pessoas)