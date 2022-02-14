from math import sqrt
qte = int(input())
for c in range(qte):
    x1 ,y1, x2, y2, x3, y3 = map(int,input().split())
    lado1 = sqrt((x1-x2)**2 + (y1 - y2)**2)
    lado2 = sqrt((x2 - x3)**2 + (y2 - y3)**2)
    lado3 = sqrt((x1 - x3)**2 + (y1 - y3)**2)
    p = (lado1 + lado2 + lado3)/2
    area = sqrt(p*(p-lado1)*(p-lado2)*(p-lado3))
    print("{:.3f}".format(area))

