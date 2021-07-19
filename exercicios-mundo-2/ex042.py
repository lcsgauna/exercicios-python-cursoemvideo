# Refaça o exercicio 035 dos triângulos, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

primeiroSegmento = float(input("Primeiro segmento: "))
segundoSegmento = float(input("Segundo segmento: "))
terceiroSegmento = float(input("Terceiro segmento: "))

if(primeiroSegmento<segundoSegmento+terceiroSegmento) and (segundoSegmento<primeiroSegmento+terceiroSegmento) and (terceiroSegmento<primeiroSegmento+segundoSegmento):
    
    if primeiroSegmento != segundoSegmento and primeiroSegmento != terceiroSegmento and segundoSegmento != terceiroSegmento:
        triangulo = "Escaleno"
    elif primeiroSegmento != segundoSegmento or primeiroSegmento !=  terceiroSegmento or segundoSegmento != terceiroSegmento:
        triangulo = "Isósceles"
    else:
        triangulo = "Equilátero"

    print("Os segmentos acima podem formar um triângulo {}".format(triangulo)) 
else:
    print("Os segmentos acima não podem formar triângulo")
