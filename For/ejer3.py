#Ejercicio 3. Crea un programa que imprima una tabla de multiplicar del número
#que introduzca el usuario.

numero = int(input("\nIntroduce un número para generar la tabla de multiplicar: "))
cuenta = 1
for i in range(10):
    multiplicacion = numero * cuenta
    print(numero,"*",cuenta,"=",multiplicacion)
    cuenta += 1
