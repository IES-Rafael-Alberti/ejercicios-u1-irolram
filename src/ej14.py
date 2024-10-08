# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

numpayaso = int(input("Cuántos payasos se han vendido en el último paquete: "))
nummuneca = int(input("Cuántas muñecas se han vendido en el último paquete: "))

pesotpayaso = (numpayaso * 0.112) # en gramos convertidos a kg
pesotmuneca = (nummuneca * 0.075) # en gramos convertidos a kg

totalpaquete = pesotmuneca + pesotpayaso # en kg

print("el peso total del paquete es: {:.2f} kg".format(totalpaquete))