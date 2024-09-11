#Ejercicio 2: Escribir un programa que pida al usuario que introduzca una frase en la
#consola y muestre por pantalla la frase invertida.

frase = input("Introduce una frase: ")

print(f"La frase invertida es: {frase[-1::-1]}")#Esta es la forma que he pensado, también es válida
print(f"La frase invertida es: {frase[::-1]}")