x = int(input("Digite um número inteiro"))
t1 = 0
t2 = 1
print("{} => {}".format(t1,t2), end="")
c = 3
while c <= x:
    soma = t1 + t2
    c += 1
    t1 = t2
    t2 = soma       
    print(" => {}".format(soma), end="")