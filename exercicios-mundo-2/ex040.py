# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final. de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado
primeiraNota = float(input("Primeira Nota: "))
segundaNota = float(input("Segunda Nota: "))
media = (primeiraNota+segundaNota)/2

print("Tirando {:.1f} na primeira nota e {:.1f} na segunda nota a média do aluno é {:.1f}".format(primeiraNota,segundaNota,media))

if media > 7:
    print("O aluno está aprovado")
elif media < 5:
    print("O aluno está reprovado")
else:
    print("O aluno está de recuperação")