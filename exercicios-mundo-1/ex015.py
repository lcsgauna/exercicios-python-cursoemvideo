# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0.15 por Km rodado.

diasAlugados = int(input("Quantos dias alugados? "))
quilometrosRodados = int(input("Quantos Km rodados? "))
valorTotalPagar = (diasAlugados*60)+(quilometrosRodados*0.15)
print("O total a pagar é de R${:.2f}".format(valorTotalPagar))