IdadeSoma = 0
SexoSoma = 0
nomehomem = ''
idadehomem = 0
for pessoa in range (1, 5):
    print('----- {}º PESSOA ------'.format(pessoa))
    nome = str(input('Nome '))
    idade = int(input('Idade '))
    sexo = str(input('Sexo [M/F] '))
    IdadeSoma += idade
    media = IdadeSoma / pessoa
    if idade < 20 and sexo == 'F':
        SexoSoma += 1
    if pessoa == 1 and sexo == 'M':
        idadehomem = idade
        nomehomem = nome
    if idade > idadehomem and sexo == 'M':
        idadehomem = idade
        nomehomem = nome
print('{} mulher/mulheres tem menos de 20 anos'.format(SexoSoma))
print('A média de idade do grupo é {:.2f}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomehomem, idadehomem))
