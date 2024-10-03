# Ejercicio 3.
# La profesora de informática quiere crear un programa para organizar la clase:
# Partiendo de la lista de nombres de los alumnos de la clase, los situe en la disposición de las
# mesas de la clase que tiene forma de matriz 3x4 de manera aleatoria. (3 filas, 4 columnas)
# Por ejemplos: La lista tiene 12 nombres, sale un nombre aleatorio de la lista, y en la primera
# posición de la matriz, la posición (0,0) se situe ese nombre.
# Nota: Una forma común de construir matrices es haciendo uso de listas anidadas (o listas de
# listas). Si una lista convencional forma un vector de elementos, al hacer que cada elemento sea
# un vector, se obtiene una matriz de elementos.
# Para crear una matriz vacía se puede utilizar listas de comprensión:
# matriz_alumnos = [[0 for _ in range(4)] for _ in range(3)]
# También se puede crear las matriz vacías de manera manual.
# matriz_alumnos = []
#  for _ in range(3):
#  fila = []
#  for _ in range(4):
#  fila.append(None)
#  matriz_alumnos.append(fila)
# (Se utiliza _ a la otra de crear la lista, 
#  porque el contenido no se va a utilizar, es para sustituirlo,
# sería una variable desechable)

