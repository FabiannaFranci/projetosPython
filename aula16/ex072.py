extenso = ('zero', 'um', ' dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Escolha um número entre 0 e 20 e eu mostrarei ele em extenso: '))
    while escolha not in range(0,20):
        escolha = int(input('ERRO. Escolha um número entre 0 e 20 e eu mostrarei ele em extenso: '))
    print(f'Você digitou o número {extenso[escolha]}')

    continuacao = str(input('Você quer continuar? [S/N] '))[0]
    while continuacao not in 'SNsn':
        continuacao = str(input('Você quer continuar? [S/N] '))[0]
    if continuacao in 'Nn':
        break
print('Programa finalizado')
