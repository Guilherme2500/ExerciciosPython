sexo = str(input('Digite seu sexo(m para masculino e f para feminino) '))
while sexo != 'f' and sexo != 'm':
    sexo = str(input('Dados inválidos! Por favor digite novamente'))
if sexo == 'f' or 'm':
         print('Seu sexo {} foi registrado!'.format(sexo.upper()))


