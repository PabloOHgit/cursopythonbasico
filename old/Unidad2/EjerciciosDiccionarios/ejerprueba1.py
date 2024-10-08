# coordenadas = [(7,3),(4,6),(2,9),(6,3)]

# for tuplas in coordenadas:
#     if coordenadas.index(tuplas) == 0:
#         for elemento in tuplas:
#             if elemento == 3:
#                 print(elemento)

coordenadas = [(7,2), (4,6), (3,3), (3,4)]

for tuplas in coordenadas:  # Uso de enumerate para obtener el índice
      # Solo entra cuando el índice es 0
    for idx,elemento in enumerate(tuplas):
        if idx == 0:
            if elemento == 3:
                print(elemento)
