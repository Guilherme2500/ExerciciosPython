participants, price, hotels, weeks = map(int, input().split())
lista = []
min_price = 0
for c in range(hotels):
    price_hotel = int(input())
    lista.append(list(map(int, input().split()))) # lista com o número de camas
for v in range(weeks):
    if '' >= participants:
        min_price = min_price * participants


if min_price > price:
    print("Stay home")
else:
    print(min_price)