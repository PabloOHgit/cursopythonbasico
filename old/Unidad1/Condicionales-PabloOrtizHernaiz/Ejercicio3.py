"""Ejercicio 3: Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es par o impar"""

numero = int(input("Escribe un número entero "))
resto_div = numero % 2

if(resto_div == 0):
    print("El número introducido es par")
else:
    print("El número es impar")