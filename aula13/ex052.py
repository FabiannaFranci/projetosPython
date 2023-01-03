total = 0
numero = int(input('digite um numero'))
for primo in range (1, numero +1):
    a = numero % primo == 0
    total += a
if total > 2:
    print('NÃO é primo, pois foi divisível {} vezes'.format(total))
else:
    print ('o numero é primo, pois foi dividivisel {} vezes'.format(total))

