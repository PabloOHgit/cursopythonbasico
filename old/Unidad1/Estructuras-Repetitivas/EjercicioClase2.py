#2. Escribir un programa que pida al usuario un número entero
#positivo y muestre por pantalla todos los números impares desde 1
#hasta ese número separados por comas.

numero = int(input("Escribe un número entero positivo "))

for i in range(1,numero,2):
    if(i == numero-1):
        print(i)
    else:
        print(i, end=", ")