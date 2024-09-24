# Ejercicios Diccionarios
# Ejercicio 1:
# A. Crear un diccionario para representar un inventario de una frutería.
# Ej.: Manzanas = 3, Peras=4, Naranjas = 8
# B. Acceder a un valor específico de Peras.
# C. Agregar un nuevo elemento.
# D. Modificar un valor existente.
# E. Mostrar las claves del inventario. (Nombres de la fruta)
# F. Mostrar los valores del inventario. (Cantidad de fruta)
# G. Mostrar el inventario completo, nombres y cantidad.
# H. Verificar la existencia de uvas en el inventario.

# A 
fruteria = {"Papayas":3,"Mangos":8}

# B
# Como no tengo peras, lo que hago es agregar otra clave "Peras" y lo añade al final automáticamente
fruteria["Peras"] = 4
# Imprime {'Uvas': 12, 'Papayas': 3, 'Mangos': 8, 'Peras': 4}
# Accedo a Peras
(fruteria["Peras"])
    # o
print(fruteria["Peras"])

# C 
fruteria["Naranjas"] = 2 #agregamos Naranjas

# D
fruteria["Peras"] = 1 #modificamos el valor de Peras

# E
for claves in fruteria:
    print(claves)
    
# F
for valores in fruteria.keys():
    print(valores)
    # O -
for valores in fruteria:
    print(fruteria[valores])
    
# G 
for claves,valores in fruteria.items():
    print(f"La cantidad de {claves} es {valores}")
    
# H
no = False
for frutas in fruteria.keys():
    if frutas == "Uvas":
        print("Hay uvas")
        no = True
if no == False:
    print("No hay")
    # O -
    
if "Papayas" in fruteria:
    print("Hay papayas")
else:
    print("No hay papayas")
    # O -
    
print(fruteria.get("Uvas"))

