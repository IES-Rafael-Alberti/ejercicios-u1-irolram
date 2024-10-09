#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
"""horast = int(input("Cuantas horas has trabajado: "))
precio = int(input("Cobro por hora: "))
importetotal = (horast * precio) #variable para multiplicar lsa horsa con el precio
print(f"el precio total es: {importetotal}")"""

def horas_de_trabajo():

    horas = int(input("Cuantas horas has trabajado: "))
    return horas

def precio_hora():
    precio = int(input("Cobro por hora: "))
    return precio

def total_totalisimo(precio, horas):
    total = float(precio) * float(horas)
    return total

def main():
    check = horas_de_trabajo(),precio_hora() 
    print("El total del trabajo es {}€".format(total_totalisimo(check[0], check[1])))


if __name__ == "__main__":
    main()