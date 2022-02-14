soma = 0
cont =0
for c in range(0,500,3):
    if c % 2 == 1:
        cont = cont + 1
        soma += c
print('O somatório dos {} valores é igual a {}'.format(cont,soma))
