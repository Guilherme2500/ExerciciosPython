a = float(input('Digite o valor da primeira reta'))
b = float(input("Digite o valor da segunda reta"))
c = float(input("Digite o valor da terceira reta"))

if a == b == c and a < b + c and b < a + c and c < a + b:
    print('É um triangulo equilátero')
elif a == b or b == c or a == c and a < b + c and b < a + c and c < a + b:
    print('É um triangulo Isósceles')
elif a != b != c and a < b + c and b < a + c and c < a + b:
    print('É um triangulo escaleno')
else:
    print('Não é um triangulo')
