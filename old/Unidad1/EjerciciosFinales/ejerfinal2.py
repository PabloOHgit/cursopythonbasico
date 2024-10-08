#Ejercicio 2: Realizar un programa que simule un simule de un cajero automático.
#Al iniciar el programa, imprime por pantalla las siguientes opciones:
    #Bienvenido al cajero automático
    #1. Consultar saldo
    #2. Retirar dinero
    #3. Ingresar dinero
    #4. Salir
    #Ingrese una opción
#El saldo inicial será de 1000€.

salir = 4
eleccion_user = 0
saldo = 1000
retirada = 0

while(eleccion_user != 4):
    print("\n1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    eleccion_user = int(input("\nIngrese una opción: "))
    if(eleccion_user == 1):
        print("Su saldo es:",saldo,"€")
    if(eleccion_user == 2):
        retirar = int(input("¿Cuánto dinero quiere retirar?: "))
        saldo -= retirar
    if(eleccion_user == 3):
        ingresar = int(input("¿Cuánto dinero quiere ingresar?: "))
        saldo += ingresar
    if(eleccion_user == 4):
        print("Saliendo...")
