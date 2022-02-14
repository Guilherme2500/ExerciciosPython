x =int(input('Digite um número'))
tot = 0
for c in range(1,x + 1):
  if x % c == 0:
    print('\033[33m', end=' ')
    tot += 1
  else:
    print('\033[31m', end=' ')
  print('{}'.format(c),end=' ')
print('\n\033[mO {} foi divisível {} vezes'.format(x,tot),end=' ')
if tot == 2:
  print('\nE por isso, ele é primo')
else:
  print('\nE por isso, ele não é primo')



