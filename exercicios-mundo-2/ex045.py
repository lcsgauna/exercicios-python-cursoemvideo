# Crie um program que faça o computador jogar Jokenpo com você
from random import randint
from time import sleep
jogada_do_usuario = int(input("""Suas opções: 
                     [ 0 ] Pedra
                     [ 1 ] Papel
                     [ 2 ] Tesoura
                     Qual é a sua jogada? """))

jogada_do_computador = randint(0, 2)
opcoes_de_jogada = ['Pedra', 'Papel', 'Tesoura']

if jogada_do_usuario == 0 or jogada_do_usuario == 1 or jogada_do_usuario == 2:
    print("JO")
    sleep(1)
    print("Ken")
    sleep(1)
    print("Po!!\n")

    print("-="*11)
    print("Computador jogou {}".format(opcoes_de_jogada[jogada_do_computador]))
    print("Jogador jogou {}".format(opcoes_de_jogada[jogada_do_usuario]))
    print('-='*11)

    if opcoes_de_jogada[jogada_do_computador] == 'Pedra' and opcoes_de_jogada[jogada_do_usuario] == 'Papel':
        print("Jogador venceu")
    elif opcoes_de_jogada[jogada_do_computador] == 'Papel' and opcoes_de_jogada[jogada_do_usuario] == 'Tesoura':
        print("Jogador Venceu")
    elif opcoes_de_jogada[jogada_do_computador] == 'Tesoura' and opcoes_de_jogada[jogada_do_usuario] == 'Pedra':
        print("Jogador Venceu")
    elif opcoes_de_jogada[jogada_do_computador] == opcoes_de_jogada[jogada_do_usuario]:
        print("Empatou")
    else:
        print("Computador Venceu")

else:
    print("Opção inválida, tente novamente")