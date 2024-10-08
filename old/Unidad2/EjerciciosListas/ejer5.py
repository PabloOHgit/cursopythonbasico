# Listas anidadas
# Ejercicio 5.
# A. Crear una matriz de 3x3 utilizando listas anidadas y mostrarlo por pantalla.
# B. Acceder al elemento 1,2 de la matriz y mostrarlo por pantalla.
# C. Imprimir todos los elementos de una lista anidada.

matriz_bis = []
matriz = [[1,2,3],[4,5,6],[7,8,9]]

print(matriz[1][2])

for fila in range(3):
    for elemento in range(3):
        elemento = int(input("Introduce un número: "))
        matriz_bis.append(elemento)
        
print(matriz_bis)