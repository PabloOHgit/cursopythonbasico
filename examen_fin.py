# num1 = int(input("Escribe el primer número: "))
# num2 = int(input("Escribe el primer número: "))
# suma = num1 + num2
# print(f"La suma es: {suma}")

# Crea un programa para controlar la edad de una persona. 

# El programa debe controlar si es mayor de edad para dejarlo entrar en la discoteca. (0.5 puntos)

# Pedir la edad por teclado
# Hacer el programa con funciones (0.75 puntos)

# edad = int(input("Por favor introduce tu edad: "))

# def comprobar_edad(edad):
#     if edad >= 18:
#         print("Es mayor de edad. Puede acceder a la discoteca.")
#     else:
#         print("Es menor de edad. No puede acceder a la discoteca.")
        
# comprobar_edad(edad)

# cadena = "Hola como estas"

# print(cadena[::-1])

# Crear un programa con funciones.

# 1. Crear una función que genere un número aleatorio entre 1 y 10. (0.25 puntos)

# 2. Crear una función para pedir al usuario un numero entre 1 y 10. (0.25 puntos)

# 3. Comprobar si ambos números coindicen. (0.25 puntos)
# import random

# def num_aleatorio():
#     numero = random.randint(1,10)
#     return numero

# num1 = num_aleatorio()
# print(f"Número aleatorio de entre 1-10: {num1}")

# def pide_num():
#     numero = int(input("Introduce un número de entre 1-10: "))
#     return numero

# num2 = pide_num()
# print(f"El número que has introducido es: {num2}")

# def son_iguales(num1,num2):
#     if num1 == num2:
#         return f"Los números son iguales"
#     else:
#         return f"Los números son distintos"
    
# print(son_iguales(num1,num2))

# # Número aleatorio de entre 1-10: 6
# # Introduce un número de entre 1-10: 6
# # El número que has introducido es: 6
# # Los números son iguales

# Crea un programa con lo siguiente:
# 1. Crea una variable que se llame comida y reciba una cadena "Huevo" (0.25 puntos)
# 2. Crea una lista de elementos con el elemento anterior, y 2 elementos más, Leche y Azúcar. (0.25 puntos)
# 3. Recorre la lista y muestra cada elemento (0.25 puntos)
# 4. Recorre la lista mostrando la posición y el elemento (0.25 puntos)

# comida = "Huevo"

# lista = [comida,"Leche","Azúcar"]

# #Recorre lista
# for ingrediente in lista:
#     print(ingrediente)

# #Recorre lista y muestra posicion y elemento    
# for i,ingrediente in enumerate(lista):
#     print(f"Posición: {i}, ingrediente: {ingrediente}")
    
# # Huevo
# # Leche
# # Azúcar
# # Posición: 0, ingrediente: Huevo
# # Posición: 1, ingrediente: Leche
# # Posición: 2, ingrediente: Azúcar

# Crear una clase Estuche. (0.25 puntos)

# Añadir método constructor con atributos: (0.25 puntos)

# Color
# Crear un método contenedor (0.25)
# Se le pasa por argumento una lista de materiales.
# Crear una clase Material(0.25 puntos)
# Añadir método constructor con atributos: (0.25 puntos)

# Nombre
# Color
# Crear un método para mostrar el contenido de del Material. Nombre y Color. (0.25 puntos)

# Crear una lista de materiales. (0.25 puntos)

# Mostrar el contenido del estuche a partir del método contenedor. (0.25 puntos)

class Estuche:
    def __init__(self,color):
        self.color = color
        
    def contenedor(self,materiales:list):
        self.materiales = materiales
        
class Material:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return f"El nombre es {self.nombre} y el color es {self.color}"
    
material1 = Material("Rotulador","Marrón")
material2 = Material("Lapiz","Rojo")
material3 = Material("Goma","Blanca")
lista_materiales = (material1,material2,material3)

estuche1 = Estuche("Azul")

estuche1.contenedor(lista_materiales)
for elemento in estuche1.materiales:
    print(elemento)


