termos = int(input('Quantos termos de Fibonacci voce gostaria de mostrar?'))
t1 = 0
t2 = 1
print(' {} > {}'.format(t1, t2), end = ' > ')
c = 0
while c <= termos:
    t3 = t1 + t2
    print ('{}'.format(t3), end = ' > ')
    t1 = t2
    t2 = t3
    c += 1
print ('FIM', c , termos)

