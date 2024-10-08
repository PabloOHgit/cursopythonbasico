# Ejercicio 5:
# A. Crea una lista de números.
# B. Convierte la lista en una tupla.
# C. Multiplica cada elemento de la tupla por 2 y guarda el resultado en
# una nueva tupla.

lista_numeros = [1,2,3,4,5,6]

tupla_numeros = tuple(lista_numeros)

nueva_tupla = tuple(elemento*2 for elemento in tupla_numeros)

print(nueva_tupla)