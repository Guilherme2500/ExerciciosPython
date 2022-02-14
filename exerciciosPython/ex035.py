a = float(input('Digite o valor da primeira reta'))
b = float(input("Digite o valor da segunda reta"))
c = float(input("Digite o valor da terceira reta"))

if abs(b-c) < a < b + c or abs(a-c) < b < a + c or abs(a-b) < c < a + b:
    print('É um triângulo')
else:
    print('Não é um triângulo')



