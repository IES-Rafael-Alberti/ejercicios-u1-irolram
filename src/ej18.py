#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

def minus(nom):
    nom = nom.lower()
    return nom



def mayus(nom):
    nom = nom.upper()
    return nom

def capital(nom):
    nom = nom.capitalize()
    return nom

def main():
    nombre = input("Dime tú nombre y un apellido: ")
    print(minus(nombre))
    print(mayus(nombre))
    print(capital(nombre))





if __name__ == "__main__":
    main()