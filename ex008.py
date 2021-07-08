medidaEmMetros = float(input("Uma distância em metros: "))
medidaEmKm = medidaEmMetros / 1000
medidaEmHm = medidaEmMetros / 100
medidaEmDam = medidaEmMetros / 10
medidaEmDm = medidaEmMetros * 10
medidaEmCm = medidaEmMetros * 100
medidaEmMm = medidaEmMetros * 1000
print("Medida em metros {:g}m corresponde a: ".format(medidaEmMetros))
print("Medida em km: {}km".format(medidaEmKm))
print("Medida em hm: {}hm".format(medidaEmHm))
print("Medida em dam: {}dam".format(medidaEmDam))
print("Medida em dm: {:g}dm".format(medidaEmDm))
print("Medida em cm: {:g}cm".format(medidaEmCm))
print("Medida em mm: {:g}mm".format(medidaEmMm))