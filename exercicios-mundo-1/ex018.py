# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo


from math import radians,cos, sin, tan
angulo = int(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("o ângulo de {} tem o seno de {:.2f}".format(angulo, seno))
print("O ângulo de {} tem o cosseno de {:.2f}".format(angulo, cosseno))
print("O ângulo de {} tem a tangente de {:.2f}".format(angulo, tangente))