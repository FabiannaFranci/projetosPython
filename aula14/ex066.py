a = b = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    a += 1
    b += n
print(f'Foram digitados {a} números e a soma entre eles é de {b}')