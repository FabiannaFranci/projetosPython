peso = float(input('Quanto você pesa? (Kg): '))
altura = float(input('Qual sua altura? (m): '))
IMC = peso/altura**2
if IMC < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo da média'.format(IMC))
elif IMC < 25:
    print('Seu IMC é {:.1f} e você está no peso ideal'.format(IMC))
elif IMC < 30:
    print('Seu IMC é {:.1f} e você está acima do peso'.format(IMC))
elif IMC < 40:
    print('Seu IMC é {:.1f} e você está obeso'.format(IMC))
elif IMC > 40:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida'.format(IMC))

