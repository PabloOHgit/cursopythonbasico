# Ejercicio 2:
# A. Crear un diccionario de estudiantes con sus calificaciones.
# Ej. Juan = Matemáticas: 9, Historia: 8, Lengua: 7
# B. Acceder a una calificación específica.
# C. Mostrar el contenido del diccionario para que quede de la siguiente manera:
# D. Elimina a Ana del diccionario.

# A Diccionario de estudiandos y notas

notas_estudiantes = {
    "Juan":{"Matemáticas":9,"Historia":8,"Lengua":7},
    "Pablo":{"Matemáticas":10,"Historia":9,"Lengua":8},
    "Ana":{"Matemáticas":4,"Historia":6,"Lengua":3.5}
}

# for estudiantes,notas in notas_estudiantes.items():
#     nota_mates = notas.get("Matemáticas")
#     print(nota_mates)
    
# B
for estudiantes,notas in notas_estudiantes.items():
    for materia,nota in notas.items():
        if nota == 9:
            print(materia)

# C
notas_juan = notas_estudiantes["Juan"]
nota_media = 0
contador = 0
for estudiantes,asigaturas_notas in notas_estudiantes.items():
    print(f"La nota de {estudiantes} es:")
    for asignatura,nota in asigaturas_notas.items():
        print(asignatura,":",nota)
        # nota_media += int(nota)
        # contador += 1
    media = sum(asigaturas_notas.values())/len(asigaturas_notas.values())
    # print(f"La nota media es: {round(nota_media / contador,2)}")
    print(f"La nota media es: {round(media,2)}")
    
# D
notas_estudiantes.pop("Ana")

print(notas_estudiantes)