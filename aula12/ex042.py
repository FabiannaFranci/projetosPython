l1 = float(input('Medida do primiero lado do triângulo: '))
l2 = float(input('Medida do segundo lado do triângulo: '))
l3 = float(input('Medida do terceiro lado do triângulo: '))

if l1+l2 > l3 and l2+l3 > l1 and l3+l1 > l2:
    print('Você pode formar um triângulo ', end = '')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print ('ISÓSCELES')

else:
    print ('Você não pode formar um triângulo!')
