import paqueteEjercicios.ejer1calculadora as calculadora
import math

while True:
    calculadora.menu()
    opcion = int(input())
    if opcion == 8:
        print("Saliendo...")
        break
    # num1 = int(input("Elija un número: "))
    # num2 = int(input("Elija otro número: "))
    if opcion in range(1,5):
        num1 = int(input("Elija un número: "))
        num2 = int(input("Elija otro número: "))
        if opcion == 1:
            print(f"SUMA: {calculadora.suma(num1,num2)}")
        elif opcion == 2:
            resultado = calculadora.resta(num1,num2)
            print(f"RESTA: {resultado}")
        elif opcion == 3:
            resultado = calculadora.multiplicacion(num1,num2)
            print(f"MULTIPLICACION: {resultado}")
        elif opcion == 4:
            if num2 == 0:
                print("Este número no es válido.")
                break
            else:
                resultado = calculadora.division(num1,num2)
                print(f"DIVISION: {resultado}")    
        else:
            continue
    elif opcion in range (5,8):
        num1 = int(input("Elija un número: "))
        if opcion == 5:
            resultado = math.factorial(num1)
            print(f"FACTORIAL: {resultado}")
        elif opcion == 6:
            resultado = math.sqrt(num1)
            print(f"RAIZ CUADRADA: {resultado}")
        elif opcion == 7:
            resultado = math.sin(num1)
            print(f"SENO en radianes: {resultado}")