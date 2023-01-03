from random import randrange
c = 0
while True:
    eu = int(input('Digite um valor: '))
    IouP = str(input('Par ou impar? [P/I]: ')).strip().upper()
    print('-'*40)
    pc = randrange(0, 11)
    resultado = eu + pc
    print(f'Você jogou {eu} e o computador {pc}')
    print('-' * 40)
    if resultado % 2 == 0 and IouP == 'P':
        print(f'PAR. Você acertou, o resultado foi {resultado}')
        c += 1
    elif resultado % 2 != 0 and IouP == 'I':
        print(f'IMPAR. Você acertou, o resultado foi {resultado}')
        c += 1
    else:
        print(f'Você ERROU, o resultado foi {resultado}')
        break
print(f'Voce acertou {c} vezes')
