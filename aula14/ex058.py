palpite = 0
from random import randrange
jogador = int(input('Digite um número: '))
pc = randrange(1, 10)
while jogador != pc:
    palpite += 1
    jogador = int(input('Errou, Digite novamente: '))
print('Acertou.\nO número escolhido foi {}, mas você demorou {} vezes para acertar'.format(pc, palpite))

