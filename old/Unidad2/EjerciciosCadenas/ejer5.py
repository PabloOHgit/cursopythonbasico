#Ejercicio 5: Escribir un programa que pregunte por consola por los productos de una
#cesta de la compra, separados por comas, y muestre por pantalla cada uno de los
#productos en una línea distinta.

lista_compra = input("Introduce varios productos de la compra (ej platanos,cebollas,etc): ")
print(lista_compra.replace(",","\n"))