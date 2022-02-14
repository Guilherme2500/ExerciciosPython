import math
x = float(input("Digite o valor do ângulo"))
print("O angulo de {} tem seno de {:.2f}.\n O angulo {} tem cosseno de {:.2f}.\n O angulo {} tem tangente de {:.2f}.".format(x,math.sin(math.radians(x)),x,math.cos(math.radians(x)),x,math.tan(math.radians(x))))