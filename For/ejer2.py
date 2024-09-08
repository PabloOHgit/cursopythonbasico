#Ejercicio 2: Pedir al usuario 5 números y decir si son par o impar.

for i in range(5):
    numero = int(input("Introduce un número: "))
    operacion = numero %2
    cuenta = 4 - i
    if(operacion == 0):
        if(cuenta == 0):
            print("El número es par, y ya no tienes más intentos")
        else:
            print("El número es par, y tienes",cuenta,"intentos más")        
    else:
        if(cuenta == 0):
            print("El número es impar, y ya no tienes más intentos")
        else:
            print("El número es impar, y tienes",cuenta,"intentos más")