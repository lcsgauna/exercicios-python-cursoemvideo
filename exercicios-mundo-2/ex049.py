# Refaça o desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando o laço for

numero = int(input("Digite um número para ver sua tabuada: "))
print('-'*12)

for multiplos in range(0,11):
    print("{} x {:2} = {}".format(numero,multiplos,numero*multiplos))

print('-'*12)