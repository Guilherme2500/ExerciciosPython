fatorial = 1
x = int(input("Digite um número para saber o seu fatorial"))
while x > 1:
    fatorial = fatorial * x
    x -= 1
print(fatorial)
