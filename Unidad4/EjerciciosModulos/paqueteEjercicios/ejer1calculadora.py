import math

# CALCULADORA


def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

def menu():
    print("\nElija una opcion: ")
    print("Opcion 1: Sumar")
    print("Opcion 2: Restar")
    print("Opcion 3: Multiplicar")
    print("Opcion 4: Dividir")
    print("Opcion 5: Factorial")
    print("Opcion 6: Raiz cuadrada")
    print("Opcion 7: Seno")
    print("Opcion 8: Salir")    
    
# while True:
#     menu()
#     opcion = int(input())
#     if opcion == 8:
#         break
#     # num1 = int(input("Elija un número: "))
#     # num2 = int(input("Elija otro número: "))
#     if opcion in range(1,5):
#         num1 = int(input("Elija un número: "))
#         num2 = int(input("Elija otro número: "))
#         if opcion == 1:
#             print(f"SUMA: {suma(num1,num2)}")
#         elif opcion == 2:
#             resultado = resta(num1,num2)
#             print(f"RESTA: {resultado}")
#         elif opcion == 3:
#             resultado = multiplicacion(num1,num2)
#             print(f"MULTIPLICACION: {resultado}")
#         elif opcion == 4:
#             if num2 == 0:
#                 print("Este número no es válido.")
#                 break
#             else:
#                 resultado = division(num1,num2)
#                 print(f"DIVISION: {resultado}")    
#         else:
#             continue
#     elif opcion in range (5,6):
#         num1 = int(input("Elija un número: "))
#         if opcion == 5:
#             resultado = math.factorial(num1)
#             print(f"FACTORIAL: {resultado}")
#         elif opcion == 6:
#             resultado = math.isqrt(num1)
#             print(f"Raiz cuadrada: {resultado}")