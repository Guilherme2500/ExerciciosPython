x = int(input('Digite o primeiro número'))
y = int(input('Digite o segundo número'))
if x > y:
    print('O número {} é o maior'.format(x))
elif y > x:
    print('O número {} é o maior'.format(y))
else:
    print('Os números {} e {} são iguais'.format(x, y))
