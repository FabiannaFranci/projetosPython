casa = float(input('Qual o preço da casa? '))
anos = int(input('Em quantos anos você quer ter pago essa prestação? '))
salario = float(input('Quanto você ganha mensalmente? '))
parcela = casa / (anos*12)
excedeu = (salario*30)/100
if parcela == excedeu or parcela > excedeu:
    print('Infelizmente, a parcela mensal de R${:.2f} excedeu os 30% do seu salário mensal de R${:.2f}, então o seu empréstimo foi negado'.format(parcela, salario))
else:
    print ('Com seu salário de R${:.2f}, a sua parcela mensal ficará R${:.2f}. Sendo assim o seu empréstimo de R${:.2f} será aprovado'.format(salario, parcela, casa))
