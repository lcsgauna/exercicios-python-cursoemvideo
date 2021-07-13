# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela 
# se o usuário venceu ou perdeu.

from random import randint
numeroRandomico = randint(0,5)
print("Dica: {}".format(numeroRandomico))
numero = int(input("Digite um número: "))

if(numero == numeroRandomico):  
    print("Você acertou !")
else: 
    print("Você errou, tente novamente")

