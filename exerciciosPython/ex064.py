contagem = 0
limite = 999
soma = 0
x = 0
while x != 999:
    x = int(input("Digite um número [999 para parar]: "))
    contagem += 1
    soma += x
    if x == 999:
        contagem -= 1
        soma -= x


print("Você digitou {} números e a soma deles é {}".format(contagem, soma))
