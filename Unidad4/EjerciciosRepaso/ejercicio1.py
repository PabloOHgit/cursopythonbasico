# Ejercicio 1.
# A. Crear un programa que imprima los 10 primeros números naturales utilizando tanto un
# bucle while como el bucle for.
# B. Modificar el programa anterior para que muestre 10 números aleatorios entre 1 y 50
# (modulo random) realizar la modificación tanto para el bucle while, como el bucle for.
# C. Crear 2 listas, una para números pares y otra impares. Rellenar esas listas con los
# números aleatorios del apartado B.
# D. Con las listas impares, crear una lista y añadir los números que sean múltiplos de 3.
# E. Con las listas pares, crear otra lista con los números menores a 25.
# F. Imprimir por pantalla ambas listas.

import random
import math

# A. 
# for i in range (1,11):
#     if i == 10:
#         print(i)
#         break
#     print(i, end=", ")
    
# contador = 1
# while contador < 11:    
#     if contador == 10:
#         print(contador)
#         break
#     print(contador, end=", ")
#     contador += 1
    
# B.

# num = 0
# for i in range (1,11):
#     num = random.randint(1,50)
#     if i == 10:
#         print(num)
#         break
#     print(num, end=", ")

# contador = 0
# while contador < 10:
#     num = random.randint(1,50)
#     if contador == 9:
#         print(num)
#         break
#     print(num, end=", ")
#     contador += 1
    
# C.
lista_par1 = []
lista_impares1 = []
num = 0
for i in range (1,11):
    num = random.randint(1,50)
    if num % 2 == 0:
        lista_par1 += [num]
    else:
        lista_impares1 += [num]
print(f"Lista de números pares: {lista_par1}")
print(f"Lista de números impares: {lista_impares1}")

lista_par2 = []
lista_impares2 = []
contador = 0
while contador < 10:
    num = random.randint(1,50)
    if num % 2 == 0:
        lista_par2 += [num]
    else:
        lista_impares2 += [num]
    contador += 1
print(f"Lista de números pares: {lista_par2}")
print(f"Lista de números impares: {lista_impares2}")

# D. 
lista_impares3 = [multiplo for multiplo in lista_impares2 if multiplo % 3 == 0]
# print(f"La lista de números impares multiplos de 3 es: {lista_impares3}")

# E. 
lista_menores = [menor for menor in lista_par2 if menor < 25]
# print(f"La lista de números pares menores de 25 es: {lista_menores}")

# F.
print(f"La lista de números impares multiplos de 3 es: {lista_impares3}")
print(f"La lista de números pares menores de 25 es: {lista_menores}")