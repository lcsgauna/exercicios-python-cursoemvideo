# Faça um programa que leia um número
# qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1=120
fatorial = 1
numero = int(input('Digite um numero para calcular seu Fatorial: '))
indice = numero
print('Calculando {}! = '.format(numero), end='')
while indice > 0:
    print('{}'.format(indice),end='')
    print(' x ' if indice > 1 else ' = ', end='')
    fatorial *= indice
    indice -=1

print('{}'.format(fatorial))