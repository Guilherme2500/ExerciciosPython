from datetime import date
ano = int(input('Digite o ano do seu nascimento'))
idade = date.today().year - ano
if idade < 18:
    print('Você tem {} anos e ainda irá se alistar no serviço miltar'.format(idade))
    print('\033[1;32mFaltam apenas {} anos'.format(18 - idade))
    print('Seu alistamento será no ano de {}!\033[m'.format(date.today().year + (18 - idade)))
elif idade == 18:
    print('\033[1;34mVocê completa 18 anos nesse ano!!! Chegou a hora de você se alistar no serviço militar')
else:
    print('\033[1;31mSeu tempo de alistamento ja passou!!')
    print('Você está atrasado {} anos'.format(idade - 18))
    print('Seu alistamento foi no ano de {}!'.format(date.today().year - (idade - 18)))
