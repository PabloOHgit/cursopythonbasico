asignaturas = ["Matematicas","Lengua","Fisica","Quimica"]

notas_y_asignaturas = [] 
posicion = []

for asignatura in asignaturas:
    nota = int(input(f"Introduce la nota de {asignatura}: "))
    notas_y_asignaturas.append([asignatura,nota])

for nota_y_asignatura in notas_y_asignaturas:
    if nota_y_asignatura[1] >= 5:
        posicion.append(notas_y_asignaturas.index(nota_y_asignatura))

# Se invierte la lista posicion para eliminar las sublistas empezando por la última, 
# evitando así que los índices se desplacen al eliminar elementos.
posicion.reverse() 
for i in posicion:
    #print(notas_y_asignaturas)
    notas_y_asignaturas.pop(i)

print(notas_y_asignaturas)