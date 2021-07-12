# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza . primeiro = Ana último=Souza

nomeCompleto = str(input("Digite seu nome completo: ")).strip()
nomeCompletoSeparado = nomeCompleto.split()
print("Muito prazer te conhecer!")
print("Seu primeiro nome é {}".format(nomeCompletoSeparado[0]))
print("Seu último nome é {}".format(nomeCompletoSeparado[len(nomeCompletoSeparado)-1]))