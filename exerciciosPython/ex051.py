x = int(input('Digite o primero termo da progressão'))
razão = int(input('Digite o valor da razão da progressão'))
for c in range(x, razão*10 + x, razão):
    print(c, end=' => ')

