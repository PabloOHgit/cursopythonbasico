"""Ejercicio 4: La pizzería “Pizza Paradiso” ofrece pizzas vegetarianas y no
vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen
a continuación.
• Ingredientes vegetarianos: Pimiento, cebolla, champiñones, ...
• Ingredientes no vegetarianos: Pepperoni, Jamón, atún, …
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o
no, y en función de su respuesta le muestre un menú con los ingredientes
disponibles para que elija.
El programa debe preguntar al usuario cuantos ingredientes quiere elegir, y
mostrárselos, hasta un total de 3 ingredientes.
Se debe mostrar el contenido de la pizza: Tomate, queso y los ingredientes
extras."""

tipo_pizza = int(input("Elige el tipo de pizza que deseas, escribe el número: 1-Vegetariana 2-Normales "))

if(tipo_pizza == 1):
    print("Pizza Vegetariana: ")
    num_ingredientes = int(input("Elige cuántos ingredientes extras deseas como máximo 3 (del 1 al 3) "))
    if(num_ingredientes == 3):
        ing1 = input("Introduce el primer ingrediente ")
        ing2 = input("Introduce el segundo ingrediente ")
        ing3 = input("Introduce el tercer ingrediente ")
        print("Pizza: Tomate, queso,",ing1,",",ing2,",",ing3)
    elif(num_ingredientes == 2):
        ing1 = input("Introduce el primer ingrediente ")
        ing2 = input("Introduce el segundo ingrediente ")
        print("Pizza: Tomate, queso,",ing1,",",ing2)
    elif(num_ingredientes == 1):
        ing1 = input("Introduce el primer ingrediente ")
        print("Pizza: Tomate, queso,",ing1)
    else:
        print("No has introducido un número correcto de ingredientes")
elif(tipo_pizza == 2):
    print("Pizza Normal: ")
    num_ingredientes = int(input("Elige cuántos ingredientes extras deseas como máximo 3 (del 1 al 3) "))
    if(num_ingredientes == 3):
        ing1 = input("Introduce el primer ingrediente ")
        ing2 = input("Introduce el segundo ingrediente ")
        ing3 = input("Introduce el tercer ingrediente ")
        print("Pizza: Tomate, queso,",ing1,",",ing2,",",ing3)
    elif(num_ingredientes == 2):
        ing1 = input("Introduce el primer ingrediente ")
        ing2 = input("Introduce el segundo ingrediente ")
        print("Pizza: Tomate, queso,",ing1,",",ing2)
    elif(num_ingredientes == 1):
        ing1 = input("Introduce el primer ingrediente ")
        print("Pizza: Tomate, queso,",ing1)
    else:
        print("No has introducido un número correcto de ingredientes")    
else:
    print("No sabemos que tipo de pizza deseas")