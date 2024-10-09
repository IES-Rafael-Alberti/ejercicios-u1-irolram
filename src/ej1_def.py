#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

def saludo():
    usu= input("Dime tu name: ")
    return usu

def main():
    usuario= saludo()
    print("Hola {}, bienvenido.".format(usuario))




if __name__ == "__main__":
    main()