#Crie um programa que leia quanto dinheiro uma pessoa
#tem na carteira e mostre quantos dolares ela pode comprar


real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = 3.27
reaisEmDolares = real/dolar
print("Valor do Dólar: {}".format(dolar))
print("Com R${} você pode comprar ${:.2f}".format(real,reaisEmDolares))