#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

#La función calcula_precio(importe: float, iva: float) -> str recibe el importe y el iva, si el iva está fuera del rango 0-100 se aplicará el 21%, y retornará una cadena de caracteres con el iva y el precio con iva mostrando solo 2 posiciones decimales. Ejemplo: calcula_precio(100, 21) -> "El precio final del artículo con IVA (21.00) es 121.00€."


def pedir_importe():
    
    importe = float(input("Ingrese el importe del artículo: "))
    iva = float(input("Ingrese el iva: "))

    return importe, iva


def importe_con_iva(importe: float, iva: float)-> str:
    if iva < 0 or iva > 100:
        iva = 21
    importe_iva = importe * (iva/100)

    return round(importe_iva,2)

def main():
    
    importe, iva = pedir_importe()
    con_iva = importe_con_iva(importe, iva)
    total = importe + con_iva
    print("El precio final del artículo con IVA {:.2f} es {:.2f}€".format(iva, total))

if __name__ == "__main__":
    main()