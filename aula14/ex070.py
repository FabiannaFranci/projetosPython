a = b = precomaisbarato = cont = 0
nomedoprecomaisbarato = ' '

while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: R$'))
    a += preco
    cont += 1
    if preco >= 1000:
        b += 1
    if cont == 1:
        precomaisbarato = preco
    else:
        if preco < precomaisbarato:
            precomaisbarato = preco
            nomedoprecomaisbarato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?')).upper().strip()
    if continuar == 'N':
        break
print(f'''O total gasto na compra é de R${a}
{b} produtos custaram mais de R$1000
O produto mais barato é {nomedoprecomaisbarato} e custa R${precomaisbarato}''')