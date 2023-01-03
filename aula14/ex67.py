n = ''
while True:
    print('-'*40)
    n = int(input("Qual tabuada você gostaria de ver? "))
    print('-'*40)
    if n < 0:
        break
    for c in range (0, 11):
        mult = n * c
        print (f'{n} x {c} = {mult}')
print('encerrado')

