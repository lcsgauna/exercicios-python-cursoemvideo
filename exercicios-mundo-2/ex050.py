# Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.
soma_numeros_pares=0
for numero in range(0,5):
    numero = int(input("Informe um número: "))
    if(numero%2==0) or numero == 0:
        soma_numeros_pares += numero

print("A soma dos numeros somente pares é {} ".format(soma_numeros_pares))