import random
from time import sleep
print("\033[1;33mVou pensar em um número entre 0 e 5. Tente adivinhar!")

number = int(input('\033[1;32mEm que número você pensou? '))
x = random.choice([0,1,2,3,4,5])
print('\033[7;36mPROCESSANDO...\033[m')
sleep(2)

if number == x:
    print('\033[7;34mVocê venceu!!!!!!Parabéns!!!\033[m')
else:
    print('\033[1;31mParece que você perdeu HAHAHAHA!!!! Eu digitei o número {}!\n Tenta de novo!!!'.format(x))
