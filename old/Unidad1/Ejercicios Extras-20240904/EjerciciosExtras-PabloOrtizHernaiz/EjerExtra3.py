"""Ejercicio 3: Escribir un programa que pida al usuario su peso (en kg) y estatura 
(en metros), calcule el índice de masa corporal y lo almacene en una variable, y 
muestre por pantalla la frase Tu índice de masa corporal es imc donde imc es el 
índice de masa corporal calculado redondeado con dos decimales.
Imc = peso/estatura**2
Redondear con 2 decimales => round(variable,2)"""

peso_usuario = int(input("Introduce tu peso en kilogramos "))
estatura_usuario = float(input("Introduce tu estatura en metros (ejemplo 1.75) "))
imc = peso_usuario / estatura_usuario**2 

print("Tu índice de masa corporal es",round(imc,2))