# ejercicio 5.
# Crear un juego educativo donde el usuario debe adivinar las capitales de los países europeos.
# Los países en cada partida deben salir en orden diferente.
# A partir de este diccionario:
# paises_capitales = {“España": "Madrid", "Francia": "París", "Alemania": "Berlín", "Italia": "Roma",
# "Reino Unido": "Londres", "Portugal": "Lisboa", "Grecia": "Atenas", "Suecia": "Estocolmo",
# "Noruega": "Oslo", "Finlandia": "Helsinki", "Bélgica": "Bruselas", "Países Bajos": "Amsterdam",
# "Suiza": "Berna", "Austria": "Viena", "Dinamarca": "Copenhague", "Irlanda": "Dublín”}
# Extra: Se pueden añadir más países, o hacerlo por continentes.

import random

paises_capitales = {
    "España": "Madrid", "Francia": "París", "Alemania": "Berlín", "Italia": "Roma",
                    "Reino Unido": "Londres", "Portugal": "Lisboa", "Grecia": "Atenas", "Suecia": "Estocolmo",
                    "Noruega": "Oslo", "Finlandia": "Helsinki", "Bélgica": "Bruselas", "Países Bajos": "Amsterdam",
                    "Suiza": "Berna", "Austria": "Viena", "Dinamarca": "Copenhague", "Irlanda": "Dublín"
}

paises_lista = []

for pais in paises_capitales:
    paises_lista.append(pais)

pais_random = random.choice(paises_lista)
print(pais_random)

capital_usuario = input(f"Introduce el nombre de la capital para el pais {pais_random}: ")

if capital_usuario.capitalize() == paises_capitales[pais_random]:
    print("Muy bien has acertado")