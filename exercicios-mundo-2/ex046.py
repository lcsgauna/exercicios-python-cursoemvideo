# Faça um programa que mostre na tela uma contagem
# regressiva para o estouro de fogos de artíficio,indo 
# de 10 até 0, com uma pausa de 1 segundo entre eles.
import emoji
import time

for contagem_regressiva in range(11):
    print(10-contagem_regressiva)
    time.sleep(1)

print(emoji.emojize(':tada::confetti_ball::tada: ', use_aliases=True))