#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def preguntar_fecha():
    fecha_int = input("Dame una fecha con formato dd/mm/aaaa: ")
    return fecha_int

def convertir_fecha(fecha_int):
    div_partes = fecha_int.split("/")

    dia = div_partes[0].zfill(2)
    mes = div_partes[1].zfill(2)
    año = div_partes[2].zfill(2)
    "".zfill

    return dia, mes, año



def main():
    fecha= preguntar_fecha()
    dia, mes, año = convertir_fecha(fecha)
    print("Tu fecha convertida es -> Dia {}, Mes {}, Año {}".format(dia, mes, año))


if __name__ == "__main__":
    main()