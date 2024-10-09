#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

def frase_invert(frase):
    frase = frase[::-1]
    return frase

def main():
    frase = input("Dame una frase para invertirla: ")

    print("tu frase invertida es: {}".format(frase_invert(frase)))

if __name__ == "__main__":
    main()