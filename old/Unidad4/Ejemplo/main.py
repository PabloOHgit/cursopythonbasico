import random
# import paquete1.modulo3 as estadistica
from paquete1.modulo3 import media
import string
import datetime

lista_numeros = [15,78,98,43,31,-54,-32]
numero_aletorio = random.choice(lista_numeros)
lista_nombres = ["alfredo","alex","antonio","luis"]
nombre_aleatorio = random.choice(lista_nombres)
print(nombre_aleatorio)

num_aleatorio = random.randint(1,18)
print(num_aleatorio)

media_numeros = media(lista_numeros)
print(media_numeros)
media(lista_numeros)

print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)
print(datetime.datetime.now())
hora = datetime.time
print(hora)