'''precosMercado = ('Leite', 6.98, 'Açucar 1kg', 3.59, 'Caderno', 10.59, 'Escova de dente', 4.99)

print('='*10, 'Promoções da Semana', '='*10)

for c in range(0, len(precosMercado)):
    if c % 2 == 0:
        print(f'{precosMercado[c]:.<30}', end= '')
    else:
        print(f'R${precosMercado[c]}')
        , 'Dermatologicamente', 'Testado', 'Spray', 'Cabelo', 'Natural', 'Tempo')'''

ex1 = "chocolate"
ex2 = "oca"

for letra in ex2:
   if letra in ex1:
      ex1 = ex1.replace(letra,'')


print(ex1)
