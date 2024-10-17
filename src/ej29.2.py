#Realiza un programa en Python que solicite un nombre y una edad.

#Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
#sEl programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir"

def nombre_edad():
    nom = str(input("Pon tu nombre: "))
    edad  =int(input("Dime tu edad: "))

    return nom, edad

def nombre_restricciones(nom):

    if nom == " ":
        return None
    else:
        return nom
    
def edad_restricciones(edad):
    if edad < 0 or edad > 125:
        print("MENTIROSO!!!!!!")
    else:
        return edad

def  diferencia_edad(edad):
    contedad = 0

    if edad < 125:
        for i in  range(edad, 125):
            contedad  += 1
        return contedad   
def main():

    nom, edad = nombre_edad()

    rnom  = nombre_restricciones(nom)

    redad = edad_restricciones(edad)

    difedad = diferencia_edad(edad)

    print("Te llamas {} y tienes {} años, te quedan aún {} años por cumplir".format(rnom,  redad, difedad))

if __name__ == "__main__":
    main()