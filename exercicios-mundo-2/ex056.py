# Desenvolva um programa que leia o nome, idade e sexo 
# de 4 pessoas. No final do programa, mostre:
# A media de idade de grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos
soma = 0
maior_idade = 0
quantidade_mulher_menor20 = 0
for pessoas in range(1,5):
    print("----- {}ª Pessoa -----".format(pessoas))
    nome_pessoa = str(input("Nome: "))
    idade_pessoa = int(input("Idade: "))
    sexo_pessoa = str(input("Sexo [M/F]: "))
   
    if sexo_pessoa != "M" and sexo_pessoa != "F":
        sexo_pessoa = str(input("Sexo [M/F]: "))
    else:
        soma += idade_pessoa

        if sexo_pessoa == 'M' and idade_pessoa > maior_idade:
            nome_homem_mais_velho = nome_pessoa
            maior_idade = idade_pessoa
        
        if sexo_pessoa == 'F' and idade_pessoa < 20:
            quantidade_mulher_menor20 += 1 

media_idade = soma/4

print("A média de idade do grupo é de {} anos".format(media_idade))
print("O homem mais velho tem {} anos e se chama {}".format(maior_idade,nome_homem_mais_velho))
print("Ao todo são {} mulheres com menos de 20 anos".format(quantidade_mulher_menor20))
    