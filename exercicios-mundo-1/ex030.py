# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou IMPAR.
numeroEscolhido = int(input("Me diga um número: "))

if numeroEscolhido % 2 == 0:
    print("O número {} é PAR".format(numeroEscolhido))
else:
    print("O número {} é IMPAR".format(numeroEscolhido))