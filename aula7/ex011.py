l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
t = l*a
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(l,a,t))
print('Para pintar essa parede voce precisará de {:.2f}L'.format(t/2))
