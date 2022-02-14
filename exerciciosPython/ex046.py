from time import sleep
import emoji
print('\033[1;31mCONTAGEM REGRESSIVA PRO PRÓXIMO ANO!!\033[m')
sleep(1)
for c in range(10,0,-1):
    print('\033[1;33m{}'.format(c))
    sleep(1)
print(emoji.emojize('\033[1;34mFELIZ ANO NOVO!!!\033[m:fireworks:',use_aliases=True))

