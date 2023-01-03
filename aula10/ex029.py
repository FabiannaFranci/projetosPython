v = int(input('Quantos km/h o carro está andando?: '))
v2= (v-80)*7
if v <= 80:
    print('Sem multa hoje')
else:
    print('Você correu {}km, então sua multa ficará no valor de R${}'.format(v, v2))