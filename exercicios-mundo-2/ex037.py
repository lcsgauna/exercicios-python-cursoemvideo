# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base da conversão
# - 1 para binario
# - 2 para octal
# - 3 para hexadecimal
valorDecimal = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão: 
         [ 1 ] Converter para Binário
         [ 2 ] Converter para Octal
         [ 3 ] Converter para Hexadecimal """)
opcao = int(input("Sua opção: "))

if opcao == 1:
    binario = bin(valorDecimal)
    print("Você selecionou a opção {} o valor decimal {} em binário é {}".format(opcao,valorDecimal,binario[2:]))
elif opcao == 2:
    octal = oct(valorDecimal)
    print("Você selecionou a opção {} o valor decimal {} em binário é {}".format(opcao,valorDecimal,octal[2:]))
elif opcao == 3:
    hexadecimal = hex(valorDecimal)
    print("Você selecionou a opção {} o valor decimal {} em binário é {}".format(opcao,valorDecimal,hexadecimal[2:]))
else: 
    print("Opção Inválida")

