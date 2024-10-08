# Crea una función que pregunte el nombre y la edad del usuario, y la
# muestre por pantalla.

def nombre_edad():
    nombre = input("¿Cómo te llamas? ")
    edad = input("¿Cuántos años tienes? ")
    print(f"Te llamas {nombre} y tienes {edad} años.")
    
nombre_edad()

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
    print("Elija una opcion: ")
    print("Opcion 1: Sumar")
    print("Opcion 2: Restar")
    print("Opcion 3: Multiplicar")
    print("Opcion 4: Dividir")
    print("Opcion 5: Salir")    
    
while True:
    menu()
    opcion = int(input())
    if opcion == 5:
        break
    num1 = int(input("Elija un número: "))
    num2 = int(input("Elija otro número: "))
    if opcion == 1:
        print(f"SUMA: {suma(num1,num2)}")
    elif opcion == 2:
        resultado = resta(num1,num2)
        print(f"RESTA: {resultado}")
    elif opcion == 3:
        resultado = multiplicacion(num1,num2)
        print(f"MULTIPLICACION: {resultado}")
    elif opcion == 4:
        if num2 == 0:
            print("Este número no es válido.")
            break
        else:
            resultado = division(num1,num2)
            print(f"DIVISION: {resultado}")    
    else:
        continue
    
