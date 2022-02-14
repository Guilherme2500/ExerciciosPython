matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


for l in range(0, 4):
   for c in range(0, 4):
        matriz[l].append(int(input(f"Digite um número para a posição ({l}:{c})")))


print("\033[1;34mMatriz 4X4\033[m")

for l in range(0, 4):
    for c in range(0, 4):
        print(f"[{matriz[l][c]:^5}]", end="")
        print()

