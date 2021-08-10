# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.
soma = 0
resposta = ''
contador = 0
maior = 0
menor = 10
while resposta != 'N':
    numero = int(input('Digite um numero: '))
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    
    soma += numero
    contador += 1 
    resposta = str(input('Deseja continuar? ')).upper()

media = soma/contador
print('Menor valor {} | Maior valor {}'.format(menor,maior))
print('A soma dos numeros é {} e sua média é {:.2f}'.format(soma,media))