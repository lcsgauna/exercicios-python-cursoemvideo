# Faça um programa que leia um ano qualquer
# e mostre se ele é Bissexto.
from datetime import date, datetime
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0 :
    ano = datetime.today().year

if(ano%400 == 0) or (ano%4==0) and (ano%100!=0):
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))