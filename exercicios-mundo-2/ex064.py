# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar 
# o valor 999, que é a condição de parada. No final, mostre 
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)
num=0
cont = 0
soma=0
while num != 999:
    num = int(input("Informe um numero: "))
    cont+=1
    soma = soma+num

print("Foram digitados {} numeros e a soma deles é {} ".format(cont,soma-999))