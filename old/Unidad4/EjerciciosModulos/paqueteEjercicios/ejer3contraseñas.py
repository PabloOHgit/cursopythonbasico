# 3. Crear un programa para crear contraseñas seguras.
# a. El usuario debe introducir la longitud que desea de la contraseña

import random
import string

def crea_contraseña(longitud_caracteres):
    contraseña = ""
    contraseña_larga = string.punctuation+string.digits+string.ascii_lowercase+string.ascii_uppercase
    for i in range(longitud_caracteres):
        contraseña += random.choice(contraseña_larga)
    return contraseña
