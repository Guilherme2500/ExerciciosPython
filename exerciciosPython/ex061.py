x = int(input("Digite o primeiro termo da progressão"))
razao = int(input("Digite a razao de sua progressão aritmética"))
c = x
while c < razao*10:
    c += razao
    print(c-razao, end=" => ")
termos = int(input("Deseja ver mais termos? Se sim, diga quantos. Se não, digite 0"))
