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

capital_usuario = ""

def crea_pais_random():
    paises_lista = []    
    for pais in paises_capitales:
        paises_lista.append(pais)
    pais_random = random.choice(paises_lista)
    return pais_random

def menu(pais_random):
    print("\n***** JUEGO DE ADIVINAR CAPITALES ****")
    print("\nPuedes fallar 3 veces por cada capital que quieras averiguar...juega bien")
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
    
def nuevo_pais_capital():
    while True:
        nuevo_pais = input("\nEscribe el nuevo país para añadir a la lista: ").capitalize()
        if nuevo_pais in paises_capitales:
            print("\nEste país ya existe, inténtalo de nuevo con otro")
        else:
            nueva_capital = input("Escribe la capital del país que has introducido: ").capitalize()
            paises_capitales[nuevo_pais] = nueva_capital
            break
    print(f"\nEl nuevo pais creado es {nuevo_pais} y su capital es {nueva_capital}")

while True:
    print("""\nOpciones:
          1. Jugar para acertar 5 capitales de países (3 vidas por país) 
          2. Añadir país/capital nueva
          3. Salir del programa
--Escribe a continuación tu elección...""")
    eleccion = int(input())
    if eleccion == 1:
        contador1 = 1
        while contador1 <= 5:            
            contador = 0
            pais_random = crea_pais_random()
            while contador <= 3:    
                if contador == 0:
                    capital_usuario = menu(pais_random)
                elif comprueba(capital_usuario,pais_random):
                    print("\nMUY BIEN HAS ACERTADO")
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
                    print(f"\nLA CAPITAL DE {pais_random} ES {paises_capitales[pais_random]}")
                contador += 1
            if contador1 == 4:
                print(f"\nPuedes jugar {5-contador1} vez más")
            elif contador1 == 5:            
                print(f"\nYa no puedes jugar más")
            else:
                print(f"\nPuedes jugar {5-contador1} veces más")
            contador1 += 1
    elif eleccion == 2:
        nuevo_pais_capital()
    elif eleccion == 3:
        print("\nSaliendo...")
        break
    else:
        print("\nTu elección es incorrecta, prueba de nuevo.")


        

