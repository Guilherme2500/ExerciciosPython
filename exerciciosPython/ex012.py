produto = float(input("Digite o valor do seu produto R$"))
desconto = (5/100)*produto
preço = produto - desconto
print("Com a promoção, o produto agora está custando R${:.2f} reais.".format(preço))

