numero = int(input('Escreva um número: '))
pergunta = str(input('''Qual será a base de conversão?
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
Sua opção: '''))

if pergunta == '1':
    print(bin(numero)[2:])
elif pergunta == '2':
    print(oct(numero)[2:])
elif pergunta == '3':
    print(hex(numero)[2:])
else:
    print('Opção inválida, tente novamente')
