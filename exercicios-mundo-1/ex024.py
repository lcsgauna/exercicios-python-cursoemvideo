# Crie um programa que leia o nome e uma cidade e diga se ela
# começa ou não com a palavra "Santo"

cidade = str(input("Em que cidade você nasceu? ")).strip()
possuiPalavraSanto = 'SANTO' in cidade.upper()
#print(cidade[:5].upper()=='SANTO')
print("Cidade possui palavra Santo? {}".format(possuiPalavraSanto))