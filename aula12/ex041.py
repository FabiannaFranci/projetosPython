from datetime import date
ano = int(input('Qual sua data de nascimento? '))
atual = date.today().year
resultado = atual - ano
if resultado < 9:
    print('Você tem {} anos, considerado como MIRIM'.format(resultado))
elif resultado <= 14:
    print('Você tem {} anos, considerado como INFANTIL'.format(resultado))
elif resultado <= 19:
    print('Você tem {} anos, considerado como JUNIOR'.format(resultado))
elif resultado <= 25:
    print('Você tem {} anos, considerado como SENIOR'.format(resultado))
elif resultado > 25:
    print('Você tem {} anos, considerado como MASTER'.format(resultado))