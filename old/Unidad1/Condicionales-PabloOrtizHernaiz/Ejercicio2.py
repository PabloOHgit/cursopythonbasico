"""Ejercicio 2: Escribir un programa que pida al usuario dos números y muestre por
pantalla su división. Si el divisor es cero el programa debe mostrar un error."""

dividendo = int(input("Introduce un número entero (el dividendo)"))
divisor = int(input("Introduce un segundo número entero para la división (el divisor)"))

if (divisor == 0):
    print("Error, el divisor es 0 y no se puede realizar la división")
else:
    print("El resultado de la división es",dividendo/divisor)