#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
articulo= float(input("Dame el importe de su articulo: "))
iva = 0.10 
total = articulo * iva
print(f"El importe solo es {articulo} y el articulo + iva es de {total}")