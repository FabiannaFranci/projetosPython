nome = str(input('Escreve seu nome: ')).strip()
dividido = nome.split()
print ('O seu primeiro nome é {}.\nO seu último sobrenome é {}.'.format (dividido[0], dividido[-1]))