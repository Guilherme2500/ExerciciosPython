frase =str(input('Digite uma frase')).strip().upper()
palavra = ''.join(frase.split())
inverso = ''
for c in range(len(palavra)-1, -1, -1):
       inverso += palavra[c]
print('A frase {} ao contrário é {} '.format(palavra, inverso))
if inverso == palavra:
       print('Temos um palíndromo')
else:
       print('Não é um palíndromo')


