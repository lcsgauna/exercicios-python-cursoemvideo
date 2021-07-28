# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
menor_idade = 0
maior_idade = 0

for pessoas in range(1,8):
    ano_nascimento = int(input('Em que ano a {}º pessoa nasceu: '.format(pessoas)))
    ano_atual =  date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 18 :
        menor_idade += 1
    else:
        maior_idade += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(maior_idade))
print("E também tivemos {} pessoas menores de idade".format(menor_idade))