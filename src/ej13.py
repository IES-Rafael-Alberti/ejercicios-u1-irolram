#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

num1 = int(input("Dame un número entero: "))
num2 = int(input("Dame otro número entero: "))

division = num1  / num2 
cociente = num1 // num2 
resto = num1 % num2 

print(f"la división de {num1} entre {num2} da un cociente {cociente} y un resto {resto}")