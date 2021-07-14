# Desenvolva um programa que pergunte a distância
# de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0,50 por km para viagens de até 200km 
# e R$0,45 para viagens mais longas.
distanciaViagem = float(input("Qual é a distância da sua viagem? "))
if distanciaViagem <=200:
    preco = distanciaViagem * 0.50
else:
    preco = distanciaViagem * 0.45
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("Você está prestes a começar uma vigem de {}Km".format(distanciaViagem))
print("E o preço da sua passagem será de R${:.2f}".format(preco))
