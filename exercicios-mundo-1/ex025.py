# Crie um programa que leia o nome de uma pessoa e diga
# se ela tem "Silva" no nome.

nomeCompleto = str(input("Qual é o seu nome completo? ")).strip()
possuiPalavraSilva = 'SILVA' in nomeCompleto.upper()
print("Seu nome possui sobrenome Silva? {}".format(possuiPalavraSilva))
#print('Seu nome tem Silva ?{}'.format('silva' in nomeCompleto.lower()))