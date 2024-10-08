# Ejercicio 6. Dada esta lista: calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]. Calcula la nota media
# de cada alumno y muéstrala por pantalla.

calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]
lista_medias = []

for notas in calificaciones:
    sumatorio = sum(notas) / len(notas)
    lista_medias.append(sumatorio)
    
for media in lista_medias:
    print(f"La media del alumno es: {round(media)}")