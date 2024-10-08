import paqueteEjercicios.ejer1calculadora as calculadora
import paqueteEjercicios.ejer2numSecreto as ejercicio2
import paqueteEjercicios.ejer3contraseñas as contraseña
import paqueteEjercicios.ejer4loteria as loteria
import math

# 1. Ejercicio calculadora
# while True:
#     calculadora.menu()
#     opcion = int(input())
#     if opcion == 8:
#         print("Saliendo...")
#         break
#     # num1 = int(input("Elija un número: "))
#     # num2 = int(input("Elija otro número: "))
#     if opcion in range(1,5):
#         num1 = int(input("Elija un número: "))
#         num2 = int(input("Elija otro número: "))
#         if opcion == 1:
#             print(f"SUMA: {calculadora.suma(num1,num2)}")
#         elif opcion == 2:
#             resultado = calculadora.resta(num1,num2)
#             print(f"RESTA: {resultado}")
#         elif opcion == 3:
#             resultado = calculadora.multiplicacion(num1,num2)
#             print(f"MULTIPLICACION: {resultado}")
#         elif opcion == 4:
#             if num2 == 0:
#                 print("Este número no es válido.")
#                 break
#             else:
#                 resultado = calculadora.division(num1,num2)
#                 print(f"DIVISION: {resultado}")    
#         else:
#             continue
#     elif opcion in range (5,8):
#         num1 = int(input("Elija un número: "))
#         if opcion == 5:
#             resultado = math.factorial(num1)
#             print(f"FACTORIAL: {resultado}")
#         elif opcion == 6:
#             resultado = math.sqrt(num1)
#             print(f"RAIZ CUADRADA: {resultado}")
#         elif opcion == 7:
#             resultado = math.sin(num1)
#             print(f"SENO en radianes: {resultado}")
            
# 2. Ejercicio averigua número
# ejercicio2.averigua_num()

# 3. Ejercicio Contraseñas
# longitud_caracteres = int(input("Introduce la longitud de caracteres para la contraseña: "))

# print(f"La contraseña es: {contraseña.crea_contraseña(longitud_caracteres)}")

# 4. Ejercicio lotería
print(f"El boleto ganador contiene los siguientes números: {loteria.genera_cinco_num()}")
print(f"El número clave es: {loteria.genera_num_clave()}")
print(f"Y está sellado en fecha: {loteria.imprime_fecha()}")



