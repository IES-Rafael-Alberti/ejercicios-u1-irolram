#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

def leer_numero():

    n = int(input("dame un número: "))

    return n

def calculo(n):

    suma = (n + 1)*n/2
    return(suma)

def main():
    
    num= leer_numero()
    calcular_num = calculo(num)
    print(calcular_num)

if __name__ == "__main__":
    main()
