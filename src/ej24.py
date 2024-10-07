# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

def pedir_precio():
    precio = input("Dame el precio del producto con dos decimales: ")
    euros = precio.split(".")[0]
    centimos = precio.split(".")[1]

    return euros, centimos

def main():
    precio  = pedir_precio()

    print("El precio introducido es {} euros y {} céntimos.".format(precio[0], precio[1]))


if __name__ == "__main__":
    main()