from random import randint

sorteados = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram {sorteados}')
print(f'O maior número sorteado é {max(sorteados)}')
print(f'O menor número sorteado é {min(sorteados)}')
