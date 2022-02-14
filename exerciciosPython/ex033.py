x = float(input("Digite o primeiro número"))
y = float(input("Digite o segundo número"))
z = float(input("Digite o terceiro número"))
maior = x
if y > maior:
    maior = y
if z > maior:
    maior = z
menor = x
if y < menor:
    menor = y
if z < menor:
    menor = z
print('O maior número é o \033[36m{:.0f}\033[m e o menor número é o \033[32m{:.0f}\033[m'.format(maior,menor))
