from datetime import date
ano = int(input('Digite o ano de seu nascimento'))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('\033[1;36mMirim!!!')
elif 9 < idade <= 14:
    print('\033[1;35mInfantil')
elif 14 < idade <= 19:
    print('\033[1;34mJunior')
elif 19 < idade <= 25:
    print('\033[1;33mSênior!!')
elif idade > 25:
    print('\033[1;31mMaster!!!')


