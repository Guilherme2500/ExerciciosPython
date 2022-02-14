nome = str(input('Qual o seu nome?'))
if nome == 'Guilherme':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome  == 'Paulo':
    print('Seu nome é bem popular no Brasil!!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else: #opicional
    print('Que nome normal!!!')
print('Tenha um bom dia {}!!!'.format(nome))