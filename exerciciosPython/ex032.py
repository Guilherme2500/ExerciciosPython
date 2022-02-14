from datetime import date
ano = int(input('Digite um ano para ser analisado. Coloque 0 para ver o número atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

