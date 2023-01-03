from random import choices
a1 = str(input('Diigite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: ' ))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = a1, a2, a3, a4
escolhido = choices(lista)
print('O aluno sorteado para apagar o quadro foi {}{}{}'.format('\033[7m', escolhido, '\033[m'))

