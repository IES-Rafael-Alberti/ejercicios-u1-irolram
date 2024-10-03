#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.

from ej18 import mayus 

def num_letras(nom):

    nom = len(nom)
    return nom

def main():

    nombre = input("Introduce tu nombre: ")
    print("{} tiene {} letras".format(nombre,nombre ))


    
if __name__ == "__main__":
    main()