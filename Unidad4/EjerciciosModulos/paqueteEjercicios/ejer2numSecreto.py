# 2. Crear un programa que consista en adivinar números.
# a. El número se debe generar de manera aleatoria
# b. El usuario cuando introduzca el número, se le debe indicar, si es
# el número, si es menor o mayor, y así poder ir cercando el
# número.
import random

def averigua_num():
    """
    Vamos a recoger el numero que introduzca el usuario
    para validar si averigua el numero secreto generado

    Args:
        num (integer):
        
    Return:
        Te va informando sobre cómo transcurre la adivinación
    """
    num_secreto = random.randint(1,20)
    print("Adivina el número secreto (entre 1 y 20):")
    while True:
        num = int(input("Introduce el número: "))
        if num > num_secreto:
            print("El número secreto es menor, prueba de nuevo:")
        elif num < num_secreto:
            print("El número secreto es mayor, prueba de nuevo:")
        else:
            print("Has acertado el número secreto")
            break
        
    


