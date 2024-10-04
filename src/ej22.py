#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

from pickle import TRUE


def Cambiar_vocal_mayus(frase, vocal):
    frase = frase.replace(vocal, vocal.upper()) #remplazo la vocal que me piden por una en mayusculas
    return frase

def es_vocal(vocal):
    if vocal not in "aeiou": #not in para comparar si es una vocal o no
        print("error, no es una vocal válida") 
        return False
    return True

def main():
    frase = input("Dame una frase: ")
    vocal = input("Dame una vocal: ")

    if es_vocal(vocal):

        print(Cambiar_vocal_mayus(frase, vocal))



if __name__ == "__main__":
    main()    