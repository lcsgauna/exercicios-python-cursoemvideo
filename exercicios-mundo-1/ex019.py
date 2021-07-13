# Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

from random import choice

primeiroAluno = str(input("Primeiro aluno: "))
segundoAluno = str(input("Segundo aluno: "))
terceiroAluno = str(input("Terceiro aluno: "))
quartoAluno = str(input("Quarto aluno: "))
alunos = [primeiroAluno,segundoAluno,terceiroAluno,quartoAluno]
alunoSorteado = choice(alunos)
print("O aluno escolhido foi: {}".format(alunoSorteado))