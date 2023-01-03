'''sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Digite seu Sexo [M/F]: ')).upper().strip()
    if sex != 'M' and sex != 'F':
        print('Erro, digite novamente o sexo')
    else:
        print('Sexo {} registrado com sucesso'.format(sex)) O MESMO CÓDIGO MAS DE OUTRA FORMA'''

sex = str(input('Informe um sexo [M/F]')).strip().upper()
while sex not in 'MfFm':
    sex = str(input('Inválido, Digite seu sexo [M/F]')).strip()
print('Seu sexo é {}'.format(sex))
