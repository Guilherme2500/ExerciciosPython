nome = input('Digite seu nome completo')
primeiro = nome.split()
último = nome.rsplit()
print('Primeiro = {}\nSegundo = {}'.format(primeiro[0],último[-1]))

