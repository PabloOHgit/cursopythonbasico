# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista para almacenar las notas correspondientes
notas = []

# Solicitar al usuario la nota para cada asignatura
for asignatura in asignaturas:
    nota = input(f"Introduce la nota que has sacado en {asignatura}: ")
    notas.append(nota)

# Mostrar las notas con el mensaje solicitado
print("\nResultados:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}.")