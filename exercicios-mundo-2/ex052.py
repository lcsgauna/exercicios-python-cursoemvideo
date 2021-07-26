# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))
total = 0
for buscar_numeros_primos in range(1,numero+1):
    if numero % buscar_numeros_primos == 0:
        print('\033[33m',end='')
        total += 1
    else:
        print('\033[31m',end='')

    print('{} '.format(buscar_numeros_primos),end='')

print("\n\033[mO número {} foi divisivel {} vezes".format(numero,total))
if total == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele não é primo")
