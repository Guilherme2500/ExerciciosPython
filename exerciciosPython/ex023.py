x =int(input("Digite um número de 0 a 9999"))
unidade = x//1 % 10
dezena = x//10 % 10
centena = x//100 % 10
milhar = x// 1000 % 10
print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(unidade,dezena,centena,milhar))

