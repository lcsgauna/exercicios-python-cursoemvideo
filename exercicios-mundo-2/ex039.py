# Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar 
# - Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta 
# ou que passou do prazo

from datetime import date
anoDeNascimento = int(input("Ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento

if idade > 18:
    tempo = idade - 18
    anoAlistamento = anoAtual-tempo
    print("Quem nasceu em {} tem {} em {}".format(anoDeNascimento,idade, anoAtual))
    print("Você já deveria ter se alistado há {} anos".format(tempo))
    print("Seu alistamento foi em {}".format(anoAlistamento))
elif idade < 18:
    tempo = 18 - idade
    anoAlistamento = anoAtual + tempo
    print("Quem nasceu em {} tem {} em {}".format(anoDeNascimento,idade, anoAtual))
    print("Seu alistamento será em {}".format(anoAlistamento))
else:
    print("É o momento do seu alistamento militar")