#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

def quitar_pre_y_ext(telefono):
    telefono = telefono.split("-", 1)[1].rsplit("-", 1)[0]

    return telefono


def main():
    tel= input("Escribe tu numero de teléfono con prefijo y extension: ")
    print(quitar_pre_y_ext(tel))

if __name__ == "__main__":
    main()      