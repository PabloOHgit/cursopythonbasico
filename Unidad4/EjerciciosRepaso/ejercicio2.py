# Ejercicio 2.
# A. Crea una función que muestra una tabla de multiplicar.
# B. Modifica ese programa para que imprima las tablas de multiplicar del 1 al 10.
# Se puede hacer con funciones.

# A.
def tabla_multiplicar(x):
    print(f"{x} x 1 = {x*1}")
    print(f"{x} x 2 = {x*2}")
    print(f"{x} x 3 = {x*3}")
    print(f"{x} x 4 = {x*4}")
    print(f"{x} x 5 = {x*5}")
    print(f"{x} x 6 = {x*6}")
    print(f"{x} x 7 = {x*7}")
    print(f"{x} x 8 = {x*8}")
    print(f"{x} x 9 = {x*9}")
    print(f"{x} x 10 = {x*10}")
    
num = int(input("Introduce un número para calcular la tabla de multiplicar: "))
tabla_multiplicar(num)

# B.
def tabla_multiplicar2():
    for x in range(1,11):
        print(f"\nLa tabla de multiplicar de {x}: ")
        print(f"{x} x 1 = {x*1}")
        print(f"{x} x 2 = {x*2}")
        print(f"{x} x 3 = {x*3}")
        print(f"{x} x 4 = {x*4}")
        print(f"{x} x 5 = {x*5}")
        print(f"{x} x 6 = {x*6}")
        print(f"{x} x 7 = {x*7}")
        print(f"{x} x 8 = {x*8}")
        print(f"{x} x 9 = {x*9}")
        print(f"{x} x 10 = {x*10}")
        
tabla_multiplicar2()