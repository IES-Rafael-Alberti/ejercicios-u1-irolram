#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

compra = float(input("Dame el coste de la compra: "))
iva= float(0.21) 
sumiva =  float(compra * iva) #variable para saber el iva de la compra
total= (compra + sumiva) #Una variable para sumar la compra con el iva
print (f"La compra sin iva es de {compra}, el iva es de {sumiva} total = {total}")