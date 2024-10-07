#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

def preguntar_cesta():
    cacharro = input("Qué productos lleva en la cesta: ")
    return cacharro

def cambiar_linea(cesta):
    cesta = cesta.replace(",","\n" )
    return cesta

def main():
    cesta= preguntar_cesta()

    print("Su cesta es:\n {}".format(cambiar_linea(cesta)))

if __name__ == "__main__":
    main()