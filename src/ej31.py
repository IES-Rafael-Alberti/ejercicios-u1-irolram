#Mostrar todos los divisores de un número

def introducir_numero():

    num= int(input("Introduce un número: "))

    return num

def recorrer_numero(num):
    divisores =[]
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
            
    return divisores



def main():
    num= introducir_numero()
    divisor_num = recorrer_numero(num)
    print("Los divisores de {} son {}".format(num, divisor_num))


if __name__ == "__main__":
    main()
