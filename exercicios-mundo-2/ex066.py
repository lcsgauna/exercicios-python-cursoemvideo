# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números forma
# digitados e qual foi a soma entre eles(desconsiderando o flag)
valor = 0
contador = 0
soma = 0
while valor != 999:
    valor = int(input('Digite um valor (999 para parar)'))
    contador += 1
    soma += valor

contador-=1
soma = soma-999

print('A soma dos {} valores foi {}'.format(contador,soma))