nome = str(input('Escreva um nome: '))
c = {'limpa': '\033[m',
         'ciano': '\033[1;36m',
         'roxo': '\033[1;35m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m'}
dividido = nome.split()
print('Seu nome em maiúsculo é {}{}{}'.format(c['ciano'], nome.upper(), c['limpa']))
print('Seu nome em minúsculo é {}{}{}'. format(c['roxo'], nome.lower(), c['limpa']))
print('Seu nome tem ao todo {}{}{} letras'.format(c['amarelo'], len(nome.replace(' ', '')), c['limpa']))
print('Seu primeiro nome é {}{}{} e tem {}{}{} letras'.format(c['vermelho'], dividido[0], c['limpa'], c['vermelho'], len(dividido[0]), c['limpa']))


