cont = 0
maior = 0
menor = 0
for c in range(1, 6):
   cont += 1
   peso = float(input('Qual é o {}° peso?'.format(cont)))
   if c == 1:
       maior = peso
       menor = peso

   else:
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print('O maior peso é o {}Kg'.format(maior))
print('O menor peso é o {}Kg'.format(menor))


