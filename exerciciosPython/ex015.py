km = float(input("Quantos kilômetros percorridos?"))
dias = int(input("Por quantos dias ele foi alugado?"))
preço = 60*dias + 0.15*km
print("O total a ser pago é de R${:.2f}".format(preço))
