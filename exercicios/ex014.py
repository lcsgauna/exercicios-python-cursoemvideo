# Escreva um programa que converta uma temperatura
# digitada em ºC e converta para ºF

temperaturaCelsius = float(input("Informe a temperatura em ºC: "))
temperaturaFahrenheit = (temperaturaCelsius*1.8)+32
print("A temperatura de {}ºC corresponde a {:.1f}ºF".format(temperaturaCelsius,temperaturaFahrenheit))