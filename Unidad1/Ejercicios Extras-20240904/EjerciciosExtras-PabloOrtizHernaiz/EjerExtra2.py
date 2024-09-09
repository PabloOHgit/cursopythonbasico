"""Ejercicio 2: Una juguetería tiene mucho éxito en dos de sus productos: payasos 
y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por 
peso de cada paquete así que deben calcular el peso de los payasos y muñecas 
que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada 
muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el 
último pedido y calcule el peso total del paquete que será enviado."""

cuenta_muniecas = int(input("Cuántas muñecas hay en el pedido? "))
cuenta_payasos = int(input("Cuántos payasos hay en el pedido? "))
peso_muniecas = cuenta_muniecas * 75
peso_payasos = cuenta_payasos * 115
peso_gr = peso_muniecas+peso_payasos
peso_kg = peso_gr /1000

print("El pedido contiene",cuenta_muniecas,"muñecas y",cuenta_payasos,
      "payasos. El peso total del pedido en gramos es",peso_gr,
      "y en kilos es",peso_kg)