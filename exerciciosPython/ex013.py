salário = float(input("Digite seu salário R$"))
desconto = (15/100)*salário
aumento = salário + desconto
print("Você recebeu um aumento e seu novo salário agora é de R${:.2f} reais".format(aumento))


