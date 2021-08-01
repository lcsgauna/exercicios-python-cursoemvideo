# Melhore o jogo do Desafio 028 onde o computador
# vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites forma necessários para vencer
from random import randint
palpites = 0
computador = randint(0,11)
tentativa_adivinhacao = 0
while tentativa_adivinhacao != computador:    
    palpites += 1
    tentativa_adivinhacao = int(input("Informe seu {}º palpite: ".format(palpites))) 
    
print("Você acertou, o número era {}".format(computador))
print("Foram necessários {} palpites para vencer".format(palpites))