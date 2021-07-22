# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento: 
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valor_do_produto = float(input("Preço das compras: R$"))
opcao = int(input("""FORMAS DE PAGAMENTO
         [ 1 ] à vista dinheiro/cheque
         [ 2 ] à vista cartão
         [ 3 ] 2x no cartão
         [ 4 ] 3x ou mais no cartão
         Qual é a opção?"""))

if opcao == 1 : 
    valor_do_produto_reajustado = valor_do_produto - (valor_do_produto*(10/100))
elif opcao == 2:
    valor_do_produto_reajustado = valor_do_produto - (valor_do_produto*(5/100))
elif opcao == 3:
    valor_do_produto_reajustado = valor_do_produto
elif opcao == 4:
    parcelas = int(input("\nQuantas parcelas? "))
    valor_do_produto_reajustado = valor_do_produto + (valor_do_produto*(20/100))
    valor_parcelado = valor_do_produto_reajustado/parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(parcelas,valor_parcelado))
else: 
    valor_do_produto_reajustado = valor_do_produto
    print("Opção inválida. Tente novamente")

print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(valor_do_produto, valor_do_produto_reajustado))

