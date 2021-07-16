# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

primeiroNumero = int(input("Primeiro número: "))
segundoNumero = int(input("Segundo número: "))

if primeiroNumero>segundoNumero:
    print("O primeiro valor é maior")
elif segundoNumero>primeiroNumero:
    print("O segundo valor é maior")
else: 
    print("Os dois valores são iguais")  