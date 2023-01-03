p = str(input('Escreva uma frase e eu direi se ela é um polindromo ou não: ')).replace(' ', '')
r = p[::-1]
print('{} ao contrário fica {}'.format(p, r))
if p == r:
    print('É um palindromo')
else:
    print('Não é um palíndromo')
