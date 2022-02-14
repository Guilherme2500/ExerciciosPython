casa = float(input('Qual o valor da sua casa? R$'))
dinheiro = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você irá pagar a casa?'))

prestação = casa / (anos * 12)

if prestação > (30/100)*dinheiro:
    print('Você não poderá comprar esta casa, pois a prestação de {:.2f} excede 30% do seu salário de {:.2f}'.format(prestação,dinheiro))
else:
    print('Você terá que pagar R${:.2f} por {} anos até completar o valor final da casa'.format(prestação,anos))