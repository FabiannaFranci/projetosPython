s = float(input('Qual o seu salário? '))
mu = {'negrito': '\033[4m', 'limpa': '\033[m'}
s2 = (s*110)/100
s3 = (s*115)/100
if s > 1250.00:
    print('O seu salário era {}R${:.2f}{} e agora será {}R${:.2f}{}'.format(mu['negrito'],s, mu['limpa'], mu['negrito'], s2, mu['limpa']))
else:
    print('O seu salário era {}R${:.2f}{} e agora será {}R${:.2f}{}'.format(mu['negrito'], s,mu['limpa'], mu['negrito'], s3, mu['limpa']))
