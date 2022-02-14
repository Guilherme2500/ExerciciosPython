speed = float(input('Digite a velocidade do seu carro'))
limite = 80
multa = (speed - limite)*7

if speed <= limite:
    print('\033[0;34mVelocidade permitida. Tenha um bom dia!')
else:
    print('\033[31mVocê está acima do limite de velocidade!\033[m')
    print('Você terá que pagar \033[31mR${}\033[m reais!'.format(multa))
