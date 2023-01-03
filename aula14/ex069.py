a = b = c = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if idade >= 18:
        a += 1
    if sexo in 'mM':
        b += 1
    if idade < 20 and sexo in 'Ff':
        c += 1
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Quer continuar?: ')).upper().strip()
    if continuar == 'N':
        break
print(f'''Total de pessoas com mais de 18: {a}
Total de homens cadastrados: {b} 
Total de mulheres com menos de 20 anos: {c}''')
