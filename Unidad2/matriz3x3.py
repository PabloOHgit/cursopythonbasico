# Inicializar una matriz vacía de 3x3
matriz = []

# Rellenar la matriz con valores introducidos por el usuario
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Introduce el valor para la posición [{i+1},{j+1}]: "))
        fila.append(valor)  # Añadir el valor a la fila
        print(fila)
    matriz.append(fila)  # Añadir la fila completa a la matriz
    print(matriz)
print(matriz)

# Mostrar la matriz por pantalla
print("\nMatriz 3x3 ingresada:")
for fila in matriz:
    print(fila)
