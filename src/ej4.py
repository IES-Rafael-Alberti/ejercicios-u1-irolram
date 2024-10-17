#Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

Celsius= int(input("Dame una temperatura: "))
fah =  ( Celsius * 9 / 5) + 32 # Calculo para convertir los celsius 
print(f"Su temperatura convertida es:{fah}°F  ")