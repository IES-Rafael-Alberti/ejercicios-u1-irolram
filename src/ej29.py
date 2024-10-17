#Cálculo de un número aleatorio entre dos valores

import random

def generar_numero(num1, num2):

    numero = random.randint(num1, num2)
    return numero

def pedir_numeros():
    num1 = int(input("Introduce el valor mínimo (num1): "))
    num2= int(input("Introduce el valor máximo (num2): "))
    return num1, num2

def main():
    num1, num2 = pedir_numeros()
    
    if num1 > num2 :
        print("El valor mínimo no puede ser mayor que el valor máximo.")
    else: 
        num_aleatorio = generar_numero(num1, num2)
        print(f"El número aleatorio entre {num1} y {num2} es: {num_aleatorio}")

if __name__ == "__main__":
    main()







