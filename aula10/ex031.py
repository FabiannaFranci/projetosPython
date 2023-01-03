d = float(input('Quantos quilometros dará a sua viagem?: '))
if d <=200:
    print('Sua viagem ficará por {}R${:.2f}{}'.format('\033[4;34m',d*0.50, '\033[m'))
else:
    print('Como sua viagem é longa, ela custará {}R${:.2f}{}'.format('\033[4;37m', d*0.45, '\033[m'))
