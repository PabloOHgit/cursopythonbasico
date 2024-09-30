# Ejercicios Funciones II
# 1. Crea un programa que introduciendo una lista como argumento de una función.
# Realice:
# a. Suma de todos los elementos de la lista
# b. La media
# c. El número mayor y menor de la lista

lista = [1,2,3,4]

def funcion_multiple(lista):
    lista = [1,2,3,4]
    suma = sum(lista)
    media = suma / len(lista)
    num_mayor = max(lista)
    num_menor = min(lista)
    print(f"La suma de todos los elementos de la lista: {suma}")
    print(f"La media de la lista: {media}")
    print(f"El mayor de de la lista: {num_mayor}")
    print(f"El menor de la lista: {num_menor}")

funcion_multiple(lista)