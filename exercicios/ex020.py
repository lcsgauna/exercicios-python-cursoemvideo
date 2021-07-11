# O mesmo professor do desofio anterior quer sorter a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos
# e mostre a ordem sorteada

from random import shuffle

primeiroAluno = str(input("Primeiro aluno: "))
segundoAluno = str(input("Segundo aluno: "))
terceiroAluno = str(input("Terceiro aluno: "))
quartoAluno = str(input("Quarto aluno: "))

ordem = [primeiroAluno,segundoAluno,terceiroAluno,quartoAluno]
shuffle(ordem)

print("A ordem de apresentação será \n {}".format(ordem))
