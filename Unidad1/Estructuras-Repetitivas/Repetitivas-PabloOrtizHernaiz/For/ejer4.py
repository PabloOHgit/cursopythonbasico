#Ejercicio 4. Crear un programa, que pida al usuario un número, y muestre por
#pantalla, los números en orden inverso hasta 0.

numero = int(input("\nIntroduce un número para visualizar los números hasta 0 en orden inverso: "))

for i in range(numero,-1,-1):
    if(i == 0):
        print(i)
    else:
        print(i, end=",")