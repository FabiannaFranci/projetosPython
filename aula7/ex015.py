d = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos quilometros o carro rodou?: '))
cd = (d*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(cd))

