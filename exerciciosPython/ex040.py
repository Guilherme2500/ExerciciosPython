nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
media = (nota1 + nota2)/2
if media < 5:
    print('\033[1;31mVocê tirou {} e está reprovado!!'.format(media))
elif 5 <= media < 7:
    print('\033[1;32mVocê tirou {} e está de recuperação!!'.format(media))
else:
    print('\033[1;34m Você tirou {} e está aprovado!!'.format(media))






