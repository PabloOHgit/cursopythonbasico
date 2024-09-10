#Ejercicio 8. Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe
# cuántos tienen notas mayores o iguales a 7 y cuantossuspensos.

notables = 0
suspensos = 0

for i in range(1,11):
    nota = int(input("Introduce una nota: "))
    if nota >= 7:
        notables += 1
    else:
        suspensos += 1
        
print("Notas mayores o iguales a 7: ",notables)
print("Suspensos: ",suspensos)