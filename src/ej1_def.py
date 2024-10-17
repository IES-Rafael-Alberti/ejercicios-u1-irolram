#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

def saludo(nombre = None):
    if nombre is None:
        nombre= input("Dime tu nombre: ")
    return nombre

def main():
    usuario= saludo()
    print("Hola {}, bienvenido.".format(usuario))

if __name__ == "__main__":
    main()