#4. Introducir una cadena de caracteres e indicar si es un palíndromo. Una
# palabra palíndroma es aquella que se lee igual adelante que atrás.

frase = input("Introduce una frase para comprobar si es palíndroma: ")

print(f"La frase es: {frase[:]}, y la frase a la inversa es: {frase[-1::-1]}")

if frase[:] == frase[-1::-1]:
    print("La frase es palíndroma.")
else:
    print("La frase NO es palíndroma.")
