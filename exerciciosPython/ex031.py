distancia = float(input("Digite a distância de sua viagem"))

if distancia<=200:
    print('Você terá que pagar \033[32mR${:.2f}\033[m de passagem'.format(distancia*0.5))
else:
    print('\033[7;37mVocê terá que pagar \033[34mR${:.2f} \033[7;37mde passagem\033[m'.format(distancia*0.45))