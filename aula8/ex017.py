from math import hypot, trunc
cores = {'limpa': '\033[m',
'azul': '\033[1;34m'}
ca = float(input('Quanto vale o cateto adjacente? '))
co = float(input('Quanto vale o cateto oposto? '))
h = hypot(ca, co)
print('A hipotenusa vale {}{}{}'.format(cores['azul'], trunc(h), cores['limpa']))
