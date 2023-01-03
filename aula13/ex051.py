primeiro = int(input('Escreva o primeiro termo da sua P.A: '))
razao = int(input('Agora escreva a razão da sua P.A: '))
decimo = primeiro + 10 * razao
for c in range (primeiro, decimo, razao):
        print(c)
