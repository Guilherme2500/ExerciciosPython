numero = int(input('Digite um número inteiro'))
print('''Escolha uma das bases para conversão:
      [1] Converter para Binário
      [2] Converter para Octal
      [3] Converter para Hexadecimal''')
opção = int(input('Qual opção você escolheu?'))

if opção == 1:
    print(bin(numero)[2:])
elif opção == 2:
    print(oct(numero)[2:])
elif opção == 3:
    print(hex(numero)[2:])





