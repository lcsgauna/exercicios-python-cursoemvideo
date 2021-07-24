# Faça um programa que calcule a soma entre todos os
# números impares que são múltiplos de três e que se 
# encontram no intervalo de 1 até 500.
for numeros in range(1,501):
    if (numeros % 2 != 0) and (numeros%3 == 0) :
        print(numeros)