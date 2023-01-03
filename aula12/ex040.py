nota1 = float(input('Qual foi a primeira nota:' ))
nota2 = float(input('Qual foi a segunda nota: '))
resultado = (nota1 + nota2)/2
if resultado < 5.0:
    print('Sua média foi {}. Você está reprovado!'.format(resultado))
elif 5.0 <= resultado <= 6.9:
    print('Sua média foi {}. Você está de recuperação!'.format (resultado))
elif resultado >= 7.0:
    print('Sua média foi {}. Você passou de ano, parabéns!!'.format(resultado))