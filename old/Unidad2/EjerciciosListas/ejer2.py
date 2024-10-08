# Ejercicio 2. Escribir un programa que pregunte al usuario los números ganadores de la lotería
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

nums_loteria = []

#CON WHILE
# contador = 0
# while contador < 6:
#     num_loteria.append(int(input("Introduce un número ganador de la primitiva (son 6): ")))
#     contador += 1

#CON FOR
for i in range(6):
    nums_loteria.append(int(input("Introduce un número ganador de la primitiva (son 6): ")))
    
nums_loteria.sort()
print(nums_loteria)

