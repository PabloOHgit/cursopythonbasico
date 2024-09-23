cadena = "Pais;oro;plata;bronce\nEstados Unidos de América;40;44;42\nRepública Popular de China;40;27;24\nJapón;20;12;13"

datos_olimpicos = cadena.split("\n")

# pais,oro,plata,bronce = cadena.split("\n")


# datos2 = datos.split(";")
medallero = {}
    
print(datos_olimpicos)
pais,oro,plata,bronce = datos_olimpicos[0].split(";")
print(pais,oro,plata,bronce)

for pais_medallas in datos_olimpicos[1:]:
    print(pais_medallas)
    split = pais_medallas.split(";")
    print(split)
    






# for i in range(3):
#     fila = []
#     for j in range(3):
#         valor = int(input(f"Introduce el valor para la posición [{i+1},{j+1}]: "))
#         fila.append(valor)  # Añadir el valor a la fila
#         print(fila)
#     matriz.append(fila)  # Añadir la fila completa a la matriz
#     print(matriz)
# print(matriz)

# print(datos[0])
# print(datos[1])
# print(datos[2])
# print(datos[3])
