peso = float(input('Digite seu peso'))
altura = float(input('Digite sua altura'))
IMC = peso/altura**2
print('Seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('\033[1;31mAbaixo do peso')
    print(f"Você precisa aumentar seu IMC em {18.5 - IMC}")
elif 18.5 < IMC < 25:
    print('\033[1;32mPeso ideal')
elif 25 < IMC < 30:
    print('\033[1;34mSobrepeso')
elif 30 < IMC < 40:
    print('\033[1;33mObesidade')
elif IMC > 40:
    print('\033[1;31mObesidade Mórbida')
