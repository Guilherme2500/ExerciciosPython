import random
from time import sleep
print('\033[1;34mPEDRA,PAPEL E TESOURA!!!\033[m')
print('\033[1;31mVamos jogar!!Quero ver se me vence!\033[m')
item = input('\033[1;36mQual você escolheu?\033[m')
x = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('\033[1;31mPEDRA, PAPEL E TESOUUUUURAA!!...\033[m')
sleep(2)
print('\033[1;32mEu escolhi {}!\033[m'.format(x))
if item == 'tesoura' and x == 'Papel':
    print('\033[1;34mVoce venceu!!!')
elif item == 'pedra' and x == 'Papel':
    print('\033[1;31mVoce perdeu!!!Tente novamente!!')
elif item == 'tesoura' and x == 'Pedra':
    print('\033[1;31mVocê perdeu !!! Tente novamente!!')
elif item == 'pedra' and x == 'tesoura':
    print('\033[1;31mVocê venceu!!!')
elif item == 'papel' and x == 'Tesoura':
    print('\033[1;31mVoce perdeu!!Tente novamente!!')
elif item == 'papel' and x == 'Pedra':
    print('\033[1;34mVoce venceu!!!')
else:
    print('\033[1;33mOcorreu um empate!!! Jogue novamente para desempatar!!')






