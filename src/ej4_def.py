#Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.


def farenheit_funcion():
    farenheit = float(input("Dame los grados farenheit: "))

    return farenheit

def celsius_funcion(farenheit):
    celsius= ( farenheit * 9 / 5) - 32

    return celsius

def main():
    conversion = farenheit_funcion()
    celsius = celsius_funcion(conversion)
    print("La conversión es {:.2f}º farenheit, {:.2f}º celsius.".format(conversion, celsius))

if __name__ == "__main__":
    main()


"""Celsius= int(input("Dame una temperatura: "))
fah =  ( Celsius * 9 / 5) + 32 # Calculo para convertir los celsius 
print(f"Su temperatura convertida es:{fah}°F  ")"""