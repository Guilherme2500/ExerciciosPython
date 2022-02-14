soma = 0
maior = 0
totmulher = 0
nomemaisvelho = ''
for c in range(1, 5):
    nome = input('Digite seu nome')
    idade = int(input('Digite sua idade'))
    sexo = input('Digite seu sexo')
    soma += idade
    if sexo in 'Mm'and c == 1:
       maior = idade
       nomemaisvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
print('O homem mais velho tem {} anos e se chama {}'.format(maior,nomemaisvelho))
print('A média de todas as idades é igual a {}'.format(soma/4))
print('A quantidade de de mulheres menores de 20 anos é igual a {}'.format(totmulher))






