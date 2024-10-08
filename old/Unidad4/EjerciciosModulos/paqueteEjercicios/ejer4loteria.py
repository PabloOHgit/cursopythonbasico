# 4. Crear un programa que genere un boleto de lotería ganador.
# a. Generar 5 números de una tabla de 54 (números del 1 al 54) y
# uno más (número clave) de una tabla de 10 (del 0 al 9). Los
# números no pueden ser repetidos.
# b. Imprimir la fecha del día de hoy. (Modulo datetime)

import random
import datetime

def genera_cinco_num():
    numeros = []
    num1 = 0
    x = 0
    while x < 5:
        num1 = random.randint(1,54)
        while num1 not in numeros:
            numeros += [num1] 
            x += 1
    return numeros

def genera_num_clave():
    num_clave = random.randint(1,10)
    return(num_clave)

def imprime_fecha():
    fecha = datetime.datetime.now()
    fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M:%S")
    return fecha_formateada
        