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

def crea_pais_random():
    paises_lista = []    
    for pais in paises_capitales:
        paises_lista.append(pais)
    pais_random = random.choice(paises_lista)
    return pais_random

capital_usuario = ""

def menu(pais_random):
    print("\n***** JUEGO DE ADIVINAR CAPITALES ****")
    print("\nDispones de 3 intentos...juega bien")
    global capital_usuario
    capital_usuario = input(f"\nIntroduce el nombre de la capital para el pais {pais_random}: ")
    return capital_usuario

def repite(pais_random):
    global capital_usuario
    capital_usuario = input(f"\nIntenta adivinar de nuevo el nombre de la capital para el pais {pais_random}: ")
    return capital_usuario

def comprueba(capital_usuario,pais_random):
    if capital_usuario.capitalize() == paises_capitales[pais_random]:
        return True

contador = 0
pais_random = crea_pais_random()
while contador <= 3:    
    if contador == 0:
        capital_usuario = menu(pais_random)
    elif comprueba(capital_usuario,pais_random):
        print("\nMuy bien has acertado")
        break
    elif contador == 1:
        print(f"Te quedan {3-contador} intentos")
        capital_usuario = repite(pais_random)
        comprueba(capital_usuario,pais_random)
    elif contador == 2:
        print(f"Te queda {3-contador} intento")
        capital_usuario = repite(pais_random)
        comprueba(capital_usuario,pais_random)
    else:
        print("Ya no te quedan intentos, has perdido...")
    contador += 1

