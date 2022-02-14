x = int(input("Digite um programa entre 0 e 1000 "))
centena = x//100
dezena = (x % 100)//10
unidade = x % 10

if x >= 100:
    print("Esse número tem {} centena(s), {} dezena(s) e {} unidade(s).".format(centena, dezena, unidade))
if x < 100:
    print("Esse número tem {} dezena(s) e {} unidade(s).".format(dezena, unidade))
