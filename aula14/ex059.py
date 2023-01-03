mult = []
n3 = '0'
n1 = int(input('Escolha um primeiro número: '))
n2 = int(input('Escolha um segundo número: '))
while n3 not in '5':
    print('--------------------')
    n3 = str(input('''Qual opção?
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA '''))
    if n3 == '1':
        print('Soma deu {}'.format(n1 + n2))
    elif n3 == '2':
        print('A multiplicação deu {}'.format(n1 * n2))
    elif n3 == '3':
        if n1 == n2 == n1:
            print('Valores iguais')
        else:
            mult += n1, n2
            print('O maior número é {}'.format(max(mult)))
    elif n3 == '4':
        n1 = int(input('Escolha um primeiro número: '))
        n2 = int(input('Escolha um segundo número: '))
print('Programa encerrado')
