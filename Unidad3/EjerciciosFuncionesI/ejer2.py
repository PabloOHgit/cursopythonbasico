# 2. Escribir una función que reciba un número entero positivo y devuelva su
# factorial. (Multiplicar todos los números enteros y positivos que hay entre
# el número máximo que queramos y el número 1.)

def factorial(a):
    a = 1
    num2 = 1
    for i in range(5):
            a = a * num2
            num2 += 1
    return a

a = int(input("Introduce un número entero: "))
print(f"El factorial de {a} es {factorial(5)}")
