from datetime import date
nascimento = int(input('Qual ano que você nasceu?: '))
ano = date.today().year
resultado = ano - nascimento
resultado2 = resultado - 18
resultado3 = 18 - resultado
if resultado < 18:
    print('Fique tranquilo! Ainda não chegou sua hora de se alistar no exército, faltam {} anos'.format (resultado3))
elif resultado == 18:
    print('Ta esperando o que? vá logo se alistar!')
else:
    print('Faz tempo que você deveria ter se alistado, já se passaram {} anos'.format(resultado2))
