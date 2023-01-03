primeiro = int(input('Primeiro termo da sua P.A: '))
razao = int(input('Escreva sua razão: '))
b = primeiro
c = 1
while c <= 10:
    c += 1
    print(b, end=' > ')
    b += razao
print('FIM')
