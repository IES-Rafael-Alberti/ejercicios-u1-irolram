#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def Remplazar_correo(correo):

    camcorreo =correo.split("@") #dividimos el correo en 2 partes
    correoempresa = camcorreo[0] + "@" + "ceu.es" #reemplazamos la segunda parte del correo por ceu.es
    return correoempresa

def main():

    correo = input("Dame tú correo electrónico: ")

    print("Tú correo de empresa es: {}".format(Remplazar_correo(correo)))


if __name__ == "__main__":
    main()    