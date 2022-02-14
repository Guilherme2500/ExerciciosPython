from datetime import date
atual = date.today().year
cont = 0
totmaior = 0
totmenor = 0
for c in range(0,7):
    cont += 1
    ano = int(input('Em que ano a {}° pessoa nasceu?'.format(cont)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Existem {} pessoas que ja atingiram a maioridade'.format(totmaior))
print('Existem {} pessoas que ainda não atingiram a maioridade'.format(totmenor))




