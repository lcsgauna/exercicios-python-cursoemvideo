# Faça um programa que leia um número inteiro e mostre
# na tela o seu sucessor e seu antecessor

valor = int(input("Digite um número: "))
antecessor = valor-1
sucessor = valor+1
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(
    valor, antecessor, sucessor))
