print('{:=^40}'.format('LOJAS MARTINS'))
preço = float(input('Digite o preço da sua compra R$'))
print('''Formas de Pagamento:
 [1] à vista dinheiro/cheque
 [2] à vista cartão
 [3] 2x no cartão
 [4] 3x ou mais no cartão''')
opção = int(input('Digite sua escolha'))

if opção == 1:
    print('O novo preço do produto será de R${}'.format(preço - (10/100)*preço))
elif opção == 2:
    print('O novo preço do produto será de R${}'.format(preço - (5/100)*preço))
elif opção == 3:
    parcela = preço/2
    print('O valor da compra será em 2x de R${}, totalizando R${}'.format(parcela, preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas?'))
    print('O valor da compra será em {} parcelas de R${:.2f}'.format(parcelas,((20/100)*preço + preço)/parcelas))
    print('O preço final é R${}'.format((20/100)*preço + preço))
else:
    print('Opção inválida de pagamento. Tente novamente!')

