# Faça um programa que leia um número
# qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1=120
fatorial = 0
numero = int(input('Digite um numero: '))

while numero > 0:
    fatorial = numero * numero - 1 
    print(fatorial)
    numero = numero - 1 
print('O fatorial de {} é {} '.format(numero,fatorial))