import math
cop = float(input("Digite o comprimento do cateto oposto"))
cadj = float(input("Digite o comprimento do cateto adjacente"))
hip = math.hypot(cop,cadj)
print("O comprimento da hipotenusa vale {:.2f}.".format(hip))
