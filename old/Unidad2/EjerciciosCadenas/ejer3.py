#Ejercicio 3: Escribir un programa que pida al usuario que introduzca una frase en la
#consola y una vocal en minúscula, y después muestre por pantalla la misma frase, pero
#con la vocal introducida en mayúscula

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

print(f"La frase introducida con la vocal elegida en mayúscula es: {frase.replace(vocal,vocal.upper())}")