#Ejercicio 6. Realizar un programa que pida al usuario números por teclado. Preguntar después
#de ingresar el valor si desea cargar otro valor debiendo el operador introducir la cadena 'si' o
#'no' por teclado. Mostrar la suma de los números una vez terminado el bucle


opcion = "si"
suma = 0

while opcion == "si":
    valor = int(input("Introduce un número: "))
    suma = suma + valor
    opcion = input("Quieres introducir otro número (si o no): ")
    
print("La suma es",suma)