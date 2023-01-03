from random import choice
from time import sleep
eu = str(input('Pedra, Papel ou Tesoura?: ')).lower()
lista = 'PEDRA', 'PAPEL', 'TESOURA'.lower()
pc = choice(lista).lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

if eu == pc:
    print('Eu escolhi {}! Empate! Tente novamente'.format(pc))

elif eu == 'papel' and pc == 'pedra' or eu == 'pedra' and pc == 'tesoura' or eu == 'tesoura' and pc == 'papel':
    print('Eu escolhi {} e você {}. Parabéns! Você ganhou!'.format(pc, eu))

elif pc == 'papel' and eu == 'pedra' or pc == 'pedra' and eu == 'tesoura' or pc == 'tesoura' and eu == 'papel':
    print('Eu escolhi {} e você {}. Você perdeu!'.format(pc, eu))

