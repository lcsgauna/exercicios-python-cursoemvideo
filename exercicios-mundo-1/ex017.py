# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa


from math import hypot
catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
#hipotenusa = sqrt(pow(catetoOposto,2)+pow(catetoAdjacente,2))
hipotenusa = hypot(catetoOposto,catetoAdjacente)
print("A hipotenusa mede: {:.2f}".format(hipotenusa))
