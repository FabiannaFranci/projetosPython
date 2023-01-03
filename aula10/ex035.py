r1 = float(input('Qual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanho da terceira reta? '))

if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print('{}Você consegue formar um triângulo!{}'.format('\033[4;32m', '\033[m'))
else:
    print('{}Você não consegue formar um triângulo{}'.format('\033[4;31m', '\033[m'))
