#Ejercicio 4. Escribir un programa que pida ingresar la coordenada de un punto en el plano, es
#decir dos valores enteros x e y, (no incluir 0). Decir que cuadrante son.

x = int(input("Introduce el valor de coordenada X (positivo o negativo): "))
y = int(input("Introduce el valor de coordenada Y (positivo o negativo): "))

if(x > 0 and y > 0):
    print("El cuadrante es el 1")
elif(x > 0 and y < 0):
    print("El cuadrante es el 4")
elif(x < 0 and y < 0):
    print("El cuadrante es el 3")
else:
    print("El cuadrante es el 2")