x = float(input("Digite um valor em metros"))
km = x/1000
hm = x/100
dm = x/10
dc = x*10
cen = x*100
mil = x*1000
print("A medida de {}m corresponde a".format(x))
print("{}km,{}hm,{}dm,{}dc,{}cm,{}mil".format(km,hm,dm,dc,cen,mil))