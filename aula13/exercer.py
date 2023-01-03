idade1 = 0
for pessoa in range (1, 4):
    print('----- {}º PESSOA ------'.format(pessoa))
    idade = int(input('Idade'))
    idade1 += idade
    media = idade1 / pessoa
print(media)
