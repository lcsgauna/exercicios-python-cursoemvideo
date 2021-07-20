# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu IMC e mostre seus status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo de peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = int(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? "))

imc = peso/pow(altura,2)

print("O IMC dessa pessoa é de {:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso normal")
elif imc >= 18.5 and imc <= 25:
    print("Parabéns, você está na faixa de peso ideal")
elif imc > 25 and imc <= 30:
    print("Você está em Sobrepeso")
elif imc > 30 and imc <= 40 :
    print("Você está em obesidade")
elif imc > 40:
    print("Você está em obesidade morbida, cuidado!")

