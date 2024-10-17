#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


def main():
    # Preguntamos el nombre del producto, precio y cantidad de unidades
    producto = input("Nombre del producto: ")
    precio = float(input("Cuanto ha costado: "))
    unidades = int(input("Cuantas unidades: "))
    
    coste_total = precio * unidades
    
    # 6 dígitos enteros para el precio unitario, 3 dígitos para unidades y 8 para el coste total
    print(f"{producto}: {precio:09.2f} € por unidad, {unidades:03d} unidades, Total: {coste_total:011.2f} €")

if __name__ == "__main__":
    main()
