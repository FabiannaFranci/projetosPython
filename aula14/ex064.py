b = a = c =  0
while c != 999:
    c = int(input('Escreva um número:'))
    if c != 999:
        b += c
        a += 1
print('Foram digitados {} número ate 999 e a soma entre eles foi de {}'.format(a, b))



