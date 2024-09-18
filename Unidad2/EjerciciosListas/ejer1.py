# A. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
# Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]

print(asignaturas)

# B. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
# Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
# el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las
# asignaturas de la lista

for asignatura in asignaturas:
    print(f"Yo estudio: {asignatura}")
    
# C. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
# mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las
# asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas
# por el usuario.

notas_asignatura = []

for asignatura in asignaturas:
    nota = int(input(f"Nota de {asignatura}: "))
    notas_asignatura.append([asignatura,nota])
    # print(f"La nota de {asignatura} es {nota}")
print(notas_asignatura)

for nota in notas_asignatura:
    print(f"La asignatura de {nota[0]} es {nota[1]}")

# D. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que
# repetir.

# for nota in notas_asignatura:
#     if nota[1] <= 5:
#         notas_asignatura.remove(nota)
# for asignatura in notas_asignatura:
#     print(f"Esta materia está suspensa: {asignatura[0]}")

asignaturas_suspensas = []

for nota in notas_asignatura:
    if nota[1] < 5:
        asignaturas_suspensas.append(nota[0])
print(f"Las asignaturas suspensas son {asignaturas_suspensas}")

#Version eliminando 

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



