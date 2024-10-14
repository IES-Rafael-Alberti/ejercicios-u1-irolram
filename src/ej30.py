#Escribir un programa que determine si un número es primo

def introducir_numero():

    num= int(input("Introduce un número: "))

    return num

def comprobar_primo(num):
    if num % num == 0 and num % 1 == 0:
        return print("Es primo")
    else:
        return print("No es primo")
    
def main():
    num = introducir_numero()
    comprobar_primo(num)

if __name__ == "__main__":
    main()
