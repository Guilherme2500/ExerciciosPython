from random import sample
a = str(input("Primeiro nome"))
b = str(input("Segundo aluno"))
c = str(input("Terceiro aluno"))
d = str(input("Quarto aluno"))
alunos = [a,b,c,d]
print("A ordem de apresentação sorteada foi {}".format(sample(alunos,4)))