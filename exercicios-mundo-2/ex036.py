# Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado

valorImovel = float(input("Qual o valor do imóvel? R$"))
valorSalario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento "))

parteSalario = valorSalario * (30/100)  
valorParcelas = valorImovel/(anos*12)

print("30% do salario {}".format(parteSalario))
print("Valor das parcelas R${:.2f} em {:.1f}anos".format(valorParcelas,anos))

if valorParcelas > parteSalario:
    print("Empréstimo Negado")
else:
    print("Empréstimo Aprovado")
