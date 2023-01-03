cont = 0
n = int(input('Quanto você vai sacar?'))
ced = 50
total = n
while True:
    if total >= ced:
        total -= ced
        cont += 1


    else:
        print(f'total de {cont} de cédulas de {ced}')

        if total >= 20:
            ced = 20
            cont += 1

        elif total >= 10:
            ced = 10
            cont += 1

        elif total < 10:
            ced = 1
        cont = 0

        if total == 0:
            break
