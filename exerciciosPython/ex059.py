
x = int(input("Digite um número"))
y = int(input("Digite outro número"))

menu = int(input("""\033[1;34mSelecione a opção desejada
                 [1] Somar
                 [2] Multiplicar
                 [3] Maior
                 [4] novos números
                 [5] sair do programa\033[m """))
while menu != 5:
    if menu == 1:
        print("A soma entre eles é de {}".format(x + y))
        menu = int(input("Digite uma nova opção"))
    elif menu == 2:
        print("{} multiplicado por {} é igual a {}".format(x, y, x * y))
        menu = int(input("Digite uma nova opção"))
    elif menu == 3:
        if x > y:
            print("O {} é o maior".format(x))
        else:
            print("O {} é o maior".format(y))
        menu = int(input("Digite uma nova opção"))
    elif menu == 4:
        x = int(input("Digite um número"))
        y = int(input("Digite outro número"))
        menu = int(input("""\033[1;34mSelecione a opção desejada
                     [1] Somar
                     [2] Multiplicar
                     [3] Maior
                     [4] novos números
                     [5] sair do programa\033[m """))
if menu == 5:
    print("Fim!")
