precosMercado = ('Leite', 6.98, 'Açucar 1kg', 3.59, 'Caderno', 10.59, 'Escova de dente', 4.99)

print('='*10, 'Promoções da Semana', '='*10)

for c in range(0, len(precosMercado), 2):
    print(f'{precosMercado[c]:.<35}R${precosMercado[c+1]}')