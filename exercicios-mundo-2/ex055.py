# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0
for pessoas in range(1,6):

    peso_pessoas = float(input("Peso da {}ª pessoa: ".format(pessoas)))

    if(pessoas == 1):
        maior_peso = peso_pessoas
        menor_peso = peso_pessoas
    else:
        if(peso_pessoas>maior_peso):
            maior_peso = peso_pessoas
        if(peso_pessoas<menor_peso):
            menor_peso = peso_pessoas
    

print("O maior peso lido foi de {}Kg ".format(maior_peso))
print("O menor peso lido foi de {}Kg ".format(menor_peso))