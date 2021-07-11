# Crie um programa que leia um número real qualquer pelo teclado e 
# mostre na tela a sua porção inteira
# Ex: valor = 6.127 porção inteira = 6

from math import trunc
valor = float(input("Digite um valor: "))
porcaoInteira = trunc(valor)
print("O valor digitado foi {} e a sua porção inteira é {}".format(valor,porcaoInteira))