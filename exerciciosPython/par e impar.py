x = int(input())

pares = []
impares = []
for c in range(x):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort(reverse=True)

for p in pares:
    print(p)

for i in impares:
    print(i)