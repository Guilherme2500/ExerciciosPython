escolha = "S"
contagem = soma = media = maior = menor = 0
while escolha != "N":
    x = int(input("Digite um numero"))
    escolha = (input("Deseja continuar? [S/N]")).upper().strip()[0]
    contagem += 1
    soma += x
    if contagem == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
media = soma/contagem
print("Você digitou {} numero(s) e a media é de {}\n O maior foi {} e o menor foi {}".format(contagem, media, maior, menor))