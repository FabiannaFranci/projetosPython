nome = str(input('Escreva seu nome completo: ')).strip()
print('Seu nome tem Silva? {}{}{}!'.format ('\033[7;35m','SILVA' in nome.upper(),'\033[m'))
