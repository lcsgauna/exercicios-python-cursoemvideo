# Crie um programa que leia dois valores e mostre
# um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do programa
# Sua operação deverá realiza a operação solicitada
# em cada caso.
opcao = 0
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
while opcao != 5:
    opcao = int(input('Informe a sua opcao: '))
    if opcao == 1:
        soma = primeiro_numero + segundo_numero
        print('A soma de {} + {} = {}'.format(primeiro_numero,segundo_numero,soma))
    elif opcao == 2:
        multiplicacao = primeiro_numero*segundo_numero
        print('O resultado da multiplicacao de {} x {} = {} '.format(primeiro_numero,segundo_numero,multiplicacao))
    elif opcao == 3:
        maior = 0
        if(primeiro_numero==segundo_numero):
            print('Os numeros são iguais')
        else:
            if(primeiro_numero>segundo_numero):
                maior = primeiro_numero
        
            if(segundo_numero>primeiro_numero):
                maior = segundo_numero
            
            print('O numero maior entre os dois é {}'.format(maior))
    elif opcao == 4:
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))
    elif opcao == 0 or opcao > 5:
        print('Opção incorreta, tente novamente')

print('Programa Finalizado')