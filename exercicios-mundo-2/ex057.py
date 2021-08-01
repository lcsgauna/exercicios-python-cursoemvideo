# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente
# até ter um valor correto.
sexo_invalido = True
while sexo_valido:
    sexo = str(input("Informe o sexo: "))
    if(sexo == 'M' or sexo == 'F'):
        sexo_valido = False
    
print('Programa Finalizado')