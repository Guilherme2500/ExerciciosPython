x = int(input('Digite um número para ver sua tabuada'))
cont = 0
for c in range(x,x*11,x):
    cont += 1
    print('{} x {} = {}'.format(x,cont,c))