#3. Escribir un programa que pida al usuario un número entero
#positivo y muestre por pantalla la cuenta atrás desde ese número
#hasta cero separados por comas

numero = int(input("Escribe un número entero positivo "))

for i in range(numero,-1,-1):
    if(i == 0):
        print(i)
    else:
        print(i, end=", ")