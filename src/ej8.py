#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

num1 = int(input("Dame  un numero: "))
num2 = int(input("Dame  un numero: ")) 

num1 = num1 + num2  #guardamos en la variable el num2 y lo volvemosa pedir
num2 = int(input("Dame  un numero: ")) 
num1 = num1 + num2  


print(f"la suma  de los 3 números  es {num1}")