from random import randrange
n = int(input('Qual número eu estou pensando?: '))
n2 = randrange(0, 5)
if n == n2:
    print ('Você acertou!')
else:
  print ('Você errou! eu pensei no {}'.format (n2))

