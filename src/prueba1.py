#Desarrolla una función en prueba1.py que reciba dos números y retorne el mayor número de los dos o 0 si son iguales. Realiza las pruebas unitarias y ejecútalas con pytest desde la terminal

def pedir_numero():

    num1 = input("Escribe un número: ")
    num2 = input("Escribe otro número: ")

    return num1, num2

def retorna_mayor_numero(num1, num2):

    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else: 
        return 0
    
