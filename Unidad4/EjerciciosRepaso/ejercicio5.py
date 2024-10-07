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
# print(pais_random)

capital_usuario = ""

def menu():
    print("\n***** JUEGO DE ADIVINAR CAPITALES ****")
    print("\nDispones de 3 intentos...juega bien")
    global capital_usuario
    capital_usuario = input(f"\nIntroduce el nombre de la capital para el pais {pais_random}: ")
    return capital_usuario

def repite():
    global capital_usuario
    capital_usuario = input(f"\nIntenta adivinar de nuevo el nombre de la capital para el pais {pais_random}: ")

def comprueba(capital_usuario):
    if capital_usuario.capitalize() == paises_capitales[pais_random]:
        return True
    

menu()
while True:
    contador = 1
    print(capital_usuario)
    if comprueba(capital_usuario):
        print("\nMuy bien has acertado")
        break
    else:
        if contador == 1:
            print(f"\nTe quedan {3-contador} intentos")
            repite()
            contador += 1
            print(capital_usuario)
            print(contador)
        elif contador == 2:
            print(f"\nTe queda {3-contador} intento")
            repite()
            contador += 1
            print(capital_usuario)
            print(contador)
        else:
            print(f"\nNO te quedan intentos")
            print("\nHAS PERDIDO")
            print(capital_usuario)
            print(contador)

