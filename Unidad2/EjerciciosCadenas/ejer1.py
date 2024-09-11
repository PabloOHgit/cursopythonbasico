#Ejercicio 1: Los teléfonos de una empresa tienen el siguiente formato 
# prefijo-número-extensión donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de
#teléfono con este formato en la consola y muestre por pantalla el número de teléfono
#sin el prefijo y la extensión.

numero = input("Introduce un número de teléfono con extensión (ej +34-913724710-56): ")

print(f"El teléfono sin el prefijo ni la extensión es: {numero[4:-3]}")