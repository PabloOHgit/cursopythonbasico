# Ejercicio 2.
# A. Crea una función que muestra una tabla de multiplicar.
# B. Modifica ese programa para que imprima las tablas de multiplicar del 1 al 10.
# Se puede hacer con funciones.

# A.
def tabla_multiplicar(x):
    print(f"\nLa tabla de multiplicar de {x}: ")
    for y in range(1,11):        
        print(f"{x} x {y} = {x*y}")
    
num = int(input("Introduce un número para calcular la tabla de multiplicar: "))
tabla_multiplicar(num)

# B.
# def tabla_multiplicar2():    
#     for x in range(1,11):
#         print(f"\nLa tabla de multiplicar de {x}: ")
#         for y in range(1,11):
#          print(f"{x} x {y} = {x*y}")
        
# tabla_multiplicar2()

def tabla_multiplicar2():    
    for x in range(1,11):
        tabla_multiplicar(x)
        
tabla_multiplicar2()