# Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.
print("-=-"*20)
print("Analisador de Triângulos")
print("-=-"*20)
primeiroSegmento = float(input("Primeiro segmento: "))
segundoSegmento = float(input("Segundo segmento: "))
terceiroSegmento = float(input("Terceiro segmento: "))
if(primeiroSegmento<segundoSegmento+terceiroSegmento) and (segundoSegmento<primeiroSegmento+terceiroSegmento) and (terceiroSegmento<primeiroSegmento+segundoSegmento):
    print("Os segmentos acima podem formar triângulo")
else:
    print("Os segmentos acima não podem formar triângulo")