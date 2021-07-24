# Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

primeiro_termo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão da progressão aritmética: "))
ultimo_termo = primeiro_termo+10

for progressao_aritmetica in range(primeiro_termo,ultimo_termo,razao):
    print(progressao_aritmetica)