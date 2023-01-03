tupla = (int(input('Digite o primeiro valor: ')),
        int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')),
        int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores {tupla}')
if 9 in tupla:
    print(f'O número 9 aparece {tupla.count(9)} vezes')
else:
    print('O número 9 não aparece nenhuma vez')
if 3 in tupla:
    print(f'O número 3 foi digitado na {tupla.index(3)} posição')
else:
    print('O número 3 não aparece na tupla')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} é par')