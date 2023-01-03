soma = 0
soma2 = 0
from datetime import date
atual = date.today().year
for c in range(1, 8):
    nascimento = int(input('Em qual ano a {}ª pessoa nasceu?:'.format(c)))
    idade = atual - nascimento
    if idade >= 21:
        soma += 1
    else:
        soma2 += 1
print ('{} pessoas já atingiram a maioridade e {} são ainda são menores de idade'.format(soma, soma2))
