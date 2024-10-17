#Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

#El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
#Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".

def elegir_numero():
    num1 = int(input("Escribe un número: "))
    num2 = int(input("Escribe un número: "))
    return num1, num2

def si_num2_es_igual(num1, num2):
    if num2 == num1:
        print("Los números no pueden ser iguales")
        return  False
    return True
def numeros_diferentes(num1, num2):

    menor = min(num1, num2)
    mayor = max(num1, num2)

    cont_enteros_dif = 0


    for i in range(menor, mayor ):
            cont_enteros_dif += 1

    return cont_enteros_dif

def main():

    num1, num2 = elegir_numero()

    diferencia = numeros_diferentes(num1,num2)

    print("La diferencia entre {} y {} es de {}".format(num1, num2, diferencia))

if __name__ == "__main__":
    main()