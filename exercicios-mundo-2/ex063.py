# Escreva um programa que leia um número n inteiro
# qualquer e mostre na tela os n primeiros elementos
# de uma Sequência de Fiobonacci.
# E: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar? '))
primeiro_termo = 0
segundo_termo = 1
print('{} -> {} '.format(primeiro_termo,segundo_termo),end='')
contador = 3
while contador <= termos:
    fibonacci = primeiro_termo+segundo_termo
    print(' -> {}'.format(fibonacci), end='')
    primeiro_termo = segundo_termo
    segundo_termo = fibonacci
    contador += 1
print(' -> FIM')