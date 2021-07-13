# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiusculas
# - O nome com toas as letras minusculas
# - Quantas letras ao todo(sem considerar espaços)
# - Quantas letras tem o primeiro nome

nomeCompleto = str(input("Digite seu nome completo: ")).strip()
separarNomeCompleto = nomeCompleto.split()
print("Analisando seu nome...")
print("Seu nome completo em maiúsculas é {}".format(nomeCompleto.upper()))
print("Seu nome completo em minúsculas é {}".format(nomeCompleto.lower()))
print("Seu nome tem ao todo {} letras".format(len(nomeCompleto) - nomeCompleto.count(' ')))
#print("Seu primeiro nome é {} e ele tem {} letras".format(nomeCompleto[0:nomeCompleto.find(' ')], nomeCompleto.find(' ')))
print("Seu primeiro nome é {} e ele tem {} letras".format(separarNomeCompleto[0], len(separarNomeCompleto[0])))