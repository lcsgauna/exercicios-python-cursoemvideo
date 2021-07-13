# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta, pinta uma área de 2m²

larguraParede = float(input("Largura da parede: "))
alturaParede = float(input("Altura da parede: "))
area = larguraParede*alturaParede
litrosTinta = area/2
print("Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m²".format(larguraParede,alturaParede,area))
print("Para pintar essa parede, você precisará de {:.2f}L de tinta".format(litrosTinta))