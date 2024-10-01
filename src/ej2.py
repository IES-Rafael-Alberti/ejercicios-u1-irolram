#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

horast = int(input("Cuantas horas has trabajado: "))
precio = int(input("Cobro por hora: "))
importetotal = (horast * precio) #variable para multiplicar lsa horsa con el precio
print(f"el precio total es: {importetotal}")