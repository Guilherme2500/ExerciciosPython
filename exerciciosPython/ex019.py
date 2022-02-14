import random
a = str(input("Primeiro aluno"))
b = str(input("Segundo aluno"))
c = str(input("Terceiro aluno"))
d = str(input("Quarto aluno"))
lista =[a,b,c,d]
print("O aluno sorteado foi {}.".format(random.choice(lista)))