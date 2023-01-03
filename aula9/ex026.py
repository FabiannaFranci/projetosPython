frase = str(input('Escreva qualquer coisa: ').replace(' ', ''))
print('A letra A aparece {} vezes nessa frase'. format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na {}º posição'.format(frase.upper().find('A')+1))
print('A letra A aperece pela ultima vez na {}º posição'.format(frase.upper().rfind('A')+1))
