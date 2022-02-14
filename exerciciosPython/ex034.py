salário = float(input('Digitem seu salário'))
if salário <= 1250:
    print('Você ganhou um aumentou de 15% e seu novo salário é de \033[32mR${:.2f}\033[m.'.format(salário*(15/100) + salário))
else:
    print('Você ganhou um aumento de 10% e seu novo salário é de \033[32mR${:.2f}\033[m.'.format(salário*(10/100) + salário))
