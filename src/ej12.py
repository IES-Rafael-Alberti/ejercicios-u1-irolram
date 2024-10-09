#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Dime tu peso: "))
estatura = float(input("Dime tu altura en metros: "))
imc =  peso /(estatura * estatura) 
#redondear = round(imc, 2)
#print(f"Su indice de masa corporal es: {redondear}")

print("Su indice de masa corporal es: {:.2f}".format(imc))