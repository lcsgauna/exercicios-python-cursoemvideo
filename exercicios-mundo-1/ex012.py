# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto

valorProduto = float(input("Qual é o preço do produto? R$"))
valorProdutoDesconto = valorProduto - (valorProduto * (5/100))
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(valorProduto,valorProdutoDesconto))