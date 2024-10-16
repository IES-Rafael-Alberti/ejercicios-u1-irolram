#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

iva = 0.21

def pedir_importe():
    
    importe = float(input("Ingrese el importe del artículo: "))

    return importe

def importe_con_iva(importe):

    importe_iva = importe * (iva + 1)

    return importe_iva

def main():

    importe = pedir_importe()
    con_iva = importe_con_iva(importe)

    print("El importe solo es: {:.2f}€, y con iva es {:.2f}€".format(importe, con_iva))

if __name__ == "__main__":
    main()