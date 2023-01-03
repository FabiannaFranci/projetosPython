num = int(input('Primeiro termo da sua P.A: '))
razao = int(input('Razão da sua P.A: '))
c = mais = 0
termo1 = num
while c <= 10:
    c += 1
    print(termo1, end=' > ')
    termo1 += razao
    mais = c
while mais != 0:
    mais = int(input('Quantos termos a mais você gostaria? '))
    if mais > 0:
        for mais in range (mais):
            print(termo1, end=' > ')
            termo1 += razao
print('FIM')

'''OUUUU RESOLUÇÃO DO CURSO EM VIDEO
primeiro = int(input('Primeiro termo da sua P.A: '))
razao = int(input('Escreva sua razão: '))
b = primeiro
c = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        c += 1
        print(b, end=' > ')
        b += razao
    mais = int(input('Quantos mais termos: '))
print('FIM, foram aprestando {} termos'.format(mais + total))'''

