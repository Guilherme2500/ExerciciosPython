import random
from time import sleep
cont = 0
print("\033[1;33mVou pensar em um número entre 0 e 10. Tente adivinhar!")
number = int(input('\033[1;32mEm que número você pensou? '))
x = random.choice([0,1,2,3,4,5,6,7,8,9,10])
print('\033[7;36mPROCESSANDO...\033[m')
sleep(2)
cont += 1
while number != x:
    print('\033[1;31mParece que você perdeu HAHAHAHA!!!! Eu digitei o número {}!\n Tenta de novo!!!'.format(x))
    number = int(input('\033[1;32mEm que número você pensou? '))
    x = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print('\033[7;36mPROCESSANDO...\033[m')
    sleep(2)
    cont += 1
if number == x:
    print('\033[7;34mVocê venceu!!!!!!Parabéns!!!\033[m')
    print('\033[1;33mVocê precisou jogar {} vezes para acertar\033[m'.format(cont))




