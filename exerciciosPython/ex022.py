nome = str(input("Qual o seu nome?")).strip()
print(nome.upper())
print(nome.lower())
letras = print(len(''.join(nome.split())))
primeiro = nome.split()
print('seu primeiro nome tem {} letras.'.format(len(primeiro[0])))

