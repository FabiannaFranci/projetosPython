preço = float(input('Qual o preço do produto?: R$'))
pagamento = str(input('''Qual a forma de pagamento?: 
[1] À vista ou em dinheiro
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão 
Opção: '''))
if pagamento == '1':
    print('O preço era R${:.2f} e pagando à vista você ganha 10% de desconto e pagará R${:.2f}'.format(preço, (preço*90)/100))
elif pagamento == '2':
    print('O preço era R${:.2f} e pagando a vista no cartão você ganha 5% de desconto e pagará agora R${:.2f}'.format(preço, (preço*95)/100))
elif pagamento == '3':
    total = preço/2
    print('O preço era R${:.2f} e ficará 2x de {:.2f} no cartão'.format (preço, total))
elif pagamento == '4':
    parcela = int(input('Quantas parcelas?: '))
    total = (preço*120)/100
    totalparcela = total/parcela
    print(' o preço era R${:.2f} e pagando {}x no cartão vocÊ pagará 20% de juros, então ficará R${:.2f} cada parcela'.format(preço, parcela, totalparcela))
    print('Sua compra de R${:.2f} reais vai acabar custando R${:.2f}'.format(preço, total))
else:
    print('Opção inválida, tente novamente!')