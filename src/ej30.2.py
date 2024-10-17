#Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

#El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10


def obtener_valores_validos():
    inicio = int(input("Introduce el número de inicio de la serie: "))
    incremento = int(input("Introduce el incremento de la serie: "))
    total = int(input("Introduce el número total de la serie: "))


    while incremento <= 0 or total <= 0:
        print("El incremento y el total deben ser mayores que cero.")
        incremento = input("Introduce el incremento de la serie: ")
        total = input("Introduce el número total de la serie: ")

                  
    return inicio, incremento, total

def generar_serie(inicio, incremento, total):
    serie = []
    for i in range(total):
        serie.append(str(inicio + i * incremento))

    return serie

def mostrar_serie(serie):
    print("SERIE => " + '-'.join(serie))

def main():
    inicio, incremento, total = obtener_valores_validos()
    serie = generar_serie(inicio, incremento, total)
    mostrar_serie(serie)

if __name__ == "__main__":
    main()